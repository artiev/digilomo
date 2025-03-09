"""
This little tool uses Python's PIL library (pillow) and some math library (numpy) to process a 
digital color image into a LomoChrome Purple or Turquoise digital equivalent. The color matching 
is subjective, and can be edited to your liking through trial and error.
"""

import os
import logging
import chromalog

import click

from PIL import Image, ImageFilter, ImageEnhance
import numpy

chromalog.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(name)s : %(message)s'
)

logger = logging.getLogger('Main App')

def add_gaussian_noise(image, noise_strength:int):
    """
    Create a monochrome gaussian noise matrix and add it to the image data pixel per pixel.
    Using a combination of rand() and normal() seem more natural than simply using normal().

    Warning: This function is slow and there has to be better ways to do it, I just won't bother 
    for how often I will use it.
    """
    
    noise = numpy.random.rand(image.width, image.height)
    noise = numpy.random.normal(0, noise_strength*noise)

    for y in range(image.height):
        for x in range(image.width):
            value = image.getpixel((x, y))
            additive_noise_pixel = int(noise[x,y])
            red = value[0] + additive_noise_pixel
            green = value[1] + additive_noise_pixel
            blue = value[2] + additive_noise_pixel
            noisy_pixel = (red, green, blue)
            image.putpixel((x, y), noisy_pixel)
      
    return image

def recompose_adjusted_channels(r, g, b, rweight, gweight, bweight):
  """
  Recompose an image from decomposed RGB channels. The weights try to 
  emulate light sensitivity of each silver halide crystals layer and their respective 
  dyes by brightening or darkening individual channels before recomposing.

  The ratios were achieved through trial and error, empirically trying to match a 
  particular look.
  """
    
  logger.info('Adjusting individual channel "light sensitivity" to rebalance the image.')
   
  red = ImageEnhance.Brightness(r)
  green = ImageEnhance.Brightness(g)
  blue = ImageEnhance.Brightness(b)

  return Image.merge('RGB', (red.enhance(rweight), green.enhance(gweight), blue.enhance(bweight)))

def correct_rgb_image(image, rcontrast, rbrightness, rcolors):
    """
    I could not achieve a level or color matching using only the channel weights during
    recompositions, so I also correct the image after the fact.
    """
    
    logger.info('Correcting RGB image colors, contrast and brightness after recomposing channels.')
   
    contrast = ImageEnhance.Contrast(image)
    image = contrast.enhance(rcontrast)

    brighten = ImageEnhance.Brightness(image)
    image = brighten.enhance(rbrightness)

    color = ImageEnhance.Color(image)
    image = color.enhance(rcolors)

    return image

def explode_path(path):
  """
  Extract folder, filename and extension.
  """
  
  dirname = os.path.dirname(input)
  basename, extension = os.path.splitext(os.path.basename(input))

  return dirname, basename, extension


@click.command()
@click.option('--input', help="Path to the image.")
@click.option('--output', help="Path to the image.")
@click.option('--recipe', default="purple", help="Purple or Turquoise.")
@click.option('--quality', default=95, help="JPEG Compression Quality. Defaults to 95")
@click.option('--blur-radius', default=0, help="Gaussian Blur value. Defaults to 0. None:0, Mid:5, High>10")
@click.option('--noise-strength', default=0, help="Gaussian Noise strength. Defaults to 20. None:0, Mid:525, High>100")
@click.option('--preview', is_flag = True, help="Generates a small image of max 1024pixel int he long axis.")
def main( input:str, output:str, recipe:str, quality:int, blur_radius:int, noise_strength:int, preview:bool ):

  logger.info('-------------------')
  logger.info('-  Digi Lomo App  -')
  logger.info('-------------------')
  logger.info('The Lomo Purple and Lomo Turquoise look for those who don\'t shoot film.')
  logger.info('A color interpretation and conversion tool by Arthur Van de Wiele.')
  logger.info('Visit https://github.com/artiev/digilomo for updates.')
  logger.info('-------------------')

  recipe = recipe.lower()
  dirname, basename, extension = explode_path(input)

  if not output:
     output = f'{dirname}/{basename}-lomo-{recipe}{extension}'

  logger.info(f'Loading image {input} and extracting color channels.')
  source = Image.open(input).convert('RGB')

  if preview:
    logger.warning('Running in preview mode. Output size and quality is restricted.')
    source.thumbnail((1024,1024))

  red, green, blue = source.split()

  if recipe == 'turquoise':
    logger.info('Swapping blue and red channels to get that Lomo Turquoise look.')
    destination = recompose_adjusted_channels(blue, green, red, 1.5, 1.0, 1.1)
    destination = correct_rgb_image(destination, 1.1, 1.0, 1.5)

  elif recipe == "purple":
    logger.info('Swapping blue and green channels to get that Lomo Purple look.')
    destination = recompose_adjusted_channels(red, blue, green, 1.2, 1.0, 0.98)
    destination = correct_rgb_image(destination, 1.4, 0.97, 0.5)

  else:
    logger.error(f'Recipe {recipe} unknown.')

  if blur_radius > 0 and not preview:
    logger.info(f'Applying Gaussian Blur (radius = {blur_radius}).')
    destination = destination.filter(ImageFilter.GaussianBlur(blur_radius))

  if noise_strength > 0 and not preview:
    logger.info(f'Adding Gaussian Noise.')
    destination = add_gaussian_noise(destination, noise_strength)


  logger.info(f'Saving new image to {output}.')
  destination.save(output, subsampling=0, quality=quality)

  logger.info('-------------------')
  logger.info('All done. Bye.')

if __name__ == '__main__':
  main()
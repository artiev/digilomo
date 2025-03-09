Digi Lomo App
=============

**The Lomo Purple and Lomo Turquoise look for those who don't shoot film.**

This is a color interpretation and conversion tool that will let you reproduce 
the unique look of Lomography's LomoChrome Purple and LomoChrome Turquzoise film
emulsions using a digital image.

By Arthur Van de Wiele. Visit https://github.com/artiev/digilomo for updates.


The Process in short
--------------------

Lomography's special films are swapping some of the dyes activated by the
silver halide crystals to achieve different looks. That can be done in digital
by swapping the color channels and adjusting each channel's "sensitivity to
light" to achieve a similar look and mix of colors.

The truth is, the final look of Lomo Purple and Lomo Turquoise is highly
dependent on the conversion from negative to positive and generally left to
interpretation. This tool creates a subjective interpretation of what I would
expect the film to look after developing and converting it to positives. If
you don't like this interpretation, you can play with the script and the
different weights and corrections I applied to the channels and to the final
image until you have something you like.

Installing and Using
--------------------

This is a Python script, I requires Python 3.10 and a few libraries including
PIL (aka. Pillow) and Numpy (used to generate convincing Gaussian noise). I
will not cover this, but https://www.python.org/about/gettingstarted/ does.

The script is self sufficient once you have your Python environment running.
Then you can call the ``digilomo.py`` script and give it the path to the source
file and the recipe you want to use: ``purple`` or ``turquoise``

```
$ python digilomo.py --src /path/to/image.jpg --recipe purple
```

By default the script will create a new image next tot he original one.
Otherwise, you can use ``--dst`` to set the destination. If you are just looking
for a quick test, use ``--preview`` to skip the heavy processing, and reduce the
filesize of the output.

Otherwise, a few additional options are present:
- ``--noise-strength`` to set the level of noise. It is 20 by default.
- ``--quality`` set the JPEG compression quality. It is 95 by default.
- ``--blur-radius`` if you want to reduce sharpness. It is off (0) by default.
- ``--help`` shows pretty much what I just described.

Warning
-------
- **[Digital Files]** I only tested the conversion with Fujifilm X-Trans CMOS 5
HR images shot in JPEG with my X-T50. Feel free to report on other models,
brands and JPEGs but it should give very similar results.
- **[Speed]** The conversion and color correction is very fast, even on large
images, but the noise generation takes a long time. Just disable the noise if
you want using ``--noise-strength 0``.

The comparison between real film and the interpreted image
----------------------------------------------------------

I do not have my own samples of Lomo Turquoise, but I have samples of Lomo
Purple which I scanned and converted myself. I used these for the empirical
mapping, and I used Lomography's sample images for Turquoise, although they
are also a bit all over the place.

True Lomo Purple | Digital Lomo Purple
:-:|:-:
![Real Lomo Purple](https://github.com/artiev/digilomo/blob/main/samples/2025-02-23-0746453.jpg?raw=true)|![Digital Lomo Purple](https://github.com/artiev/digilomo/blob/main/samples/2024-12-25-1248461-lomo-purple.jpg?raw=true)
![Real Lomo Purple](https://github.com/artiev/digilomo/blob/main/samples/2025-02-23-0754090.jpg?raw=true)|![Digital Lomo Purple](https://github.com/artiev/digilomo/blob/main/samples/2024-08-05-190245-lomo-purple.jpg?raw=true)

Conversion Samples
------------------

Original | Digital Lomo Purple | Digital Lomo Turquoise
:-:|:-:|:-:
![](https://github.com/artiev/digilomo/blob/main/samples/2024-08-02-173158.jpg?raw=true)|![](https://github.com/artiev/digilomo/blob/main/samples/2024-08-02-173158-lomo-purple.jpg?raw=true)|![](https://github.com/artiev/digilomo/blob/main/samples/2024-08-02-173158-lomo-turquoise.jpg?raw=true)
![](https://github.com/artiev/digilomo/blob/main/samples/2024-08-05-114259.jpg?raw=true)|![](https://github.com/artiev/digilomo/blob/main/samples/2024-08-05-114259-lomo-purple.jpg?raw=true)|![](https://github.com/artiev/digilomo/blob/main/samples/2024-08-05-114259-lomo-turquoise.jpg?raw=true)
![](https://github.com/artiev/digilomo/blob/main/samples/2025-01-03-1147042.jpg?raw=true)|![](https://github.com/artiev/digilomo/blob/main/samples/2025-01-03-1147042-lomo-purple.jpg?raw=true)|![](https://github.com/artiev/digilomo/blob/main/samples/2025-01-03-1147042-lomo-turquoise.jpg?raw=true)
![](https://github.com/artiev/digilomo/blob/main/samples/2024-08-05-121734.jpg?raw=true)|![](https://github.com/artiev/digilomo/blob/main/samples/2024-08-05-121734-lomo-purple.jpg?raw=true)|![](https://github.com/artiev/digilomo/blob/main/samples/2024-08-05-121734-lomo-turquoise.jpg?raw=true)
![](https://github.com/artiev/digilomo/blob/main/samples/2024-08-05-190245.jpg?raw=true)|![](https://github.com/artiev/digilomo/blob/main/samples/2024-08-05-190245-lomo-purple.jpg?raw=true)|![](https://github.com/artiev/digilomo/blob/main/samples/2024-08-05-190245-lomo-turquoise.jpg?raw=true)
![](https://github.com/artiev/digilomo/blob/main/samples/2024-09-22-114331.jpg?raw=true)|![](https://github.com/artiev/digilomo/blob/main/samples/2024-09-22-114331-lomo-purple.jpg?raw=true)|![](https://github.com/artiev/digilomo/blob/main/samples/2024-09-22-114331-lomo-turquoise.jpg?raw=true)
![](https://github.com/artiev/digilomo/blob/main/samples/2024-09-22-1114231.jpg?raw=true)|![](https://github.com/artiev/digilomo/blob/main/samples/2024-09-22-1114231-lomo-purple.jpg?raw=true)|![](https://github.com/artiev/digilomo/blob/main/samples/2024-09-22-1114231-lomo-turquoise.jpg?raw=true)
![](https://github.com/artiev/digilomo/blob/main/samples/2024-12-25-1248461.jpg?raw=true)|![](https://github.com/artiev/digilomo/blob/main/samples/2024-12-25-1248461-lomo-purple.jpg?raw=true)|![](https://github.com/artiev/digilomo/blob/main/samples/2024-12-25-1248461-lomo-turquoise.jpg?raw=true)
![](https://github.com/artiev/digilomo/blob/main/samples/2025-01-03-1144512.jpg?raw=true)|![](https://github.com/artiev/digilomo/blob/main/samples/2025-01-03-1144512-lomo-purple.jpg?raw=true)|![](https://github.com/artiev/digilomo/blob/main/samples/2025-01-03-1144512-lomo-turquoise.jpg?raw=true)

Conversion Artifacts
--------------------

The conversion is not perfect. There are some photos that show a heavy
aberration in the highlights. I have not investigated it further as this does
not distract me much, but it is a departure from the real film look.

# Funnel

A simple tool to create an 8-bit RGB image using colour channels from other images.

## Installation

Pillow is used for image manipulation. All dependencies can be installed with `pip install -r requirements.txt`.

## Usage

Creating an image using 3 channels:

```
python funnel.py --R=r.png --G=g.png --B=b.png
```

Creating an image using only one channel to a custom location:

```
python funnel.py --R=r.png --path=images/coloured.png
```

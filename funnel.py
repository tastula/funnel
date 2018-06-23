"""
Create an RGB image from 3 separate images using their colour channels.
"""


from argparse import ArgumentParser
from PIL import Image


def parse_args():
    """
    Parse and return arguments from command line.
    """

    parser = ArgumentParser()
    parser.add_argument("--R", type=str, default=None)
    parser.add_argument("--G", type=str, default=None)
    parser.add_argument("--B", type=str, default=None)
    parser.add_argument("--path", type=str, default="result.png")

    return parser.parse_args()


def load_channel(path, channel):
    """
    Load image from path. Extract and return wanted channel.
    """

    if not path:
        return None

    try:
        channels = Image.open(path).split()
        return channels[channel]
    except FileNotFoundError:
        print(f"No image in path {path}, using empty channel")
        return None


def create_image(channels, path):
    """
    Create and save image from list of channels.
    """

    size = None

    for channel in channels:
        if channel:
            if not size:
                size = channel.size
            elif channel.size != size:
                print("Images have different dimensions!")
                return

    if not size:
        print("No images given!")
        return

    for index, channel in enumerate(channels):
        if not channel:
            channels[index] = Image.new("L", size)

    try:
        image = Image.merge("RGB", (channels[0], channels[1], channels[2]))
        image.save(path)
    except FileNotFoundError:
        print(f"Couldn't save to path {path}!")
        return


def main():
    """
    Create the colorized image from other images.
    """

    args = parse_args()

    channel_r = load_channel(args.R, 0)
    channel_g = load_channel(args.G, 1)
    channel_b = load_channel(args.B, 2)

    create_image([channel_r, channel_g, channel_b], args.path)


main()

from rembg import remove
from PIL import Image
import sys
import os


def remove_background(input_path, output_path=None):
    # Open input image
    with open(input_path, "rb") as i:
        input_image = i.read()

    # Remove background
    output_image = remove(input_image)

    # If output path is not specified, use input name with '_nobg.png'
    if not output_path:
        base, _ = os.path.splitext(input_path)
        output_path = base + "_nobg.png"

    # Save the output
    with open(output_path, "wb") as o:
        o.write(output_image)
    print(f"Background removed! Saved as: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python remove_bg.py <input_image> [output_image]")
    else:
        input_image = sys.argv[1]
        output_image = sys.argv[2] if len(sys.argv) > 2 else None
        remove_background(input_image, output_image)

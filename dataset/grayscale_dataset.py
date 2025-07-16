import os
import argparse
from PIL import Image

def convert_to_grayscale(input_dir, output_dir):
    """
    Converts all RGB PNG images in the input directory to 8-bit grayscale.
    Saves converted images in a separate output directory without overwriting originals.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".png"):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            with Image.open(input_path) as img:
                if img.mode != 'L':
                    img_gray = img.convert('L')
                    print(f"Converted to grayscale: {filename}")
                else:
                    img_gray = img.copy()
                    print(f"Already grayscale: {filename}")

                img_gray.save(output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert PNG images to grayscale.")
    parser.add_argument("input_dir", type=str, help="Path to input directory containing PNG images.")
    parser.add_argument("output_dir", type=str, help="Path to output directory to save grayscale images.")

    args = parser.parse_args()
    convert_to_grayscale(args.input_dir, args.output_dir)


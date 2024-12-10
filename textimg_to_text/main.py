import pytesseract
from PIL import Image
import argparse

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def main():
    parser = argparse.ArgumentParser(description='Extract text from an image using OCR.')
    parser.add_argument('image-path', type=str, help='Path to the image file')

    args = parser.parse_args()

    extracted_text = extract_text_from_image(args.image_path)

    print("Extracted text:")
    print(extracted_text)

if __name__ == "__main__":
    main()

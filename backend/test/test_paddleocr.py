from paddleocr import PaddleOCR
import cv2
import sys

def extract_text(image_path):
    ocr = PaddleOCR(use_angle_cls=True, lang='en')
    img = cv2.imread(image_path)
    if img is None:
        print("Could not read image:", image_path)
        return
    result = ocr.ocr(image_path)
    texts = [line[1][0] for line in result[0]] if result and result[0] else []
    if texts:
        print("Extracted text:")
        for text in texts:
            print(text)
    else:
        print("No text found")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python test_paddleocr.py <image_path>")
    else:
        extract_text(sys.argv[1])
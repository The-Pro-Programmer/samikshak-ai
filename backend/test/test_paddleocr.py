from paddleocr import PaddleOCR
import cv2
import sys

def extract_text(image_path: str, lang: str = "en") -> str:
    ocr = PaddleOCR(use_angle_cls=True, lang=lang)
    # Debug: check if image is readable
    import os
    if not os.path.exists(image_path):
        print(f"Image file does not exist: {image_path}")
        return "No text found"
    img = cv2.imread(image_path)
    if img is None:
        print(f"cv2 could not read image: {image_path}")
        return "No text found"
    result = ocr.predict(image_path)

    if not result or len(result) == 0 or len(result[0]) == 0:
        return "No text found"

    extracted = []
    for line in result[0]:
        text = line[1][0]
        if text.strip():
            extracted.append(text)

    # Join lines with newlines for better readability
    return "\n".join(extracted).strip() if extracted else "No text found"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python test_paddleocr.py <image_path>")
    else:
        print(extract_text(sys.argv[1]))
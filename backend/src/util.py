import cv2
import numpy as np
from pdf2image import convert_from_path
from backend.src import parser_prescription,parser_patient_details
import pytesseract


class Extract:
    def __init__(self, file_path, file_format: str):
        self.pdf_path = fr"{file_path}"
        self.file_format = fr"{file_format}"
        self.poppler_path = r"D:\TOOLS\poppler-22.04.0\Library\bin"
        self.tesseract_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        self.text = self.extract()

    def extract(self):
        """
        extract the text from the given pdf
        :return: text from the image
        """
        extracted_text = ""
        pages = convert_from_path(pdf_path=self.pdf_path, poppler_path=self.poppler_path)
        if len(pages)>0:
            page = pages[0]
            img = preprocess_image(page)
            pytesseract.pytesseract.tesseract_cmd = self.tesseract_path
            text = pytesseract.image_to_string(img, lang="eng")
            extracted_text += text + "\n"
        return extracted_text

    def extract_text(self):

        if self.file_format == "prescription":
            extracted_data = parser_prescription.PrescriptionParser(self.text).parser()
            return extracted_data
        elif self.file_format == "patient_details":
            extracted_data = parser_patient_details.PatientDetailsParser(self.text).parser()
            return extracted_data
        else:
            raise Exception(f"invalid document format: {self.file_format}")


def preprocess_image(img):
    gray = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
    processed_image = cv2.adaptiveThreshold(
        resized,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        61,
        11
    )
    return processed_image




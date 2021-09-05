"""The module engine is used as a machine to carry the conversion from the pdf
into a txt file. Can be called in your own application after passing these three
arguments: file_to_conver, output_folder, output_text"""

# REQUIREMENTS: pytesseract.exe and poppler bin folder
# PLEASE REFER TO THE DOCUMENTATION FOR MORE DETAILS

import os
import json
import pytesseract
from PIL import Image
from pdf2image import convert_from_path

# error handler of json files
ERROR_MSG_2 = "Json file does not exist"


class Engine:
    """Takes care of converting pdf files into txt format"""

    def __init__(self, file_to_convert, output_folder, output_text):
        """initialize the conversion"""
        self.file_to_convert = file_to_convert
        self.output_folder = output_folder
        self.output_text = output_text
        self.launch_engine()

    def launch_engine(self):
        """Part #1 : Converting PDF to images"""
        try:
            with open("settings.json") as json_file:
                data = json.load(json_file)
                for p in data["settings"]:
                    json_poppler = p["poppler"]
                    json_pytesseract = p["pytesseract"]
        except FileNotFoundError:
            print(ERROR_MSG_2)

        pages = convert_from_path(
            self.file_to_convert,
            500,
            poppler_path=json_poppler,
        )

        image_counter = 1  # variable to check no of images in the pdf
        check_folder = True  # boolean type to stop creating new dirs
        i = 1  # rand variable to check if output folder exists
        path = self.output_folder + "/extract no. "

        try:
            os.makedirs(path + str(i), exist_ok=False)
        except:
            while check_folder:
                if os.path.exists(path + str(i)):
                    i += 1
                else:
                    os.makedirs(path + str(i), exist_ok=False)
                    check_folder = False

        path = path + str(i) + "/"

        for page in pages:
            filename = path + "page_" + str(image_counter) + ".jpg"
            page.save(filename, "JPEG")
            image_counter = image_counter + 1

        """Part #2 - Recognizing text from the images using OCR"""

        file_limit = image_counter - 1
        outfile = path + self.output_text + ".txt"
        f = open(outfile, "a")

        for i in range(1, file_limit + 1):
            filename = path + "page_" + str(i) + ".jpg"

            pytesseract.pytesseract.tesseract_cmd = json_pytesseract

            text = str((pytesseract.image_to_string(Image.open(filename))))
            text = text.replace("-\n", "")

            f.write(text)

        f.close()
        print("The file has been converted successfully.")

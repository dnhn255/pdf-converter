"""This module is used to store and use default filepath of tesseract.exe and poppler.
Once settings are applied the program will initialize these at the start."""

import json

data = {"settings": []}


class CreateNewJson:
    def __init__(self, poppler, pytesseract):
        self.poppler = poppler
        self.pytesseract = pytesseract
        self.create_json()

    def create_json(self):
        data["settings"].append(
            {
                "poppler": self.poppler,
                "pytesseract": self.pytesseract,
            }
        )

        with open("settings.json", "w") as outfile:
            json.dump(data, outfile)

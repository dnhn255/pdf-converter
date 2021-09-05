# pdf-converter

The pdf-converter is a simple tool that uses tesseract to convert images to text. It was designed mostly for the purposes of converting relatively small files as larger ones can take too much time with no guarantee of success. Recommended max page limit: 30, otherwise, other and more advaned solutions might be more desirable. Another disadvantage of the tool is that it requires initial setup to be done, i.e. specify tesseract.exe in settings and installation of poppler. 

# User Guide

1. Install Google Tesseract OCR engine from: https://github.com/tesseract-ocr/tesseract
2. Download poppler from: https://poppler.freedesktop.org/
3. Go to the Settings tab and use Browse button to locate: tesseract.exe file and bin folder for poppler.
4. Go to the Convert tab and select the PDF file to convert, output folder where the files should be extracted into, and (optionally) filename of the output file.
5. Wait for the converter to be done, watch the status bar at the bottom of the Convert tab to be notified when the processing ends.

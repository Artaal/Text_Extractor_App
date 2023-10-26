# Text Extractor

This is a simple text extraction application using Python and Tkinter that allows you to extract text from PDF and image files and save it in a text file.

## Usage

1. Run the script by executing the following command: python text_extractor.py

2. To extract text from a PDF file:
   - Select a PDF file with the "Browse PDF" button.
   - The text will be extracted and saved to a text file with the same name as the PDF but with a .txt extension.

3. To extract text from an image (JPG, JPEG, or PNG):
   - Select an image file with the "Browse Image" button.
   - The text will be extracted using Pytesseract and saved to a text file with the same name as the image but with a .txt extension.

4. The application displays the input file in red and the output text file in green in the right-side text box.

## Customization

You can customize the appearance and behavior of the application by modifying the Python script. For example, you can change the window size, button colors, fonts, and more.

## Acknowledgments

- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the graphical user interface.
- [PyPDF2](https://pythonhosted.org/PyPDF2/) for PDF file handling.
- [pytesseract](https://pypi.org/project/pytesseract/) for image text extraction.
- [PIL (Pillow)](https://python-pillow.org/) for image processing.

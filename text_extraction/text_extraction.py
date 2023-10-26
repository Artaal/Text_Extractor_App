import tkinter as tk
from tkinter import filedialog
import PyPDF2
import pytesseract
from PIL import Image
from tkinter import scrolledtext

root = tk.Tk()
root.title("Text Extractor")
root.geometry("1000x600")  

# labels and buttons

left_frame = tk.Frame(root, padx=10)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# scrollable text box

right_frame = tk.Frame(root, padx=10)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# PDF file text extraction

def extract_pdf_text():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        # Open the PDF file
        pdf_file = open(file_path, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        # Create a text file for saving extracted text
        txt_file_path = file_path.replace(".pdf", ".txt")
        txt_file = open(txt_file_path, 'w')

        # Loop through each page and extract text
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            txt_file.write(text)

        # Close the files
        pdf_file.close()
        txt_file.close()

        # Update the displayed information
        update_info(file_path, txt_file_path)

# image file text extraction

def extract_image_text():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
    if file_path:
        # Open and process the image using Pytesseract
        img = Image.open(file_path)
        text = pytesseract.image_to_string(img)

        # Create a text file for saving extracted text
        txt_file_path = file_path.replace(".jpg", ".txt").replace(".jpeg", ".txt").replace(".png", ".txt")
        txt_file = open(txt_file_path, 'w')
        txt_file.write(text)
        txt_file.close()

        # Update the displayed information
        update_info(file_path, txt_file_path)

# update the information in the text box with colored tags

def update_info(input_file, output_file):
    info_text.config(state=tk.NORMAL)
    info_text.delete('1.0', tk.END)  # Clear existing text
    info_text.insert(tk.END, f"Input File: {input_file}\n")
    info_text.insert(tk.END, f"Output Text: {output_file}\n")

    # Apply color tags to the text
    info_text.tag_configure("red", foreground="red")
    info_text.tag_configure("green", foreground="green")
    info_text.tag_add("red", "1.0", "1.end")
    info_text.tag_add("green", "2.0", "2.end")

    info_text.config(state=tk.DISABLED)

# labels, buttons, and text display on the left side

pdf_label = tk.Label(left_frame, text="Extract Text from PDF:", font=("Helvetica", 14), bg="orange")
pdf_button = tk.Button(left_frame, text="Browse PDF", command=extract_pdf_text, font=("Helvetica", 12), fg="white", bg="green")
image_label = tk.Label(left_frame, text="Extract Text from Image:", font=("Helvetica", 14), bg="orange")
image_button = tk.Button(left_frame, text="Browse Image", command=extract_image_text, font=("Helvetica", 12), fg="white", bg="green")

pdf_label.pack(pady=(20, 0))
pdf_button.pack(pady=10)
image_label.pack(pady=10)
image_button.pack(pady=10)

# scrollable text box on the right side

info_text = scrolledtext.ScrolledText(right_frame, width=40, height=20, state=tk.DISABLED)
info_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

root.mainloop()

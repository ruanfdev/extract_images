# PyMuPDF
import fitz
import os

def extract_images_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    images = []
    for page in doc:
        image_list = page.get_images(full=True)
        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image_filename = f"image{page.number}_{img_index}.{image_ext}"
            with open(image_filename, "wb") as img_file:
                img_file.write(image_bytes)
            images.append(image_filename)
    doc.close()
    return images

pdf_filename = input("Enter the PDF filename or full path: ")

# Check if input is a full path or just a filename
if not os.path.isabs(pdf_filename):
    # If filename, check if it already has the ".pdf"
    if not pdf_filename.lower().endswith(".pdf"):
        # If not, add the ".pdf"
        pdf_filename += ".pdf"
    # Prepend current directory to construct the full path
    pdf_filename = os.path.join(os.getcwd(), pdf_filename)

extracted_images = extract_images_from_pdf(pdf_filename)
print("Extracted images:", extracted_images)
# import PyPDF4
# from PyPDF4 import PdfFileReader, PdfFileWriter

# PyPDF4.PdfFileReader("imageTest2.pdf")
# def watermark(inputPdf, outputPdf, watermark):
#     watermark = PdfFileReader(watermark)
#     pageWatermark = watermark.getPage(0)
#     inputPdfReader = PdfFileReader(inputPdf)
#     outputPdfWriter = PdfFileWriter()
#     for page in range(inputPdfReader.getNumPages()):
#         page = inputPdfReader.getPage(page)

#         # print('Hello>>>>>>>', page.extractText())
        
#         page.mergePage(pageWatermark)
#         outputPdfWriter.addPage(page)
#     with open(outputPdf, "wb") as output:
#         outputPdfWriter.write(output)
# if __name__ == "__main__":
#     watermark(
#         inputPdf="imageTest2.pdf", 
#         outputPdf="imageWatermark.pdf", 
#         watermark="watermark.pdf")

# import fitz

# file = 'imageTest1.pdf'

# pdf = fitz.open(file)
# imageList = pdf.get_page_images(0)
# for image in imageList:
#     xref = image[0]
#     pix = fitz.Pixmap(pdf, xref)
#     if pix.n < 4:
#         pix.save(f'{xref}.png')
#     else:
#         pix1 = fitz.open(fitz.csRGB, pix)
#         pix1.save(f'{xref}.png')
#         pix1 = None
#     pix = None
# print(len(imageList), 'detected')
# -----------------------------------------------------------

# import fitz
# input_pdf = "imageTest1.pdf"

# file = fitz.open(input_pdf)
# for pageNumber, page in enumerate(file.pages(), start=1):
#     text = page.get_text()
#     txt = open(f'text{pageNumber}.txt', 'a')
#     txt.writelines(text)
#     txt.close()
# -----------------------------------------------------------
# importing the required modules
import fitz
import os
# the PDF file from which images will be extract
input_pdf = "imageTest2.pdf"
# The directory where we want to output the images
output_dir = "images"
# The prefix of the images name
image_prefix = "codeunderscored"
# openig the pdf file
pdf = fitz.open(input_pdf)
# creating the output directory if not present already
if not os.path.exists(output_dir):
    os.mkdir(output_dir)
# changing the path to the output directory
os.chdir(output_dir)
# extracting all the images from the pdf
for page in range(len(pdf)):
    for image in pdf.get_page_images(page):
        xref = image[0]
        pix = fitz.Pixmap(pdf, xref)
        if pix.n < 4:
            pix.save(f"{image_prefix}{page}-{xref}.png")
        else:
            pix1 = fitz.Pixmap(fitz.csRGB, pix)
            pix1.save(f"{image_prefix}{page}-{xref}.png")
            pix1 = None
        pix = None
# end of the program
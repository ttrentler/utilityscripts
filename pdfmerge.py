#! uses python3 with pyPDF4
# combinePdfs.py - Combines all the PDFs in the current working directory into 
# a single PDF.

import PyPDF4, os

# Get all the PDF filenames.
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort()

pdfWriter = PyPDF4.PdfFileWriter()

# Loop through all the PDF files.
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF4.PdfFileReader(pdfFileObj)
'''
# Loop through all the pages (starting at zero) and add them. 
If you change this to a one you can omit the first page of every PDF 
(useful to remove cover pages)

'''
    for pageNum in range(0, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

# Save the resulting PDF to a file.
pdfOutput = open('combined_pdfs.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()

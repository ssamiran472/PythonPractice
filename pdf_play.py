from PyPDF2 import PdfFileReader, PdfFileWriter
import sys
import os
scriptPath = sys.path[0]
downloadPath = os.path.join(scriptPath)
downloadPath = downloadPath + '/SamiranSarkar.pdf'
# pdf_file_obj = open('alqabas_pdf_2020-09-02.pdf', 'rb')
pdf_file_obj = open(downloadPath, 'rb')
pdfReader = PdfFileReader(pdf_file_obj)

# print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page
# text = pageObj.extractText()
# print('text of the page', text.decode())

# pdf_file_obj.close()
output = PdfFileWriter()
output.addPage(pageObj)

# with open("alqabas2020_09_02_pages0.pdf", "wb") as outputStream:
#     output.write(outputStream)

for i in range(pdfReader.numPages):
    output = PdfFileWriter()
    output.addPage(pdfReader.getPage(i))
    with open("alqabas2020_09_02_pages%s.pdf" % i, "wb") as outputStream:
        output.write(outputStream)

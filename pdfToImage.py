'''
    INSTRACTION::
        1.Download poppler package form http://blog.alivate.com.au/poppler-windows/
            and after that extract it. Add a variable with the path of the file(bin)  in path.
        2. pip install pdf2image
'''


from pdf2image import convert_from_path
import os

outputDir = "image/"
 
def convert(file, outputDir):
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)
    
    pages = convert_from_path(file, 500)
    counter =1
    for page in pages:
        myfile=outputDir + 'output' + str(counter) + ".jpg"
        counter += 1
        # print(myfile, 'JPEG')
        page.save(myfile, 'JPEG')


file = 'dhidata.pdf'
convert(file, outputDir)
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 15:10:02 2018
@author: renato.caetano

Simple script for convert pdf image and return a code pattern using OCR pytesseract and regular expression

"""

import pytesseract as ocr
import re
import PyPDF2


from PIL import Image


img = ''
pdf_path = 'PEDIDO_CREDITO_1410692_20180612_1048_27040.pdf'

# Exploring the PDF document and convert it to image
if __name__ == '__main__':
    input1 = PyPDF2.PdfFileReader(open(pdf_path, "rb"))
    page0 = input1.getPage(0)
    xObject = page0['/Resources']['/XObject'].getObject()

    for obj in xObject:
        if xObject[obj]['/Subtype'] == '/Image':
            size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
            data = xObject[obj].getData()
            if xObject[obj]['/ColorSpace'] == '/DeviceRGB':
                mode = "RGB"
            else:
                mode = "P"

            if xObject[obj]['/Filter'] == '/FlateDecode':
                img = Image.frombytes(mode, size, data)
                img.save(obj[1:] + ".png")
            elif xObject[obj]['/Filter'] == '/DCTDecode':
                img = open(obj[1:] + ".jpg", "wb")
                img.write(data)
                img.close()
            elif xObject[obj]['/Filter'] == '/JPXDecode':
                img = open(obj[1:] + ".jp2", "wb")
                img.write(data)
                img.close()

# Convert the image to string by OCR                
output = ocr.image_to_string(img, config='outputbase digits')

# Remove all non number and point characters
result = re.sub('[^0-9, .]','', str(output))

# Regular expression for get the payment code
result2 = re.search('\d{5}.\d{5}\s\d{5}.\d{6}\s\d{5}.\d{6}\s\d\s\d*', result)
print(result2.group())

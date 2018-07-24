# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 14:16:02 2018

@author: renato.caetano
"""

import pytesseract as ocr
import base64 as bs

from PIL import Image


encoded_string = ''

with open('boleto-teste.pdf', 'rb') as pdf_file:
    encoded_string = bs.b64encode(pdf_file.read())
    
with open('img.png', 'wb') as img_file:
    img_file.write(bs.decodestring(encoded_string))
    img_file.close()

output = ocr.image_to_string(Image.open('img.png'), config='outputbase digits')
#print(output)

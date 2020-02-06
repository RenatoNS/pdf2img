# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 14:23:00 2020

@author: renatons
"""
import os
from pdf2image import convert_from_path

pdf_file = r'C:\Users\RenatoNS\Desktop\pdf2img2txt\teste_pdf_1pg.pdf'
pages = convert_from_path(pdf_file, 500)

path = r'C:\Users\RenatoNS\Desktop\pdf2img2txt'

retval= os.getcwd()
os.chdir(path)

for page in pages:
    page.save('saida_img.jpg', 'JPEG')
    
os.chdir(retval)


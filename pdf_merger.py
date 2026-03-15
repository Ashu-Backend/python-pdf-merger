from PyPDF2 import PdfWriter
import os

merger = PdfWriter()
files = [file for file in os.listdir() if file.endswith(".pdf")]

for pdf in files:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()



import string
import random
def missingCharacters(s):
    s = set(s.lower())
    
    digits = ""
    letters = ""
    
    for d in string.digits:
        if d not in s:
            digits += d
            
    for l in string.ascii_lowercase:
        if l not in s:
            letters += l
            
    return digits + letters
    
s = "0123456789"
print(missingCharacters(s))
    

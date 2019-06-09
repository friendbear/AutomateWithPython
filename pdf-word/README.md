## PDF and Word document

### PDF

**pip3 install PyPDF2**

encrypt
---
* isEncrypted
* PyPDF2.PdfFileReader(...).decrypt('password)

rotate
---
```python

PyPDF2.PdfFileReader(open('pdffilename', 'rb')).getpage(0).rotateClockwise(90)
```

### Word

**pip3 install python-docx**


---

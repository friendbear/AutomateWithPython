## PDF and Word document

encrypt
---
* isEncrypted
* PyPDF2.PdfFileReader(...).decrypt('password)

rotate
---
```python

PyPDF2.PdfFileReader(open('pdffilename', 'rb')).getpage(0).rotateClockwise(90)
```

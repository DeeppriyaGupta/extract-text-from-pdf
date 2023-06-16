from PyPDF2 import PdfReader

open=PdfReader('J:\\Tech Ascent\\temporary\\pdf to text\\maths.pdf')

for i in range(len(open.pages)):
    page=open.pages[i]
    print(page.extract_text())
    print('--------',i,'--------')
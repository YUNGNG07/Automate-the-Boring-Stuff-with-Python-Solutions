import PyPDF2

path = r'C:\Users\yungng07\Documents\Automate-the-Boring-Stuff-with-Python-Solutions\Chapter 13_Working with PDF and Word Documents\meetingminutes.pdf'

pdf_file = open(path, 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)
print(len(pdf_reader.pages))

page_obj = pdf_reader.pages[0]
print(page_obj.extract_text())

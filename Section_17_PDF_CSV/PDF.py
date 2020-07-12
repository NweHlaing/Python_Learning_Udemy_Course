import PyPDF2
#Read PDF
f = open('D:\\Backup from old PC\\Learning\\Section_17_PDF_CSV\\Working_Business_Proposal.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(f)
print("Pages...",pdf_reader.numPages)
page_one = pdf_reader.getPage(0)
page_one_text = page_one.extractText()
print("Get text....",page_one_text)

#Adding to PDF
f = open('D:\\Backup from old PC\\Learning\\Section_17_PDF_CSV\\Working_Business_Proposal.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(f)
first_page = pdf_reader.getPage(0)
pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(first_page)
pdf_output = open("D:\\Backup from old PC\\Learning\\Section_17_PDF_CSV\\Some_New_Doc.pdf","wb")
pdf_writer.write(pdf_output)
f.close()

#Getting text from PDF
f = open('D:\\Backup from old PC\\Learning\\Section_17_PDF_CSV\\Working_Business_Proposal.pdf','rb')

# List of every page's text.
# The index will correspond to the page number.
pdf_text = []

pdf_reader = PyPDF2.PdfFileReader(f)

for p in range(pdf_reader.numPages):
    
    page = pdf_reader.getPage(p)
    
    pdf_text.append(page.extractText())

    print("Text...",pdf_text)



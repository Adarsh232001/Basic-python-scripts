import PyPDF2
pdfFile = open("Desktop\file.pdf",'rb') #file name
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()
for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))

pdfWriter.encrypt('adarsh') #password
resultPdf = open('encryptedfile.pdf','wb') #outputfile name
pdfWriter.write(resultPdf)
resultPdf.close()
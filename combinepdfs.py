import PyPDF2, os

# Get all the PDF filenames.
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort()

pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the PDF files.
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # Loop through all the pages and add them.
    
    # If you want to skip the first page, you should use- 
    #for pageNum in range(1, pdfReader.numPages):
    
    # If you want to skip the first 2 pages, you should use-
    #for pageNum in range(2, pdfReader.numPages):
    #and so on..
    
    for pageNum in range(0, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

# Save the resulting PDF to a file.
pdfOutput = open('combined.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()

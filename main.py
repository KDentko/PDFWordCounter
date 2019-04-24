import PyPDF2

filename = open('tl082-OpAmp-Datasheet.pdf' , 'rb')
pdfReader = PyPDF2.PdfFileReader(filename)
word = input('What word do you want me to count? /n')
num = 0
for x in range(pdfReader.numPages):
    page = pdfReader.getPage(x)
    text = page.extractText()
    print(text)
    pgcount = text.count(word)
    num =+ pgcount

print ('The ' + word + ' appears ' + str(num) + ' times.')
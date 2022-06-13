# importing modules
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from textwrap import wrap

def CreatePDF(filePath, body):

    # creating a pdf object
    pdf = canvas.Canvas(filePath)

    # creating a multiline text using
    # textline and for loop
    text = pdf.beginText(40, 780)
    text.setFont("Times-Roman", 14)
    temp_list = body.split('\n')
    
    for line in temp_list:
        for temp in wrap(line, 80):
            text.textLine(temp)
        text.textLine('')
        
        #print(text.getStartOfLine())
        # if the text reaches bottom of page
        # draw all text, and create new page with new text
        if text.getY() < 180:
            pdf.drawText(text)
            pdf.showPage()
            text = pdf.beginText(40, 780)
            text.setFont("Times-Roman", 14)
    
    pdf.drawText(text)
    #pdf.showPage() # creates a new page

    # saving the pdf
    pdf.save()

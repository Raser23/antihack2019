from xhtml2pdf import pisa
from io import StringIO
htmltopdf = open('ticket1.html', 'r')
pdf = pisa.pisaDocument(StringIO(htmltopdf), dest=StringIO())
htmltopdf.close()

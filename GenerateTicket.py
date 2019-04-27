import pyqrcode as pqr
import hashlib
import png
import os
import text_config as tc
from PIL import ImageFont, ImageDraw, Image


#ticket.show()

def GenerateTicket(address, ticket_code, message):
    path, dirs, files = next(os.walk("tickets"))
    file_count = len(files)
    name = str(file_count)
    ticket = pqr.create(message, mode='binary')
    _path = 'tickets/_'+name+'ticket.png'
    path = 'tickets/' + name + 'ticket.png'
    ticket.png(_path, scale=10)
    QRimage = Image.open(_path)

    fontSize = 20

    QRwidth, QRheight = QRimage.size
    resultImg = Image.new('RGB', (QRwidth, QRheight+100), color=(255, 255, 255))
    d = ImageDraw.Draw(resultImg)
    font = ImageFont.truetype("fonts/9654.ttf", 20)

    addressLen = len(address)*fontSize/2
    ticket_codeLen = len(ticket_code)*fontSize/2

    d.text(((QRwidth-addressLen)/2.0, 10), address, fill=(0, 0, 0),font=font)
    d.text(((QRwidth-ticket_codeLen)/2.0, 50), ticket_code, fill=(0, 0, 0),font=font)

    fontSize1 = 10
    helpLen = len(tc.help) * fontSize1 / 2
    resultImg.paste(QRimage,(0,80))
    font1 = ImageFont.truetype("fonts/9654.ttf", 10)
    d.text(((QRwidth-helpLen)/2.0, QRheight+70), tc.help, fill=(0, 0, 0), font=font1)
    resultImg.save(path)
    os.remove(_path)
    return path
GenerateTicket("123","123","Zhopa ilyi 5/10")

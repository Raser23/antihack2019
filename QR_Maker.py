import pyqrcode as pqr
import png
Ticket_number = "A0123"  # str(input())
ticket = pqr.create(Ticket_number, mode='binary')
ticket.png('ticket.png', scale=10)
ticket.show()

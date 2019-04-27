class Adress(object):
    def __init__(self, town=None, willage=None, home=None):
        self.town = str(town)
        self.willage = str(willage)
        self.home = str(home)


ticket_town = 'A'  # str(input())
ticket_willage = 'B'  # str(input())
ticket_home = 'C'  # str(input())
ticket_adress = Adress(ticket_town, ticket_willage, ticket_home)
ticket_number = 'A0123'  # str(input())
ticket = open("ticket1.html", "w")
ticket.write('''<!DOCTYPE html> 
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Ticket</title>
</head>
<body>

<h1>
    УРАЛСИБ
</h1>

<h1>
    Адрес: 
    г. ''' + str(ticket_adress.town)+''', ул. ''' + str(ticket_adress.willage) + ''', д. ''' + str(ticket_adress.home) + '''
</h1>

<h1>
    ''' + ticket_number + '''
</h1>

<img src = "ticket.png"></img> 

</body>
</html>''')
ticket.close()

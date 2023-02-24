oper = print_last5_operation()
    date = oper[numb]['date']
    thedate = datetime.fromisoformat(date)
    date_format = thedate.strftime('%d.%m.%Y')
    description = oper[numb]['description']
    if 'from' in oper[numb]:
      from1 = oper[numb]['from']
    else:
      from1 = ''
    to1 = oper[numb]['to']
    summa = oper[numb]['operationAmount']['amount']
    currency = oper[numb]['operationAmount']['currency']['name']
    message = f'{date_format} {description}\n{from1[0:16]} -> {to1}\n{summa} {currency}\n'
    return message
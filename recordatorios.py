
recordatorios = [
    ['2021-01-01', '11:00', 'Levantarse y ejercitar'],
    ['2021-07-15', '13:00', 'No hacer nada es feriado'],
    ['2021-09-18', '16:00', 'Ramadas']
]


recordatorios.append(['2021-02-02', '06:00', 'Empezar el año'])

for evento in recordatorios:
    if evento[0] == '2021-07-15':
        evento[0] = '2021-07-16'  


recordatorios = [evento for evento in recordatorios if 'Trabajo' not in evento[2]]


recordatorios.append(['2021-12-24', '22:00', 'Cena de Navidad'])
recordatorios.append(['2021-12-31', '22:00', 'Cena de Año Nuevo'])


recordatorios.sort()


for evento in recordatorios:
    print(evento)



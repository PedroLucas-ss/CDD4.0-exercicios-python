quantMacas = int(input("Quatas macas voce vai comprar?"))
valorMacas = 1.30
if quantMacas >= 12:
    valorMacas = 1.0
    print(f'voce deve pagar ${valorMacas * quantMacas}')
else:
    print(f'voce deve pagar ${valorMacas * quantMacas}')


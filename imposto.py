numero = float(input('Digite o valor Bruto: '))
inss = numero * 11/100
if (inss >= 482.93 ):
    real = 482.93
else:
    real = inss
   
Pissqn = numero - real
issqn = Pissqn * 3/100
Pissqn = numero - real - issqn

if (numero <= 1787.77 ):
    num = 'Não desconta inposto'
    vp = 0
elif (numero <= 2679.29):
    num = 'Aliquota 7,5%'
    vp = numero * 7.5/100 - 134.08 
elif (numero <= 3572.43):
    num = 'Aliquota 15%'
    vp = numero * 15/100 - 335.03
elif (numero <= 4463.81):
    num = 'Aliquota 22,5%'
    vp = numero * 22.5/100 - 602.96
elif (numero > 4463.81):
    num = 'Aliquota 27,5%'
    vp = numero * 27.5/100 - 826.15

vl = numero - real - issqn - vp

print("Vapor do Inss: ", round(real, 2))
print("Vapor do Issqn: ", round(issqn, 2))
print("Vapor do inposto: ", round(vp, 2), num)
print("Valor liquido: ", round(vl, 2))


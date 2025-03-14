def altura_estimada_mulher(aj, idade):
   return ((1.83 * aj) + (0.24 * idade) + 84.88)/100

def altura_estimada_homem(aj, idade):
   return ((2.02 * aj) + (0.04 * idade) + 64.19)/100     

def peso_estimado_homem(cb, aj): 
    return aj * 1.19 + cb * 3.14 - 86.82

def peso_estimado_mulher(cb, aj):
   return aj * 1.09 + cb * 2.68 - 65.51

idade = int(input('Digite a idade do paciente: '))
sexo = input('Qual o sexo do paciente?(M/F) ').strip().upper()

cb = float(input('Digite CB: '))
cp = float(input('Digite CP: '))
aj = float(input('Digite AJ: '))

if sexo == 'F':
    altura_estimada = altura_estimada_mulher(aj, idade)
    peso_estimado = peso_estimado_mulher(cb, aj) 
elif sexo == 'M':
   altura_estimada = altura_estimada_homem(aj, idade)
   peso_estimado = peso_estimado_homem(cb, aj) 
else: 
   print('Valor incorreto.')
   altura_estimada = None
   peso_estimado = None

imc = peso_estimado / (altura_estimada * altura_estimada)

print(altura_estimada)
print(peso_estimado)
print(imc)

lista_pacientes = []

def mostrar_menu_principal():
    print("----- MENU PRINCIPAL -----")
    print("(1) Adicionar paciente")
    print("(2) Mostrar paciente")
    print("(3) Reavaliar")
    print("(4) Excluir paciente")
    print("(0) Sair")
    return input("Digite uma opção válida: ")

def altura_estimada(aj, idade, sexo):
    if sexo.upper() == 'F':
        if 9 <= idade <= 19:
            altura = (1.9 * aj) + (0.2 * idade) + 80
        elif 18 <= idade <= 60:
            altura = (1.83 * aj) + (0.24 * idade) + 84.88
        elif idade > 60:
            altura = (1.76 * aj) + (0.25 * idade) + 85
        else:
            return "Idade fora do intervalo válido."
    
    elif sexo.upper() == 'M':
        if 9 <= idade <= 19:
            altura = (2.0 * aj) + (0.15 * idade) + 85  
        elif 18 <= idade <= 60:
            altura = (2.02 * aj) + (0.04 * idade) + 64.19
        elif idade > 60:
            altura = (1.98 * aj) + (0.05 * idade) + 65  
        else:
            return "Idade fora do intervalo válido."
    
    else:
        return "Erro: Sexo inválido! Use 'M' ou 'F'."
    
    return round((altura/100), 2)

def peso_estimado(aj, cb, sexo, etnia, idade):
   if 19 <= idade <= 59:
        if sexo == 'f' and etnia == 'negra':
            peso = (1.24 * aj) + (2.97 * cb) - 82.48
        elif sexo == 'f' and etnia == 'branca':
            peso = (1.01 * aj) + (2.81 * cb) - 66.04
        elif sexo == 'm' and etnia == 'negra':
            peso = (1.09 * aj) + (3.14 * cb) - 83.72
        elif sexo == 'm' and etnia == 'branca':
            peso = (1.19 * aj) + (3.14 * cb) - 86.82
        else:
            return "Erro: Etnia inválida. Escolha entre 'negra' ou 'branca'."
    
   elif 60 <= idade <= 80:
        if sexo == 'f' and etnia == 'negra':
            peso = (1.50 * aj) + (2.58 * cb) - 84.22
        elif sexo == 'f' and etnia == 'branca':
            peso = (1.09 * aj) + (2.68 * cb) - 65.51
        elif sexo == 'm' and etnia == 'negra':
            peso = (0.44 * aj) + (2.86 * cb) - 39.21
        elif sexo == 'm' and etnia == 'branca':
            peso = (1.10 * aj) + (3.07 * cb) - 75.81
        else:
            return "Erro: Etnia inválida. Escolha entre 'negra' ou 'branca'."
    
   else:
        return "Erro: Idade fora das faixas disponíveis (19-80 anos)."
    
   return round(peso, 2)

def cadastrar_paciente():
   nome = input('Digite o nome: ')
   idade = int(input('Digite a idade do paciente: '))
   sexo = input('Qual o sexo do paciente?(M/F) ').strip().upper()
   etnia = input('Digite a etnia: ')

   cb = float(input('Digite CB: '))
   cp = float(input('Digite CP: '))
   aj = float(input('Digite AJ: '))

   if sexo == 'F':
      altura_estimada = altura_estimada(aj, idade, sexo)
      peso_estimado = peso_estimado(aj, cb, sexo, etnia, idade)
   elif sexo == 'M':
      altura_estimada = altura_estimada(aj, idade, sexo)
      peso_estimado = peso_estimado(aj, cb, sexo, etnia, idade) 
   else: 
      print('Valor incorreto.')
      altura_estimada = None
      peso_estimado = None

   imc = peso_estimado / (altura_estimada * altura_estimada)

   cadastro_paciente = {
      "nome": nome,
      "Idade": idade,
      "Sexo": sexo,
      "C.B": cb,
      "C.P": cp,
      "A.J": aj,
      "Peso estimado": peso_estimado,
      "Altura estimada": altura_estimada,
      "IMC": imc      
   }
   lista_pacientes.append(cadastro_paciente)
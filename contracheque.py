import os
os.system('cls')
def VerificaNome():
    nome = input("Nome: ").strip()
    while True:
        if not nome:
            os.system('cls')
            print("É necessário digitar algum nome para continuar.")
            nome = input("Nome: ").strip()
        elif len(nome) < 3:
            os.system('cls')
            print("Este nome é muito curto.")
            nome = input("Nome: ").strip()
        elif all(part.isalpha() or part.isspace() for part in nome.split()):
            return nome
        else:
            os.system('cls')
            print("Um nome não possui números, favor digite corretamente.")
            nome = input("Nome: ").strip()

def VerificaSalario():
    while True:
        try:
            salario = float(input("Digite seu salário: R$"))
            while salario < 0:
                os.system('cls')
                salario = float(input("Digite um salário válido, acima de 0: R$"))
            return salario
        except ValueError:
            os.system('cls')
            print("Por favor digite seu salário corretamente")

def calculoHoraExtra(salario):
    setores = [1, 2]
    while True:
        try:
            horasextras = float(input("Digite seu número de horas extras no formato (Horas.Minutos): "))
            horas = int(horasextras)
            minutos = round((horasextras - horas)*100)
            while (horasextras < 0) or (minutos >= 60):
                os.system('cls')
                horasextras = float(input("Digite um valor válido, acima de 0 e no formato (Horas.Minutos): "))
                horas = int(horasextras)
                minutos = round((horasextras - horas)*100)
            banco = 0
            while True:
                try:
                    setor = int(input("Digite seu setor [1] para Admnistração e [2] para Operacional: "))
                    while setor not in setores:
                        os.system('cls')
                        setor = int(input("Favor digite somente um desses setores [1] para Admnistração e [2] para Operacional: "))
                    break
                except ValueError:
                    os.system('cls')
                    print("Por favor digite seu setor corretamente")
            horascalculadas = horas
            if horas >= 4:
                for c in range(4, horas):
                    banco += 60
                banco += minutos
                horascalculadas = 4
            if setor == 1:
                salario += (horascalculadas * 4.50)
            else:
                salario += (horascalculadas * 3.50)
            return salario, banco
        except ValueError:
            os.system('cls')
            print("Por favor, digite corretamente")

lista = []
print("Bem-Vindo ao nosso sistema de cadastro! (outra vez)")
while True:
    print("\nO que deseja fazer?\n[1] Cadastrar Funcionário\n[2] Listar Funcionários\n[3] Sair do Programa")
    escolha = input("Digite aqui: ")
    if escolha == "1":
        print()
        a = VerificaNome()
        b = VerificaSalario()
        c = calculoHoraExtra(b)
        lista.append([a, *c])
        os.system('cls')
        print("Funcionário adicionado!")
    elif escolha == "2":
        os.system('cls')
        for c in lista:
            print(f"Nome: {c[0]} \nSalário: R${c[1]:.2f} \nBanco de Horas: {c[2]} minuto(s)\n")
        if len(lista) == 0:
            print("Não existe nenhum cadastro, por favor cadastre algum funcionário para listar.")
    elif escolha == "3":
        print("\nSistema encerrado.")
        break
    else:
        os.system('cls')
        print("Escolha inválida, por favor digite novamente.")
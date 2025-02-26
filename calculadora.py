def adicao(a, b):
  return a + b

def subtracao(a, b):
  return a - b

def divisao(a, b):
  return a / b

def multiplicacao(a, b):
  return a * b

def calculadora():
  print("Calculadora iniciada.")
  while True:
    operacao = input("""As operações são:
             1: Adição
             2: Subtração
             3: Divisão
             4: Multiplicação

             0: Sair
             Escolha a operação: """)

    if operacao == "0":
            print("Saindo da calculadora...")
            break

    if operacao in ["1", "2", "3", "4"]:
        num1 = float(input("Ok. Agora por favor escolha o primeiro número: "))
        num2 = float(input("E o segundo número: "))

        if operacao == "1":
            print(f"{num1} + {num2} = {adicao(num1, num2)}")

        elif operacao == "2":
            print(f"{num1} - {num2} = {subtracao(num1, num2)}")

        elif operacao == "3":
            print(f"{num1} / {num2} = {divisao(num1, num2)}")

        elif operacao == "4":
            print(f"{num1} * {num2} = {multiplicacao(num1, num2)}")
        else:
            print("Escolha uma das operações válidas")

calculadora()

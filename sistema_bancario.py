menu = """

[d] depositar
[s] sacar
[e] extrato
[q] encerrar
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
        escolha = input(menu)

        if escolha == "d":
            valor = float(input("Informe o valor para o depósito: "))

            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n REALIZADO!"

            else:
                print("Valor inválido.")

        elif escolha == "s":
            valor = float(input("Informe o valor do saque: "))
            saques_ultrapassados = numero_saques >= LIMITE_SAQUES
            saldo_ultrapassado = valor > saldo
            limite_ultrapassado = valor > limite

            if saldo_ultrapassado:
                print("Saldo suficiente.")

            elif limite_ultrapassado:
                print(" Valor ultrapassa o limite.")

            elif saques_ultrapassados:
                print("Operação falhou! Número máximo de saques excedido.")

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1

            else:
                print("Operação falhou! O valor informado é inválido.")

        elif escolha == "e":
            print("\n ___________ Extrato ____________")
            print("f\n Saldo: R$ {saldo:.2f}")
            print("\n ________________________________")

            if not extrato:
                print("Não foram realizadas movimentações.")

        elif escolha == "q":
            break

        else:
            print("Operação inválida. Tente Novamente.")        

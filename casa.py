valor_casa = float(input("Qual é o valor da casa a comprar? "))
anos_a_pagar = float(input("Deseja pagar em quantos anos? "))
salario = float(input("Qual é o seu salário? "))
n_messes=anos_a_pagar*12
prestacao = valor_casa/n_messes
if prestacao <= (0.3*salario):
    print("Empréstimo aprovado")
else:
    print("Empréstimo reecusada")

kwh=float(input("Quantos KWH SÃO CONSUMIDOS? ")) 
tipo_instalacao = input("""Qual é o tipo de instalação
    Digite "R" para residencial
    Digite "C" para comercial
    Digite "I" para industrial
    Digite aqui: """)
preco_a_pagar=0
#Residencial
if tipo_instalacao == "R":
    if kwh<=500:#Menor ou igual a 500 kwh
        preco_a_pagar=0.4*kwh
    else:#Maior a 500 kwh
        preco_a_pagar=0.65*kwh
    print(f"Você deve pagar R$: {preco_a_pagar} de energia elétrica. ")
#Comercial
elif tipo_instalacao == "C":
    if kwh<=1000:#Menor ou igual a 1000 kwh
        preco_a_pagar=0.55*kwh
    else:#Maior a 1000 kwh
        preco_a_pagar=0.6*kwh
    print(f"Você deve pagar R$: {preco_a_pagar} de energia elétrica. ")
#Industrial
elif tipo_instalacao == "I":
    if kwh<=5000:#Menor ou igual a 5000 kwh
        preco_a_pagar=0.55*kwh
    else:#Maior a 5000 kwh
        preco_a_pagar=0.6*kwh
    print(f"Você deve pagar R$: {preco_a_pagar} de energia elétrica. ")    
else:
    print("Opção inválida, por favor digite novamente.")

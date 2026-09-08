cigarros_p_dia=int(input("Quantos cigarros você fuma por dia? "))
anos_fumados=int(input("Você fumou por quantos anos? "))
cigarros_fumados=cigarros_p_dia*360*anos_fumados
MINUTOS_P_CIGARRO = 10
MINUTOS_P_DIA=60*24
minutos_perdidos = MINUTOS_P_CIGARRO*cigarros_fumados
dias_perdidos = minutos_perdidos/MINUTOS_P_DIA
print(f"Você teve uma redução de {dias_perdidos} dias de vida")

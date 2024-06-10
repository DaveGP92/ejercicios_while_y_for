#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

#Fórmula para calcular el interés compuesto (anual) = Cf = Ci * (1 + %interés(en decimales)/1(año)) ^1(año)*t(tiempo). 

# ejemplo:
# capital_final = 6000 * (1 + (0.03/1))**(1*t(años))


print("Este programa te permitirá saber cuánta ganancia anual obtendrás por los intereses de un capital inicial.")

capital_inicial = float(input("Escriba la cantidad de dinero a invertir:\n"))

interes_anual = float(input("Porcentaje de interés anual:\n")) / 100

num_years = int(input("Número de años:\n"))


for i in range(1, num_years + 1):
    capital_final = capital_inicial * (1 + interes_anual)**(1 * num_years)
    print((f"En el año {i} su capital inicial fue ${round(capital_inicial)}, y su capital final fue = ${round(capital_final)}. Su rentabilidad fue de {round(capital_final - capital_inicial)}"))
    capital_inicial = capital_final
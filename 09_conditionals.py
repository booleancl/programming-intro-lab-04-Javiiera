# Tenemos expresiones que se pueden evaluar en terminos booleanos 
# ó dicótomicos 
# Ejemplo:

print(10 > 9)

# Esto nos permite hacer ejecuciones condicionales, por ejemplo 

def is_adult(age):
   if age >= 18:
    return True
   else:
    return False 

Gaby_age = 20
Yaritza_age = 20

# Estas siguientes intrucciones las podríamos leer como:
# "Si (if) el resultado de is_adult ejecutada con la variable Gaby_age
# es verdadero, entonces el programa imprime '¿Quieres una cerveza?'
# DE OTRO MODO (else), imprime 'Cantemos chuchuwa'"

if is_adult(Yaritza_age):
    print("¿Quieres una cerveza?")
else:
    print("¿Cantemos chuchuwa?")

# El if es una abreviacion del "else if", nos permite seguir evaluando expresiones
# Podemos tener tantas como necesitemos    

if Yaritza_age > Gaby_age:
    print("Yaritza es mayor que gaby")
elif Yaritza_age < Gaby_age:
    print("Gaby es mayor que Yaritza")
else:
    print("Tienen la misma edad Gaby y Paola")    
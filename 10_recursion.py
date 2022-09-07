import time

# Es perfectamente posible llamar una funcion dentro de otr
# Lo hicimos cuando calculamos el volumen de un cilindro

# Pero tambien es perfectamente posible que una funcion se llame a si misma
# Esto es una tecnica muy poderosa para ciertos problemas 

# Funcion  conteo regresivo
# Es una funcion que se llama asi mismo
def countdown(number):
    if number <= 0:
        print("KABUMM")
    else:
        print(number)
        time.sleep(0.5)
        countdown(number - 1) 

countdown(5) 

# Otro ejemplo para hacer una sumatoria
def super_sum (number):
  if number <= 0:
    return number
  else:
   return number + super_sum(number -1)

print(super_sum(10))    
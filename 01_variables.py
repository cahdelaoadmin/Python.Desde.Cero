# Variables en Python

my_string_variable = "My string variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenación de variables
print(my_string_variable, my_int_variable, my_bool_variable)

print(type(print("My cadena de texto"))) # Tipo Non type
print(my_string_variable,my_int_to_str_variable,my_bool_variable)
print("Este es el valor de:",my_bool_variable)

# Funciones del sistema
print(len(my_string_variable))

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Carlos", "Hernández", "Charlie", 51
print("me llamo:", name, surname, ". Mi edad es:", age, ". Y mi alias es:", alias)

# Inputs
"""
name = input('¿Cuál es tu nombre?: ')
age = input('¿Cuántos años tienes? ')

print(name)
print(age)
"""

# Cambiamos su tipo
name = 35
age = "Charlie"
print(name)
print(age)

# Frozamos el tipo
address: str = "Mi dirección"
address = 32
print(type(address))
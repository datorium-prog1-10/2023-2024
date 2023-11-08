names = ['Anna', 'Oskars', 'Jennifer']
numbers = ['123456789', '987654321', '852123674']

new_name = input('Uzraksti vārdu: ')
new_number = input('Uzraksti numuru: ')

names.append(new_name)
numbers.append(new_number)

# UZDEVUMS 1 
# Izvadīt šos datus lai konsolē ir sekojoši:
# Anna: 123456789
# Oskars: 987654321
# Jenifer: 852123674

for i in range(len(names)):
    print(f"{names[i]}: {numbers[i]}")

# UZDEVUMS 2
# Izveido kodu lai lietotāja(s) var pievienot jaunu kontaktu un numuru

# UZDEVUMS 3
# Izveido kodu kas ļaus dzēst noteiktu cilvēku no tel grālamatas

name_to_delete = input('Name to delete: ')

index_to_remove = names.index(name_to_delete)

names.pop(index_to_remove)
numbers.pop(index_to_remove)

for i in range(len(names)):
    print(f"{names[i]}: {numbers[i]}")
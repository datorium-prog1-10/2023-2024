phonebook_with_tuple = [('Anna', '123456789'), ('Oskars', '987654321'), ('Anna', '852147963')]

name_to_add = input('Enter new name: ')
number_to_add = input('Enter new number: ')

phonebook_with_tuple.append((name_to_add, number_to_add))
print(phonebook_with_tuple)

name_to_delete = input('Enter name to delete: ')

# UZDEVUMS 4
# turpni izstrādāt šo kodu lai tas idzēš gan vārdu gan numuru no saraksta

for row in phonebook_with_tuple:
    if name_to_delete in row:
        phonebook_with_tuple.remove(row)
        break

print(phonebook_with_tuple)

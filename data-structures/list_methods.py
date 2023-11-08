shopping_list = ['milk', 'avokado']
shopping_list.extend(['maize', 'kartupeļi', 'saldējums'])
print(shopping_list)

item_to_delete = input("Kuru elementu gribi izdēst?: ")

if item_to_delete in shopping_list:
    shopping_list.remove(item_to_delete)
else:
    print(f"Could not find {item_to_delete} in your list")

print(shopping_list)

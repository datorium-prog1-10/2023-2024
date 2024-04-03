import json

phonebook = []

def add_contact():
    name = input("Uzraksti vārdu: ")
    number = input("Uzraksti numuru: ")
    person = {
        "name": name,
        "number": number
    }
    phonebook.append(person)
    print("Kontakts ir veiksmīgi pievienots!")

def print_contacts():
    for person in phonebook:
        print(f"{person['name']}: {person['number']}")

def find_contact():
    name = input("Kuru kontaktu gribi atrast? ")
    found = False
    for person in phonebook:
        if person['name'] == name:
            print(f"Found {person['name']}: {person['number']}")
            found = True
            break
    if not found:
        print(f"Kontaktu {name} nevaru atrast!")

def delete_contact():
    pass

def save_contacts():    
    with open("phonebook.json", "w") as file:
        json.dump(phonebook, file)

def exit_app():
    save_contacts()
    print("Bye, thanks for using our phonebook!")
    exit()

def load_data():
    global phonebook
    try:
        with open('phonebook.json', 'r') as file:
            phonebook = json.load(file)
    # exception ir kļūda
    except:
        print('Notika kļūda, phonebook dati nav ielādēti!')
        phonebook = []

def main():
    load_data()
    while True:
        choice = input("1-pievienot, 2-izvadīt, 3-atrast, 4-izdzēst, 5-iziet: ")

        if choice == "1":
            add_contact()            
        elif choice == "2":
            print_contacts()            
        elif choice == "3":
            find_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            exit_app()
        else:
            print("Nebija pareiza izvēle")

main()
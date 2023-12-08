f = open("demofile.txt", "a")
f.write("100\n")
f.close()

#open and read the file after the appending:
f = open("demofile.txt", "r")
print(f.read())
f.close()

# UZDEVUMS
# Izveido failu "counter.txt"
# Ieraksti ar Python skaitļus no 1 līdz 100

f = open("counter.txt", "w")
for i in range (1, 101):   
    f.write(f"{str(i)}\n")
f.close

with open('counter.txt', 'w') as f:
    for i in range(1, 101):
        f.write(str(i) + '\n')

# UZDEVUMS 3
# Izveido ar Python failu ar sādu saturu
# name1, surname1, email1
# name2, surname2, email2
# ...
# name10, surname10, email10

with open("contacts.csv", "w") as file:
    for i in range(1, 11):
        file.write(f"name{i}, surname{i}, email{i}\n")
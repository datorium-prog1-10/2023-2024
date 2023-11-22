# Skolēni, katrs skolēns pieder kādai klasei, un katram skolēnam ir
# vairākas atzīmes, katra atzīme ir par kādu priekšmetu

students = ["Anna", "Oskars"]
# Anna (10b): 8 (Matemātika), 5 (Fizika), 9 (Bioloģija), 7 (Ķīmija), 10 (Programmēšana)
# Oskars (10c): 9 (Matemātika), 6 (Fizika), 8 (Programmēšana)

# DICTIONARY (VĀRDNĪCA)

words = {
    "cat": "kaķis",
    "table": "galds",
    "computer": "dators"
}

dictionary = {
    "kaķis": "dzīvnieks ar 4 kājām un ūsam",
    "dators": "eletroniska ierice, ..."
}

grades = {
    "Fizika": 9, 
    "Matematika": 8, 
    "Bioloģija": 7
}

# ATRISINĀJUMS PARASTAIS
school = {
    "Anna": {
        "Matemātika": 9,
        "Fizika": 10,
        "Bioloģija": 6,
        "Programmēšana": 8
    },
    "Oskars": {
        "Matemātika": 6,
        "Fizika": 8,
        "Bioloģija": 10
    } 
}

# print(f"Skolēna atzīme: {school['Anna']['Programmēšana']}")


# ATRISINĀJUMS PILNS
students = [
    {
        "name": "Anna",
        "class": "10b",
        "grades": {
            "Matemātika": 9,
            "Fizika": 10,
            "Bioloģija": 6,
            "Programmēšana": 8
        }
    },
    {
        "name": "Oskars",
        "class": "10c",
        "grades": {
            "Matemātika": 10,
            "Fizika": 6,
            "Bioloģija": 8        
        }
    }
]

for student in students:
    print(f"{student['name']} no {student['class']}")
    for subject, grade in student["grades"].items():
        print(f"{subject}: {grade}")
    print("----------------------")

for student in students:
    print(f"{student['name']} no {student['class']}")
    for subject in student["grades"]:
        print(f"{subject}: {student['grades'][subject]}")
    print("----------------------")


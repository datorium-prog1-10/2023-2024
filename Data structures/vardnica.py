students = [
    {
        "name": "Anna",
        "class": "10a",
        "grades": {
            "Matemātika": 9, 
            "Bioloģija": 10, 
            "Fizika": 8
        }
    }, 
    {
        "name": "Oskars",
        "class": "10c",
        "grades": {
            "Matemātika": 6, 
            "Bioloģija": 10, 
            "Fizika": 8,
            "Programmēšana": 9
        }
    }
]

for student in students:
    print(f"{student['name']} ({student['class']}) {student['grade']}")

# Anna (10a) 9


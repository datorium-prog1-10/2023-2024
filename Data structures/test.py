students = [
    {
        'name': 'Anna',
        'class': '10a',
        'grade' : { 
            "Fizika": 9,
            'Matemātika': 10,
            'Bioloģija': 8
        }
    },
    {
        'name': 'Oskars',
        'class': '10c',
        'grade': { 
            "Fizika": 6,
            'Matemātika': 10,
            'Bioloģija': 8,
            'Programmēšana': 9
        }
    },
]
# Anna (10a) 9
for student in students:
    print(f"{student['name']} ({student['class']}) {student['grade']}")
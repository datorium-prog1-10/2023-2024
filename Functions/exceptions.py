while True:
    try:
        a = float(input('Ievadi pirmo skaitli: '))
        b = float(input('Ievadi otro skaitli: '))
        print(f'Summa ir {a + b}')
    except Exception as kludas_apraksts:
        print(f'Kļuda: {kludas_apraksts}')





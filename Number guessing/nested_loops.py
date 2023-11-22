results = []
for i in range(0, 10):
    for j in range(0, 10):
        results.append(i*j)
    print(f"i={i} {results}")
    results.clear()
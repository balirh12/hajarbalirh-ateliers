def divide_conquere(data):
    i = 0
    export = []
    for i in range(0, 9, 3):
        export.append(data[i:i + 3])
    return export


print(divide_conquere([1, 2, 3, 4, 5, 6, 7, 8, 9]))
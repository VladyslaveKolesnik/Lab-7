def pascal(n):
    row = [1]
    for i in range(n):
        print(row)
        new_row = [1]
        for j in range(len(row) - 1):
            new_row.append(row[j] + row[j + 1])
        new_row.append(1)
        row = new_row
try:
    n = int(input())
    pascal(n)
except:
    pass
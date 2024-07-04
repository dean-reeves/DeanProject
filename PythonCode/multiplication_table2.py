# multiplication_table2.py
def multiplication_table(n):
    table = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(i * j)
        table.append(row)
    return table

if __name__ == "__main__":
    n = int(input("Enter the size of the multiplication table: "))
    table = multiplication_table(n)
    for row in table:
        print("\t".join(map(str, row)))

start = int(input("Enter the starting table: "))
end = int(input("Enter the ending table: "))

print("Multiplication table from", start, "to", end, ":")
for i in range(1, 11):
    for j in range(start, end + 1):
        result = j * i
        print(j, "*", i, "=", result, end=" ")
    print()

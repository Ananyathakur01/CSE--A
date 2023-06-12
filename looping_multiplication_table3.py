start = int(input("Enter the starting table: "))
end = int(input("Enter the ending table: "))

for i in range(start, end + 1):
    for j in range(1, i + 1):
        result = i * j
        print(f"{i}*{j} = {result}")
    print()

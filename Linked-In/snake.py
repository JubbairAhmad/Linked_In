def print_snake_pattern(size):
    num = 1
    for i in range(size):
        if i % 2 == 0:
            for j in range(num, num + size):
                print(j, end=" ")
            num += size
        else:
            for j in range(num + size - 1, num - 1, -1):
                print(j, end=" ")
            num += size
        print()
while True:
    size = int(input())
    if  1 <= size <= 9:
        break
    else:
        print("Invalid input")

size = int(input())
print_snake_pattern(size)


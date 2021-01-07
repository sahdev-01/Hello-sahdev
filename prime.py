number = int(input("Enter number(till) prime numbers to be printed: "))
for n in range(1, number):
    flag = True
    for i in range(2, n):
        if n % i == 0:
            flag = False
            break
    if flag:
        print(n)
print("The above mentioned are Prime numbers till " + str(number))

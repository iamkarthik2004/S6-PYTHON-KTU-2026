n = int(input("Enter the number of terms: "))

if n<=0:
    print("Invalid Input. Please Enter a Positive Number")
else:
    a = 0
    b = 1

    print("Fibonacci Series: ", end="")

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

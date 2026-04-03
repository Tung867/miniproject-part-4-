def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Sum:", add(a, b))
    print("Difference:", subtract(a, b))

    if a > b:
        print("a is bigger")
        print("difference:", a - b)
    else:
        print("b is bigger")
        print("difference:", b - a)

if __name__ == "__main__":
    main()
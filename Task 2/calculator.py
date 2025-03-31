def main():
    print("+++++CALCULATOR++++++")
    print()
    print("1. + ")
    print("2. - ")
    print("3. * ")
    print("4. / ")
    print("=====================")
    num1=float(input("Enter first number: \t"))
    num2=float(input("Enter second number: \t"))
    sign = input("Enter you oprator example 1 for '+' ")
    try:
        if sign=="1":
            print("Answer",add(num1,num2))
        elif sign=="2":
            print("Answer",minus(num1,num2))
        elif sign=="3":
            print("Answer",multiply(num1,num2))
        elif sign=="4":
            print("Answer",format(divide(num1,num2),".2f"))
        else:
            print("Invalid operator")
    except ZeroDivisionError:
        print("can not divide number by zero")


def add(num1, num2):
    return num1 + num2

def minus(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2


if __name__=="__main__":
    main()
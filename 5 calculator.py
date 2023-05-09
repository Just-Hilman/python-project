# define the functions needed
def add(a, b):
    answer = a + b
    print(str(a) + "+" + str(b) + "=" + str(answer))

def sub(a, b):
    answer = a - b
    print(str(a) + "-" + str(b) + "=" + str(answer))

def mul(a, b):
    answer = a * b
    print(str(a) + "*" + str(b) + "=" + str(answer))

def div(a, b):
    answer = a / b
    print(str(a) + "/" + str(b) + "=" + str(answer))

print("A. Addition")
print("B. Substraction")
print("C. Multiplication")
print("D. Divission")
print("E. Exit")

choice = input("Input your choice: ")
if choice == "A" or choice =="a":
    print("Addition")
    a = int(input("Input the first number: "))
    b = int(input("Input the second number: "))
    add(a, b)
elif choice == "B" or choice =="b":
    print("Addition")
    a = int(input("Input the first number: "))
    b = int(input("Input the second number: "))
    sub(a, b)
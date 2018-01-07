# Question 1
from fractions import Fraction


def rationaln(num1, num2):
    print("The fraction is: ")
    print(Fraction(num1 / num2))


n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
rationaln(n1, n2)


# Question 3
def print_hello():
    print("Hello")


def print_world():
    print("World")


def default():
    print("Wrong choice")


def Zeroerror():
    print("Cannot be zero")


switch = {
    1: print_hello,
    2: print_world
}
inp = input("enter a value: ")

try:
    val = int(inp)
    switch[inp]()

except ValueError:
    print("Wrong value")
except:
    default()

# Question 4
my_list = list(range(0, 100))
print(my_list)


def prime(x):
    for i in range(2, x):
        if (x % i == 0):
            break
        else:
            return x


fp = open("d://newfile.txt", "w")
fp.write(str(list(filter(prime, my_list))))
fp.close()

# Question 5
with open("D:\\newfile1.txt", "a") as fp:
    fp.write(str(list(filter(prime, my_list))))

# Question 6
with open("D:\\newfile.txt", "r")as fp:
    print(fp.read())

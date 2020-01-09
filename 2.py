print(list(range(5)))
for i in range(5):
    print("Hello world!")

names = ["haim", "moshe", "david"]
for i in range(len(names)):
    print("current name is: " +names[i] )
for name in names:
    print(name)
a = 0
b = 5
while a < b:
    print(a)
    a = a + 1
for i in range(10):
    print(i)
else:
    print("loop finished ok")

for i in range (1,100):
    print ("boom")
    if i %7 ==0:
        continue
    print("number is: " + str(i))

def my_function():
    print("this function is printing!")
    print("another text to print")


def square_of_number(number):
    result = number * number
    return result
for i in range(1, 10):
    current_sq = square_of_number(i)
    print(current_sq)
def check_between_range():
    input_from_user = input("please enter value from 1 to 10:")
    my_number = int(input_from_user)
    if 1 < my_number and my_number < 10:
        print("in range")
    else:
        print("not in range")





# basic data types
# integer floating point string list dictionaries tuples sets booleans
# int float str list dict tup set bool
# 3 2.3 'sammy' [10,'hrlo',23.4] {"mykey":"Value", "name":"frankie"} (10,'hello',574.4) {"A","B"} ture/false
def ord_seq():
    my_list=[1,2,3]
    print(my_list)
    my_list = ["string",45,45.5]
    print(len(my_list))
    #we can use indexing and slicing as strings
    #
    #
    #
    another_list = [1,2,3,4]
    x = my_list + another_list

    x[0] = 4
    print(x)

    x.append('loh') # add item to the end of the list
    f = x
    print(f)
    popped = x.pop()
    print(popped)
    g = x
    print(g)
    #other useful methods - .sort / .reverse
    x.sort()
    print(x)
    x.reverse()
    print(x)
    return

def printing():
    #string interpolation
    #.format()
    print("this is a string {}".format("inserted"))
    print("the {} {} {}".format("brown","quick","fox"))
    print("the {q} {b} {f}".format(b="brown",q="quick",f="fox"))
    #float formating
    result = 100/777
    print(result)
    print("the restult was {r}".format(r=result))
    print("the result was {r:1.3f}".format(r=result))
    print("the result was {r:10.3f}".format(r=result))
    print("the result was {r:1.7f}".format(r=result))

    # other method
    name = "jose"
    print(f"hello, his name is {name}")
    print(f"name = {name} is {result:1.3f} years old")

def more_strings():
    #immutability
    name = "Sam"
    print(name)
    # name[0] = 'P' # wrooong
    last_letters = name[1:]
    final = 'P' + last_letters # string concatenation
    print(final)
    multi = 'z' * 10
    print(multi)
    #built in methods
    x = "hello world"
    print(x)
    print(type(x))
    x = x.upper()
    print(x)
    print(type(x))
    x = x.split()
    print(x)
    print(type(x))
    x = "hello world"
    x = x.split('l')
    print(x)
    print(type(x))

    return


def strings():
    # character h e l l o
    # indx      0 1 2 3 4
    # rev ind    0 -4 -3 -2 -1
    # slicing in python
    # [start:stop:step]
    # start: is a numerical index for the slice start
    # stop: is the index you will go up to (but not include)
    # step: is the size of the jump you take
    a = "hello\n"  # \n new line \t tab
    print(a)
    b = "hell bo\n"
    print(b)
    x = len(b)
    print(x)
    my_string = "Hello World"
    print(my_string[0])
    print(my_string[8])  # pos index pos
    print(my_string[-1])  # neg index pos

    # slicing

    my_string = "abcdefghijk"
    print(my_string[2:])
    print(my_string[:3])
    print(my_string[2::2])
    print(my_string[::-1])
    return


def variables():
    b = 0
    a = 5
    print(a)
    a = 10
    print(a)
    print(type(a))
    b = a + b
    print(b)
    return


def basics():
    addition = 2 + 1
    print("addition = ", addition)
    substraction = 2 - 1
    print("substraction = ", substraction)
    division = 7 / 4
    print("division = ", division)
    remainder = 7 % 4
    print("remainder = ", remainder)
    power = 2 ** 3
    print("2 ^ 3 == ", power)
    complex = (2 + 10) * (10 + 3)
    print("more complex shit = ", complex)
    return


if __name__ == '__main__':
    basics()
    print("-----")
    variables()
    print("-----")
    strings()
    print("-----")
    more_strings()
    print("-----")
    printing()
    print("-----")
    ord_seq()

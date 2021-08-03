import sys  # first, we import the module

args = sys.argv  # we get the list of arguments

if len(args) != 3:
    print("The script should be called with two arguments, the first and the second number to be multiplied")

else:
    first_num = float(args[1])  # convert arguments to float
    second_num = float(args[2])

    product = first_num * second_num

    print("The product of " + args[1] + " times " + args[2] + " equals " + str(product))

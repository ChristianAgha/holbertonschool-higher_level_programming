#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    import sys

    operators = ["+", "-", "*", "/"]

    if len(sys.argv) == 4:

        a, op, b = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])

        if op in operators:
            if sys.argv[2] is "+":
                print("{:d} {:s} {:d} = {:d}".format(a, op, b, a + b))

            if sys.argv[2] is "-":
                print("{:d} {:s} {:d} = {:d}".format(a, op, b, a - b))

            if sys.argv[2] is "*":
                print("{:d} {:s} {:d} = {:d}".format(a, op, b, a * b))

            if sys.argv[2] is "/":
                print("{:d} {:s} {:d} = {:d}".format(a, op, b, int(a / b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

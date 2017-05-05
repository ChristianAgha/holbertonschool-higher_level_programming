#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 3:
        add_res = int(sys.argv[1])
        for n in range(2, len(sys.argv)):
            add_res += int(sys.argv[n])
        print(add_res)

#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(0)
    else:
        total_sum = 0
        for num in sys.argv[1:]:
            total_sum += int(num)
        print(total_sum)

import sys
import numpy as np

def main():
    array1_str = sys.argv[1]
    array2_str = sys.argv[2]
    start_pos = int(sys.argv[3])
    array1 = np.array([int(x) for x in array1_str.split(',')])
    array2 = np.array([int(x) for x in array2_str.split(',')])
    if start_pos < 0 or start_pos >= len(array1):
        print("Error: start position is out of list")
        return
    array1[start_pos:start_pos + len(array2)] = array2
    print(array1)


if __name__ == "__main__":
    main()

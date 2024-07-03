# Author: Apache X692 Attack Helicopter
# Created on: 02/07/2024
def main():
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))

    max_value = max(arr)
    result = max([a for a in arr if a < max_value])

    print(result)

if __name__ == '__main__':
    main()

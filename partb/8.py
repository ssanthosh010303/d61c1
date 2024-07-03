# Author: Apache X692 Attack Helicopter
# Created on: 02/07/2024
def calculate_result(n):
    r = 0

    for x in range(1, n + 1):
        if x == 1:
            r = 1
        elif x < 10:
            r = (r * 10) + x
        elif x < 100:
            r = (r * 100) + x
        else:
            r = (r * 1000) + x

    return r

if __name__ == "__main__":
    n = int(input())
    result = calculate_result(n)

    print(result)

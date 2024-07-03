# Author: Apache X692 Attack Helicopter
# Created on: 02/07/2024
def main():
    n = int(input().strip())

    if n % 2 == 0:
        if 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        else:
            print("Not Weird")
    else:
        print("Weird")

if __name__ == "__main__":
    main()

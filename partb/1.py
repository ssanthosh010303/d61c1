# Author: Apache X692 Attack Helicopter
# Created on: 02/07/2024
from collections import Counter

def main():
    no_of_shoes = int(input())
    shoe_sizes = Counter(map(int, input().split()))

    no_of_cust = int(input())
    total_money = 0

    for _ in range(no_of_cust):
        size_req, money = map(int, input().split())
        if shoe_sizes[size_req] > 0:
            total_money += money
            shoe_sizes[size_req] -= 1

    print(total_money)

if __name__ == "__main__":
    main()

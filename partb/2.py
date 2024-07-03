# Author: Apache X692 Attack Helicopter
# Created on: 02/07/2024
from collections import Counter

def main():
    s = input().strip()
    sorted_s = sorted(s)
    cnt = Counter(sorted_s).most_common(3)

    for item in cnt:
        result = ' '.join(map(str, item))
        print(result)

if __name__ == "__main__":
    main()

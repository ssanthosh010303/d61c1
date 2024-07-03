# Author: Apache X692 Attack Helicopter
# Created on: 02/07/2024
def main():
    limits = input("Enter x, y, z limits: ").split()

    x_limit = int(limits[0])
    y_limit = int(limits[1])
    z_limit = int(limits[2])

    target_sum = int(input("Enter target sum: "))

    result_list = []

    for i in range(x_limit + 1):
        for j in range(y_limit + 1):
            for k in range(z_limit + 1):
                if i + j + k != target_sum:
                    result_list.append([i, j, k])

    print(result_list)

if __name__ == "__main__":
    main()

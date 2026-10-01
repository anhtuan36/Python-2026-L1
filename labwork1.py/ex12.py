
def print_pattern(m, n):
    for i in range(m):
        if i == 0 or i == m - 1:
            print("* " * n)
        else:
            if n > 1:
                print("* " + "  " * (n - 2) + "* ")
            else:
                print("* ")

m = int(input("Enter rows (m): "))
n = int(input("Enter cols (n): "))
print_pattern(m, n)
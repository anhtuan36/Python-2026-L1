
def extract_even(l):
    result = []
    for x in l:
        if x % 2 == 0:
            result.append(x)
    return result

raw = input("Enter integers separated by space: ")
l = [int(x) for x in raw.split()]
print(extract_even(l))
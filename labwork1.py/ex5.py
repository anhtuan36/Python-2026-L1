
colors = ["Blue", "Yellow", "Black", "Red", "White"]
fav = input("What is your favorite color? ")

found = False
for i in range(len(colors)):
    if colors[i].lower() == fav.lower():
        print(f"Your color is at index {i} in my list")
        found = True
        break

if not found:
    print("Sorry, I could not find your color")
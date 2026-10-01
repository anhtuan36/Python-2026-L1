
c = float(input("Enter the temperature in Celsius? "))
f = c * 9 / 5 + 32
print(f"{int(c) if c.is_integer() else c} (C) = {f:.1f} (F)")
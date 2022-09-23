weight = int(input("Weight: "))

unit = input("(K)ilos (P)ounds: ")
newUnit=""

if unit.upper() == "K":
    newUnit = "Pound"
    converted = weight* 2.20462
elif unit.upper() == 'P':
    newUnit = "Kilos"
    converted = weight/ 2.20462
else:
    print("You entered incorrect value")

print(f"Weight in {newUnit} is {converted}")
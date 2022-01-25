weight = float(input("Enter your weight : "))
unit = input("(K)gs or (L)bs : ")

if unit.upper() == 'K':
    weight_in_lbs = weight / 0.45
    print(f"Your weight in lbs: {weight_in_lbs}")
else:
    weight_in_kg = weight * 0.45
    print(f"Your weight in Kg : {weight_in_kg}")

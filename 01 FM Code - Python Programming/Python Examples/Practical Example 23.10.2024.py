guests = int(input("How many guests are invited?: "))
number_of_slices = int(input("How many slices will each guest need?: "))

def amount_of_pizza(guests , number_of_slices) :
    total = guests * number_of_slices
    return total

total = amount_of_pizza(guests , number_of_slices)

print(f"The required amount of slices will be {total} for {guests} guests")
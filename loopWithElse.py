food = ["murga", "bakra", "machli", "panner", "steak"]

# print(len(food))

for items in range(len(food)):
    if food[items] == "panner masala":
        print(f"Your item is found at {items+1}")
        break

else:
    print("Your item is not found in our list")


def print_line():
    return print("----------------------------------------------")


# 1.1 Schleifen
array_names = ["Max", "Lisa", "Bob", "Daniel", "Luca"]

for array_name in array_names:
    print(array_name)

print_line()

counter = 0
while counter < len(array_names):
    print(array_names[counter])
    counter += 1

# 1.2 If-Else
ages = [18, 5, 19, 29, 15, 16]

print_line()
for age in ages:
    if age < 16:
        print(f"Sie haben angeben, dass Sie {age} Jahre alt sind. Sie dürfen noch keinen Alkohol kaufen")
    elif 16 <= age <= 18:
        print("Sie dürfen nur Getränke mit wenig Alkohol kaufen.")
    else:
        print("Sie dürfen alles kaufen.")


# 1.3 If-Else
def check_age(age):
    if age < 16:
        return -1
    elif 16 <= age < 18:
        return 0
    else:
        return 1


print_line()
print(check_age(12))
print(check_age(17))
print(check_age(12345))

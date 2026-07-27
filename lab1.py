text = input("Enter a string: ")

if len(text.strip()) == 0:
    print("No empty string allowed")
elif text == text[::-1]:
    print("It's a palindrome")
else:
    print("It's not a palindrome")

lst1 = [1, 3, 4, "Ahmed"]
lst2 = [5, 6, 7, "Ali"]

lst1.extend(lst2)
print(lst1)

list_alpha = ["Ahmed", "Youssef", "Dina", "Ali", "Amr"]

list_alpha.sort()

result = {}

for name in list_alpha:
    key = name[0].upper()

    if key not in result:
        result[key] = []

    result[key].append(name)

print(result)

name = input("Enter your name: ")

if len(name.strip()) == 0 or name.isdigit():
    print("Enter a valid name")
else:
    email = input("Enter your email: ")

    if len(email.strip()) == 0:
        print("Email cannot be empty")
    elif "@" not in email:
        print("Invalid email")
    else:
        print("Name:", name)
        print("Email:", email)

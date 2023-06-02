def Greet(language):
    if language == "Hindi":
        return "Namaskar"
    elif language == "English":
        return "Hello"
    else:
        return "Wrong Language"


x = input("Enter your Language\n")
print(Greet(x))

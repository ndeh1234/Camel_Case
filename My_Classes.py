




classList = [] # Defining an empty class list

name = input("Enter name of class(empty to exit): ")  # Getting input from user

while name != "": # While that goes over the empty list and appends a name
     classList.append(name)

     name = input(" Enter name of class(empty to exit): ")

print("\nList of all classes you're taking this semester is: ") # Printing list of all classes

for Class_Name in classList: # For loop that goes over the class list and printing class list

    print(Class_Name)
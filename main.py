def add_person():
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")

    person = {"name": name, "age": age, "email": email}
    return person


print("Hi, welcome to the Contact Managent System.")
print()
command = input("You can 'Add', 'Delete' or 'Search': ").upper()
people = []

if command == "ADD":
    person = add_person()
    people.append(person)
    print("Person added.")
elif command == "DELETE":
    pass
elif command == "SEARCH":
    pass
else:
    print("Invalid command.")

print(people)    
# Phonebook Dictionary

phonebook = {
    "Simran": {"phone": "9876543210", "email": "simran@gmail.com", "city": "Darbhanga"},
    "Aman": {"phone": "9876543211", "email": "aman@gmail.com", "city": "Patna"},
    "Priya": {"phone": "9876543212", "email": "priya@gmail.com", "city": "Delhi"},
    "Rahul": {"phone": "9876543213", "email": "rahul@gmail.com", "city": "Mumbai"},
    "Neha": {"phone": "9876543214", "email": "neha@gmail.com", "city": "Patna"},
    "Riya": {"phone": "9876543215", "email": "riya@gmail.com", "city": "Darbhanga"},
    "Arjun": {"phone": "9876543216", "email": "arjun@gmail.com", "city": "Kolkata"},
    "Sneha": {"phone": "9876543217", "email": "sneha@gmail.com", "city": "Delhi"}
}

# b) Search Contact
def search_contact(name):
    if name in phonebook:
        print(phonebook[name])
    else:
        print("Contact not found")

# c) Add Contact
def add_contact(name, phone, email, city):
    phonebook[name] = {
        "phone": phone,
        "email": email,
        "city": city
    }
    print(name, "added successfully")

# d) Delete Contact
def delete_contact(name):
    if name in phonebook:
        del phonebook[name]
        print(name, "deleted successfully")
    else:
        print("Contact not found")

# e) Contacts in a City
def contacts_in_city(city):
    result = []
    for name, details in phonebook.items():
        if details["city"].lower() == city.lower():
            result.append(name)
    return result

# f) Display All Contacts
def display_all():
    print("\nPHONEBOOK")
    print("-" * 40)
    for name, details in phonebook.items():
        print(f"Name : {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
        print(f"City : {details['city']}")
        print("-" * 40)

# g) Testing Functions

# Search Contact (3 calls)
search_contact("Simran")
search_contact("Rahul")
search_contact("John")

# Add Contact (3 calls)
add_contact("Karan", "9999999991", "karan@gmail.com", "Patna")
add_contact("Pooja", "9999999992", "pooja@gmail.com", "Delhi")
add_contact("Vikas", "9999999993", "vikas@gmail.com", "Mumbai")

# Delete Contact (3 calls)
delete_contact("Aman")
delete_contact("Pooja")
delete_contact("Unknown")

# Contacts in City (3 calls)
print(contacts_in_city("Patna"))
print(contacts_in_city("Delhi"))
print(contacts_in_city("Mumbai"))

# Display All Contacts
display_all()
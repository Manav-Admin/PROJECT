new_dict={1: 'hello', 2: 'world', 3: 'python', 4: 'programming'}
print(new_dict)
print(new_dict[1])
print(new_dict[2])
print(new_dict[3])

new_dict[5] = 'new'
print(new_dict)


new_dict[1] = 'new_hello'
print(new_dict[1])

# Create a dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Access values
print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])

# Add a new key-value pair
person["job"] = "Engineer"

# Update a value
person["age"] = 26

# Remove a key-value pair
del person["city"]

# Loop through dictionary
for key, value in person.items():
    print(key, ":", value)

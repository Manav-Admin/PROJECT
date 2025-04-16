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

def first_non_repeating_char(s):
    char_count = {}

    # Count characters
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the first non-repeating character
    for char in s:
        if char_count[char] == 1:
            return char

    return None

# Example usage
string = "aabbcddex"
result = first_non_repeating_char(string)
print("First non-repeating character:", result)

def two_sum(nums, target):
    num_map = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i

    return None
numbers = [2, 7, 11, 15]
target = 9
result = two_sum(numbers, target)
print("Indices of two numbers that add up to target:", result)

def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    count = {}

    for char in s1:
        count[char] = count.get(char, 0) + 1

    for char in s2:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False

    return True


'''
CHALLENGE: Family Dictionary
    1. Define a dictionary that contains information about several members of your family.
    Use the following example as a template:
    my_family = {
    "sister": {
        "name": "Krista",
        "age": 42
    },
    "mother": {
        "name": "Cathie",
        "age": 70
    }
}
'''
my_family = {
    "oldest_sister": {
        "name": "Olivia",
        "age": 22
    },
    "middle_sister": {
        "name": "Sydney",
        "age": 18
    },
    "youngest_sister": {
        "name": "Emma",
        "age": 16
    },
    "mother": {
        "name": "Malisha",
        "age": 45
    },
    "father": {
        "name": "David",
        "age": 48
    }
}

'''
    2. Using a dictionary comprehension, produce output that looks like the following example.
    "Krista is my sister and is 42 years old"
'''
# Dictionary Comprehension is a method for transforming one dictionary into another dictionary
new_family = {value["name"].capitalize():f'is my {key} and is {value["age"]} years old' for (key, value) in my_family.items()}

for (key, value) in new_family.items():
    print(f'{key} {value.replace("_", " ")}')
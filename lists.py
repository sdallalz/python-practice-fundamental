# List operations and data structures

# Basic list operations
colors = ["red", "pink", "blue", "purple", "green"]

print("First color:", colors[0])
print("Slice (1 to 3):", colors[1:3])
print("Last color:", colors[-1])

colors.append("white")
colors.insert(0, "black")
print("Updated colors:", colors)


# Custom function to add items to a list
def custom_add_to_list(items, value):
    if isinstance(value, int):
        items.insert(0, value)
    elif isinstance(value, str):
        items.append(value)
    return items


custom_add_to_list(colors, "orange")
custom_add_to_list(colors, 4)
print("After custom add:", colors)


# Working with numbers list
numbers = [70, 45, 12, 6]
print("Numbers:", numbers)

last_number = numbers.pop()
print("Popped number:", last_number)
print("After pop:", numbers)

numbers.reverse()
numbers = numbers + [16, 18]
print("Final numbers:", numbers)


# Sorting with priority
def sort_by_priority(jobs, priority):
    paired = list(zip(priority, jobs))
    paired_sorted = sorted(paired)
    return [job for _, job in paired_sorted]


jobs = ["rest", "read book", "wash"]
priority = [3, 1, 2]
print("Sorted jobs:", sort_by_priority(jobs, priority))


# Nested data example
people = [
    {
        "name": "Ali",
        "age": 18,
        "skills": ["html", "php"]
    },
    {
        "name": "Sana",
        "age": 25,
        "skills": ["html", "php"]
    }
]

# Add a new skill to Ali
for person in people:
    if person["name"] == "Ali":
        person["skills"].append("django")

print("People data:", people)

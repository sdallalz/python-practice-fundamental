# Object-Oriented Programming (OOP) examples


class Car:
    def __init__(self, name, model, color, door_count):
        self.name = name
        self.model = model
        self.color = color
        self.door_count = door_count

    def get_full_description(self):
        return f"{self.name} {self.model} | Color: {self.color} | Doors: {self.door_count}"

    def is_family_car(self):
        return self.door_count >= 4

    def change_color(self, new_color):
        self.color = new_color


# Example usage
bmw = Car("BMW", "730", "black", 4)
print(bmw.get_full_description())
bmw.change_color("red")
print("After color change:", bmw.get_full_description())
print("Family car?", bmw.is_family_car())


class Student:
    def __init__(self, name, age, courses, address):
        self.name = name
        self.age = age
        self.courses = courses  # list of dicts: {"name": ..., "score": ...}
        self.address = address

    def passed_courses(self, pass_score=12):
        passed = []
        for course in self.courses:
            if course["score"] >= pass_score:
                passed.append(course["name"])
        return passed


# Example usage
sana_courses = [
    {"name": "computer", "score": 20},
    {"name": "graphic", "score": 11},
]

sana = Student("Sana", 25, sana_courses, "1632 Lions Gate")
print("Passed courses:", sana.passed_courses())

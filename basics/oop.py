class animal:
    def eat():
        print("eating...")

    def __init__(self, age, color) -> None:
        self.age = age
        self.color = color


dog = animal(25, "black")

print(dog.age)

# required more theoritical knowledge of OOP

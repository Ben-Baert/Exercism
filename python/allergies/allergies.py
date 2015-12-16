def to_binary_reversed(x):
    return bin(x % 256)[2:][::-1]

class Allergies:
    allergens = [
    "eggs",
    "peanuts",
    "shellfish",
    "strawberries",
    "tomatoes",
    "chocolate",
    "pollen",
    "cats"]

    def __init__(self, score):
        self.score = score
        self.list = [
        allergen for allergen, conversion in zip(Allergies.allergens, to_binary_reversed(score))
        if conversion == "1"
        ]

    def is_allergic_to(self, allergen):
        if allergen in self.list:
            return True
        return False
from string import ascii_uppercase, digits
from random import choice

class Robot:
    @staticmethod
    def _name_generator():
        return (choice(ascii_uppercase) +
        choice(ascii_uppercase) +
        choice(digits) +
        choice(digits) +
        choice(digits))

    def reset(self):
        self.name = self._name_generator

    def __init__(self):
        self.name = self._name_generator()
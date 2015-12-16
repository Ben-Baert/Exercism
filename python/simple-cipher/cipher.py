from string import ascii_lowercase
import re

class Caesar:
    def __init__(self, key='d'):
        self.key = key

    @staticmethod
    def _clean(input_string):
        return re.sub('[^a-z]*','', input_string.lower())

    def _letter_generator(self, current_index, letter, encode=True):
        current_key = self.key[current_index % len(self.key)]
        if encode:
            current_key = (ascii_lowercase.index(current_key) + ascii_lowercase.index(letter)) % 26
        else:
            current_key = (ascii_lowercase.index(letter) - ascii_lowercase.index(current_key)) % 26
        return ascii_lowercase[current_key]


    def encode(self, value):
        return ''.join([self._letter_generator(index, letter) for index, letter in enumerate(self._clean(value))])

    def decode(self, value):
        return ''.join([self._letter_generator(index, letter, encode=False) for index, letter in enumerate(value)])


class Cipher(Caesar):
    pass
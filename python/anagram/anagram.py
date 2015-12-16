from collections import Counter
from functools import partial

def is_anagram(word, candidate):
    word = word.lower()
    candidate = candidate.lower()
    return Counter(word) == Counter(candidate) and word != candidate

def detect_anagrams(word, candidates):
    return [candidate
            for candidate in candidates
            if is_anagram(word, candidate)]
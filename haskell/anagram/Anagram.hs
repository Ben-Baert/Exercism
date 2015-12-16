module Anagram (anagramsFor) where
import Data.List(sort)
import Data.Char(toLower)

anagramsFor :: String -> [String] -> [String]
anagramsFor word candidates = filter (match) candidates
    where
        match y = loweredWord /= lower y && sortedWord == sort (lower y)
        lower x = map toLower x
        loweredWord = lower word
        sortedWord = sort loweredWord
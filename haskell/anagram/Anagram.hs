module Anagram (anagramsFor) where
import Data.List(sort)
import Data.Char(toLower)

anagramsFor :: String -> [String] -> [String]
anagramsFor word candidates = filter match candidates
    where
        match candidate = loweredWord /= lower candidate && sortedWord == sort (lower candidate)
        lower = map toLower 
        loweredWord = lower word
        sortedWord = sort loweredWord

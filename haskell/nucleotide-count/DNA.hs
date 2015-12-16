module DNA (count, nucleotideCounts) where
import Data.Map(Map, fromList)
import Data.List(group, sort)

type NucleotideMap = Map Char Int

count :: Char -> [Char] -> Int
count x y = length (filter (==checkDNA x) (map checkDNA y))

nucleotideCounts :: [Char] -> NucleotideMap
nucleotideCounts x = fromList [(nucleotide, count nucleotide x) | nucleotide <- dna]

checkDNA :: Char -> Char
checkDNA x
    | x `elem` dna = x
    | otherwise = error ("invalid nucleotide " ++ show x)

dna :: String
dna = "ATCG"
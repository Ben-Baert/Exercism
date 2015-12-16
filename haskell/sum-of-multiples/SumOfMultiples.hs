module SumOfMultiples(sumOfMultiples, sumOfMultiplesDefault) where

sumOfMultiples :: [Int] -> Int -> Int
sumOfMultiples multiples maxRange = sum [x | x <- [1..pred maxRange], any((==0) . mod x) multiples]

sumOfMultiplesDefault :: Int -> Int
sumOfMultiplesDefault maxRange = sumOfMultiples [3, 5] maxRange
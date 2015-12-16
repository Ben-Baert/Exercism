module DNA (hammingDistance) where

hammingDistance :: String -> String -> Int
hammingDistance x y = length $ filter id $ zipWith (/=) x y
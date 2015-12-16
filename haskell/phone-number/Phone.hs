module Phone(areaCode, number, prettyPrint) where
import Data.Char(isDigit)

areaCode :: String -> String
areaCode x = take 3 $ number x

number :: String -> String
number x
    | length x' == 10 = x'
    | length x' == 11  && head x' == '1' = tail x'
    | otherwise = replicate 10 '0'
        where x' = filter isDigit x

prettyPrint :: String -> String
prettyPrint x = "(" ++ p1 ++ ") " ++ p2 ++ "-" ++ p3
    where
        (p1,rest) = splitAt 3 (number x)
        (p2,p3) = splitAt 3 rest
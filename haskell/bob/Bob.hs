module Bob(responseFor) where
import Data.Char(isLetter, isSpace, toUpper)

responseFor :: String -> String
responseFor x
    | all isSpace x = "Fine. Be that way!"
    | any isLetter x && map toUpper x == x = "Whoa, chill out!"
    | last x == '?' = "Sure."
    | otherwise = "Whatever."
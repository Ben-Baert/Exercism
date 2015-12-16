module DNA (toRNA) where

toRNA :: String -> String
toRNA = map transcribe where
    transcribe 'C' = 'G'
    transcribe 'G' = 'C'
    transcribe 'A' = 'U'
    transcribe 'T' = 'A'
    transcribe x = error (show x ++ " is not a nucleotide.")
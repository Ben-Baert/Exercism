module SpaceAge (Planet(..), ageOn) where
import Data.Maybe

data Planet = Earth
            | Mercury
            | Venus
            | Mars
            | Jupiter
            | Saturn
            | Uranus
            | Neptune
            deriving (Eq, Show)

type Seconds = Double
type Years = Double

ageOn :: Planet -> Seconds -> Years
ageOn planet seconds = seconds / planetSeconds
    where
        planetSeconds = case planet of
            Earth   ->   31557600
            Mercury ->    7600544
            Venus   ->   19414149
            Mars    ->   59354033
            Jupiter ->  374355659
            Saturn  ->  929292363
            Uranus  -> 2651370019
            Neptune -> 5200418560
        --  _       -> error (show planet ++ " is not a planet in our solar system.")
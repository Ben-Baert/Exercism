module Accumulate(accumulate) where

accumulate :: (a -> b) -> [a] -> [b]
accumulate _ [] = []
accumulate func (x:xs) = func x : accumulate func xs
module Main where

import Test.HUnit
import System.Exit
import Control.Monad
import #_#class_dojogen#_#


main = do counts <- runTestTT tests
          when ((errors counts, failures counts) /= (0, 0)) $
              exitWith (ExitFailure 1)

tests = TestList [#_#camel_dojogen#_#Test]

#_#camel_dojogen#_#Test = TestList [
        "#_#camel_dojogen#_# 1 retorna -1" ~: 
             #_#camel_dojogen#_# 1 ~=? -1, 
        "#_#camel_dojogen#_# 2 retorna -1" ~: 
             #_#camel_dojogen#_# 2 ~=? -1
    ]


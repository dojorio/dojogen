module Main where

import Test.HUnit
import System.Exit
import Control.Monad
import ___class_dojogen___


main = do counts <- runTestTT tests
          when ((errors counts, failures counts) /= (0, 0)) $
              exitWith (ExitFailure 1)

tests = TestList [___camel_dojogen___Test]

___camel_dojogen___Test = TestList [
        "___camel_dojogen___ 1 retorna -1" ~: 
             ___camel_dojogen___ 1 ~=? -1, 
        "___camel_dojogen___ 2 retorna -1" ~: 
             ___camel_dojogen___ 2 ~=? -1
    ]


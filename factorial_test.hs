import System.CPUTime
import Text.Printf

-- Naive recursive factorial
factorialNaive :: Integer -> Integer
factorialNaive 0 = 1
factorialNaive n = n * factorialNaive (n - 1)

-- Tail recursive factorial
factorialTail :: Integer -> Integer
factorialTail n = go n 1
  where go 0 acc = acc
        go n acc = go (n-1) (n*acc)

-- Built-in product version
factorialProduct :: Integer -> Integer
factorialProduct n = product [1..n]

-- Timing function
timeFactorial :: (Integer -> Integer) -> Integer -> String -> IO ()
timeFactorial func n name = do
    start <- getCPUTime
    let result = func n
    let digits = length (show result)
    result `seq` return ()  -- Force evaluation
    end <- getCPUTime
    let diff = (fromIntegral (end - start) :: Double) / (10^12)
    printf "%s factorial(%d): %.6fs, %d digits\n" name n diff digits

main :: IO ()
main = do
    let testValues = [100, 1000, 5000, 10000]
    
    mapM_ testValue testValues
  where
    testValue n = do
        putStrLn $ "\nTesting n = " ++ show n
        timeFactorial factorialTail n "Tail Recursive"
        timeFactorial factorialProduct n "Product"
        -- Skip naive for large values to avoid stack overflow
        if n <= 1000 
            then timeFactorial factorialNaive n "Naive Recursive"
            else putStrLn "Naive Recursive: Skipped (would overflow)"


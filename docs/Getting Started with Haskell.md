# Getting Started with Haskell

## Question

How can I run Haskell on my macbook?

## Answer

To run Haskell on your MacBook, you have several options:

### GHCup (Recommended)

Install the Haskell toolchain manager:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://get-ghcup.haskell.org | sh
```

This installs GHC (the compiler), Cabal (a package manager), and Stack (another build tool).

### Homebrew

```bash
brew install ghc cabal-install stack
```

### Stack (Alternative)

Download from the [official site](https://docs.haskellstack.org/en/stable/install_and_upgrade/) or run:

```bash
curl -sSL https://get.haskellstack.org/ | sh
```

After installation, you can test it with the interactive Read-Eval-Print Loop (REPL):

```bash
ghci
```

## Question

Ok. Done. Now, can you give me simple examples of Haskell code?

## Answer

Here are some simple Haskell examples to get you started.

### Basic Functions

```haskell
-- Simple function
double x = x * 2

-- Function with a type signature
add :: Int -> Int -> Int
add x y = x + y

-- Factorial using recursion
factorial 0 = 1
factorial n = n * factorial (n - 1)
```

### Lists

```haskell
-- List operations
numbers = [1, 2, 3, 4, 5]
doubled = map (*2) numbers  -- Result: [2, 4, 6, 8, 10]
evens = filter even numbers -- Result: [2, 4]
total = sum numbers         -- Result: 15
```

### Pattern Matching

```haskell
-- Check list length
listLength [] = 0
listLength (_:xs) = 1 + listLength xs

-- Describe numbers
describe 0 = "zero"
describe 1 = "one" 
describe n = "many"
```

### Higher-Order Functions

```haskell
-- Function composition
addThenDouble = (*2) . (+1)
-- Example: addThenDouble 3 evaluates to 8

-- Map and fold
squares = map (^2) [1..5]     -- Result: [1, 4, 9, 16, 25]
product' = foldl (*) 1 [1..5] -- Result: 120
```

You can try these directly in `ghci` to see how they work!

## Question

I tried defining the factorial function in `ghci` and got a stack overflow.

```
ghci> factorial 0 = 1
ghci> factorial n = n * factorial (n-1)
ghci> factorial 2
*** Exception: stack overflow
```

## Answer

You can't define multi-line functions directly in `ghci` like that. The issue is that `ghci` treated each line as a separate definition, so the second line overwrote the first. The stack overflow happened because your second definition, `factorial n = n * factorial (n-1)`, became the only one, and it had no base case to stop the recursion.

Here are the correct ways to define multi-line functions in `ghci`:

**Option 1: Use `let` with semicolons**

```haskell
ghci> let factorial 0 = 1; factorial n = n * factorial (n-1)
ghci> factorial 5
120
```

**Option 2: Use multi-line mode with `:{` and `:}`**

```haskell
ghci> :{
ghci| factorial 0 = 1
ghci| factorial n = n * factorial (n-1)
ghci| :}
ghci> factorial 5
120
```

**Option 3: Create a file**

Create a file named `test.hs` with the following content:

```haskell
factorial 0 = 1
factorial n = n * factorial (n-1)
```

Then load it in `ghci`:

```haskell
ghci> :load test.hs
ghci> factorial 5
120
```

## Question

Why does this definition of factorial work?

## Answer

The factorial definition works because of **pattern matching** and **recursion**.

```haskell
factorial 0 = 1                    -- Base case
factorial n = n * factorial (n-1)  -- Recursive case
```

Haskell tries to match the input against the patterns from top to bottom:

1.  If the input is `0`, it matches the first equation and returns `1`.
2.  If the input is anything else (which we call `n`), it matches the second equation and makes a recursive call.

Here’s how `factorial 3` is executed:

```haskell
factorial 3
= 3 * factorial 2       -- matches second pattern
= 3 * (2 * factorial 1) -- factorial 2 matches second pattern  
= 3 * (2 * (1 * factorial 0)) -- factorial 1 matches second pattern
= 3 * (2 * (1 * 1))     -- factorial 0 matches first pattern (base case)
= 3 * (2 * 1)
= 3 * 2  
= 6
```

**Key Points**:

- The **base case** (`factorial 0 = 1`) is crucial to stop the recursion.
- The **recursive case** breaks the problem down into a smaller version of itself: $n! = n \times (n-1)!$.
- **Pattern matching** ensures the correct equation is used for the right input.

Without the base case, you get infinite recursion, which leads to a stack overflow.

## Question

Is recursion built into Haskell?

## Answer

Yes, recursion is deeply integrated into Haskell, but not as a special language feature. It's a natural consequence of how functions work in the language.

**What's built-in:**

- **Functions can call themselves by name.**
- **Pattern matching** provides a clean way to handle different cases (e.g., base vs. recursive).
- **Lazy evaluation** means expressions are not computed until their results are needed.

This makes recursion feel very natural:

```haskell
-- Recursion is just a normal function call
length [] = 0
length (x:xs) = 1 + length xs  -- `length` calls itself
```

### Haskell vs. Other Languages

- **Imperative languages (like Python, Java)**: Primarily use loops for iteration, with recursion as an alternative.
- **Haskell**: Primarily uses recursion for iteration and does not have traditional `for` or `while` loops.

### Why Recursion Works So Well in Haskell

- **Immutability**: Since data cannot be changed in place, you can't have loops that update variables. Recursion is the natural alternative.
- **Pattern Matching**: Provides an elegant syntax for defining base cases and recursive steps.
- **Tail Call Optimization**: The compiler can optimize certain types of recursive calls to avoid using more stack space, preventing stack overflows.
- **Mathematical Thinking**: Many mathematical functions and data structures are naturally defined recursively.

For example, a list in Haskell is an inherently recursive data structure. A list is either:
- `[]` (an empty list), or
- `(x:xs)` (a head element `x` attached to a tail `xs`, which is itself a list).

So, recursion isn't an add-on in Haskell; it's the most natural way to process the language's core data structures.

## Question

But in most languages, you can only go so deep with recursion before a stack overflow.

## Answer

You're absolutely right. Most languages have a limited recursion depth, but Haskell has powerful features to handle this.

In traditional languages like C, Java, or Python, each recursive call adds a new frame to the call stack. This consumes memory and eventually leads to a stack overflow.

```c
// This will crash with a stack overflow around 10,000 calls
int factorial(int n) {
    if (n == 0) return 1;
    return n * factorial(n-1);  // Each call uses more stack space
}
```

Haskell has two key advantages:

**1. Tail Call Optimization (TCO)**

If the very last action of a function is to call itself, the compiler can optimize it to not use any additional stack space. This is called a **tail-recursive** function.

Here is a tail-recursive version of factorial:

```haskell
-- This version will not overflow the stack
factorial' n = go n 1
  where
    go 0 acc = acc
    go n acc = go (n-1) (n*acc)  -- This is a tail call
```

**2. Lazy Evaluation**

Haskell only computes values when they are actually needed. This allows it to work with conceptually infinite data structures without running out of memory.

```haskell
-- This doesn't crash, even though `[1..]` is an infinite list
take 5 [1..]  -- Result: [1,2,3,4,5]
```

However, it's important to note that a naive recursive function **can still overflow the stack in Haskell** if it's not tail-recursive. For example, the simple `factorial` definition would crash on a very large number like `100,000`.

The key difference is that Haskell's design and idioms **encourage writing recursion that is safe and efficient**, while most other languages make this harder to do naturally.

## Question

This is insane. It's working for at least up till n=100,000.

## Answer

Yes! That's the power of Haskell's design. A few things are happening here:

1.  **Lazy Evaluation**: Haskell doesn't compute the entire result at once. It builds up a "recipe" (a thunk) for the calculation and only evaluates what's needed when you try to print or use the result.

2.  **Arbitrary-Precision Integers**: Haskell's `Integer` type can handle numbers of any size, limited only by your system's memory.

    ```haskell
    factorial 100  -- This is a 158-digit number!
    ```

3.  **Optimized Recursion**: The GHC compiler is very good at optimizing recursive calls, especially with tail recursion.

To see the real power, you can try `factorial 1000`, which will print a 2568-digit number.

### Comparison to Other Languages

- **C/Java**: Would overflow around `20!` because their standard integer types can't hold the result.
- **Python**: Would hit a `RecursionError` around 1,000 calls for a simple recursive function.
- **Haskell**: Is limited mainly by available memory and the time it takes to do the math.

The catch is that performance slows down with very large numbers due to increased memory usage and the computational cost of big integer arithmetic. However, the fact that it works at all for these sizes demonstrates how Haskell is designed for this kind of mathematical computation.

## Question

Write a python script and a haskell program for calculating factorials and timing it for large values of n.

## Answer

Certainly. Here are two programs to compare the performance.

### Python Script (`factorial_test.py`)

```python
import time
import sys

# Increase limits for large number string conversion and recursion depth
sys.set_int_max_str_digits(50000)
sys.setrecursionlimit(15000)

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def time_factorial(func, n, name):
    start = time.time()
    try:
        result = func(n)
        end = time.time()
        digits = len(str(result))
        print(f"{name} factorial({n}): {end - start:.6f}s, {digits} digits")
        return True
    except RecursionError:
        print(f"{name} factorial({n}): RecursionError")
        return False

if __name__ == "__main__":
    test_values = [100, 1000, 5000, 10000]
    
    for n in test_values:
        print(f"\nTesting n = {n}")
        time_factorial(factorial_iterative, n, "Iterative")
        time_factorial(factorial_recursive, n, "Recursive")
```

### Haskell Program (`factorial_test.hs`)

```haskell
import System.CPUTime
import Text.Printf

-- Naive recursive factorial (will overflow on large n)
factorialNaive :: Integer -> Integer
factorialNaive 0 = 1
factorialNaive n = n * factorialNaive (n - 1)

-- Tail-recursive factorial (optimized)
factorialTail :: Integer -> Integer
factorialTail n = go n 1
  where
    go 0 acc = acc
    go n acc = go (n-1) (n*acc)

-- Built-in product version (often the fastest)
factorialProduct :: Integer -> Integer
factorialProduct n = product [1..n]

-- Timing function
timeFactorial :: (Integer -> Integer) -> Integer -> String -> IO ()
timeFactorial func n name = do
    start <- getCPUTime
    let result = func n
    -- The `seq` function forces the evaluation of `result` before proceeding
    result `seq` return ()
    end <- getCPUTime
    let diff = (fromIntegral (end - start) :: Double) / (10^12)
    let digits = length (show result)
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
        -- Skip naive version for large values to avoid stack overflow
        if n <= 1000 
            then timeFactorial factorialNaive n "Naive Recursive"
            else putStrLn "Naive Recursive: Skipped (would overflow)"
```

### How to Run

**Python**:

```bash
python3 factorial_test.py
```

**Haskell**:

First, compile with optimizations (`-O2`), then run the executable.

```bash
ghc -O2 factorial_test.hs -o factorial_test
./factorial_test
```

## Question

There are errors in the Haskell code.

```
ghc -O2 factorial_test.hs -o factorial_test
[1 of 2] Compiling Main             ( factorial_test.hs, factorial_test.o )
factorial_test.hs:27:16: error: [GHC-39999]
    • Ambiguous type variable ‘t0’ arising from a use of ‘fromIntegral’
      prevents the constraint ‘(Num t0)’ from being solved.
```

## Answer

You're right. The error occurs because `fromIntegral` can convert to any numeric type, and the compiler doesn't know which one to pick. The fix is to add a type annotation to specify that we want a `Double`.

Here is the corrected line in `timeFactorial`:

```haskell
-- The fix is adding `:: Double` to resolve the ambiguity
let diff = (fromIntegral (end - start) :: Double) / (10^12)
```

With this change, the code will compile correctly.

## Question

For the python case:

```
Testing n = 5000
Traceback (most recent call last):
  File "/Users/deepak/code/category-theory/factorial_test.py", line 35, in <module>
    time_factorial(factorial_iterative, n, "Iterative")
  File "/Users/deepak/code/category-theory/factorial_test.py", line 20, in time_factorial
    digits = len(str(result))
                 ^^^^^^^^^^^
ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
```

## Answer

Here's the fix for the Python script. The error happens because Python has a built-in safeguard to prevent performance issues when converting extremely large integers to strings. We can increase this limit.

Add this line at the top of your Python script:

```python
import sys

# Fix for large integer string conversion limit
sys.set_int_max_str_digits(50000)
```

This allows Python to convert integers with up to 50,000 digits to strings, which is more than enough for our tests.

## Question

Add the following information regarding benchmarks to the above file.

## Answer

### Performance Benchmarks

Here are the benchmark results from running the corrected scripts.

**Python Results**

```
Testing n = 100
Iterative factorial(100): 0.000009s, 158 digits
Recursive factorial(100): 0.000010s, 158 digits

Testing n = 1000
Iterative factorial(1000): 0.000329s, 2568 digits
Recursive factorial(1000): 0.000385s, 2568 digits

Testing n = 5000
Iterative factorial(5000): 0.008428s, 16326 digits
Recursive factorial(5000): 0.007629s, 16326 digits

Testing n = 10000
Iterative factorial(10000): 0.029013s, 35660 digits
Recursive factorial(10000): 0.029987s, 35660 digits
```

**Haskell Results**

```
Testing n = 100
Tail Recursive factorial(100): 0.000213s, 158 digits
Product factorial(100): 0.000008s, 158 digits
Naive Recursive factorial(100): 0.000008s, 158 digits

Testing n = 1000
Tail Recursive factorial(1000): 0.000131s, 2568 digits
Product factorial(1000): 0.000133s, 2568 digits
Naive Recursive factorial(1000): 0.000138s, 2568 digits

Testing n = 5000
Tail Recursive factorial(5000): 0.005968s, 16326 digits
Product factorial(5000): 0.002467s, 16326 digits
Naive Recursive: Skipped (would overflow)

Testing n = 10000
Tail Recursive factorial(10000): 0.007419s, 35660 digits
Product factorial(10000): 0.005533s, 35660 digits
Naive Recursive: Skipped (would overflow)
```

### Analysis

- **Python**: The iterative and recursive versions have very similar performance. Python's recursion is not as optimized as Haskell's, but for these values, the difference is minimal.
- **Haskell**: The `product` version is generally the fastest, as it's a highly optimized built-in function. The tail-recursive version is also very performant and, crucially, does not cause a stack overflow on large inputs, unlike the naive recursive version.
- **Haskell vs. Python**: For larger numbers (`n=10000`), the optimized Haskell versions (`Product` and `Tail Recursive`) are significantly faster than Python's implementations.

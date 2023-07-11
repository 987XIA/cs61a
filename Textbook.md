# Composing Programs



## Chapter 1: Building Abstractions with Functions



### 1.1 Getting Started

textbook *Structure and Interpretation of Computer Programs* ([SICP](http://mitpress.mit.edu/sicp)) by Harold Abelson and Gerald Jay Sussman with Julie Sussman



#### 1.1.1 Programming in Python

#### 1.1.2  Installing Python 3

#### 1.1.3  Interactive Sessions

#### 1.1.4  First Example

```python
from urllib.request import urlopen
shakespeare = urlopen('http://composingprograms.com/shakespeare.txt')

# we read the data from the opened URL
# then decode the data into text
# and finally split the text into words
# All of those words are placed in a set
words = set(shakespeare.read().decode().split())

# compound expression that evaluates to the set of all Shakespearian words that are simultaneously a word spelled in reverse
{w for w in words if len(w) == 6 and w[::-1] in words}

# {'repaid', 'diaper', 'drawer', 'redder', 'reward'}
```



#### 1.1.5 Errors

Guiding principles of debugging:

1. **Test incrementally**: Every well-written program is composed of small, modular components that can be tested individually. Try out everything you write as soon as possible to identify problems early and gain confidence in your components.
2. **Isolate errors**: An error in the output of a statement can typically be attributed to a particular modular component. When trying to diagnose a problem, trace the error to the smallest fragment of code you can before trying to correct it.
3. **Check your assumptions**: Interpreters do carry out your instructions to the letter — no more and no less. Their output is unexpected when the behavior of some code does not match what the programmer believes (or assumes) that behavior to be. Know your assumptions, then focus your debugging effort on verifying that your assumptions actually hold.
4. **Consult others**: You are not alone! If you don't understand an error message, ask a friend, instructor, or search engine. If you have isolated an error, but can't figure out how to correct it, ask someone else to take a look. A lot of valuable programming knowledge is shared in the process of group problem solving.



### 1.2 Elements of Programming

Three elements of every powerful language

- **primitive expressions and statements**, which represent the simplest building blocks that the language provides,
- **means of combination**, by which compound elements are built from simpler ones, and
- **means of abstraction**, by which compound elements can be named and manipulated as units.



#### 1.2.1  Expressions

#### 1.2.2  Call Expressions

#### 1.2.3  Importing Library Functions



```python
from math import sqrt
from operator import add, sub, mul
from math import pi
```



#### 1.2.4  Names and the Environment

#### 1.2.5  Evaluating Nested Expressions

expression tree



#### 1.2.6  The Non-Pure Print Function

**Pure functions** have the property that applying them has no effects beyond returning a value. Moreover, a pure function must always return the same value when called twice with the same arguments.

**Non-pure functions.** In addition to returning a value, applying a non-pure function can generate *side effects*, which make some change to the state of the interpreter or computer. A common side effect is to generate additional output beyond the return value, using the `print` function.

```python
print(1)
print(2)
print(print(1),print(2))

# 1
# 2
# None None
# The fact that it returns None means that 
# it should not be the expression in an assignment statement.

# the return value is none
```



### 1.3  Defining New Functions



#### 1.3.1 Environments

#### 1.3.2 Calling User-Defined Functions

#### 1.3.3 Example: Calling a User-Defined Function

#### 1.3.4 Local Names

#### 1.3.5 Choosing Names

#### 1.3.6 Functions as Abstractions

#### 1.3.7 Operators



### 1.4 Designing Functions



#### 1.4.1  Documentation



A function definition will often include documentation describing the function, called a *docstring*, which must be indented along with the function body. Docstrings are conventionally triple quoted. The first line describes the job of the function in one line. The following lines can describe arguments and clarify the behavior of the function:

```python
def pressure(v, t, n):
        """Compute the pressure in pascals of an ideal gas.

        Applies the ideal gas law: http://en.wikipedia.org/wiki/Ideal_gas_law

        v -- volume of gas, in cubic meters
        t -- absolute temperature in degrees kelvin
        n -- particles of gas
        """
        k = 1.38e-23  # Boltzmann's constant
        return n * k * t / v
```

using help(name of function) to see its docstring, type q to quit help



#### 1.4.2  Default Argument Values



### 1.5 Control



#### 1.5.1  Statements

#### 1.5.2  Compound Statements



**Practical Guidance.** When indenting a suite, all lines must be indented the same amount and in the same way (use spaces, not tabs). Any variation in indentation will cause an error.



#### 1.5.3  Defining Functions II: Local Assignment

#### 1.5.4  Conditional Statements

#### 1.5.5  Iteration

#### 1.5.6  Testing



**Assertions.** Programmers use `assert` statements to verify expectations, such as the output of a function being tested. An `assert` statement has an expression in a boolean context, followed by a quoted line of text (single or double quotes are both fine, but be consistent) that will be displayed if the expression evaluates to a false value.

```python
def fib_test():
        assert fib(2) == 1, 'The 2nd Fibonacci number should be 1'
        assert fib(3) == 1, 'The 3rd Fibonacci number should be 1'
        assert fib(50) == 7778742049, 'Error at the 50th Fibonacci number'
```

In Python tests are typically written in the same file or a neighboring file with the suffix `_test.py`.



**Doctests.** Python provides a convenient method for placing simple tests directly in the docstring of a function. The first line of a docstring should contain a one-line description of the function, followed by a blank line. A detailed description of arguments and behavior may follow. In addition, the docstring may include a sample interactive session that calls the function:

```python
def sum_naturals(n):
    """Return the sum of the first n natural numbers.

	>>> sum_naturals(10)
	55
	>>> sum_naturals(100)
	5050
	"""
	total, k = 0, 1
	while k <= n:
		total, k = total + k, k + 1
	return total
```

Then, the interaction can be verified via the doctest module. Below, the `globals` function returns a representation of the global environment, which the interpreter needs in order to evaluate expressions.

```python
>>> from doctest import testmod
>>> testmod()
TestResults(failed=0, attempted=2)
```

To verify the doctest interactions for only a single function, we use a `doctest` function called `run_docstring_examples`. This function is (unfortunately) a bit complicated to call. Its first argument is the function to test. The second should always be the result of the expression `globals()`, a built-in function that returns the global environment. The third argument is `True` to indicate that we would like "verbose" output: a catalog of all tests run.

```python
>>> from doctest import run_docstring_examples
>>> run_docstring_examples(sum_naturals, globals(), True)
Finding tests in NoName
Trying:
    sum_naturals(10)
Expecting:
    55
ok
Trying:
    sum_naturals(100)
Expecting:
    5050
ok
```

When the return value of a function does not match the expected result, the `run_docstring_examples` function will report this problem as a test failure.

When writing Python in files, all doctests in a file can be run by starting Python with the doctest command line option:

```
python3 -m doctest <python_source_file>
```

The key to effective testing is to write (and run) tests immediately after implementing new functions. It is even good practice to write some tests before you implement, in order to have some example inputs and outputs in your mind. A test that applies a single function is called a *unit test*. Exhaustive unit testing is a hallmark of good program design.



### 1.6  Higher-Order Functions



#### 1.6.1  Functions as Arguments

#### 1.6.2  Functions as General Methods

First, naming and functions allow us to abstract away a vast amount of complexity. While each function definition has been trivial, the computational process set in motion by our evaluation procedure is quite intricate. 

Second, it is only by virtue of the fact that we have an extremely general evaluation procedure for the Python language that small components can be composed into complex processes. 

Understanding the procedure of interpreting programs allows us to validate and inspect the process we have created.



#### 1.6.3  Defining Functions III: Nested Definitions

[1.6.4 Functions as Returned Values](http://www.composingprograms.com/pages/16-higher-order-functions.html#functions-as-returned-values)

[1.6.5 Example: Newton's Method](http://www.composingprograms.com/pages/16-higher-order-functions.html#example-newton-s-method)

[1.6.6 Currying](http://www.composingprograms.com/pages/16-higher-order-functions.html#currying)

[1.6.7 Lambda Expressions](http://www.composingprograms.com/pages/16-higher-order-functions.html#lambda-expressions)

[1.6.8 Abstractions and First-Class Functions](http://www.composingprograms.com/pages/16-higher-order-functions.html#abstractions-and-first-class-functions)

[1.6.9 Function Decorators](http://www.composingprograms.com/pages/16-higher-order-functions.html#function-decorators)


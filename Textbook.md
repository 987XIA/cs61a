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
```


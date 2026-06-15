I was going to jump to OOP, but I think it's a smarter play to just do everything with some functions in one, maybe two files before I implement best practices and OOP.

Given a file path:
    - look at everything inside it
        - start basic, then grow to be able to look through my c drive without it getting stuck

    - if it's a .py file:
        - collect it into a list, then return the number of .py files
        - can also return the names of the .py files

    - if it's a directory:
        -  recursively scan it

When using recursion where the function calls itself:


sum([1,2,3,4,5])

calls

sum([2,3,4,5])

calls

sum([3,4,5])

calls

sum([4,5])

calls

sum([5])

calls

sum([])

The base case is reached now the function has to go back up

0

5 + 0

4 + 5

3 + 9

2 + 12

1 + 14

Basic call stack

sum([1,2,3])

|
v

sum([2,3])

|
v

sum([3])

|
v

sum([])

0

^

3

^

5

^

6

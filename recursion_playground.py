""""
Recursion Playground

I will be putting a bunch of recursive functions here to test and experiment with recursion techniques in different scenarios.
Visualize the recursion process and understand how it works.

Will use graphviz to visualize the recursion process.

Before using graphviz, I'll make a decorator with 4 wrapper functions to track the recursion.

Learned how to create decorators in Python by creating track_recursion with a wrapper that helps track the function's call stack and execution time.


"""
import time
from functools import wraps

#for binary tree traversal
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


#recursion decorator
def track_recursion(func):
    """
    A decorator to track the recursion of a function.
    Will record:
        - Function name
        - Arguments passed to the function
        - Parent calls
        - Return values

    """
    @wraps(func) #python automatically converts into explicit function assignment under the hood
    def wrapper(*args, **kwargs):
        #the print statement runs before the function is called
        #this print statement will show the function call and list the positional and keyword arguments
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")

        #this line calls the original function with the provided arguments, and grabs the result
        result = func(*args, **kwargs)

        #this statement runs after the function runs through from the top to the bottom
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper


#time decorator
def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Execution time of {func.__name__}: {end - start:.4f} seconds")
        return result
    return wrapper



#@measure_time
#@track_recursion
def count_down(n):
    if n == 0: # Base case
        print("Blast off!")
        return

    print(n)
    count_down(n-1) # Recursive case

"""
count_down(5)
count_down(0)
count_down(-3) # Caused RecursionError: maximum recursion depth exceeded
count_down(10)
count_down(100)
"""

#@measure_time
#@track_recursion
def sum_list(lst):
    if not lst: # Base case
        return 0
    #print("This is the current list:\n",lst)
    #print("This is the sum of the current list so far:\n",lst[0] + sum_list(lst[1:]))
    return lst[0] + sum_list(lst[1:]) # Recursive case


#count_down(5)
#sum_list([1, 2, 3, 4, 5])


#@measure_time
#@track_recursion
#reverse_string = measure_time(track_recursion(reverse_string))
def reverse_string(s):
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string(s[:-1])

#why isn't the time being measured until the bottom of the top down call stack?
#only the time for building the list reversal is measured
#think thats because the time decorator is below the track_recursion decorator
reverse_string("hello")

#binary tree traversal

root = TreeNode("A")
root.left = TreeNode("B")
root.right = TreeNode("C")
root.left.left = TreeNode("D")
root.left.right = TreeNode("E")

#Will do a preorder, in-order, and post-order traversal of the binary tree.


@measure_time
@track_recursion
def preorder(node):
    """
    visits the current node, then the left subtree, then the right subtree
    """
    if node is None:
        return
    print("Visiting node:", node.val)
    preorder(node.left)
    preorder(node.right)

preorder(root)

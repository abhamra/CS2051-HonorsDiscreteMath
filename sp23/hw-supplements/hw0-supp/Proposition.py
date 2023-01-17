import re
# CS 2051 Spring 2023 - HW0 Supplement : Python Primer
# Instructor: Gerandy Brito
# Created by Sarthak Mohanty

# This assignment is designed to help you get familiar with Python and submitting assignments on Gradescope.
# This assignment is ungraded.

# First, create a class called Proposition.
# It takes in a string as an argument.
# Assume the string is a valid propositional formula that uses the variables p - z and the operators 'and', 'or', and 'not'.
# Examples of such strings are:
    # "p and (q or r)"
    # "p or q"
    # "not p"
    # "p and q and r"
    # "(p) or q or (not r)"
# The string should be stored as an instance variable called self.func.

class Proposition():
    def __init__(self, function:str):
        self.func:str = function


# Next, create two subclasses of Proposition called Implication and Equivalence.
# These classes should take in two Proposition objects as arguments.
# WLOG, assume the first Proposition object is the antecedent (p) and the second is the consequent (q).
# self.func should be set equivalent to the string "p implies q" or "p iff q" respectively.
# However, since the Propsition class does not support the implies and iff operators, you will need to represent these strings using the operators 'and', 'or', and 'not'
# Make sure to use parentheses appropriately.

class Implication(Proposition):
    def __init__(self, p:Proposition, q:Proposition):
        self.func:str = "not " + p.func + " or " + q.func



class Equivalence(Proposition):
    def __init__(self, p:Proposition, q:Proposition):
        self.func:str = "(" + p.func + " and " + q.func + ") or (not " + p.func + " and " + q.func + ")"
        

# Finally, create a method called extract_variables.
# This method should take in a Proposition object and return a Set of all the variables in the proposition.
# For example, if the proposition is "p and (q or r)", the method should return the set {"p", "q", "r"}.

def extract_variables(p:Proposition)->set:
    s = re.sub('not', "", p.func)
    
    vars = set(re.findall("[p-z]", s))

    return vars

# To submit, upload this file (proposition.py) to Gradescope.



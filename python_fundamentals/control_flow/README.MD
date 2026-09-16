Readme · MD
Python - Control Flow
Description

This project focuses exclusively on control flow in Python. It covers how a program can make decisions and repeat actions using conditional statements and loops. The tasks are adapted from the broader "Python - if/else, loops, functions" project, keeping only the parts aligned with control flow (no functions, no imports).

Topics Covered
if, elif, else statements
Comparison operators (==, !=, >, <, >=, <=)
Boolean logic (and, or, not)
while loops
for loops with range()
Learning Objectives

By the end of this project, you should be able to:

Write conditional statements using if, elif, and else.
Use comparison and logical operators correctly.
Control repetition using while and for loops.
Reason about loop boundaries and iteration ranges.
Generate formatted output using numeric iteration.
Combine conditions and loops to produce deterministic output.
Resources
Python Tutorial — Control Flow Tools
Python Tutorial — More on Conditions
Requirements
General
Allowed editors: vi, vim, emacs
All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.x)
All files should end with a new line
The first line of all files should be exactly #!/usr/bin/env python3
All files must be executable
Code should be PEP8 compliant (version pycodestyle 2.7.x)
No external libraries are allowed
No functions are allowed in this project
No imports are allowed, except where a task explicitly provides a line using __import__()
Output must match the expected formatting exactly
Tasks
Task	File	Description
0	positive_or_negative.py	Assigns a random integer to number and prints whether it is positive, zero, or negative.
0. Positive anything is better than negative nothing

File: positive_or_negative.py

Assigns a random integer between -10 and 10 to a variable named number using the line:

python
number = __import__('random').randint(-10, 10)

Using conditional statements, prints:

<number> is positive if the number is greater than 0
<number> is zero if the number equals 0
<number> is negative if the number is less than 0

Example:

text
$ ./positive_or_negative.py
-4 is negative
$ ./positive_or_negative.py
0 is zero
$ ./positive_or_negative.py
10 is positive
Author

Rakan
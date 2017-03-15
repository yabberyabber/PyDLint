# PyDLint

The goal of this project is to create a Dynamic Analysis tool for Python similar to [DLint](https://github.com/Berkeley-Correctness-Group/DLint).  In essence, this project aims to fill in the gap in the following table: 

|                 |Python | Javascript | C      |
|-----------------|-------|------------|--------|
|Static Analysis  |Pylint |JSHint      |lint    |
|Dynamic Analaysis|       |DLint       |valgrind|

## What is Static Analaysis
Static Analysis is any analysis of a computer program that does not involve running the program.  Generally this involves programmatically reading the source code of a computer program, finding portions that are likely to be erroneous or unintuitive, and reporting them to the programmer so that the programmer may change them.

Tools that perform Static Analysis are often called `linters`.  Pylint, pyflakes, pychecker, jshint, jslint, and cppcheck are all examples of common linters.  

## What is Dynamic Analysis
Dynamic Analysis is analysis of a computer program that does involve running the program.  Dynamic analysis can sometimes catch more types of errors than dynamic analysis because the program can find the values of variables at runtime.  However, Dynamic Analysis is limited to checking only the code branches that are executed while under inspection.  Also, Dynamic Analysis programs are not guaranteed to terminate, especially if the underlying program does not terminate.

While Dynamic Analysis tools are less common than Static Analysis, there are a few that people do use.  Valgrind/Memcheck is the most common; it's a tool that can detect and report certain classes of memory errors by running the program under inspection.

## How well does PyDLint work?
Check back later.

## Can I read the paper you wrote?
Check back later.  

# Acknowledgements
This project is a modification of an existing project called [Byterun](https://github.com/nedbat/byterun).  Byterun is a pure-Python implementation of a Python bytecode execution virtual machine.  Check out [A Python Interpretor Written in Python](http://aosabook.org/en/500L/a-python-interpreter-written-in-python.html) for an awesome explanation of how Byterun works.  

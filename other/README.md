@mainpage

This is Hai Vu's playground where he attempts to response to technical
interview questions. The purpose of this project is to practice for
interview, but more importantly, to learn and gain insight into the
software development process.


# Ubuntu and OS X Setup

## Install the Tools

    sudo apt-get install libgtest-dev scons cmake
    
The above command will install Google Test and Scons. Google Test
can be found at the following locations:

    /usr/src/gtest
    /usr/include/gtest

    
Meanwhile, Scons resides in

    /usr/bin/scons

## Setup Google Test

1. Download [Google Test](https://code.google.com/p/googletest/downloads/list) version
1.7 or later
2. Unpack to a directory, say `~/project/gtest`
3. Set the environment variable `GTEST_DIR=~/project/gtest`

# The Questions

## Questions in C/C++
- Putlong in C: putlong.c
- Linked %List interview questions in C++: List.h
- Squeeze multiple spaces into one: SqueezeSpaces.md
- Reverse a string: ReverseString.md

## Questions in Java
- RecruitingPoint.md: Coding tests from Recruiting Point 

## Questions in Python
- build_tree.py
- A strategy game: pots_of_gold
- String replacement: string_generator_solution.md
- Sum of polynomials: poly_sum.md


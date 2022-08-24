# Module 07 
*Erica Peterson, 08/23/2022*
## Introduction
In this paper I will go over pickling and error handling, using the try-except function. Pickling is used to store data in a binary format, and this can be useful for making files smaller or sending files from one program to another. After discussing pickling and error-handling I will go over a program that uses both to do simple calculations and then save them to a binary file. 
## Pickling
Data can be saved in a binary format, rather than plain text as we have seen in the previous assignments. In python, this is called pickling. Pickling is also used to serialize and deserialize a python object. Pickling is a way to convert python objects, such as lists or dictionaries, into a character stream. This character stream contains all the necessary information to reconstruct the object in another python script. Pickling is similar to files where you use the “w”, “a” and “r” modes but instead of just “w”, you would use “wb”, “ab”, or “rb” because everything is stored in bytes. “pickle.dump()” is used to pickle a file whereas “pickle.load()” is used to unpickle. An example of pickling and saving to a binary file can be found in Figure 1, on the next page. 
![Figure 1](https://github.com/ericapet/ITFnd100-Mod07/blob/main/docs/Figure1.png "Figure 1")

*Figure 1. How to pickle data to save it in a binary file. The top image shows the script: In line 22, it is vital that you start with import pickle. Notice the use of “ab” and “rb” in lines 26 and 31. Line 32 is where the file is binarized using the pickle.load() function.  The middle image shows the output while running the script, with user input in green. The bottom image shows the figure1.dat file, with binary characters.*

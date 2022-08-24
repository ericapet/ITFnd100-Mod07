# Module 07 
*Erica Peterson, 08/23/2022*
## Introduction
In this paper I will go over pickling and error handling, using the try-except function. Pickling is used to store data in a binary format, and this can be useful for making files smaller or sending files from one program to another. After discussing pickling and error-handling I will go over a program that uses both to do simple calculations and then save them to a binary file. 
## Pickling
Data can be saved in a binary format, rather than plain text as we have seen in the previous assignments. In python, this is called pickling. Pickling is also used to serialize and deserialize a python object. Pickling is a way to convert python objects, such as lists or dictionaries, into a character stream. This character stream contains all the necessary information to reconstruct the object in another python script. Pickling is similar to files where you use the “w”, “a” and “r” modes but instead of just “w”, you would use “wb”, “ab”, or “rb” because everything is stored in bytes. “pickle.dump()” is used to pickle a file whereas “pickle.load()” is used to unpickle. An example of pickling and saving to a binary file can be found in Figure 1, on the next page. 
![Figure 1](https://github.com/ericapet/ITFnd100-Mod07/blob/main/docs/Figure1.png "Figure 1")

*Figure 1. How to pickle data to save it in a binary file. The top image shows the script: In line 22, it is vital that you start with import pickle. Notice the use of “ab” and “rb” in lines 26 and 31. Line 32 is where the file is binarized using the pickle.load() function.  The middle image shows the output while running the script, with user input in green. The bottom image shows the figure1.dat file, with binary characters.*

Pickling is not only used to save data to a binary file- it can also be used to serialize and deserialize, as mentioned earlier. You can pickle any data type, such as dictionaries, tuples, lists, strings, etc.  An example of pickling, using pickle.load(), and then unpickling, using “pickle.dump()”, data can be found in Figure 2. 
![Figure 2](https://github.com/ericapet/ITFnd100-Mod07/blob/main/docs/figure2.png "Figure 2")

*Figure 2. How to pickle and unpickle an object. The top image shows the script whereas the bottom image shows the output.*

## Structured Error-Handling
Structured error-handling is used to guess what errors a user might make and provide a clearer error message to the user. Basically, you want to look at your script, think of possible errors that could be caused by user input, and then tell the user what happened if they do cause an error. This is done using the try-except function, also known as try-catch in other languages. The reason why programmers use try-except rather than using the standard python error messages is because sometimes python error messages can be confusing for the average user who may not know programming. Using try-except makes your program more user friendly.  Exception is a built-in python class that holds information about an error, python automatically creates an exception object when there is an error. The exception object will automatically fill in information about what caused the error. An example using try-except, and exception objects can be seen on the following page, in Figure 3. 
![Figure 3](https://github.com/ericapet/ITFnd100-Mod07/blob/main/docs/figure3.png "Figure 3")

*Figure 3. How to use try-except for structured error-handling. The top image shows the script, with the error occurring in line 3. Line 5 shows how to use an exception object, e, to show pythons built in error message. The bottom image shows the output when the script is run.*

Python has many built in exception classes, such as a file not existing, or the zero-division error mentioned above. You can also raise your own custom errors if there is not a built-in one or if you do not like the way the built-in one works. An example of raising custom errors can be seen in Figure 4, below. 

![Figure 4](https://github.com/ericapet/ITFnd100-Mod07/blob/main/docs/figure4.png "Figure 4")

*Figure 4. How to raise custom error messages. The top image shows the script for raising custom error messages. The middle image shows the error message when a file name is numeric. The bottom image shows the error message when the file does not end in .txt.*

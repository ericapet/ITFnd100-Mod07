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

## Using Pickling and Structured Error-Handling in a Script
Now that we know more about pickling and structured error-handling, I have designed a script to demonstrate how they work in a complete program. My program will do basic math calculations, based of numbers the user inputs, and then save them to a binary file that is named by the user.  The first code block in this script focuses on gaining user input for the file name and numbers to do math with - this code block can be seen in Figure 5. 

![Figure 5](https://github.com/ericapet/ITFnd100-Mod07/blob/main/docs/figure5.png "Figure 5")

*Figure 5. The top image shows the code block to obtain user input data. Notice line 9 has the vital import pickle code. Line 11-17 deals with gaining the file name and using structured error handling to make sure that the file has an alphabet character name, not numeric. Lines 18-21 get the user input numbers to perform mathematical equations on. The bottom image shows what happens if the user inputs a file name with numbers, causing the try except to run and outputting our custom error message, “Please do not use numbers for the files name”.*

The next code block, processes the mathematical data to perform simple calculations, including 3 try-excepts. Two of the try-excepts are built-in: ZeroDivisionError and OverflowError. ZeroDivisionError happens when you try to divide a number by 0. OverflowError happens when the number entered is too large and the computer cannot perform calculations with it. The third custom try-except is that you cannot use alphabetical characters, only numbers. An example of the code block can be found in Figure 6, on the next page. 

![Figure 6](https://github.com/ericapet/ITFnd100-Mod07/blob/main/docs/figure6.png "Figure 6")

*Figure 6. The code block to do basic calculations, including three try-except statements. The first try-except, ZeroDivisionError, can be seen in lines 29-31. The second try-except, OverflowError, can be seen in lines 31-34. The custom try-except, for when the input is alphabetical, can be seen in lines 35-39.*

As an example, I will also show how this code block runs and what happens when the user tries to enter an alphabetical input or a 0 as the second input. This can be seen below in Figure 7. 

![Figure 7](https://github.com/ericapet/ITFnd100-Mod07/blob/main/docs/figure7.png "Figure 7")

*Figure 7. The top image shows the error message that is presented to the user when they use alphabetical characters instead of numerical. The bottom image shows the error message when the user tries to divide by 0.*

The next code block creates the functions to save data to a binary file and to read data from that binary file. This is done using the pickle.dump() and pickle.load() functions. The code block can be found in Figure 8, on the following page. 

![Figure 8](https://github.com/ericapet/ITFnd100-Mod07/blob/main/docs/figure8.png "Figure 8")

*Figure 8. Functions for creating and saving to a binary file (lines 41-44) and reading data from that file and displaying it to the user (line 45-49). Notice the “ab” in line 42 and the “rb” in line 46, which tell us this is binary and stored in bytes.*

The final part of this code is to run the above-mentioned functions and present the saved data to the user. These two code blocks can be seen in Figure 9. 

![Figure 9](https://github.com/ericapet/ITFnd100-Mod07/blob/main/docs/figure9.png "Figure 9")

*Figure 9. How to save the data to a binary file and then read it out for the user to see.*

Now that we have seen every individual part of the code block, we can put it all together and see how it runs in both PyCharm and Command Prompt. First, lets look at the entire script in Figure 10, on the following page. in Figure 11, we can look at how the code runs in PyCharm, with no errors, including an image of the file that was created. 


![Figure 10](https://github.com/ericapet/ITFnd100-Mod07/blob/main/docs/figure10.png "Figure 10")

*Figure 10. The completed script to do basic math and save it in a binary file, including structured error-handling.*

In Figure 11, on the following page, we can look at how the code runs in PyCharm, with no errors, including an image of the binary file that was created.

![Figure 11](https://github.com/ericapet/ITFnd100-Mod07/blob/main/docs/figure11.png "Figure 11")

*Figure 11. The script running in PyCharm is seen in the top image, including user input in green. The bottom image shows the binary file, named Figure 11, as inputted.*

Next, we can confirm that this script also runs in Command Prompt, with no user errors. This can be seen in Figure 12. Also in Figure 12 is the file created when the script is run in Command Prompt. 

![Figure 12](https://github.com/ericapet/ITFnd100-Mod07/blob/main/docs/figure12.png "Figure 12")

*Figure 12. The completed script running in command prompt is seen in the top image. The bottom image shows the binary file created by the script, including the correct name for the file, figure 12.*

## Summary
In this paper I went over pickling and structured error-handling and then combined these ideas into a program that showcased what they do. Structured error-handling will be very important in future projects to make them more user friendly, especially as the script gets more complex. Pickling is also useful for sharing files across programs. 

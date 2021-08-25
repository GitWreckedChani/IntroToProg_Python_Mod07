# **Pickling and Error Handling in Python**
**Date** *8/23/2021*

**Student Dev** *Chani, rabbit of Midas* 🐇
## Introduction
Lets discuss the merits of *pickling* and *unpickling*, and the **try/except** functions. 
## Pickling & Unpickling
Also referred to as serializing and de-serializing a python object structure, pickling and unpickling is used 
for storing data to a binary file or database.
### *Pickling*
In Python, pickling an object refers to tranforming an object(or objects) into a single bytestream in a file. 
This is differnt from a text file because it uses less memory, but is also different from a secure file as 
it does not encrypt. 

*Example*:
```
import pickle

integers = [1, 2, 3, 4, 5]

with open('pickle-example.p', 'wb') as pfile:
    pickle.dump(integers, pfile)
```
This will dump the `integers list` to a binary file called `pickle-example.p`.

### *Unpickling*
Unpickling is the inverse of this process. A binary file or byte-like object is converted back into an
object heirarchy. 

*Example*
```
import pickle

with open('pickle-example.p', 'rb') as pfile:
    integers = pickle.load(pfile)
    print integers
```
The above will output `[1, 2, 3, 4, 5]`.

## Structured Error Handling
In python, the program terminates when it encounters an error. These errors usually come in two forms: 
a `syntax error` or an *exception* error. 

*Example*
```
>>> open("imaginary.txt")
Traceback (most recent call last):
 File "<string>", line 301, in runcode
 File "<interactive input>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'imaginary.txt'
```
You might see this if you attempt to open a file that does not exist. 
The **try/except** error handling method can give you some control
over how exception objects are handled. 

To see a list of built-in exceptions, type this into your python IDE (although, be aware that custom 
exceptions exist):
`print(dir(locals()['__builtins__']))`

### *Try*
The call to **try** allows you to anticipate and head off some issues before they raise an exception. Following
"try" you should list the critical operation which can raise an exception. Perhaps, something like this:

*Example*
```
try:
    linux_interaction()
```

### *Except*
"Except" allows you to field and handle the exception that would arise from this action. To do this, you could
hand out a `pass`, like so:

*Example*
```
try:
    linux_interaction()
except:
    pass
```
If you were to run this code, what you might get back is nothing. The program would skip this command and continue
without crashing.

### *Raising Custom Errors*
While not crashing is great, it would be nice if a dev could communicate to the user what exactly happened. That is 
where custom errors are useful. Following "except", the dev can have the code display a customized message.

*Example*
```
try:
    linux_interaction()
except:
    print('Linux function was not executed')
```
Rather than nothing, this function would return to the user the line
> Linus functon was not executed

### *Catching Multiple and Specific Exceptions*
The Exception class can catch any type of error, but you can catch specific errors using more specific exception classes.
![Imageforgithub](https://user-images.githubusercontent.com/88753715/130565391-dc106ebd-252d-4dc4-833c-bd3189a8d0df.PNG)
![Figure13](https://user-images.githubusercontent.com/88753715/130565414-957bd876-911e-42a2-aff1-74fad7bc2489.png)

## Summary
To summarize, pickling and unpickling data to a file is different from packing and unpacking it in that pickling saves it as
a bytestream. Over the course of a particularly large code, this could mean using significantly less memory to run.

Try/except is useful in break-proofing your code and can even be used to make code more user friendly.

#### Citations: 
[https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf]

(https://www.programiz.com/python-programming/exception-handling)

https://realpython.com/python-exceptions/

https://www.geeksforgeeks.org/understanding-python-pickling-example/

https://realpython.com/python-pickle-module/

https://pythonprogramming.net/python-pickle-module-save-objects-serialization/

https://pythonbasics.org/try-except/

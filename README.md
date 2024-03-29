# Complex-Numbers
## inspiration
****
There are many mathematical functions that we know take in real number inputs to return real number answers. However, Real numbers are only a subset of the complex numbers. To be completely rigorous, a function must be able to take in complex input values, and return the correct complex result. 

Most conventional calculators cannot intake complex number inputs and process them, normally returning a math error. This project will applies mathematical definitions of functions, and extends the definition to handle complex number inputs.
This allows us to answer questions like :
- $sin(x) = 2$
- $x^2 + 1 = 0$
- $x = ln(-1)$


and many other results that would normally return errors on normal calculators.
All mathematical definitions for this project were derived from scratch and implemented into the python code. There is no use of of Python's cmath library; All complex numbers are coded from scratch using OOP concepts.


## Derivations:
****

With the use of some complex theorems and identities, namely Euler's identity and De Moivre's theorem, many traditional mathematical functions have a complex definition. I have explained the derivations for many of these in the [complex.py](<./model/complex.py>) file, as well as explained how I have implemented them into Python.
Here are some derivations that were too long to put in comments-

![hyperbolic trig derivations](./derivations/hyperbolic-trig/hyp_trig_complex_1.png)

check [derivations](<./derivations>) for more.

## User Interface:
****
The User interface was built using Python's Tkinter library. I built the UI with the iPhone's in-built calculator design in mind. Here is an example of what the UI looks like upon running $i^i$ in it:

![UI Result](./images/UI_result.png)

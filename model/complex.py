import real as r
import imaginary as i


# defines a complex number
class Complex (r.Real, i.Imaginary):

    # creates a complex number consisting of a real and imaginary part
    # if number of arguments is 1, its given a string and creates a complex number
    # if number of arguments is 2, its given a real and imaginary component and creates a complex number
    def __init__(self, *args):
        if len(args) == 1:
            self.real = string_to_complex(args[0])[0]
            self.imaginary = string_to_complex(args[0])[1]
        else:
            self.real = args[0]
            self.imaginary = args[1]

    # returns complex number as a string
    def complex_to_string(self):
        real = self.real
        imaginary = self.imaginary
        if real == 0:
            if imaginary < 0:
                return f"- {-1 * imaginary}i"
            elif imaginary == 0:
                return "0"
            else:
                return f"{imaginary}i"
        else:
            if imaginary < 0:
                return f"{real} - {-1 * imaginary}i"
            elif imaginary == 0:
                return f"{real}"
            else:
                return f"{real} + {imaginary}i"

    # returns complex conjugate
    def conjugate(self):
        return Complex(self.real, -1 * self.imaginary)

    # gets the sign of the imaginary component
    def get_sign(self):
        complex_number = self.complex_to_string().split()
        return complex_number[1]


# helper methods

# returns string as real and imaginary components
def string_to_complex(complex_number_string):
    complex_number = complex_number_string.split()
    real = int(complex_number[0])
    sign = complex_number[1]
    if sign == '-':
        imaginary = -1 * int(complex_number[2][0: -1])
    else:
        imaginary = int(complex_number[2][0: -1])
    return real, imaginary

# print the complex number String onto console
def print_complex(c):
    print(c.complex_to_string())


# adds two complex numbers together
def add(c1, c2):
    real = c1.real + c2.real
    imaginary = c1.imaginary + c2.imaginary
    return Complex(real, imaginary)


# adds two complex numbers together
def sub(c1, c2):
    real = c1.real - c2.real
    imaginary = c1.imaginary - c2.imaginary
    return Complex(real, imaginary)

# adds two complex numbers together
def mult(c1, c2):
    real = c1.real*c2.real - c1.imaginary*c2.imaginary
    imaginary = c1.real*c2.imaginary + c1.imaginary*c2.real
    return Complex(real, imaginary)


# testing
c1 = Complex(1, 1)
c2 = Complex(1, -1)
c3 = Complex("3 + 2i")
c4 = mult(c1,c2)
print_complex(c1)
print_complex(c2)
print_complex(c4)



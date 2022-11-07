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
        if self.imaginary < 0:
            return f"{self.real} - {-1* self.imaginary}i"
        else:
            return f"{self.real} + {self.imaginary}i"

    # returns complex conjugate
    def conjugate(self):
        return Complex(self.real, -1 * self.imaginary)

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




# testing
c1 = Complex(1, 1)
c2 = Complex(1, -1)
c3 = Complex("3 + 2i")
print_complex(c3)

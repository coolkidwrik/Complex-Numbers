import real as r
import imaginary as i


# defines a complex number consisting of a real and imaginary part
class Complex (r.Real, i.Imaginary):

    # creates a complex number consisting of a real and imaginary part
    # if number of arguments is 1, its given a string and creates a complex number
    # if number of arguments is 2, its given a real and imaginary component and creates a complex number
    def __init__(self, *args):
        assert len(args) < 3, "no constructor for these arguments"
        if len(args) == 1:  # constructor one
            assert type(args[0]) == str, f"argument \"{args[0]}\" is not of type str"
            nums = string_to_complex(args[0])
            self.real = nums[0]
            self.imaginary = nums[1]
        else:              # constructor two
            assert (type(args[0]) == type(args[1])) and (type(args[0]) == int or type(args[0]) == float), \
                f"arguments, \"{args[0]}\" or \"{args[1]}\" are not of type str"
            self.real = args[0]
            self.imaginary = args[1]

    # prints out complex number in the form a + bi when print(Complex) is called
    def __repr__(self):
        return complex_to_string(self)

    # returns complex conjugate
    def conjugate(self):
        return Complex(self.real, -1 * self.imaginary)

    # gets the sign of the imaginary component
    def get_sign(self):
        complex_number = self.complex_to_string().split()
        return complex_number[1]

    # adds two complex numbers together
    @staticmethod
    def add(c1, c2):
        real = r.Real.add(c1.real, c2.real)
        imaginary = i.Imaginary.add(c1.imaginary, c2.imaginary)
        return Complex(real, imaginary)

    # subtracts two complex numbers together
    @staticmethod
    def sub(c1, c2):
        real = r.Real.sub(c1.real, c2.real)
        imaginary = i.Imaginary.sub(c1.imaginary, c2.imaginary)
        return Complex(real, imaginary)

    # multiplies two complex numbers together
    @staticmethod
    def mult(c1, c2):
        real = r.Real.mult(c1.real, c2.real) + i.Imaginary.mult(c1.imaginary, c2.imaginary)
        imaginary = c1.real * c2.imaginary + c1.imaginary * c2.real
        return Complex(real, imaginary)

    # divides two complex numbers
    @staticmethod
    def div(c1, c2):
        numerator = Complex.mult(c1, c2.conjugate())
        denominator = Complex.mult(c2, c2.conjugate())
        real = r.Real.div(numerator.real, denominator.real)
        imaginary = i.Imaginary.div(numerator.imaginary, denominator.real)
        return Complex(real, imaginary)


# helper methods

# returns string as real and imaginary components
def string_to_complex(complex_number_string):
    assert type(complex_number_string) == str, f"{complex_number_string} is not a str"
    complex_number = complex_number_string.split()
    assert len(complex_number) == 3, f"{complex_number_string} is not formatted correctly! try adding spaces"
    real = int(complex_number[0])
    sign = complex_number[1]
    if sign == '-':
        imaginary = -1 * int(complex_number[2][0: -1])
    else:
        imaginary = int(complex_number[2][0: -1])
    return real, imaginary


# returns complex number as a string
def complex_to_string(self):
    real = self.real
    imaginary = self.imaginary
    if real == 0:
        if imaginary < 0:
            return f" {-1 * imaginary}i"
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


# print the complex number String onto console
def print_complex(c):
    print(complex_to_string(c))

# testing


t1 = Complex(2, 3)
t2 = Complex(5, 2)
t3 = Complex.add(t1, t2)
t4 = Complex.mult(t1, t2)
t5 = Complex.div(t1, t2)
print(t1)
print(t2)
print(t3)
print(t4)
print(t5)






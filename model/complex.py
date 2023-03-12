import real as r
import imaginary as i
import math as m


# defines a complex number consisting of a real and imaginary part
class Complex (r.Real, i.Imaginary):

    # creates a complex number consisting of a real and imaginary part
    # if number of arguments is 1, its given a string and creates a complex number
    # if number of arguments is 2, its given a real and imaginary component and creates a complex number
    def __init__(self, *args):
        assert 3 > len(args) > 0, "no constructor for these arguments"
        if len(args) == 1:  # constructor one
            assert type(args[0]) == str, f"argument \"{args[0]}\" is not of type str"
            nums = string_to_complex(args[0])
            self.real = nums[0]
            self.imaginary = nums[1]
        else:              # constructor two
            # assert type(args[0]) == int, f"->{args[0]}"
            # assert type(args[0]) == float, f"->{args[0]}"
            # assert type(args[1]) == int, f"->{args[1]}"
            # assert type(args[1]) == float, f"->{args[1]}"
            assert (type(args[0]) == int or type(args[0]) == float) and \
                   (type(args[1]) == int or type(args[1]) == float), \
                   f"one of arguments, \"{args[0]}\" or \"{args[1]}\" are not numbers"

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

    # returns the argument of a complex number
    def arg(self):
        real = self.real
        imaginary = self.imaginary
        result = m.atan(imaginary/real)
        if real >= 0:
            return Complex(str(result))
        else:
            return Complex(str(m.pi - result))

    # returns the modulus of a complex number, which is itself a complex number
    def mod(self):
        result = m.sqrt(pow(self.real, 2) + pow(self.imaginary, 2))
        return Complex(str(result))

    # returns a string representation of euler's form of the complex number in
    # rectangular form
    def rect_to_euler(self):
        argument = complex_to_string(self.arg())
        modulo = complex_to_string(self.mod())
        if abs(m.sin(float(argument))) < 1e-7:
            return modulo
        else:
            return f"{modulo}e^{argument}i"

    # returns a string representation of euler's form of the complex number
    # in rectangular form
    def rect_to_cis(self):
        argument = complex_to_string(self.arg())
        modulo = complex_to_string(self.mod())
        if abs(m.sin(float(argument))) < 1e-7:
            return modulo
        else:
            return f"{modulo}(cos({argument}) + isin({argument}))"

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

    # raises complex number, c1 to the power of another complex number, c2
    @staticmethod
    def power(c1, c2):
        # modulo = c1.mod()
        # exponent = euler_exponent(c1)
        # c = Complex.mult(exponent, c2)
        # real = m.exp(c.real) +
        pass



# helper methods

# returns string as real and imaginary components
def string_to_complex(complex_number_string: str):
    assert type(complex_number_string) == str, f"{complex_number_string} is not a str"
    complex_number = complex_number_string.split()
    assert len(complex_number) == 3 or len(complex_number) == 1, \
        f"{complex_number_string} is not formatted correctly! must be in the for \"a + bi\""
    if len(complex_number) == 1:
        return string_to_complex_one_arg(complex_number)
    else:
        return string_to_complex_three_arg(complex_number)


# helper function for string_to_complex, if the input string is 1 distinct character
def string_to_complex_one_arg(complex_number):
    if complex_number[0][-1] == "i":
        if complex_number[0] == 'i':
            imaginary = 1
        else:
            imaginary = float(complex_number[0][0: -1])
        return 0, imaginary
    else:
        return float(complex_number[0]), 0


# helper function for string_to_complex, if the input string is 3 distinct characters
def string_to_complex_three_arg(complex_number):
    real = float(complex_number[0])
    sign = complex_number[1]
    assert sign in ["+", "-"], f"\"{sign}\" is not valid, must be either \"+\" or \"-\""
    if complex_number[2] == 'i':
        imaginary = 1
    else:
        imaginary = float(complex_number[2][0: -1])
    if sign == '-':
        imaginary *= -1
    return real, imaginary


# returns complex number as a string
def complex_to_string(self):
    real = self.real
    imaginary = self.imaginary
    if real == 0:
        if imaginary == 0:
            return "0"
        elif imaginary == 1:
            return "i"
        else:
            return str(imaginary) + "i"
    else:
        if imaginary < 0:
            return f"{real} - {-1 * imaginary}i"
        elif imaginary == 0:
            return f"{real}"
        else:
            return f"{real} + {imaginary}i"


# returns the exponent of euler's form as a complex number
def euler_exponent(complex_number):
    s = f"{complex_number.arg()}i"
    return Complex(s)



# print the complex number String onto console
# def print_complex(c):
#     print(complex_to_string(c))

# testing

t1 = Complex("-3")
t2 = Complex.div(t1, t1)
t3 = Complex.div(t2, t1)
t4 = Complex.div(t1, t3)
print(t1.rect_to_cis())
print(t2.rect_to_cis())
print(t3.rect_to_cis())
print(t4.rect_to_cis())








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

    # returns the argument of a complex number, which is itself a complex number
    def arg(self):
        real = self.real
        imaginary = self.imaginary
        if abs(real) < 1e-7:
            if imaginary < 0:
                result = m.pi*(-1/2)
            else:
                result = m.pi*(1/2)
        elif real < 0:
            if imaginary < 0:
                result = -1*m.pi + m.atan(imaginary/real)
            else:
                result = m.pi + m.atan(imaginary/real)
        else:
            result = m.atan(imaginary/real)
        return Complex(result, 0)

    # returns the modulus of a complex number, which is itself a complex number
    def mod(self):
        result = m.sqrt(pow(self.real, 2) + pow(self.imaginary, 2))
        return Complex(result, 0)

    # returns a string representation of euler's form of the complex number in
    # rectangular form
    def rect_to_euler(self):
        argument = complex_to_string(self.arg())
        modulo = complex_to_string(self.mod())
        if abs(m.sin(float(argument))) < 1e-7:
            return modulo
        else:
            return f"{modulo}e^{argument}i"

    # returns a string representation of cis form of the complex number
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
    # input expression looks like (a + bi)^(c + di)
    @staticmethod
    def power(c1, c2):
        if c2.imaginary == 0:
            return pow_with_real_exp(c1, c2)
        else:
            return pow_with_complex_exp(c1, c2)

    #takes the sine of a complex number
    # using the complex definition of the sine function
    # sin(c) = (e^(ic) - e^(-ic) )/2i
    @staticmethod
    def sin(c):
        # if the argument, "c", is real
        if c.imaginary == 0:
            return m.sin(c.real)
        # if the argument, "c", is complex
        else:
            # c has an imaginary component
            if c.real == 0:
                # if c = ai where a is an arbitrary constant
                it = i.Imaginary.mult(c.imaginary, i)
                pass
            else:
                pass

    # takes the cosine of a complex number
    # using the complex definition of the sine function
    # cos(t) = (e^(it) + e^(-it) )/2
    @staticmethod
    def cos(c):
        if c.imaginary == 0:
            return m.cos(c.real)
        else:
            # c has a complex component
            if c.real == 0:
                # if c = ai where a is an arbitrary constant

                #it = i * (ai) = -a
                it = i.Imaginary.mult(c.imaginary, 1)
                return (m.exp(it) + m.exp(-1 * it))/2
            else:
                # if c = a + bi where a and b are arbitrary constants
                #
                exp = Complex(0, 1)
                # new_cis(c, exp)

    # takes the tangent of a complex number
    @staticmethod
    def tan(c):
        return Complex.sin(c)/Complex.cos(c)

    # takes in a complex number and returns the e to the power of that number.
    # assumes the input is a complex number of the form: c = a + bi
    # e^c = (e^a) * e^(bi)
    @staticmethod
    def exp(c):
        ea = m.exp(c.real) # e^a

        # e^(bi) = cos(b) + i*sin(b)
        # ebi = m.co
        pass

    # takes in a complex number and returns the natural log of it.
    # assumes the input is a complex number of the form: c = a + bi
    # using euler's form, can be re-written as c = r * e^(it),
    # where r is the mod and t is the argument of the number
    # the goal: ln(a + bi) = ln(r * e^(it)) = ln(r) + it
    @staticmethod
    def natural_log(c):
        real = m.log(c.mod().real, m.e)
        imaginary = c.arg().real
        return Complex(real, imaginary)




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
def string_to_complex_one_arg(complex_number: str):
    if complex_number[0][-1] == 'i':
        if complex_number[0] == 'i':
            imaginary = 1
        elif complex_number[0] == '-i':
            imaginary = -1
        else:
            imaginary = float(complex_number[0][0: -1])
        return 0, imaginary
    else:
        return float(complex_number[0]), 0


# helper function for string_to_complex, if the input string is 3 distinct characters
def string_to_complex_three_arg(complex_number: str):
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
def complex_to_string(complex_number: Complex):
    real = complex_number.real
    imaginary = complex_number.imaginary
    if real == 0:
        if imaginary == 0:
            return "0"
        elif imaginary == 1:
            return "i"
        elif imaginary == -1:
            return "-i"
        else:
            return str(imaginary) + "i"
    else:
        if imaginary == 0:
            return f"{real}"
        elif imaginary == 1:
            return f"{real} + i"
        elif imaginary == -1:
            return f"{real} - i"
        elif imaginary < 0:
            return f"{real} - {-1 * imaginary}i"
        else:
            return f"{real} + {imaginary}i"


# returns the exponent of euler's form as a complex number
# a + bi = r * e^(ti). returns t given 'a + bi'
def euler_exponent(complex_number: Complex):
    return Complex(0, complex_number.arg().real)


# helper for pow function if exponent is complex (in the form c + di)
def pow_with_complex_exp(c1: Complex, c2: Complex):
    modulo = c1.mod()  # r for c1 = r * e^(ti)
    c1_exponent = euler_exponent(c1)  # ti for c1 = r * e^(ti)

    # modulus
    n_modulo = new_modulo(modulo, c2)
    # cis
    n_cis = new_cis(c1_exponent, c2)
    # result
    result = Complex.mult(n_modulo, n_cis)
    return result


# helper for pow_with_complex_exp()
# the following code works as follows:
# a + bi = r*e^ti where r is modulus and t is the argument.
# ti is c1_exponent
# when raised to the power of c + di, we get (r^(c + di))*e^((c + di)ti)
# this part of the code will focus on r^(c + di), which yields a complex number
# r^(c + di) = (r^c)*(r^di)
def new_modulo(modulo, exp):
    # r^c
    rc = Complex(pow(modulo.real, exp.real), 0)

    # r^(di) = e^(ln(r^d)i) = cos(ln(r^d)) + i*sin(ln(r^d))
    n_arg = m.log(pow(modulo.real, exp.imaginary), m.e)  # ln(r^d)
    rdi = Complex(m.cos(n_arg), m.sin(n_arg))

    # (r ^ c) * (r ^ di)
    return Complex.mult(rc, rdi)


# helper for pow_with_complex_exp() and sin and cos
# the following code works as follows:
# a + bi = r*e^ti where r is modulus and t is the argument.
# ti is c1_exponent
# when raised to the power of c + di, we get (r^(c + di))*e^((c + di)ti)
# this part of the code will focus on e^((c + di)ti, which yields a complex number
# e^((c + di)ti) = (e^-(dt)) * (e^(cti))
def new_cis(c1_exponent, exp):
    # (e^-(dt))
    edt = Complex(m.exp(-1 * c1_exponent.imaginary * exp.imaginary), 0)

    # (e ^ (cti)) = cos(ct) + i*sin(ct)
    ct = exp.real * c1_exponent.imaginary
    ecti = Complex(m.cos(ct), m.sin(ct))

    # (e^-(dt))*(e^(cti))
    return Complex.mult(edt, ecti)


# helper for pow function if exponent is real
# uses De Moivre's theorem for simplification
# De Moivre's theorem: (a + bi)^n = (r(cos(t) + i*sin(t)))^n = (r^n)(cos(nt) + i*sin(nt)), where r is the modulo
# and t is the argument
def pow_with_real_exp(c1: Complex, c2: Complex):
    exp = c2
    modulo = c1.mod()
    arg = c1.arg()
    n_arg = arg.real * c2.real
    n_mod = Complex(m.pow(modulo.real, exp.real), 0)
    result = cis_correction(n_mod, n_arg)
    return result


# sine and cosine functions, for cis form of complex numbers,
# result in floating point errors when the argument is around
# 0, pi/2, -pi/2, or pi/-pi
# this code takes in the modulus of the complex number, and the argument, and returns
# the complex number after floating point error corrections
def cis_correction(n_mod: Complex, n_arg: float):
    sin_n_arg = m.sin(n_arg)
    cos_n_arg = m.cos(n_arg)
    if abs(sin_n_arg) < 1e-7: # when the argument is 0 or pi or -pi
        if cos_n_arg < 0:
            n_cis = Complex(-1, 0) # when the argument is pi or -pi
        else:
            n_cis = Complex(1, 0) # when the argument is 0
    elif abs(cos_n_arg) < 1e-7: # when the argument is pi/2 or -pi/2
        if sin_n_arg < 0:
            n_cis = Complex(0, -1) # when the argument is -pi/2
        else:
            n_cis = Complex(0, 1) # when the argument is pi/2
    else:
        n_cis = Complex(cos_n_arg, sin_n_arg)
    return Complex.mult(n_mod, n_cis)


# print the complex number String onto console
# def print_complex(c):
#     print(complex_to_string(c))

# testing

t1 = Complex("0.7071067811865475 + 0.7071067811865475i")
# t2 = Complex(str(m.pi/2))
t2 = Complex("5")
t3 = Complex.power(t1, t2)
print(t1)
print(t2)
print(t3)

print(1/m.sqrt(2))


#print(Complex.power(t1, t1))








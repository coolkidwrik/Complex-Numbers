import model.real as r
import model.imaginary as imag
import math as m


# defines a complex number consisting of a real and imaginary part
class Complex (r.Real, imag.Imaginary):

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

    # overwrites the object classes equal function to compare complex numbers based on their
    # real and imaginary components
    def __eq__(self, other):
        error = 1e-7
        if abs(self.real - other.real) < error  and abs(self.imaginary - other.imaginary) < error:
            return True
        return False

    # returns complex conjugate
    def conjugate(self):
        return Complex(self.real, -1 * self.imaginary)

    # gets the sign of the imaginary component
    def get_sign(self):
        if self.imaginary >= 0:
            return "+"
        else:
            if self.imaginary < 0:
                return "-"


    # returns the argument of a complex number, which is itself a complex number
    def arg(self):
        real = self.real
        imaginary = self.imaginary
        if abs(imaginary) < 1e-7 and abs(real) < 1e-7:
            return Complex (0,0)
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
        # assume complex number in question, c, is in the form: c = a + bi
        # modulus of c is sqrt(a^2 + b^2)
        # therefore result = m.sqrt(pow(self.real, 2) + pow(self.imaginary, 2))
        # or
        # c * c_conjugate = (a + bi) * (a - bi)
        #                 = a^2 - (bi)^2
        #                 = a^2 + b^2          = modulus^2
        # sqrt(c * c_conjugate) = modulus
        # this version doesn't use math.power

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
            if argument == "1.0":
                if modulo == "1.0":
                    return f"e^i"
                else:
                    return f"{modulo}e^i"
            else:
                if modulo == "1.0":
                    return f"e^({argument}i)"
                else:
                    return f"{modulo}e^({argument}i)"

    # returns a string representation of cis form of the complex number
    # in rectangular form
    def rect_to_cis(self):
        argument = complex_to_string(self.arg())
        modulo = complex_to_string(self.mod())
        if abs(m.sin(float(argument))) < 1e-7:
            return modulo
        else:
            if float(modulo) < 1e-7:
                return "0"
            elif modulo == "1.0":
                return f"cis({argument})"
            else:
                return f"{modulo}(cis({argument}))"

    # adds two complex numbers together
    @staticmethod
    def add(c1, c2):
        real = r.Real.add(c1.real, c2.real)
        imaginary = imag.Imaginary.add(c1.imaginary, c2.imaginary)
        return Complex(real, imaginary)

    # subtracts two complex numbers together
    @staticmethod
    def sub(c1, c2):
        real = r.Real.sub(c1.real, c2.real)
        imaginary = imag.Imaginary.sub(c1.imaginary, c2.imaginary)
        return Complex(real, imaginary)

    # multiplies two complex numbers together
    @staticmethod
    def mult(c1, c2):
        real = r.Real.mult(c1.real, c2.real) + imag.Imaginary.mult(c1.imaginary, c2.imaginary)
        imaginary = c1.real * c2.imaginary + c1.imaginary * c2.real
        return Complex(real, imaginary)

    # divides two complex numbers
    @staticmethod
    def div(c1, c2):
        numerator = Complex.mult(c1, c2.conjugate())
        denominator = Complex.mult(c2, c2.conjugate())
        real = r.Real.div(numerator.real, denominator.real)
        imaginary = imag.Imaginary.div(numerator.imaginary, denominator.real)
        return Complex(real, imaginary)

    # raises complex number, c1 to the power of another complex number, c2
    # input expression looks like (a + bi)^(c + di)
    @staticmethod
    def power(c1, c2):
        if c2.imaginary == 0:
            return pow_with_real_exp(c1, c2)
        else:
            return pow_with_complex_exp(c1, c2)

    # take the c2-th root of c1
    # input expression looks like (a + bi)^(1/(c + di))
    @staticmethod
    def root(c1, c2):
        exp = Complex.div(one, c2)
        return Complex.power(c1, exp)

    # takes in a complex number and returns the e to the power of that number.
    # assumes the input is a complex number of the form: c = a + bi
    # e^c = (e^a) * e^(bi)
    @staticmethod
    def exp(c):
        n_mod = Complex(m.exp(c.real), 0) # e^a

        # e^(bi) = cos(b) + i*sin(b)
        n_arg = c.imaginary
        return cis_correction(n_mod, n_arg)

    # takes in a complex number and returns the natural log of the number.
    # assumes the input is a complex number of the form: c = a + bi
    # using euler's form, can be re-written as c = r * e^(it),
    # where r is the mod and t is the argument of the number
    # the goal: ln(a + bi) = ln(r * e^(it)) = ln(r) + it
    @staticmethod
    def natural_log(c):
        assert c != zero, "cannot take the log of 0"
        real = m.log(c.mod().real, m.e)
        imaginary = c.arg().real
        return Complex(real, imaginary)

    # takes in a complex number and a base, and returns the log of the number.
    # assumes both inputs are a complex number of the form: c or b = a + bi
    # will utilize the natural log function made as follows:
    # result we want is y = log_b(c), where log_b means log in the base given
    # b^y = c
    # ln(b^y) = ln(c)
    # y*ln(b) = ln(c)
    # y = ln(c)/ln(b)
    # therefore log_b(c) = ln(c)/ln(b)
    @staticmethod
    def log(c, b):
        assert c != zero, "cannot take the log of 0"
        assert b != zero, "log with base 0 is not defined"
        # assert b != one, "log with base 1 is not defined" # can be handled, use 1 = e^(i(2pi))
        ln_c = Complex.natural_log(c)
        if b == one:
            ln_b = Complex(0, 2*m.pi)
        else:
            ln_b = Complex.natural_log(b)
        result = Complex.div(ln_c, ln_b)
        return result

    # trig functions
    # regular trig functions

    # takes the sine of a complex number, t
    # input is in the form t = a + bi
    # using the complex definition of the sine function
    # sin(t) = (e^(it) - e^(-it) )/2i
    @staticmethod
    def sin(c):
        return trig(Complex.sub, c, "2i")

    # takes the cosine of a complex number
    # input is in the form t = a + bi
    # using the complex definition of the cosine function
    # cos(t) = (e^(it) + e^(-it) )/2
    @staticmethod
    def cos(c):
        return trig(Complex.add, c, "2")

    # takes the tangent of a complex number
    # input is in the form c = a + bi
    @staticmethod
    def tan(c):
        sin_c = Complex.sin(c)
        cos_c = Complex.cos(c)
        return Complex.div(sin_c, cos_c)

    # reciprocal trig functions

    # takes the cosine of a complex number
    # input is in the form c = a + bi
    # will use the sine function
    # csc(c) = 1/sin(c)
    @staticmethod
    def csc(c):
        return reciprocal_trig(Complex.sin, c)

    # takes the cosine of a complex number
    # input is in the form c = a + bi
    # will use the cosine function
    # sec(c) = 1/cos(c)
    @staticmethod
    def sec(c):
        return reciprocal_trig(Complex.cos, c)

    # takes the cotangent of a complex number
    # input is in the form c = a + bi
    @staticmethod
    def cot(c):
        sin_c = Complex.sin(c)
        cos_c = Complex.cos(c)
        return Complex.div(cos_c, sin_c)

    # hyperbolic trig functions

    # takes the hyperbolic-sine of a complex number, t
    # input is in the form t = a + bi
    # using the relation between hyperbolic and regular trig functions
    # sinh(t) = sin(it)/i
    @staticmethod
    def sinh(c):
        return hyperbolic_trig(Complex.sin, Complex.div, c)

    # takes the hyperbolic-cosine of a complex number, t
    # input is in the form t = a + bi
    # using the relation between hyperbolic and regular trig functions
    # cosh(t) = cos(it)
    @staticmethod
    def cosh(c):
        return hyperbolic_trig(Complex.cos, return_first, c)

    # takes the hyperbolic-tangent of a complex number
    @staticmethod
    def tanh(c):
        sinh_c = Complex.sinh(c)
        cosh_c = Complex.cosh(c)
        return Complex.div(sinh_c, cosh_c)

    # inverse trig functions

    # takes the arcsin of a complex number, c
    # where c is in the form: c = a + bi
    # use the principal branch of the natural log for the complex definition
    # arcsin(c) = ln(ic + sqrt(1-c^2) )/i
    @staticmethod
    def arcsin(c):
        return inverse_trig(Complex.mult, return_first, c)

    # takes the arccos of a complex number, c
    # where c is in the form: c = a + bi
    # use the principal branch of the natural log for the complex definition
    # arccos(c) = ln(c + sqrt(c^2 - 1) )/i
    @staticmethod
    def arccos(c):
        return inverse_trig(return_first, mult_minus_one, c)

    # takes the arctan of a complex number, c
    # where c is in the form: c = a + bi
    # use complex definition of arctan(c)
    # arctan(c) = ln((1 + ic)/(1 - ic)) / (2i)
    @staticmethod
    def arctan(c):
        two_iota = Complex("2i") # 2i
        ic = Complex.mult(c, iota) # ic
        numerator_arg = Complex.add(one, ic) # 1 + ic
        denominator_arg = Complex.sub(one, ic) # 1 - ic
        arg = Complex.div(numerator_arg, denominator_arg) # (1 + ic)/(1 - ic)
        ln_arg = Complex.natural_log(arg)
        return Complex.div(ln_arg, two_iota)

    # non-elementary functions

    # takes the gamma of a complex number, c
    # where c is in the form: c = a + bi
    # utilizes the Euler reflection formula recursively and
    # Lanczos numerical approximation as a base case to calculate a value
    # Euler reflection formula is as follows:
    # Γ(c) * Γ(1 - c) = π/sin(πc)
    # hence, to calculate Γ(c):
    # Γ(c) = π/(sin(πc) * Γ(1 - c))
    # c cannot be an integer for the reflection formula
    # the reflection formula is good for approximating complex numbers with
    # a negative real part. This will be used while c.real < 0.5
    # when c.real >= 0.5, switch to Lanczos approximation
    # Lanczos is more efficient and works as follows:
    # Γ(c+1) ≈ sqrt(2π) * (c + g + 0.5)^(c + 0.5) * e^(-(c + g + 0.5)) * A(c)
    # g is Lanczos parameter which is typically 5
    # A(c) = a0 + a1/(c + 1) + a2/(c + 2) + a3/(c + 3) + ...
    # a0, a1, a2 are pre-calculated coefficients
    # only provides a very rough approximation
    @staticmethod
    def gamma(c):
        if c.imaginary == 0:
            return Complex(m.gamma(c.real), 0)
        elif c.real >= 0.5: # base case
            return lanczos_approx(c)
        else: # c.real < 0.5
            # use Euler's reflection
            # Γ(c) = π/(sin(πc) * Γ(1 - c))
            pic = Complex.mult(pi, c)  # πc
            sin_pic = Complex.sin(pic)  # sin(πc)
            new_arg = Complex.sub(one, c)  # 1 - c
            gamma_new_arg = Complex.gamma(new_arg)  # Γ(1 - c), recursive step
            denominator = Complex.mult(gamma_new_arg, sin_pic)  # sin(πc) * Γ(1 - c)
            result = Complex.div(pi, denominator)
            return result

    # takes the erf() of a complex number, c
    # where c is in the form: c = a + bi
    @staticmethod
    def erf(c):
        if c.imaginary == 0:
            return Complex(m.erf(c.real), 0)
        else:
            # return erf_continued_fraction_approx(c)
            # taylor polynomial approximation provides a better approximation
            return erf_taylor_approx(c)

    # takes the erfi() {imaginary error function} of a complex number, c
    # where c is in the form: c = a + bi
    # erfi(c) = -i * erf(i*c)
    @staticmethod
    def erf_i(c):
        # result = Complex.erf(c)
        # return Complex(result.imaginary, result.real)
        # or

        new_c = Complex.mult(c, iota) # new_c = i * c
        result = Complex.mult(Complex.erf(new_c), iota) # i*erf(ic)
        return Complex(-result.real, -result.imaginary) # -i*erf(ic)


    # takes the zeta (Riemann-Zeta function) of a complex number, c
    @staticmethod
    def zeta(c):
        # known cases
        # if c.real == 1:
        # undefined. Harmonic series, which diverges
        assert c.real != 1, f"zeta function diverges for {c}"
        # interesting to see what value zeta approaches for c = 0. -1/2? -1/12? undefined?
        # trivial zeros
        # for all negative and even integers, zeta returns a 0
        if c.imaginary == 0 and c.real < 0 and c.real%2 == 0:
            return Complex(0, 0)
        return zeta_helper(c)







# constants for functions
zero = Complex(0, 0)                    # 0
pi = Complex(m.pi, 0)                   # pi
pi_over_two = Complex(m.pi / 2, 0)      # pi/2
neg_pi_over_two = Complex(-m.pi / 2, 0)  # -pi/2
one = Complex(1, 0)                     # 1
iota = Complex(0, 1)                    # i



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
def string_to_complex_one_arg(complex_number: list[str]):
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
def string_to_complex_three_arg(complex_number: list[str]):
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

# helper, higher-order function for sine and cosine
# abstracts away most of the code required for sine and cosine
def trig(func, c: Complex, denominator: str):
    neg_iota = Complex("-i")
    denominator = Complex(denominator)
    ic = Complex.mult(iota, c)
    neg_ic = Complex.mult(neg_iota, c)

    # e^(ic)
    eic = Complex.exp(ic)
    # e^(-ic)
    neg_eic = Complex.exp(neg_ic)

    numerator = func(eic, neg_eic)
    return Complex.div(numerator, denominator)

# helper, higher-order function for co-secant and secant
# abstracts away most of the code required for co-secant and secant
def reciprocal_trig(func, c: Complex):
    # one = numerator
    denominator = func(c)
    return Complex.div(one, denominator)

# helper, higher-order function for sinh and cosh
# abstracts away most of the code required for sinh and cosh
def hyperbolic_trig(func1, func2, c: Complex):
    it = Complex.mult(iota, c)
    result = func1(it)
    return func2(result, iota)

# helper, higher-order function for arc-sine and arc-cosine
# abstracts away most of the code required for arc-sine and arc-cosine
def inverse_trig(func1, func2, c: Complex):
    # iota = denominator
    two = Complex("2")  # 2

    # numerator
    ic = func1(c, iota)  # ic for arc-sine and c for arc-cosine
    c_squared = Complex.power(c, two)  # c^2
    diff = Complex.sub(one, c_squared)  # 1 - c^2
    diff = func2(diff)              # (1 - c^2) for arc-sine and (c^2 -1) for arc-cosine
    sqrt = Complex.root(diff, two)  # sqrt(1 - c^2) or sqrt(c^2 - 1)
    summ = Complex.add(ic, sqrt)  # ic + sqrt(1 - c^2) or c + sqrt(c^2 - 1)
    numerator = Complex.natural_log(summ)  # ln(ic + sqrt(1 - c^2)) or ln(c + sqrt(c^2 - 1))

    result = Complex.div(numerator, iota)
    return result

# helper function for hyperbolic_trig and inverse_trig when performing cosh
# returns first argument
def return_first(result, arbitrary = 0):
    return result

# helper function for hyperbolic_trig and inverse_trig when performing cosh
# returns input Complex number, times -1
def mult_minus_one(c: Complex):
    return Complex(-c.real, -c.imaginary)


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
    n_mod = Complex(pow(modulo.real, exp.real), 0)

    # r^(di) = e^(ln(r^d)i) = cos(ln(r^d)) + i*sin(ln(r^d))
    n_arg = m.log(pow(modulo.real, exp.imaginary), m.e)  # ln(r^d)
    # rdi = Complex(m.cos(n_arg), m.sin(n_arg))

    # (r ^ c) * (r ^ di)
    return cis_correction(n_mod, n_arg)


# helper for pow_with_complex_exp() and sin and cos
# the following code works as follows:
# a + bi = r*e^ti where r is modulus and t is the argument.
# ti is c1_exponent
# when raised to the power of c + di, we get (r^(c + di))*e^((c + di)ti)
# this part of the code will focus on e^((c + di)ti, which yields a complex number
# e^((c + di)ti) = (e^-(dt)) * (e^(cti))
def new_cis(c1_exponent, exp):
    # (e^-(dt))
    n_mod = Complex(m.exp(-1 * c1_exponent.imaginary * exp.imaginary), 0)

    # (e ^ (cti)) = cos(ct) + i*sin(ct)
    n_arg = exp.real * c1_exponent.imaginary # ct
    # ecti = Complex(m.cos(ct), m.sin(ct))

    # (e^-(dt))*(e^(cti))
    return cis_correction(n_mod, n_arg)


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
    error = 1e-15
    sin_n_arg = m.sin(n_arg)
    cos_n_arg = m.cos(n_arg)
    if abs(sin_n_arg) < error: # when the argument is 0 or pi or -pi
        if cos_n_arg < 0:
            n_cis = Complex(-1, 0) # when the argument is pi or -pi
        else:
            n_cis = Complex(1, 0) # when the argument is 0
    elif abs(cos_n_arg) < error: # when the argument is pi/2 or -pi/2
        if sin_n_arg < 0:
            n_cis = Complex(0, -1) # when the argument is -pi/2
        else:
            n_cis = Complex(0, 1) # when the argument is pi/2
    else:
        n_cis = Complex(cos_n_arg, sin_n_arg)
    return Complex.mult(n_mod, n_cis)

# Lanczos approximation helper function for the gamma function
def lanczos_approx(c: Complex):
    # use Lanczos approximation
    # Γ(c+1) ≈ sqrt(2π) * (c + g + 0.5)^(c + 0.5) * e^(-(c + g + 0.5)) * A(c)

    # approximation term (A(c)). a.k.a, a0, a1, a2...
    # the following list consists of coefficients staring from a1
    coefficients = [676.5203681218851, -1259.1392167224028, 771.3234287776531,
                    -176.6150291621406, 12.507343278686905, -0.13857109526572012,
                    9.984369578019571e-6, 1.5056327351493116e-7, -1.2109640976628544e-9]
                    # -5.363819747944671e-11, 4.5052547179567e-13, -7.08150596454932e-15,
                    # 1.19506271168695e-16, 2.315818733241201e-18, -5.027761020408414e-20]

    # result = A(c) = a0 + a1/(c + 1) + a2/(c + 2) + a3/(c + 3) + ...
    term = Complex(1.000000000190015, 0.999999998819215)
    result = Complex(0.9999999999998099, 0)               # a0 = 0.9999999999998099
    for index, coefficient in enumerate(coefficients):
        # term = term /= (c + i + 1)
        term = Complex.div(term, Complex.add(c, Complex(str(index + 1))))
        # result += coefficient * term
        result = Complex.add(result, Complex.mult(Complex(str(coefficient)), term))

    # p = c + (g+1) - 0.5 = c + g + 0.5
    p = Complex.add(c, Complex(str(len(coefficients) - 0.5)))

    # q = c + 0.5
    q = Complex(c.real + 0.5, c.imaginary)

    # exp_p_nep = e^(-p) = e^(-(c + g + 0.5))
    p_neg = Complex(-1 * p.real, -1 * p.imaginary)
    exp_p_nep = Complex.exp(p_neg)

    # p_to_q = p^q = (c + g + 0.5)^(c + 0.5)
    p_to_q = Complex.power(p, q)

    # sqrt(2pi)
    sqrt_two_pi = Complex.root(Complex(2 * m.pi, 0), Complex("2"))

    # result = sqrt(2π) * (c + g + 0.5)^(c + 0.5) * e^(-(c + g + 0.5)) * A(c)
    result = Complex.mult(result, exp_p_nep)
    result = Complex.mult(result, p_to_q)
    result = Complex.mult(result, sqrt_two_pi)

    return result

# helper function for the complex error function that uses the continued fraction approximation
def erf_continued_fraction_approx(complex_number: Complex):
    if complex_number.imaginary == 0:
        return m.erf(complex_number.real)  # Use math.erf for real numbers
    else:
        a = Complex.mult(Complex(1, 0), complex_number)  # (1 + 0i) * c
        b = Complex(m.sqrt(m.pi), 0)  # ((0 + 0i) * c) + sqrt(π)
        c = Complex.mult(Complex(1, 0), complex_number)  # (1 + 0i) * c
        d = Complex.add(Complex.mult(complex_number, complex_number), Complex(0.5, 0))  # (0.5 + 0i) + c^2

        n = 100  # Number of iterations
        error = 1e-15  # Tolerance for convergence

        for i in range(n):
            an = Complex.mult(a, Complex(1 + 2*i, 0))  # an = (2 * i + 1) * a
            bn = Complex.mult(d, Complex(1 + 2*i, 0))  # bn = (2 * i + 1) * d
            c, d = d, Complex.sub(Complex.mult(bn, d), Complex.mult(an, c))  # c, d = d, bn * d - an * c
            c = Complex.div(c, d)  # c = c/d
            a = an
            b = Complex.add(b, c)
            if c.mod().real < error:
                break

        # (0.5 - 0.5j) * e^(-z ^ 2) / z * b
        num = Complex(0.5, 0.5)
        result = Complex.mult(complex_number, complex_number)
        result = Complex.exp(Complex(-result.real, -result.imaginary))
        result = Complex.div(result, complex_number)
        result = Complex.mult(result, b)
        result = Complex.mult(num, result)
        return result

# helper function for the complex error function that uses the taylor series approximation
def erf_taylor_approx(c: Complex):
    result = c
    term = c

    for i in range(1, 50):
        num1 = Complex.mult(c, c)                                 # c^2
        num1 = Complex.exp(Complex(-num1.real, -num1.imaginary))  # e^(-c^2)
        num2 = Complex(1 + 2*i, 0)                                # 1+2*(iteration no.)
        term = Complex.mult(term, num1)
        term = Complex.div(term, num2)
        result = Complex.add(result, term)

    sqrt_pi = Complex(m.pi ** 0.5, 0)
    result = Complex.div(result, sqrt_pi)
    return Complex(result.real*2, result.imaginary*2)



# helper function for the Riemann-Zeta function
# gives an approximation for the zeta function by calculating the first n terms in the series for "c"
def zeta_helper(c: Complex, n: int = 100):
    result = Complex(0, 0)
    for i in range(1, n+1):
        step_1 = Complex(i, 0)
        step_2 = Complex.power(step_1, c)
        step_3 = Complex.div(one, step_2)
        result =  Complex.add(result, step_3)
    return result


# testing
t1 = Complex(m.e, 0)
t2 = Complex(0, m.pi)
t3 = Complex.gamma(Complex("1 + i"))      # i! = 0.498015668 - 0.154949828i
t4 = Complex.power(t1, t2)
# print(t1)
# # print(t2)
print(t4)
print(Complex.zeta(Complex(2, 0)))
print((m.pi**2)/6)

# t4 = Complex("0")
# t5 = Complex(str(m.pi/2))
# print(Complex.sin(t4))
# print(Complex.sin(t5))
# print(Complex.cos(t4))
# print(Complex.cos(t5))
# print(Complex.sin(pi))
# print(Complex.cos(pi))


#print(Complex.power(t1, t1))








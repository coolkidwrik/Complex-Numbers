from model.complex import Complex
import unittest as t
import math as m

class TestComplex(t.TestCase):

    # setup
    @classmethod
    def setUpClass(cls):
        cls.zero = Complex(0, 0)
        cls.one = Complex(1, 0)        # 1
        cls.neg_one = Complex(-1, 0)   # -1
        cls.i = Complex(0, 1)          # i
        cls.neg_i = Complex(0, -1)     # -i
        cls.pi = Complex(m.pi, 0)                   # π
        cls.pi_over_two = Complex(m.pi / 2, 0)      # π/2
        cls.pi_over_four = Complex(m.pi / 4, 0)     # π/4
        cls.neg_pi_over_two = Complex(-m.pi / 2, 0) # -π/2
        cls.E = Complex(m.e, 0)                    # e
        cls.a = Complex(1, 1)          # 1 + i
        cls.b = Complex(1, -1)         # 1 - i
        cls.c = Complex(-1, 1)         # -1 + i
        cls.d = Complex(3, 4)          # 3 + 4i
        cls.e = Complex(7, -14)        # 7 - 14i




    # testing


    # test for conjugate of a complex number
    def test_conjugate(self):
        self.assertEqual(self.i.conjugate(), self.neg_i)
        self.assertEqual(self.a.conjugate(), self.b)
        self.assertNotEqual(self.a.conjugate(), self.c)
        self.assertNotEqual(self.d.conjugate(), self.d)


    # test get_sign(gets the sign of the imaginary component)
    def test_get_sign(self):
        self.assertEqual(self.i.get_sign(), "+")
        self.assertEqual(self.i.conjugate().get_sign(), self.neg_i.get_sign())
        self.assertEqual(self.c.get_sign(), self.d.get_sign())
        self.assertNotEqual(self.a.conjugate().get_sign(), "+")
        self.assertNotEqual(self.d.get_sign(), self.e.get_sign())


    # test for argument of a complex number
    def test_arg(self):
        self.assertEqual(self.zero.arg(), self.zero)
        self.assertEqual(self.one.arg(), self.zero)
        self.assertEqual(self.neg_one.arg(), self.pi)
        self.assertEqual(self.i.arg(), self.pi_over_two)
        self.assertEqual(self.neg_i.arg(), self.neg_pi_over_two)
        self.assertEqual(self.a.arg(), self.pi_over_four)
        self.assertEqual(self.e.arg(), Complex(m.atan(-2), 0))


    # test to get the modulus of a complex number
    def test_mod(self):
        self.assertEqual(self.one.mod(), self.one)
        self.assertEqual(self.pi.mod(), self.pi)
        self.assertEqual(self.i.mod(), self.one)
        self.assertEqual(self.neg_i.mod(), self.one)
        self.assertEqual(self.a.mod(), Complex(m.sqrt(2), 0))
        self.assertEqual(self.d.mod(), Complex.root(Complex.mult(self.d, self.d.conjugate()), Complex(2, 0)))


    # test to convert rectangular form to euler form
    def test_rect_to_euler(self):
        self.assertEqual(self.zero.rect_to_euler(), "0")
        self.assertEqual(self.one.rect_to_euler(), "1.0")
        self.assertEqual(self.i.rect_to_euler(), f"e^({self.pi_over_two.real}i)")
        self.assertEqual(self.a.rect_to_euler(), f"{m.sqrt(2)}e^({self.pi_over_four.real}i)")
        self.assertEqual(self.d.rect_to_euler(), f"{self.d.mod()}e^({self.d.arg()}i)")


    # test to convert rectangular form to cis form
    def test_rect_to_cis(self):
        self.assertEqual(self.zero.rect_to_cis(), "0")
        self.assertEqual(self.one.rect_to_cis(), "1.0")
        po2 = self.pi_over_two.real
        self.assertEqual(self.i.rect_to_cis(), f"cos({po2}) + isin({po2})")
        po4 = self.pi_over_four.real
        self.assertEqual(self.a.rect_to_cis(), f"{m.sqrt(2)}(cos({po4}) + isin({po4}))")
        self.assertEqual(self.d.rect_to_cis(), f"{self.d.mod()}(cos({self.d.arg()}) + isin({self.d.arg()}))")




    # test static methods


    # test adding two complex numbers
    def test_add(self):
        # combining real and imaginary components
        self.assertEqual(Complex.add(self.i, self.one), self.a)
        self.assertEqual(Complex.add(self.one, self.i), self.a)
        self.assertEqual(Complex.add(self.one, self.neg_i), self.b)
        self.assertEqual(Complex.add(self.neg_i, self.one), self.b)
        self.assertEqual(Complex.add(self.neg_one, self.i), self.c)
        # adding only real numbers
        self.assertEqual(Complex.add(self.one, self.one), Complex(2, 0))
        self.assertEqual(Complex.add(self.one, self.neg_one), self.zero)
        # adding only imaginary numbers
        self.assertEqual(Complex.add(self.i, self.i), Complex(0, 2))
        self.assertEqual(Complex.add(self.i, self.neg_i), self.zero)
        # adding complex numbers
        self.assertEqual(Complex.add(self.a, self.a), Complex(2, 2))
        self.assertEqual(Complex.add(self.a, self.b), Complex(2, 0))
        self.assertEqual(Complex.add(self.a, self.c), Complex(0, 2))
        self.assertEqual(Complex.add(self.d, self.e), Complex(10, -10))


    # test subtracting two complex numbers
    def test_sub(self):
        # combining real and imaginary components
        self.assertEqual(Complex.sub(self.i, self.one), self.c)
        self.assertEqual(Complex.sub(self.one, self.i), self.b)
        self.assertEqual(Complex.sub(self.one, self.neg_i), self.a)
        self.assertEqual(Complex.sub(self.neg_i, self.one), Complex(-1, -1))
        self.assertEqual(Complex.sub(self.neg_one, self.i), Complex(-1, -1))
        # subtracting only real numbers
        self.assertEqual(Complex.sub(self.one, self.one), self.zero)
        self.assertEqual(Complex.sub(self.one, self.neg_one), Complex(2, 0))
        # subtracting only imaginary numbers
        self.assertEqual(Complex.sub(self.i, self.i), self.zero)
        self.assertEqual(Complex.sub(self.i, self.neg_i), Complex(0, 2))
        # subtracting complex numbers
        self.assertEqual(Complex.sub(self.a, self.a), self.zero)
        self.assertEqual(Complex.sub(self.a, self.b), Complex(0, 2))
        self.assertEqual(Complex.sub(self.a, self.c), Complex(2, 0))
        self.assertEqual(Complex.sub(self.d, self.e), Complex(-4, 18))


    # test multiplying two complex numbers
    def test_mult(self):
        # multiplying real and imaginary components
        self.assertEqual(Complex.mult(self.i, self.one), self.i)
        self.assertEqual(Complex.mult(self.one, self.i), self.i)
        self.assertEqual(Complex.mult(self.one, self.neg_i), self.neg_i)
        self.assertEqual(Complex.mult(self.neg_i, self.one), self.neg_i)
        self.assertEqual(Complex.mult(self.neg_one, self.i), self.neg_i)
        self.assertEqual(Complex.mult(self.neg_one, self.neg_i), self.i)
        # multiplying only real numbers
        two = Complex(2, 0)
        three = Complex(3, 0)
        self.assertEqual(Complex.mult(self.one, self.one), self.one)
        self.assertEqual(Complex.mult(self.one, self.neg_one), self.neg_one)
        self.assertEqual(Complex.mult(self.neg_one, self.one), self.neg_one)
        self.assertEqual(Complex.mult(two, three), Complex(6, 0))
        # multiplying only imaginary numbers
        i_squared = Complex.mult(self.i, self.i)
        i_cubed = Complex.mult(self.i, i_squared)
        i_to_the_fourth = Complex.mult(self.i, i_cubed)
        i_to_the_fifth = Complex.mult(self.i, i_to_the_fourth)
        i3 = Complex(0, 3)
        i4 = Complex(0, 4)
        self.assertEqual(i_squared, self.neg_one)
        self.assertEqual(i_cubed, self.neg_i)
        self.assertEqual(i_to_the_fourth, self.one)
        self.assertEqual(i_to_the_fifth, self.i)
        self.assertEqual(Complex.mult(i3, i4), Complex(-12, 0))
        # multiplying complex numbers
        self.assertEqual(Complex.mult(self.a, self.a), Complex(0, 2))
        self.assertEqual(Complex.mult(self.a, self.b), Complex(2, 0))
        self.assertEqual(Complex.mult(self.a, self.c), Complex(-2, 0))
        self.assertEqual(Complex.mult(self.d, self.e), Complex(77, -14))


    # test dividing two complex numbers
    def test_div(self):
        # divide by 0 = undefined
        self.assertRaises(AssertionError, Complex.div, self.a, self.zero)
        self.assertRaises(AssertionError, Complex.div, self.b, self.zero)
        self.assertRaises(AssertionError, Complex.div, self.d, self.zero)
        # dividing real and imaginary components
        self.assertEqual(Complex.div(self.i, self.one), self.i)
        self.assertEqual(Complex.div(self.one, self.i), self.neg_i)
        self.assertEqual(Complex.div(self.one, self.neg_i), self.i)
        self.assertEqual(Complex.div(self.neg_i, self.one), self.neg_i)
        self.assertEqual(Complex.div(self.neg_one, self.i), self.i)
        self.assertEqual(Complex.div(self.neg_one, self.neg_i), self.neg_i)
        # dividing only real numbers
        two = Complex(2, 0)
        three = Complex(3, 0)
        six = Complex(6, 0)
        self.assertEqual(Complex.div(self.one, self.one), self.one)
        self.assertEqual(Complex.div(self.one, self.neg_one), self.neg_one)
        self.assertEqual(Complex.div(self.neg_one, self.one), self.neg_one)
        self.assertEqual(Complex.div(two, three), Complex(2/3, 0))
        self.assertEqual(Complex.div(six, three), two)
        # dividing only imaginary numbers
        i_to_the_0 = Complex.div(self.i, self.i)
        i_to_the_neg_one = Complex.div(i_to_the_0, self.i)
        i_to_the_neg_two = Complex.div(i_to_the_neg_one, self.i)
        i_to_the_neg_three = Complex.div(i_to_the_neg_two, self.i)

        i3 = Complex(0, 3)
        i4 = Complex(0, 4)
        self.assertEqual(i_to_the_0, self.one)
        self.assertEqual(i_to_the_neg_one, self.neg_i)
        self.assertEqual(i_to_the_neg_two, self.neg_one)
        self.assertEqual(i_to_the_neg_three, self.i)
        self.assertEqual(Complex.div(i3, i4), Complex(3/4, 0))
        # dividing complex numbers
        self.assertEqual(Complex.div(self.a, self.a), self.one)
        self.assertEqual(Complex.div(self.a, self.b), self.i)
        self.assertEqual(Complex.div(self.a, self.c), self.neg_i)
        self.assertEqual(Complex.div(self.d, self.e), Complex(-0.14285714285714285, 0.2857142857142857))


    # test taking a complex power of complex numbers
    def test_power(self):
        two = Complex(2, 0)
        three = Complex(3, 0)
        four = Complex(4, 0)
        five = Complex(5, 0)

        # test with real base and exponent
        self.assertEqual(Complex.power(self.one, self.one), self.one)
        self.assertEqual(Complex.power(self.one, self.neg_one), self.one)
        self.assertEqual(Complex.power(self.one, two), self.one)
        self.assertEqual(Complex.power(self.neg_one, self.one), self.neg_one)
        self.assertEqual(Complex.power(self.neg_one, two), self.one)
        self.assertEqual(Complex.power(self.neg_one, three), self.neg_one)
        self.assertEqual(Complex.power(two, three), Complex(8, 0))
        self.assertEqual(Complex.power(three, two), Complex(9, 0))
        self.assertEqual(Complex.power(two, two), Complex(4, 0))
        self.assertEqual(Complex.power(three, three), Complex(27, 0))

        # test with real base and imaginary exponent
        ipi = Complex.mult(self.pi, self.i)
        ipi_over_two = Complex.mult(self.pi_over_two, self.i)
        self.assertEqual(Complex.power(self.one, ipi), self.one)
        self.assertEqual(Complex.power(two, ipi), Complex(-0.5702332487688776, 0.8214828312256388))
        self.assertEqual(Complex.power(self.one, ipi_over_two), self.one)
            # e^(iπ) = -1
        self.assertEqual(Complex.power(self.E, ipi), self.neg_one)
            # e^(iπ/2) = i
        self.assertEqual(Complex.power(self.E, ipi_over_two), self.i)

        # test with imaginary base and real exponent
        i_to_the_0 = Complex.power(self.i, self.zero)
        i_squared = Complex.power(self.i, two)
        i_cubed = Complex.power(self.i, three)
        i_to_the_fourth = Complex.power(self.i, four)
        i_to_the_fifth = Complex.power(self.i, five)
        i3 = Complex(0, 3)

        self.assertEqual(i_to_the_0, self.one)
        self.assertEqual(i_squared, self.neg_one)
        self.assertEqual(i_cubed, self.neg_i)
        self.assertEqual(i_to_the_fourth, i_to_the_0)
        self.assertEqual(i_to_the_fifth, self.i)
        self.assertEqual(Complex.power(i3, self.one), i3)
        self.assertEqual(Complex.power(i3, two), Complex(-9, 0))

        # test with imaginary base and exponent
        self.assertEqual(Complex.power(i3, self.i), Complex(0.09455037136778624, 0.18513277812960613))
            # i^i = 0.20787957635076193
        self.assertEqual(Complex.power(self.i, self.i), Complex(0.20787957635076193, 0))

        # test with complex base and real exponent
        self.assertEqual(Complex.power(self.a, two), Complex(0, 2))
        self.assertEqual(Complex.power(self.a, three), Complex(-2, 2))
        self.assertEqual(Complex.power(self.b, three), Complex(-2, -2))
        self.assertEqual(Complex.power(self.c, three), Complex(2, 2))
        self.assertEqual(Complex.power(self.e, three), Complex(-3773, 686))

        # test with complex base and imaginary exponent
        self.assertEqual(Complex.power(self.a, self.i), Complex(0.4288290062943679, 0.1548717524642468))
        self.assertEqual(Complex.power(self.a, self.neg_i), Complex(2.0628722350809046, -0.745007062179724))
        self.assertEqual(Complex.power(self.b, self.i), Complex(2.0628722350809046, 0.745007062179724))
        self.assertEqual(Complex.power(self.c, i3), Complex(0.0004312203536189743, 0.000734163645397619))
        self.assertEqual(Complex.power(self.e, i3), Complex(-10.73357878989517, 25.536275610786227))

        # test with real base and complex exponent
        self.assertEqual(Complex.power(self.one, self.a), self.one)
        self.assertEqual(Complex.power(self.one, self.e), self.one)
        self.assertEqual(Complex.power(two, self.b), Complex(1.5384778027279442, -1.2779225526272695))
        self.assertEqual(Complex.power(three, self.c), Complex(0.15161080760886989, 0.296859013889249))
        self.assertEqual(Complex.power(four, self.d), Complex(47.34786346201795, -43.06018840625417))

        # test with imaginary base and complex exponent
        self.assertEqual(Complex.power(self.i, self.a), Complex(1.272895288930342e-17, 0.20787957635076193))
        self.assertEqual(Complex.power(i3, self.d), Complex(-0.047893929427421704, 0.015762109683589577))

        # test with complex base and complex exponent
        self.assertEqual(Complex.power(self.a, self.a), Complex(0.2739572538301211, 0.5837007587586147))
        self.assertEqual(Complex.power(self.a, self.b), Complex(2.8078792972606292, 1.3178651729011808))
        self.assertEqual(Complex.power(self.e, self.d), Complex(55299.43691682981, 316620.1042138665))


    # test taking a complex root of complex numbers
    def test_root(self):
        # derivative of the power function
        # use the power function for testing
        two = Complex(2, 0)
        three = Complex(3, 0)
        four = Complex(4, 0)
        twenty7 = Complex(27, 0)

        self.assertEqual(Complex.root(self.one, two), self.one)
        self.assertEqual(Complex.root(self.one, twenty7), self.one)
        self.assertEqual(Complex.root(two, two), Complex(1.4142135623730951, 0))
        self.assertEqual(Complex.root(two, three), Complex(1.2599210498948732, 0))
        self.assertEqual(Complex.root(four, two), two)
        self.assertEqual(Complex.root(twenty7, three), three)
        self.assertEqual(Complex.root(self.a, self.i), Complex.power(self.a, self.neg_i))
        self.assertEqual(Complex.root(self.a, self.b), Complex.power(self.a, Complex.power(self.b,self.neg_one)))
        self.assertEqual(Complex.root(self.d, self.e), Complex.power(self.d, Complex.power(self.e,self.neg_one)))

        # i√i = 4.810477380965351
        self.assertEqual(Complex.root(self.i, self.i), Complex(4.810477380965351, 0))


    # test taking e to the power of a complex number
    def test_exp(self):
        self.assertEqual(Complex.exp(self.i), Complex(0.5403023058681398, 0.8414709848078965))
        self.assertEqual(Complex.exp(self.a), Complex(1.4686939399158851, 2.2873552871788423))
        self.assertEqual(Complex.exp(self.b), Complex(1.4686939399158851, -2.2873552871788423))

        # identities
            # e^1 = e
        self.assertEqual(Complex.exp(self.one), self.E)
            # e^0 = 1
        self.assertEqual(Complex.exp(self.zero), self.one)
            # e^(iπ/2) = i
        ipi_over_2 = Complex.mult(self.pi_over_two, self.i)
        self.assertEqual(Complex.exp(ipi_over_2), self.i)
            # e^(-iπ/2) = -i
        neg_ipi_over_2 = Complex.mult(self.neg_pi_over_two, self.i)
        self.assertEqual(Complex.exp(neg_ipi_over_2), self.neg_i)
            # e^(iπ) = -1
        ipi = Complex.mult(self.pi, self.i)
        neg_ipi = Complex.mult(self.pi, self.neg_i)
        self.assertEqual(Complex.exp(ipi), self.neg_one)
        self.assertEqual(Complex.exp(neg_ipi), self.neg_one)

    # test taking natural log of a complex number
    def test_natural_log(self):
        ipi_over_2 = Complex.mult(self.pi_over_two, self.i)
        neg_ipi_over_2 = Complex.mult(self.neg_pi_over_two, self.i)
        ipi = Complex.mult(self.pi, self.i)

        self.assertEqual(Complex.natural_log(self.a), Complex(0.34657359027997264, 0.7853981633974483))
        self.assertEqual(Complex.natural_log(self.b), Complex(0.34657359027997264, -0.7853981633974483))
        self.assertEqual(Complex.natural_log(self.e), Complex(2.7506291052723637, -1.1071487177940904))
        # identities
            # ln(0) = undefined
        self.assertRaises(AssertionError, Complex.natural_log, self.zero)

            # ln(-1) = iπ
        self.assertEqual(Complex.natural_log(self.neg_one), ipi)
            # ln(1) = 0
        self.assertEqual(Complex.natural_log(self.one), self.zero)
            # ln(i) = iπ/2
        self.assertEqual(Complex.natural_log(self.i), ipi_over_2)
            # ln(-i) = -iπ/2
        self.assertEqual(Complex.natural_log(self.neg_i), neg_ipi_over_2)


    # test taking log of a complex number with a complex base
    def test_log(self):
        # derivative of natural_log function
        # assertion error tests.
        # test for base 0
        self.assertRaises(AssertionError, Complex.log, self.one, self.zero)
        # test for base 1
        self.assertRaises(AssertionError, Complex.log, self.one, self.one)

        # regular tests
        self.assertEqual(Complex.log(self.a, self.i), Complex(0.5, -0.2206356001526516))
        self.assertEqual(Complex.log(self.a, self.neg_i), Complex(-0.5, 0.2206356001526516))
        self.assertEqual(Complex.log(self.a, self.neg_one), Complex(0.25, -0.1103178000763258))
        self.assertEqual(Complex.log(self.b, self.i), Complex(-0.5, -0.2206356001526516))
        self.assertEqual(Complex.log(self.b, self.neg_i), Complex(0.5, 0.2206356001526516))
        self.assertEqual(Complex.log(self.d, self.b), Complex(-0.2313646183234306, 2.1512945377428627))
        self.assertEqual(Complex.log(self.e, self.d), Complex(0.9855503329158666, -1.2557457563244918))

    # test trig functions

    # test taking sine of a complex number
    def test_sin(self):
        self.assertEqual(Complex.sin(self.a), Complex(1.2984575814159773, 0.6349639147847361))
        self.assertEqual(Complex.sin(self.b), Complex(1.2984575814159773, -0.6349639147847361))
        self.assertEqual(Complex.sin(self.d), Complex(3.853738037919377, -27.016813258003936))
        # identities
            # sin(0) = 0
        self.assertEqual(Complex.sin(self.zero), self.zero)
            # sin(π/2) = 1
        self.assertEqual(Complex.sin(self.pi_over_two), self.one)
            # sin(π/4) = 1/√(2)
        self.assertEqual(Complex.sin(self.pi_over_four), Complex(0.7071067811865475, 0))
            # sin(-π/2) = -1
        self.assertEqual(Complex.sin(self.neg_pi_over_two), self.neg_one)
            # sin(π) = 0
        self.assertEqual(Complex.sin(self.pi), self.zero)

    # test taking cosine of a complex number
    def test_cos(self):
        self.assertEqual(Complex.cos(self.a), Complex(0.8337300251311491, -0.9888977057628651))
        self.assertEqual(Complex.cos(self.b), Complex(0.8337300251311491, 0.9888977057628651))
        self.assertEqual(Complex.cos(self.d), Complex(-27.034945603074224, -3.8511533348117775))
        # identities
            # cos(0) = 1
        self.assertEqual(Complex.cos(self.zero), self.one)
            # cos(π/2) = 0
        self.assertEqual(Complex.cos(self.pi_over_two), self.zero)
            # cos(π/4) = 1/√(2)
        self.assertEqual(Complex.cos(self.pi_over_four), Complex(0.7071067811865475, 0))
            # cos(-π/2) = 0
        self.assertEqual(Complex.cos(self.neg_pi_over_two), self.zero)
            # cos(π) = -1
        self.assertEqual(Complex.cos(self.pi), self.neg_one)

    # test taking tangent of a complex number
    def test_tan(self):
        # derivative of sine and cosine
        self.assertEqual(Complex.tan(self.a), Complex(0.2717525853195118, 1.0839233273386946))
        self.assertEqual(Complex.tan(self.b), Complex(0.2717525853195118, -1.0839233273386946))
        self.assertEqual(Complex.tan(self.d), Complex(-0.0001873462046294784, 0.999355987381473))
        # test for singularities
        self.assertRaises(AssertionError, Complex.tan, self.pi_over_two)
        self.assertRaises(AssertionError, Complex.tan, self.neg_pi_over_two)

        # identities
        # tan(0) = 0
        self.assertEqual(Complex.tan(self.zero), self.zero)
        # tan(π/4) = 1
        self.assertEqual(Complex.tan(self.pi_over_four), self.one)
        # tan(π) = 0
        self.assertEqual(Complex.tan(self.pi), self.zero)

    # test taking cosecant of a complex number
    def test_csc(self):
        # derivative of the sine function

        self.assertEqual(Complex.csc(self.a), Complex(0.6215180171704284, -0.30393100162842646))
        self.assertEqual(Complex.csc(self.b), Complex(0.6215180171704284, 0.30393100162842646))
        self.assertEqual(Complex.csc(self.d), Complex(0.005174473184019397, 0.03627588962862601))
        # test for singularities
        self.assertRaises(AssertionError, Complex.csc, self.zero)
        self.assertRaises(AssertionError, Complex.csc, self.pi)

    # test taking secant of a complex number
    def test_sec(self):
        # derivative of the cosine function

        self.assertEqual(Complex.sec(self.a), Complex(0.49833703055518686, 0.5910838417210451))
        self.assertEqual(Complex.sec(self.b), Complex(0.49833703055518686, -0.5910838417210451))
        self.assertEqual(Complex.sec(self.d), Complex(-0.03625349691586887, 0.00516434460775318))
        # test for singularities
        self.assertRaises(AssertionError, Complex.sec, self.pi_over_two)
        self.assertRaises(AssertionError, Complex.sec, self.neg_pi_over_two)

    # test taking cotangent of a complex number
    def test_cot(self):
        # derivative of the tangent function

        self.assertEqual(Complex.cot(self.a), Complex(0.21762156185440273, -0.8680141428959249))
        self.assertEqual(Complex.cot(self.b), Complex(0.21762156185440273, 0.8680141428959249))
        self.assertEqual(Complex.cot(self.d), Complex(-0.0001875877379836592, -1.0006443924715591))
        # test for singularities
        self.assertRaises(AssertionError, Complex.cot, self.zero)
        self.assertRaises(AssertionError, Complex.cot, self.pi)

    # test taking hyperbolic sine of a complex number
    def test_sinh(self):
        ipi_over_2 = Complex.mult(self.pi_over_two, self.i)
        # identities
            # sinh(0) = 0
        self.assertEqual(Complex.sinh(self.zero), self.zero)
            # sinh(iπ/2) = i
        self.assertEqual(Complex.sinh(ipi_over_2), self.i)
        # general test
        self.assertEqual(Complex.sinh(self.a), Complex(0.6349639147847361, 1.2984575814159773))

    # test taking hyperbolic cosine of a complex number
    def test_cosh(self):
        ipi_over_2 = Complex.mult(self.pi_over_two, self.i)
        # identities
            # cosh(0) = 1
        self.assertEqual(Complex.cosh(self.zero), self.one)
            # cosh(iπ/2) = 0
        self.assertEqual(Complex.cosh(ipi_over_2), self.zero)
        # general test
        self.assertEqual(Complex.cosh(self.a), Complex(0.8337300251311491, 0.9888977057628651))

    # test taking hyperbolic tangent of a complex number
    def test_tanh(self):
        ipi_over_2 = Complex.mult(self.pi_over_two, self.i)
        # test for singularities
        self.assertRaises(AssertionError, Complex.tanh, ipi_over_2)
        # identities
            # tanh(0) = 0
        self.assertEqual(Complex.tanh(self.zero), self.zero)
        # general test
        self.assertEqual(Complex.tanh(self.a), Complex(1.0839233273386946, 0.2717525853195118))

    # test taking inverse  sine of a complex number
    def test_arcsin(self):
        # identities
            # arc-sin(0) = 0
        self.assertEqual(Complex.arcsin(self.zero), self.zero)
            # arc-sin(1) = π/2
        self.assertEqual(Complex.arcsin(self.one), self.pi_over_two)
            # arc-sin(-1) = -π/2
        self.assertEqual(Complex.arcsin(self.neg_one), self.neg_pi_over_two)
            # arc-sin(2) = π/2 - iln(2 + √(3))
        ans = Complex(m.pi/2, -m.log(2 + m.sqrt(3),m.e))
        self.assertEqual(Complex.arcsin(Complex(2, 0)), ans)

    # test taking inverse  cosine of a complex number
    def test_arccos(self):
        # identities
            # arc-cos(0) = π/2
        self.assertEqual(Complex.arccos(self.zero), self.pi_over_two)
            # arc-cos(1) = 0
        self.assertEqual(Complex.arccos(self.one), self.zero)
            # arc-cos(-1) = π
        self.assertEqual(Complex.arccos(self.neg_one), self.pi)
            # arc-cos(2) = iln(2 + √(3))
        ans = Complex(0, m.log(2 - m.sqrt(3), m.e))
        self.assertEqual(Complex.arccos(Complex(2, 0)), ans)

    # test taking inverse tangent of a complex number
    def test_arctan(self):
        # identities
            # arc-tan(0) = 0
        self.assertEqual(Complex.arctan(self.zero), self.zero)
            # arc-tan(1) = π/4
        self.assertEqual(Complex.arctan(self.one), self.pi_over_four)
            # arc-tan(-1) = -π/4
        self.assertEqual(Complex.arctan(self.neg_one), Complex(-self.pi_over_four.real, 0))
            # arc-tan(2 + i) = (3π/8) + iln(2)/4
        ans = Complex(3*m.pi/8, m.log(2, m.e)/4)
        self.assertEqual(Complex.arctan(Complex(2, 1)), ans)


    # test for non-elementary functions

    # test taking inverse  sine of a complex number
    def test_gamma(self):
        # test for singularities
            # Γ(0) = undefined, even if 0! = 1
        self.assertRaises(ValueError, Complex.gamma, self.zero)
        self.assertRaises(ValueError, Complex.gamma, self.neg_one)
        # test for real integers
            # Γ(1) = 0!
        self.assertEqual(Complex.gamma(self.one).real, factorial(self.zero))
            # Γ(10 + 1) = 10!
        self.assertEqual(Complex.gamma(Complex(11, 0)).real, float(factorial(Complex(10, 0))))
        # rough test
        test = Complex.gamma(self.i)
        self.assertNotEqual(test.real, 0)
        self.assertNotEqual(test.imaginary, 0)
        pass

    # test taking inverse  cosine of a complex number
    def test_erf(self):
        pass

    # test taking inverse tangent of a complex number
    def test_erfi(self):
        pass


# recursive, helper, factorial function to test gamma function
def factorial(c: Complex):
    assert c.imaginary == 0, "must be a real number"
    num = c.real
    assert type(num) == int, "must be an integer"

    if num == 0:
        return 1
    else:
        return num * factorial(Complex(num-1, 0))



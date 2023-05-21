from model.complex import Complex
import unittest as t
import math as m

class TestComplex(t.TestCase):
    # setup : class variables
    zero = Complex(0, 0)
    one = Complex(1, 0)        # 1
    neg_one = Complex(-1, 0)   # -1
    i = Complex(0, 1)          # i
    neg_i = Complex(0, -1)     # -i
    pi = Complex(m.pi, 0)                   # pi
    pi_over_two = Complex(m.pi / 2, 0)      # pi/2
    pi_over_four = Complex(m.pi / 4, 0)     # pi/4
    neg_pi_over_two = Complex(-m.pi / 2, 0)  # -pi/2
    a = Complex(1, 1)          # 1 + i
    b = Complex(1, -1)         # 1 - i
    c = Complex(-1, 1)         # -1 + i
    d = Complex(3, 4)          # 3 + 4i
    e = Complex(7, -14)        # 7 - 14i


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
        self.assertEqual(self.one.arg(), self.zero)
        self.assertEqual(self.neg_one.arg(), self.pi)
        self.assertEqual(self.i.arg(), self.pi_over_two)
        self.assertEqual(self.neg_i.arg(), self.neg_pi_over_two)
        self.assertEqual(self.a.arg(), self.pi_over_four)
        self.assertEqual(self.e.arg(), Complex(m.atan(-2), 0))

    # test to get the modulus of a complex number
    def test_mod(self):
        pass

    # test to convert rectangular form to euler form
    def test_rect_to_euler(self):
        pass

    # test to convert rectangular form to cis form
    def test_rect_to_cis(self):
        pass

    # test static methods

    # test adding two complex numbers
    def test_add(self):
        pass

    # test subtracting two complex numbers
    def test_sub(self):
        pass

    # test multiplying two complex numbers
    def test_mult(self):
        pass

    # test dividing two complex numbers
    def test_div(self):
        pass

    # test taking a complex power of complex numbers
    def test_power(self):
        pass

    # test taking a complex root of complex numbers
    def test_root(self):
        pass

    # test taking e to the power of a complex number
    def test_exp(self):
        pass

    # test taking natural log of a complex number
    def test_natural_log(self):
        pass

    # test taking log of a complex number with a complex base
    def test_log(self):
        pass

    # test trig functions

    # test taking sine of a complex number
    def test_sin(self):
        pass

    # test taking cosine of a complex number
    def test_cos(self):
        pass

    # test taking tangent of a complex number
    def test_tan(self):
        pass

    # test taking cosecant of a complex number
    def test_csc(self):
        pass

    # test taking secant of a complex number
    def test_sec(self):
        pass

    # test taking cotangent of a complex number
    def test_cot(self):
        pass

    # test taking hyperbolic sine of a complex number
    def test_sinh(self):
        pass

    # test taking hyperbolic cosine of a complex number
    def test_cosh(self):
        pass

    # test taking hyperbolic tangent of a complex number
    def test_tanh(self):
        pass

    # test taking inverse  sine of a complex number
    def test_arcsin(self):
        pass

    # test taking inverse  cosine of a complex number
    def test_arccos(self):
        pass

    # test taking inverse tangent of a complex number
    def test_arctan(self):
        pass


    # test for non-elementary functions

    # test taking inverse  sine of a complex number
    def test_gamma(self):
        pass

    # test taking inverse  cosine of a complex number
    def test_erf(self):
        pass

    # test taking inverse tangent of a complex number
    def test_erfi(self):
        pass




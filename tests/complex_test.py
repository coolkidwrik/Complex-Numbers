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
        cls.pi = Complex(m.pi, 0)                   # pi
        cls.pi_over_two = Complex(m.pi / 2, 0)      # pi/2
        cls.pi_over_four = Complex(m.pi / 4, 0)     # pi/4
        cls.neg_pi_over_two = Complex(-m.pi / 2, 0)  # -pi/2
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




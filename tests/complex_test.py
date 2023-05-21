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




import number as n


# defines all the same functions as the Number class, except multiply and power
class Imaginary(n.Number):

    @staticmethod
    def mult(r1, r2):
        # (ai) * (bi) = a * b * i^2
        # (ai) * (bi) = -1 * a * b
        return -1 * (r1 * r2)

    @staticmethod
    def power(r1, r2):
        assert r1 != 0 and r2 != 0, "0^0 is undefined"
        # (ai)^(bi) using euler's identity can be expressed as the following:
        # ( a * e^(i(pi/2)) )^(bi) = a * e^(i(pi/2) * bi)
        #                          = a * e^(i^2 * (b * pi/2))
        # ( a * e^(i(pi/2)) )^(bi) = a * e^(-b* pi/2)
        pi_over_two = n.m.pi/2
        return r1 * n.m.exp(-1 * r2 * n.m.pi/2)



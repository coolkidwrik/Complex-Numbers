import number


# defines all the same functions as the Number class, except multiply
class Imaginary(number.Number):

    @staticmethod
    def mult(r1, r2):
        return -1 * (r1 * r2)

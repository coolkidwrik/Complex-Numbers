import number


class Imaginary(number.Number):

    @staticmethod
    def mult(r1, r2):
        return -1 * (r1 * r2)

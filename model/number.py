import math as m

class Number:
    @staticmethod
    def add(r1, r2):
        return r1 + r2

    @staticmethod
    def sub(r1, r2):
        return r1 - r2

    @staticmethod
    def mult(r1, r2):
        return r1 * r2

    @staticmethod
    def div(r1, r2):
        assert r2 != 0, "Cannot divide by 0"
        return r1 / r2

    @staticmethod
    def power(r1, r2):
        assert r1 != 0 and r2 != 0, "0^0 is undefined"
        return m.pow(r1, r2)

    # raises r1 to the power of r2
    ## should work using maclaurin expansion to work for all real numbers
    ## (x + 1)^n = 1 + n(x+1)^(n-1) + n(n-1)(x+1)^(n-2) + n(n-1)(n-2)(x+1)^(n-3) + ...
    ## for all real numbers n and x
    ## can be used when solving for a^n, where a = x + 1
    # @staticmethod
    # def power(r1, r2):
    #     assert r1 != 0 and r2 != 0, "0^0 is undefined"
    #     if r2 == 1:
    #         return r1
    #     elif r2 == 0:
    #         return 1
    #     else:
    #         x = r1  # r1 = a = x + 1
    #         n = r2  # r2 = n


# def power_int(r1, r2):
#     if r2 == 1:
#         return r1
#     elif r2 == 0:
#         return 1
#     else:
#         return r1 * power_int(r1, r2-1)
#
# # helper function for the power method that performs the taylor expansion till the first i1 terms
# # i1 is an accumulator, and i2 is a constant. i2 = i1
# def taylor_expand(a, n, i1, i2):
#     if i1 <= 0:
#         return a
#     else:
#         return power_int()


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

class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return f"{self.real + other.real} + {self.imaginary + other.imaginary}i"

    def __mul__(self, other):
        # (a1 + b1i) (a2 + b2i) = (a1a2 - b1b2) + (a1b2 + a2b1) i.
        return f"{self.real * other.real - self.imaginary * other.imaginary} + " \
               f"{self.real * other.imaginary  + other.real * self.imaginary}i"


a = Complex(3, 4)
b = Complex(2, 3)
print(a + b)
print(a * b)

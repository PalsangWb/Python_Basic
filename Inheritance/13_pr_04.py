# Write a class complex to represent complex numbers, along with overloaded operators + and * which adds 
# and multiplies them.
""" Sum formula for complex:
        (a + bi) + (c + di) = (a + c) + (b + d)i
    Multiplication formula for complex:    
        (a + bi) + (c + di) = (ac - bd) + (ad + bc)i  
"""
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, c):
        real_part = self.real + c.real
        imag_part = self.imag + c.imag
        return Complex(real_part, imag_part)

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
              return f"{self.real} - {-self.imag}i"
    
    def __mul__(self, c):
        real_part = self.real * c.real + self.imag * c.imag
        imag_part = self.real * c.imag - self.imag * c.real
        return Complex(real_part, imag_part)

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
              return f"{self.real} - {-self.imag}i"
        
c1 = Complex(-1, 8)
c2 = Complex(-9, 98)
c3 = c1 + c2
print(f"The sum of complex number is: {c3}")

c4 = c1 * c2
print(f"The multiplication of complex number is: {c4}")


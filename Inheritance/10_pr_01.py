# Create a class C-2d vector and use it to create another class representing a 3-d vector.

class c2dVector:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        if self.jcap >= 0:
             return f"{self.icap}i + {self.jcap}j"
        else:
            return f"{self.icap}i - {-self.jcap}j"
   
class c3dVector(c2dVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k
    
    def __str__(self):
        if self.jcap >= 0:
            return f"{self.icap}i + {self.jcap}j + {self.kcap}k"
        else:
            return f"{self.icap}i - {-self.jcap}j - {-self.kcap}k"

v2d = c2dVector(1, -2)
print(f"The 2d vector is: {v2d}")

v3d = c3dVector(1, -2, -9)
print(f"The 3d vector is: {v3d}")
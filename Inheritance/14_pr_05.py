# Write a class Vector representing a vector of n dimension. Overload the + and * operator which calculates the 
# sum and the dot product of them.

class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f"{i}a{index} "
            index += 1
        return str1

    def __add__(self, vec1):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec1.vec[i])
        return Vector(newList)

    def __mul__(self, vec1):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] * vec1.vec[i]
        return sum

v1 = Vector([2, 3, 5])
v2 = Vector([1, 2, 6])
v3 = v1 + v2
v4 = v1 * v2
print(f"The sum of 2 vector is: {v3}")
print(f"The multiplication of 2 vector is: {v4}")



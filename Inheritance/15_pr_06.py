#Override the len() method on Vector of problem 5 to display the dimesnsion of the vector.
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
        if len(self.vec) != len(vec1.vec):
            raise ValueError("They have different dimensions to execute they must have same dimensions.")
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec1.vec[i])
        return Vector(newList)

    def __mul__(self, vec1):
        if len(self.vec) != len(vec1.vec):
            raise ValueError("They have different dimensions to execute they must have same dimensions.")
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] * vec1.vec[i]
        return sum

    def __len__(self):
        return len(self.vec)

v1 = Vector([2, 3, 5, 6, 7])
v2 = Vector([1, 2, 6,])

print(len(v1))
print(len(v2))

# try:
#     v3 = v1 + v2
#     print(f"The sum of 2 vector is: {v3}")
# except ValueError as e:
#     print(f"Error occur in addition: {e}")

# try:
#     v4 = v1 * v2
#     print(f"The multiplication of 2 vector is: {v4}")
# except ValueError as e:
#     print(f"Error occur in addition: {e}")






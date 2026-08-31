"""
Write a class vector representing a vector of n dimensions. Overload the + and * 
operator which calculates the sum and the dot(.) product of them.
"""


class Vector:
    def __init__(self,list):
        self.list = list

    def __len__(self):
        return len(self.list)



v1 = Vector([1,2,3])
print(len(v1))
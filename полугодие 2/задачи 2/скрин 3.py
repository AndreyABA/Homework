class trianglechecker:
    def __init__(self, sides):
        self.sides=sides
    def is_triangle(self):
        if all(isinstance(side, (int, float)) for side in self.sides):
            if all(side>0 for side in self.sides):
                if (self.sides[0] < self.sides[1]+self.sides[2]
                    and self.sides[1]<self.sides[0]+self.sides[2]
                    and self.sides[2]<self.sides[0]+self.sides[1]):
                    return 'треугольник сделать можно'
                else:
                    return 'жаль, но из этого треугольник не сделать'
            else:
                return 'с отрицательными числами нельзя'
        else:
            return 'можно ввести только числа'
a=trianglechecker([3, 4, 'негр'])
print(a.is_triangle())

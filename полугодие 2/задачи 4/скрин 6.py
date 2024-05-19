import numpy as np
class name:
    def __init__(self, A, B):
        self.A=np.array(A)
        self.B=np.array(B)
    def solve(self):
        try:
            otvet=np.linalg.solve(self.A, self.B)
            return otvet
        except np.linalg.LinAlgError:
            return 'система уравнений не имеет решений'
A=[[6, 8], [4, 5]]
B=[9, 34]
g=name(A, B)
f=g.solve()
print('решение: ', f)
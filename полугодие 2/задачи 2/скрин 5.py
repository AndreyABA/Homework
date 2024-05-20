class aviacompany:
    def __init__(self):
        self.planes=[]
        self.negr={}
    def add_plane(self, model):
        self.planes.append(model)
    def remove_plane(self, model):
        if model in self.planes:
            self.planes.remove(model)
    def add_negr(self, gorod, zxc):
        if gorod in self.negr:
            self.negr[gorod].append(zxc)
        else:
            self.negr[gorod]=[zxc]
    def remove_negr(self, gorod, zxc):
        if gorod in self.negr and zxc in self.negr[gorod]:
            self.negr[gorod].remove(zxc)
    def find_plane(self, model):
        return model in self.planes
    def find_negr(self, gorod):
        return self.negr.get(gorod, [])
a=aviacompany()
a.add_plane('Боинг 747')
print(a.planes)
a.add_negr('Москва', 'Бахмут')
a.add_negr('Москва', 'Киев')
print(a.find_negr('Москва'))
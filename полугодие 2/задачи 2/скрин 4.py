class nikolai:
    def __init__(self, imya, age):
        self.imya2=imya
        self.imya='Николай'
        self.age=age
        if self.imya2!='Николай':
            print(f'я не {self.imya2}, а {self.imya}')
a=nikolai('Адольф', 13)
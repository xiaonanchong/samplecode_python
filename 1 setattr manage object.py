class M:
    def __init__(self):
        self.__dict__['modules']={}
    def __setattr__(self, key, value):
        if isinstance(value, M):
            self.__dict__['modules'].update({key:value})
class C(M):
    def __init__(self):
        super().__init__()
class N(M):
    def __init__(self):
        super().__init__()
        self.conv1 = C()
        self.conv2 = C()
        self.x = 1
    def optimization(self):
        print(self.modules)

net = N()
net.optimization()
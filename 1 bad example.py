class module:
    def __init__(self):
        self.parameter = 0

class conv(module):
    def __init__(self):
        super().__init__()
    def update(self):
        self.parameter+=1

class ful(module):
    def __init__(self):
        super().__init__()
    def update(self):
        self.parameter+=2

class net(module):
    def __init__(self):
        self.conv = conv()
        self.conv.update()
        self.ful = ful()
        self.ful.update()

    def parameters(self):
        list = []
        for atr in dir(self):
            try:
                p = getattr(self, atr).parameter
            except:
                pass
            else:
                list.append(p)
        return list

    def print(self):
        print(self.conv.parameter)
        print(self.ful.parameter)
        print(self.parameters())


net = net()
net.print()
class module:
    def __init__(self):
        self.moduledict = {}

    def __setattr__(self, conv, a_module):
        if isinstance(a_module, module):
            self.moduledict.update({conv: a_module})

class conv(module):
    def __init__(self):
        super(conv,self).__init__()

class ful(module):
    def __init__(self):
        super(ful,self).__init__()

class net(module):
    def __init__(self):
        super().__init__()
        self.conv = conv()
        self.ful = ful()

class net2(module):
    def __init__(self):
        super().__init__()
        self.conv2 = conv()

net = net()
print(net.moduledict)
net2 = net2()
print(net2.moduledict)


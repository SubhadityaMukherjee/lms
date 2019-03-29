class encp:
    def __init__(self):
        self.username= ''
        self.password = ''
    def en(self,p):
        s = ''
        for a in p:
             s+= chr(ord(a)+11)
        return s
    def dec(self,p):
        s = ''
        for a in p:
             s+= chr(ord(a)-11)
        return s

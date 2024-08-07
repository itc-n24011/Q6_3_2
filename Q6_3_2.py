class r:
    a = 90
    def __init__(self, w, h):
        self.name = "長方形"
        self.w = w
        self.h = h
        self.pe = self.c_pe()
        self.ar = self.c_ar()

    def c_pe(self):
        wi = self.w
        he =self.h
        return (wi + he) * 2

    def c_ar(self):
        wi = self.w
        he = self.h
        return wi * he
    def s_a(self):
        an = self.a
        n = self.name
        wi = self.w
        he = self.h
        p = self.pe
        ar = self.ar
        print("名前:{}, 幅:{}, 高さ:{}, 角度:{}".format(n, wi, he, an))
        print("長さ:{}, 面積:{}".format(p, ar))

class s(r):

    def __init__(self, w):
        super().__init__(w, w)
        self.name = '正方形'

s1 = s(7)
s1.s_a()

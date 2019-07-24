class node:
    def __init__(self,data):
        print(2)
        self.now = data
        print("2 ok")
        print(3)
        self.nxt = None
        print("3 ok")

class single:
    def __init__(self):
        print(1)
        self.head = None
        print("1 ok")

    def pri(self):
        print(3)
        now = self.head
        print("3ok")
        while now:
            print(now.now)
            now = now.nxt
            print('fnf')


bench = single()
print("start")
bench.head = node('nikASH')
print("start 2")
member_2 = node('Nik')
print("start 3")
bench.head.nxt = member_2
print("start 4")

bench.pri()
print("finish")


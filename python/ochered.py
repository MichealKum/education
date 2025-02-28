

class Patient(object):

    def __init__(self, name, prv, nxt):
        self.name = name
        self.prv = prv
        self.nxt = nxt

    def print_us(self):
        print(self.name)
        if self.nxt is not None:
            self.nxt.print_us()

head = Patient("Илья", None, None)

tail = Patient("Елена", head, None)
head.nxt = tail

head.print_us()

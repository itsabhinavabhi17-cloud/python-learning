class parent:
    def __init__(self):
        print("constructor")

class child(parent):
    def __init__(self):
        super().__init__()
        print("child constructor")



obj=child()
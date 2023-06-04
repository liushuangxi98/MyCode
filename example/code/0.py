class A:
    def __init__(self):
        pass

    def __del__(self):
        print('del')

a = A()
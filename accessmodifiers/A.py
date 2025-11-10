class A:

    st = 'I am Public string'

    _st1 = 'I am Protected string'

    __st2 = 'I am Private string'


    def __init__(self):
        print('I am a constructor of class A')

    def _protectedMethod(self):
        print('I am protected Method')

    def __privateMethod(self):
        print('I am private Method')

    def publicMethod(self):
        print('I am Public Method')




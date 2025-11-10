class Computer:
    def config(self):
        print('i5 machine with 16gb ram,  1 TB Ram')

# Method 2 ---- Mostly Used ----
comp1 = Computer()

comp1.config()

# Method 2
Computer.config(comp1)



class Mycomplexnumber :
    #constactor method
    def __init__(self,real=0,imag=0):
        print("my complex number constractor execton...")
        self.real_part=real
        self.imag_part=imag
    def displaycomplex(self):
        print("{0}+{1}j".format(self.real_part,self.imag_part))

cmplxl=Mycomplexnumber(40,50)
cmplxl.displaycomplex()
cmplxl2=Mycomplexnumber(60,70)
cmplxl2.displaycomplex()
print(cmplxl)
#deleting cmplxl
del cmplxl.real_part
del cmplxl2.real_part
print(cmplxl)
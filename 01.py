class Fraction:
    def __init__(self,n=0,d=0):
        self.numerator=n
        self.denominator=d

    
    def add(self,other):
        sum=Fraction()
        if self.denominator==other.denominator:
            sum.numerator=self.numerator+other.numerator
            sum.denominator=self.denominator
        else:
            sum.numerator=(self.numerator*other.denominator)+(other.numerator*self.denominator)
            sum.denominator=self.denominator*other.denominator

        return sum
        
    
    def sub(self,other):
        subm=Fraction()
        if self.denominator==other.denominator:
            subm.numerator=self.numerator-other.numerator
            subm.denominator=self.denominator
        else:
            subm.numerator=(self.numerator*other.denominator)-(other.numerator*self.denominator)
            subm.denominator=self.denominator*other.denominator

        return subm

    
    def mul(self,second):
        mult=Fraction()
        mult.numerator=self.numerator*second.numerator
        mult.denominator=self.denominator*second.denominator
        return mult
    
    def div(self,other):
        divide=Fraction()
        divide.numerator=self.numerator*other.denominator
        divide.denominator=self.denominator*other.numerator
        return divide

    
    def show(self):
        print(self.numerator,"/",self.denominator)

#tabe vared kardan surat
def get_numerator():
    print("Enter the numerator and the denominator:")
    input_nume=int(input("numerator:"))

    return input_nume

#tabe vared kardn makhraj
def get_denominator():
    input_denome=int(input("denominator:"))

    #check 0 nabudan
    while input_denome==0:
        print("0 is not valid for denominator! try again.")
        input_denome=int(input("denominator:"))
    
    return input_denome



################


print("Enter one option:\n1.Sum\n2.Sub\n3.Mul\n4.Div")
choose=int(input("-->"))

#jam kardn 2 kasr
if choose==1:
    #sakht shei aval
    obj1=Fraction(get_numerator(),get_denominator())

    #sakht shei dovom
    obj2=Fraction(get_numerator(),get_denominator())
    
    #kasr hasel
    result = obj1.add(obj2)

    #namayesh kasr hasel
    result.show()


#tafriq 2 kasr
elif choose==2:
    #sakht shei aval
    obj1=Fraction(get_numerator(),get_denominator())

    #sakht shei dovom
    obj2=Fraction(get_numerator(),get_denominator())

    #kasr hasel
    result = obj1.sub(obj2)

    #namayesh kasr hasel
    result.show()

#zarb 2 kasr
elif choose==3:
    #sakht shei aval
    obj1=Fraction(get_numerator(),get_denominator())

    #sakht shei dovom
    obj2=Fraction(get_numerator(),get_denominator())

    #kasr hasel
    result = obj1.sub(obj2)

    #namayesh kasr hasel
    result.show()

#taqsim 2 kasr
elif choose==4:
    #sakht shei aval
    obj1=Fraction(get_numerator(),get_denominator())

    #sakht shei dovom
    obj2=Fraction(get_numerator(),get_denominator())

    #kasr hasel
    result = obj1.sub(obj2)

    #namayesh kasr hasel
    result.show()
        

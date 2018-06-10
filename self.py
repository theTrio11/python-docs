class phone:
    price=0
    brand=""
    def p(self):
        print("%s brand phone worth %d"%(self.brand,self.price))
t1=phone()
t1.price=10000
t1.brand="sam"
t2=phone()
t2.price=20000
t2.brand="as"
t1.p
t2.p
        

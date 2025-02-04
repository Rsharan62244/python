class point():
    def __init__(self,x,y):
        self.x=x
        self.y=y

a=int(input("enter x cordinate:"))
b=int(input("enter y cordinate:"))
p=point(a,b)
print(f"x cordinate {p.x}")
print(f"y cordinate {p.y}")
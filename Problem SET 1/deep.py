
def deep():
    x = input ("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    return x.lower().strip()

x= "Forty Two".lower()
y= "forty-two".lower()
z= "42"

user_r= deep()

if user_r==z or user_r==x or user_r==y:
    print ("Yes")

else:
    print ("No")






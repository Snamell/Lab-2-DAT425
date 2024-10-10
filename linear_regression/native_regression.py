from matrix import *
import matplotlib.pyplot as plt

def native_regression(file):

    X=transpose(loadtxt(file))[0]
    Y=transpose(loadtxt(file))[1]

    Xp=(powers(X,0,1))
    Yp=(powers(Y,1,1))

    Xpt=transpose(Xp)

    b,m= matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp)) 

    Y2=[]
        
    for n in X:
        Y2.append(b[0]+m[0]*n)

    plt.plot(X,Y,'ro')
    plt.plot(X,Y2)
    plt.show()
    

native_regression("dataset1.txt")

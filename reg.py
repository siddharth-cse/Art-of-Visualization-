import  numpy  as  np 
from matplotlib import pyplot as plt
import time
from mpl_toolkits.mplot3d import Axes3D

def  gradient_descent1( x , y ): 
    m_curr  =  b_curr  =  0 
    iterations  =  250
    n  =  len(x)
    learning_rate  =  0.001 
    fig, ax = plt.subplots(1)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    slopes=[]
    y_ints=[]
    costs=[]
    counts=[]
    # fig = plt.figure()
    # ay=Axes3D(fig)
    for  i  in  range ( iterations ): 
        y_predicted  =  m_curr  *  x  +  b_curr 
        ax.clear()
        ax.scatter(x,y,color="red")
        ax.plot(x,y_predicted)
        cost  =  ( 1 / n )  *  sum ([ val ** 2  for  val  in  ( y - y_predicted )]) 
        costs.append(cost)
        counts.append(i+1)
        slopes.append(m_curr)
        y_ints.append(b_curr)
        #ay.scatter(counts,costs)
        md  =  - ( 2 / n ) * sum ( x * ( y - y_predicted )) 
        bd  =  - ( 2 / n ) * sum ( y - y_predicted ) 
        m_curr  =  m_curr  -  learning_rate  *  md 
        b_curr  =  b_curr  -  learning_rate  *  bd 
        ax.set_xlim([0, 6])
        ax.set_ylim([0, 30])
        ax.text(2,25,"cost="+str(cost))
        ax.set_xlabel('x', fontweight ='bold')  
        ax.set_ylabel('y', fontweight ='bold')  
        # ay.set_zlabel('Cost', fontweight ='bold') 
        # ay.plot_trisurf(slopes,y_ints,costs, alpha=0.5)
        plt.pause(0.1)
        fig.savefig(str(i)+"image.png")
    plt.show()
    return (slopes,y_ints,costs)      

def  gradient_descent( x , y ,X,Y,Z): 
    m_curr  =  b_curr  =  0 
    iterations  =  250
    n  =  len(x)
    learning_rate  =  0.001 
    count=0
    costs=[]
    counts=[]
    slopes=[]
    #ax.plot_trisurf(X,Y,Z, alpha=0.5)
    #fig=plt.figure()
    #ax = fig.add_subplot(111)
    fig = plt.figure()
    ay=Axes3D(fig)
    ay.plot_trisurf(X,Y,Z, alpha=0.5)
    ay.set_xlabel('slope', fontweight ='bold')  
    ay.set_ylabel('Y_intercept', fontweight ='bold')  
    ay.set_zlabel('Cost', fontweight ='bold') 

    for  i  in  range ( iterations ): 
        y_predicted  =  m_curr  *  x  +  b_curr 
        #ax.clear()
        #ax.scatter(x,y)
        #ax.plot(x,y_predicted)
        cost  =  ( 1 / n )  *  sum ([ val ** 2  for  val  in  ( y - y_predicted )]) 
        # costs.append(cost)
        # counts.append(i+1)
        # slopes.append(m_curr)
        # y_ints.append(b_curr)
        ay.scatter(X[i],Y[i],Z[i],color='blue')
        md  =  - ( 2 / n ) * sum ( x * ( y - y_predicted )) 
        bd  =  - ( 2 / n ) * sum ( y - y_predicted ) 
        m_curr  =  m_curr  -  learning_rate  *  md 
        b_curr  =  b_curr  -  learning_rate  *  bd 
        #print  ( "m {}, b {}, cost {} iteration {}" . format ( m_curr , b_curr , cost ,  i ))  
        # print('ax.azim {}'.format(ay.azim))
        # print('ax.elev {}'.format(ay.elev))
        # # #ax.set_xlim([1, 7])
        #ax.set_ylim([0, 30])
        #ax[1].set_xlim([0, iterations])
        #ax[1].set_ylim([0, 110])
        #ax.text(6, 25,"cost="+str(cost))
        ay.view_init(18.75,-58.875)
        fig.set_size_inches(18.5, 10.5)
        stri="~/Desktop/Algorithms_for_ML_inference/frames/pic"+str(i)+".png"
        plt.pause(0.1)
        fig.savefig(str(i)+"image.png")
        
    #plt.show()


def three_d(x,y):
    X=[]
    Y=[]
    Z=[]
    n=len(x)
    m=np.linspace(-100,100,201)
    print(len(m))
    fig = plt.figure()
    ax=Axes3D(fig)
    for slope in m:
        for j in range(20):
            y_predicted  =  slope  *  x  +  j
            cost  =  ( 1 / n )  *  sum ([ val ** 2  for  val  in  ( y - y_predicted )])
            X.append(slope)
            Y.append(j)
            Z.append(cost)
    X=np.array(X)
    Y=np.array(Y)
    Z=np.array(Z)
    ax.set_xlabel('slope', fontweight ='bold')  
    ax.set_ylabel('Y_intercept', fontweight ='bold')  
    ax.set_zlabel('Cost', fontweight ='bold') 
    #Z.reshape(Y.shape)        
    ax.plot_trisurf(X,Y,Z, alpha=0.5)
    plt.show()
    return(X,Y,Z)


x  =  np . array ([ 1 , 2 , 3 , 4 , 5 ]) 
y  =  np . array ([ 4 , 6 , 7 , 15 , 13 ]) 

plt.plot(x,y,marker="o")
m_curr = 2.1336838087708983
b_curr =  0.7780869783447201
y_predicted  =  m_curr  *  x  +  b_curr

for i in range(len(y)):
    xdif = 0
    ydif = abs(y[i] - y_predicted[i])
    plt.plot([x[i],x[i]],[y[i],y_predicted[i]])  #                    midX-y2+y1, midY + x2-x1


plt.plot(x,y_predicted)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

#X,Y,Z=three_d(x,y)

print(x,y,y_predicted)

X,Y,Z=gradient_descent1(x,y) 

#gradient_descent(x,y,X,Y,Z)
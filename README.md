# Visualizing Linear regression




## The essence of the algorithm 
It tries to fit a line on a scatter plot of random points. The way the algorithm "learns" is where Machine "Learning" comes in. Fortunately unlike other Machine Learning algorithms, we can see how the model learns to fit this line.  
## Working of Linear Regression with an example
Given a any random data set which has a set of x and y values, lets try and fit a line through this curve.  
```python
x  =  np . array ([ 1 , 2 , 3 , 4 , 5 ]) 
y  =  np . array ([ 4 , 6 , 7 , 15 , 13 ]) 
```
![plot](https://github.com/siddharth-cse/Art-of-Visualization-/blob/main/Figure_1.png)

We need to find a line that is closer to all the points, in other words the sum of the distances from all the points to this line must be minimum. 

<img src="https://github.com/siddharth-cse/Art-of-Visualization-/blob/main/Figure_2.png" width="300" height="270"><img src="https://github.com/siddharth-cse/Art-of-Visualization-/blob/main/Figure_3.png" width="300" height="270"><img src="https://github.com/siddharth-cse/Art-of-Visualization-/blob/main/Figure_4.png" width="300" height="270">

## Relevant Math 
So we have the random points <a href="https://www.codecogs.com/eqnedit.php?latex=(x_0,y_0),(x_1,y_1),(x_2,y_2)&space;......&space;(x_n,y_n)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?(x_0,y_0),(x_1,y_1),(x_2,y_2)&space;......&space;(x_n,y_n)" title="(x_0,y_0),(x_1,y_1),(x_2,y_2) ...... (x_n,y_n)" /></a>  <br /> 

Now we need to predict a line <a href="https://www.codecogs.com/eqnedit.php?latex=y&space;=&space;mx&space;&plus;&space;c" target="_blank"><img src="https://latex.codecogs.com/gif.latex?y&space;=&space;mx&space;&plus;&space;c" title="y = mx + c" /></a>  <br /> <br />

This function below is commonly reffered to as **cost function** or **mean squared error function** (MSE).

<a href="https://www.codecogs.com/eqnedit.php?latex=Cost&space;=Min&space;\left&space;\{&space;\frac{1}{N}\sum_{i=0}^{N}(y_i-y_{predicted})^2&space;\right&space;\}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Cost&space;=Min&space;\left&space;\{&space;\frac{1}{N}\sum_{i=0}^{N}(y_i-y_{predicted})^2&space;\right&space;\}" title="Cost =Min \left \{ \frac{1}{N}\sum_{i=0}^{N}(y_i-y_{predicted})^2 \right \}" /></a> <br/> <br/><a href="https://www.codecogs.com/eqnedit.php?latex=Cost&space;=Min&space;\left&space;\{&space;\frac{1}{N}\sum_{i=0}^{N}(y_i-(m*x_i&plus;c))^2&space;\right&space;\}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Cost&space;=Min&space;\left&space;\{&space;\frac{1}{N}\sum_{i=0}^{N}(y_i-(m*x_i&plus;c))^2&space;\right&space;\}" title="Cost =Min \left \{ \frac{1}{N}\sum_{i=0}^{N}(y_i-(m*x_i+c))^2 \right \}" /></a> <br /> <br /> So we observe the only variables in the above equations are 'm' and 'c'. We can start plugging in random values of 'm' and 'c' and guess our way to the minima. But the sea of 'm' and 'c' values looks like this. 
![](https://github.com/siddharth-cse/Art-of-Visualization-/blob/main/Figure_5.png)
Beautiful isnt it?

<br /> Now we must narrow down to an otimal value of 'c' and 'm' such that they have the least corresponding cost in the above 3d graph, we call this optimal value as 'minima'. We could point to some random value by looking at the graph, unfortunately we must make the machine learn to solve this. 

## Gradient Descent 
<br /> There exist this optimaztion algorithm know as **Gradient Descent**, its sole purpose of existence is to determine this very value we require. (**Google:** Gradient descent is a first-order iterative optimization algorithm for finding a local minimum of a differentiable function). Now lets get back to our function  ...   <br /><br />
<a href="https://www.codecogs.com/eqnedit.php?latex=Cost&space;=&space;\left&space;\{&space;\frac{1}{N}\sum_{i=0}^{N}(y_i-(m*x_i&plus;c))^2&space;\right&space;\}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Cost&space;=&space;\left&space;\{&space;\frac{1}{N}\sum_{i=0}^{N}(y_i-(m*x_i&plus;c))^2&space;\right&space;\}" title="Cost = \left \{ \frac{1}{N}\sum_{i=0}^{N}(y_i-(m*x_i+c))^2 \right \}" /></a> <br /><br />

Differentiation essentially measures the change in a value with respect to another. In graphical terms we measure the differentation of the 'cost' with respect to 'm' and 'c'. This slight change measured  <a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;(Cost)}{\partial&space;(m)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;(Cost)}{\partial&space;(m)}" title="\frac{\partial (Cost)}{\partial (m)}" /></a> and <a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;(Cost)}{\partial&space;(c)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;(Cost)}{\partial&space;(c)}" title="\frac{\partial (Cost)}{\partial (c)}" /></a> essentially gives us the slope at that very instance, suggesting where the curve or the 3d plane is heading towards. So following this we should head towards our local minima. So when we apply this to our equation we get the following two partial derivate equations. 

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;(Cost)}{\partial&space;m}&space;=&space;\frac{2}{N}\sum_{i=0}^{N}-x_i(y_i-(m*x_i&plus;c))^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;(Cost)}{\partial&space;m}&space;=&space;\frac{2}{N}\sum_{i=0}^{N}-x_i(y_i-(m*x_i&plus;c))" title="\frac{\partial (Cost)}{\partial m} = \frac{2}{N}\sum_{i=0}^{N}-x_i(y_i-(m*x_i+c))^2" /></a> ........ (1)

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;(Cost)}{\partial&space;m}&space;=&space;\frac{2}{N}\sum_{i=0}^{N}-(y_i-(m*x_i&plus;c))" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;(Cost)}{\partial&space;m}&space;=&space;\frac{2}{N}\sum_{i=0}^{N}-(y_i-(m*x_i&plus;c))" title="\frac{\partial (Cost)}{\partial m} = \frac{2}{N}\sum_{i=0}^{N}-(y_i-(m*x_i+c))" /></a>         ........... (2)

So to start off with we can start with 'm' and 'c' initiallized to 0 and start iterating to solve our cost function equation. 

```python


import  numpy  as  np 

def  gradient_descent ( x , y ): 
    m  =  0
    c  =  0 
    iterations  =  10000 
    n  =  only ( x ) 
    learning_rate  =  0.08 
    for  i  in  range ( iterations ): 
        y_predicted  =  m *  x  +  b 
        cost  =  ( 1 / n )  *  sum ([ val ** 2  for  val  in  ( y - y_predicted )])       #Cost function equation
        md  =  - ( 2 / n ) * sum ( x * ( y - y_predicted ))                               #equation 1 
        bd  =  - ( 2 / n ) * sum ( y - y_predicted )                                      #equation 2
        m  =  m  -  learning_rate  *  md                                                  #Updating new slope
        c  =  c -  learning_rate  *  bd                                                   #Updating new Y-intercept
        print  ( "m {}, b {}, cost {} iteration {}" . format ( m_curr , b_curr , cost ,  i )) 

```
The above learning_rate decides the order in which the values 'm' and 'c' should jump in order to find a local minima. Greater the learning rate, larger the jump. (Having a smaller learning rate will ensure finding a fine grained optimum value but may take few more iterations). The iterations above in machine learning terms is known as an **'epoch'**.

![](grad.gif)

The above animation shows how the gradient descent algorithm converges towards the local minima and starts taking smaller steps as it reaches the optimal value. 
 
![](fitting.gif)

While the least cost value is determined through the above algorithm we take the correspoding slope(m) and y_itercept(c) value and plot our best fit line iteratively. We observe it saturates after a given number of iterations, suggesting this is the final line which can fit these set of points most optimally. 


# Visualizing Linear regression




## The essence of the algorithm 
We try and fit a line on a scatter plot of random points. The way the algorithm learns to is where Machine Learning comes in. Fortunately unlike other Machine Learning algorithms, we can see how the model learns to fit this line.  
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
So we have the random points <a href="https://www.codecogs.com/eqnedit.php?latex=(x_0,y_0),(x_1,y_1),(x_2,y_2)&space;......&space;(x_n,y_n)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?(x_0,y_0),(x_1,y_1),(x_2,y_2)&space;......&space;(x_n,y_n)" title="(x_0,y_0),(x_1,y_1),(x_2,y_2) ...... (x_n,y_n)" /></a>  <br /> Now we need to predict a line <a href="https://www.codecogs.com/eqnedit.php?latex=Cost&space;=Min&space;\left&space;\{&space;\frac{1}{N}\sum_{i=0}^{N}(y_i-y_{predicted})^2&space;\right&space;\}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Cost&space;=Min&space;\left&space;\{&space;\frac{1}{N}\sum_{i=0}^{N}(y_i-y_{predicted})^2&space;\right&space;\}" title="Cost =Min \left \{ \frac{1}{N}\sum_{i=0}^{N}(y_i-y_{predicted})^2 \right \}" /></a> <br /> <br />
<a href="https://www.codecogs.com/eqnedit.php?latex=C=Min&space;\left&space;\{&space;\frac{1}{N}\sum_{i=0}^{N}(y_i-y_{predicted})^2&space;\right&space;\}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?C=Min&space;\left&space;\{&space;\frac{1}{N}\sum_{i=0}^{N}(y_i-y_{predicted})^2&space;\right&space;\}" title="C=Min \left \{ \frac{1}{N}\sum_{i=0}^{N}(y_i-y_{predicted})^2 \right \}" /></a> <br/> <br/>
<a href="https://www.codecogs.com/eqnedit.php?latex=C=Min&space;\left&space;\{&space;\frac{1}{N}\sum_{i=0}^{N}(y_i-(m*x_i&plus;c))^2&space;\right&space;\}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?C=Min&space;\left&space;\{&space;\frac{1}{N}\sum_{i=0}^{N}(y_i-(m*x_i&plus;c))^2&space;\right&space;\}" title="C=Min \left \{ \frac{1}{N}\sum_{i=0}^{N}(y_i-(m*x_i+c))^2 \right \}" /></a> <br /> <br /> So we observe the only variables in the above equations are 'm' and 'c'. We can start plugging in random values of 'm' and 'c' and guess our way to the minima. But the sea of 'm' and 'c' values looks like this. 
![](https://github.com/siddharth-cse/Art-of-Visualization-/blob/main/Figure_5.png)
Beautiful isnt it? <br /> Now we must narrow down to an otimal value of 'c' and 'm' such that they have the least corresponding cost in the above 3d graph, we call this optimal value as 'minima'. We could point to some random value by looking at the graph, unfortunately we must make the machine learn to solve this.  <br 

## Gradient Descent 
/><br /> There exist this optimaztion algorithm know as **Gradient Descent**, its sole purpose of existence is to determine this value. (**Google:** Gradient descent is a first-order iterative optimization algorithm for finding a local minimum of a differentiable function). Now lets get back to our function  ...   <br /><br />



![](grad.gif)
![](fitting.gif)

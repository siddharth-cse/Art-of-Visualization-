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
So we have the random points <a href="https://www.codecogs.com/eqnedit.php?latex=(x_0,y_0),(x_1,y_1),(x_2,y_2)&space;......&space;(x_n,y_n)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?(x_0,y_0),(x_1,y_1),(x_2,y_2)&space;......&space;(x_n,y_n)" title="(x_0,y_0),(x_1,y_1),(x_2,y_2) ...... (x_n,y_n)" /></a>  <br /> Now we need to predict a line <a href="https://www.codecogs.com/eqnedit.php?latex=y_{predicted}=mx&space;&plus;&space;c" target="_blank"><img src="https://latex.codecogs.com/gif.latex?y_{predicted}=mx&space;&plus;&space;c" title="y_{predicted}=mx + c" /></a> , such that the distance between all the points and this predicted line is minimum. Since the difference in this distance can be negative, we square the value and divide the overall value by N (total number of points) <br />
<a href="https://www.codecogs.com/eqnedit.php?latex=C=Min&space;\left&space;\{&space;\frac{1}{N}\sum_{i=0}^{N}(y_i-y_{predicted})&space;\right&space;\}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?C=Min&space;\left&space;\{&space;\frac{1}{N}\sum_{i=0}^{N}(y_i-y_{predicted})&space;\right&space;\}" title="C=Min \left \{ \frac{1}{N}\sum_{i=0}^{N}(y_i-y_{predicted}) \right \}" /></a> <br/> <br/>
<a href="https://www.codecogs.com/eqnedit.php?latex=C=Min&space;\left&space;\{&space;\frac{1}{N}\sum_{i=0}^{N}(y_i-(m*x_i&plus;c))&space;\right&space;\}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?C=Min&space;\left&space;\{&space;\frac{1}{N}\sum_{i=0}^{N}(y_i-(m*x_i&plus;c))&space;\right&space;\}" title="C=Min \left \{ \frac{1}{N}\sum_{i=0}^{N}(y_i-(m*x_i+c)) \right \}" /></a>

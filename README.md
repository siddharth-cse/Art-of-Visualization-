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
So we have the random points **(x<sub>0</sub>,y<sub>0</sub>),(x<sub>1</sub>,y<sub>1</sub>).......(x<sub>n</sub>,y<sub>n</sub>)**  <br /> Now we need to predict a line **Y= m X + C** , such that the distance between all the points and this predicted line is minimum. 
<a href="https://www.codecogs.com/eqnedit.php?latex=C=Min&space;\left&space;\{&space;\frac{1}{N}\sum_{i=0}^{N}(y_i-y_{predicted})&space;\right&space;\}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?C=Min&space;\left&space;\{&space;\frac{1}{N}\sum_{i=0}^{N}(y_i-y_{predicted})&space;\right&space;\}" title="C=Min \left \{ \frac{1}{N}\sum_{i=0}^{N}(y_i-y_{predicted}) \right \}" /></a>

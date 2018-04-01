# RandomWalk
RandomWalk with variable square terrain size and variable step length

I wanted to code a "newer" variant of the RandomWalk simulation usually encountered in undergraduate OOP classes.

In this variant, the size of the terrain and steps can vary, so an unit on the terrain is not "forced" to move in 1x1 in a single direction.

The starting position is currently set to be right in the middle of the square terrain, 
but I am planning on making it moveable and randomnizable.

Furthermore, I will store the values of these runs in a Dataframe so to perform further statistical analysis on them.

Here are some examples of questions that can be asked:

    1- Given steps of size N and a square terrain of size N2, what is the average minimum number of steps before an unit positioned at the center of the square reaches (beyond) the borders?
    
    2- What is the probability of reaching position (X,Y) starting from position (X0,Y0), on a square terrain with side lengths N2?
    
    3- If S units are placed on this square terrain (randomly or not), how many collisions can be expected on average during a run?
    
   ETC...
    
I know that many of these questions are actually a matter of solving for probabilities and/or stochastic processes.
However, it is my opinion that there is still some value in being able to obtain the answers through simulations of the sort.
(At the very least, it will help my practice using Python for data analysis and whatever skills I obtained through DataCamp)

I hope this code will be useful to whoever is curious enough to read it.

Homework-2
==========

Sage Homework 2

The function factor takes an integer n and prints its factors to the screen.
I also wrote another function, NewFactor, that returns a list of factors.
This one is not recursive, so if there are a lot of factors it seems to be faster.

For example, NewFactor(1227184536156238675) yields [5, 5, 29, 1289, 347443, 3779509L]
while factor(1227184536156238675) prints
5
5
29
1289
347443
3779509. 
(In this case factor is faster.)

For 2^32, however, or other similar powers, NewFactor is faster.

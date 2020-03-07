#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) 
The last line is O(n^2) due to input multiplied to itself for output.
while loop is O(n^3) because n is multiplied three times to itself to change the marker for condition.
a = 0 is constant.

The answer is O(n^3) as that is the worst part of the code and like a bottle neck it will deminish performance.

b)
j *= 2  O(1) input does not effect this
sum += 1  O(1) input does not effect this
both of the above = O(2) = O(1) which is still a constant.
The while loop is O(n) as the condition is set on the n value no mater what. n has a linear relationship to the condition statement.
j = 1 is constant O(1)
range(n) is also constant as a Python operator.
sum = 0 is constant.

The answer is O(n) because the output is linear to the input.

c)
the first return is constant.
the if statement is constant.
the last return statement is O(n) because as the inputs increase, the output also increases linearly.

## Exercise II

Inputs:
floors = n
eggs = 100
midway = f and the starting floor for breaking eggs
broken = [f:] if f or higher
unbroken = [:f] if f or lower

Outputs:
f = The floor where the eggs start to break and with the least amount of dropped eggs to find it.

Using binary search principle:

Go half way up the building and test the first egg.

If the egg breaks, then divide the unbroken array (unbroken/2) and test another egg. 
Else, if the egg doesn’t break, divide the broken array and test another egg. (broken/2)
When the n = broken and n-1 = unbroken, f = n

OR

If the egg doesn’t break, go up a floor by one and toss egg. Repeat if egg doesn’t break.
Then If egg does break, the floor is f

If the egg does break, move down a floor and toss another egg.
if the egg then does not break, give the previous floor as f

The above code = O(logn).
Because of the input in floors can increase dramatically but the algorithm is running less operations than the input increase.

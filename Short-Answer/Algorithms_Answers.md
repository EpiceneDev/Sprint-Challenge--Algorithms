#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

```python
a)  a = 0  # O(1)
    while (a < n * n * n): # (O(n^3))
      a = a + n * n # O(n^2)
```

O(1) + ((O(n^3))*O(n^2)) = O(n^5)

```py
b)  sum = 0 # O(1)
    for i in range(n): # O(n)
      j = 1  #O(1)
      while j < n: # O(n)
        j *= 2  # O(1)
        sum += 1 # O(1)
```

O(1) + [O(n) * O(1) * O(n) * O(1) * O(1)] = O(n^2)

```py
c)  def bunnyEars(bunnies):
      if bunnies == 0: # O(1)
        return 0

      return 2 + bunnyEars(bunnies-1) # O(n)
```

O(1) + O(n)

## Exercise II

go half way up and drop the egg # O(1)
if it breaks, go halfway down the lower steps and drop again. # O(logn)
repeat the above until it does not break
if it does not break, move up one step until it does. O(1)
Step where breakage starts = f
Because it is an egg, i would expect it to break before the middle. So after dividing floors in half, I would step up or down instead of taking bigger slices.
O(logn)
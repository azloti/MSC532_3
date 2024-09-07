# Quick Sort

In quick_sort.py you can find a quick sort implementation. Using the PivotSelection enum you can choose between a random or deterministic pivot selection algorithm.

### Analysis

We will prove that the average-case time complexity of Randomized Quicksort is at most O(n log n).

Consider that when we pick a pivot on an array of size X, we then perform X-1 comparisons (compare all other elements to it in order to partition them). Depending on the pivot, the resulting array lengths will be one of: (0, X-1), (1, X-2), ..., (X-1, 0). Since the pivot selection is random, the probability of picking either of these is random.

Therefore, we can write a recurrence relation for the expected number of comparisons required:

T(x) = (x - 1) + 1/x * $$\ \sum_{i=0}^{x-1} T(i) + T(x-i-1)  $$

By using the general expression for expectation of random variable X, we can rewrite the equation, simplifying it and getting rid of T(0):

T(x) = (x - 1) + 2/x * $$\ \sum_{i=1}^{x-1} T(i) $$

We can solve this function using the induction method. Let's prove that T(i) <= ci ln(i) fir i<=n-1. For T(1) = 0 the proof is simple: if there is only one element, there are no comparisons to make.
Deriving from that, we get:

T(x) <= (x-1) + 2/x * $$\ \sum_{i=1}^{x-1} (ci * ln(i)) $$ 
     <= (x-1) + 2/x * $$\int_1^x (cx * ln(x))dx \$$ 
     <= (x-1) + 2/x ((c/2)x^2 * ln(x) - c(n^2)/4 + c/4) 
     <= cx * ln(x), for c = 2

Which shows that the aerage-case running time for Randomized quicksort is O(_n_ log _n_)

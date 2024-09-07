# Quick Sort

In quick_sort.py you can find a quick sort implementation. Using the PivotSelection enum you can choose between a random or deterministic pivot selection algorithm.

### Analysis

We will prove that the average-case time complexity of Randomized Quicksort is at most O(n log n).

Consider that when we pick a pivot on an array of size X, we then perform X-1 comparisons (compare all other elements to it in order to partition them). Depending on the pivot, the resulting array lengths will be one of: (0, X-1), (1, X-2), ..., (X-1, 0). Since the pivot selection is random, the probability of picking either of these is random.

Therefore, we can write a recurrence relation for the expected number of comparisons required:

T(x) = (x - 1) + 1/n \* Σ

```text
$$\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)$$
```

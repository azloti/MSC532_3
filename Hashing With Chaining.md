# Quick Sort

In hash_chaining.py you can find a hash table implementation. If there is a hash collision, it uses a linked list to chain the collided elements together.

### Analysis

For the following examples, I will assume uniform hashing (all elements are distributed equally)

For some of these operations, the load factor of the hash table is important, which we can note as: α = n / m, where n = the number of pairs in the table, and m = the number of slots in the table.

###### Search

Considering uniform distribution, the average chain length will be approximately equal to the load factor, since all chains are approximately the same size.

This means the expected search time is O(1 + α), where α is the load factor. Assuming a proper hash table size, this of course approaches O(1), since most chains would be of length max 1

###### Insert

The insert operation is the simplest one: since the implementation inserts new values at the beginning of the chain, the chain length / load factor does not matter. This means it will always be an O(1) operation.

###### Delete

The delete functionality requires finding the key in the hash table, so it can be removed from its chain. This means it has the same complexity as the search operation, O(1+α), since the deletion itself, once it is found, is an O(1) operation.

It is worth mentioning that in the best case scenario, all these operations are O(1), since there is no chain to traverse. This would be the expected behaviour assuming proper sizing of the hash table.

On the other hand, assuming that all hashes collide, the search and delete operations would have O(n) complexity, while insertion would remain O(1).

###### Mitigation strategies

As seen above, maintaining a low load factor is essential for maintaining good performance. This can be achieved by giving the hash table a proper size when constructing it, but can also be handled by dynamically resizing the table.

Resizing the table is quite simple: once it approaches a certain threshold size, counted by the number of elements inside of it, its size can be increased (to keep it simple, doubled).

The implementation would be quite simple: the threshold could be considered as 80% of the table size. A length property would keep track of how many values are in the table, increased by 1 when a new value is added and decreased when it is deleted.

If table size \* 0.8 >= length, a "resize" method would be called. That would create a new internal table, and recalculate the hashes for all existing values, and add them to the new table. Since it requires looping through all the values, and insertion is an O(1) operations, total complexity of a resize is O(n).

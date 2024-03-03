The user enters the number of cats.

We place the cats in a huge circle. At first, none of the cats has a hat. We go around the circle the number of times the user entered, always starting at the same place, the first cat (cat #1). Every time we stop by a cat, we either put a hat on it if it isn't wearing one, or take it off if it is.

In the first round, we stop at each cat, putting a hat on each.
In the second round, we only stop at every other cat (#2, #4, #6, #8, etc.).
In the third round, we stop only at every third cat (#3, #6, #9, #12, etc.).
We continue this process until we have made a given number of rounds around the cats.

The program displays which cats have hats at the end.

The complexity of this algorithm is O(n^2).

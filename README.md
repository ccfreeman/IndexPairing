# IndexPairing

When we have a two groups of natural number pairs, we may want a quick way to see what pairs are shared between the two groups. For instance, if we have pairs in one group as ((1, 2), (3,4)), and ((5,6), (2,1)) in another group, we may want to know that the unordered pair of (1,2) exists in both sets. This process can be slow, and we may want a smarter way to do this than brute-force searching.

In this repo, we test two fast approaches. The first is using a pairing function (https://en.wikipedia.org/wiki/Pairing_function). Here, a set of two natural numbers are combined into a unique single natural number. These combination numbers can then be cross-checked with other lists for overlap or difference. 

The second approach is more subtle. It uses bitshift operations to create a combination of two natural numbers. We represent each number as (for example) a 4-bit unsigned integer, and then create an 8-bit integer where the upper four bits represent the left number and the lower four bits represent the right number. (Endianness may come into play, but if comparisons are made on the same ordering we should be safe). These 8-bit unsigned integers can then be checked with others for equality, and comparisons between groups made. 

We tested the two approaches, and, as expected, bitshifting is significantly faster (4-5x with sets of 100,000 natural numbers that are less than 500).

## APPLICATIONS

Graph-based applications are at hand here. We may want a quick way to see whether two undirected graphs with overlap of node IDs (represented as natural numbers) have similar edges. 
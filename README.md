# Solution
## Plan
Because I was going to represent the data as an almost-full table, the data structure I chose to use was an **Adjacency Matrix**. This is because it is very intuitive to access data inside the data structure (one only needs to pass in the x and y parameters of the table to get the data at the desired location).

I also elected to use a **Dictionary** to compose my adjacency matrix so that the string codes for each team could be passed into the table directly, rather than need to be converted to a numerical index first, as would be the case if I was using lists/arrays

## Implementation
My `generate_H2H_WL_table` function has 3 parts: 
- Initialize local variables
- Read file data into local object
- Process file data iteratively, storing in local variable

and then, finally, I returned the completed adjacency matrix as output.

That last part is the most complex part of the function, so let me elaborate more on what I'm doing. The first `for loop` iterates through the record lists of each team (`w_team`), initializing that team's sub-dictionary and setting the self-record case (BRO vs BRO) to `'--'`. 

The interior `for loop` iterates through every team (`l_team`) that the winning team (`w_team`) has a record with and sets the value of that pairing to the number of times `w_team` has beat `l_team`. EX: `adj_matrix[BRO][BSN] = 10` means that the first time, `BRO` has beaten the second team `BSN` 10 times.
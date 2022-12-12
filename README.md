# advent_of_code_2022
my 2022 [advent of code](https://adventofcode.com/2022) work

I like solving the puzzles and trying out different approaches. All python so far and will probably stay that way. Not going for most elegant, fastest solution, or anything like that.

### Notes along the way
### Day 11
I kept re-reading the part "find another way to keep your worry levels manageable" and knew that was the key. Reviewing the overall problems, I spotted the primes and started thinking on the factorization path, but my mind was just going slow on a Sunday (or I didn't want to tax my mind). I checked for hints on reddit and then the light bulb went off. By the time I got to that, my code was a mess with all the changes. It's ugly but it works.

### Day 10
Did not realize it but I shouldn't be pushing the input data to git. Woops, let's fix that. I updated my git ignore and did a commit to get them out of HEAD, then used [BFG Repo Cleaner](https://rtyley.github.io/bfg-repo-cleaner/) to remove them from git history. It was instructive to walk through this proess. I guess this is what you'd do if somone accidenty committed keys or other sensitive data into a public repo. Good exercise. The data is still out there if anyone cloned my repo, but such is the ways of the internet.


### Day 9
This was a fun puzzle for Friay, but it gave me lot of fits. I got a reasonalbe understanding and start in the morning, but then during the work day I wasn't able to spend much time on it. After just gutting through part 1 to get it done, I knew what I wrote was already long in the tooth. Once I saw part 2, I knew a full refactor was the best approach - thus, rope generation 2. 

I take a couple of good lessons from working through the ropes
- buidling a quick first version to understand the problem, then starting over with improved appreciation of the problem makes a lot of sense
- break things into very small parts and test each. Trying to debug/troublshoot the 10 knot rope at the high level was challenging. Being able to look at a lot of small parts and walk through them made the bugs easy to see
- after a certain amount of time on a problem, just step away and do something else. I did this a few times and when I came back to it, minor woops were much easier to spot and fix

#### Day 6
Looking back on what's done so far, I've started to develop a point of view for this year. Generally, I'm writing code that's flexible and easy to understand. As I'm working on my solutions, I find myself asking "If someone looked at this two years from now and had to modfiy it, how easy or hard would that be." As a result, it's definitely not the most compact code. The code is also not super efficient - though I'm trying to not be aggregiously wasteful of computer stuff.

It's fun reading through the [Adent of Code Reddit thread](https://www.reddit.com/r/adventofcode/) each day. I found links to some extra large inputs for the Day 5 crate stacking problem. Trying those clearly showed that my python was not super-optimized. Sure my code could plow through crates stacked 8 high, but trying to work with stacks nearly 1.5 million crates high was another matter.






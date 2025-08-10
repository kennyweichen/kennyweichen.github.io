---
layout: post
category: problems
full_width: false
title: "Problem: Even Before Odd"
---

Suppose you roll a fair 6-sided die until you've seen all 6 faces. What is the probability you won't see an odd numbered face until you have seen all even numbered faces?

My attempt: 

A fair-sided dice implies the $$P(X = \text{any face}) = 1/6$$

We need to see all even numbered faces so we need to see 2, 4, and 6 before we see 1, 3, or 5. Since we only care about the first time we see a number, we don't care about repeats so if we roll 2 on the first roll and then 2 again on the second roll we don't consider that. So what is the probability of seeing 2,4,6 in any combination? That is $$\frac{1}{6}^3 * 6 = 1/36.$$

After my simulations, I'm getting about 0.05 which is 1/20 so my math is definitely off.

The solution says to focus on the orderings. We know that we can uniquely order the faces of a die using 6!. Let's use this as the denominator and for the numerator, we have 3! unique orderings of even numbers and the same for odd numbers. So this turns out to be $$\frac{3!3!}{6!} = \frac{1}{20}$$.  

Takeaway:

Focus less on the probability and more on the total orderings and counts. 


```python
import random
random_int = random.randint(1, 6)  # Generates a random integer between 1 and 6 (inclusive)
# print(random_int)
num_simulations = 10000
num_event = 0
for i in range(1, num_simulations+1):
    even_before_odd = False
    keepGoing = True
    even_dict = {2: False, 4: False, 6: False}

    while keepGoing:
        # print("beginning of loop")
        random_int = random.randint(1, 6)
        # print(random_int)
        if random_int in (2, 4, 6):
            even_dict[random_int] = True
            # print(even_dict)
        elif random_int in (1, 3, 5) and not all(even_dict.values()):
            # print(random_int)
            keepGoing = False
        else: 
            even_before_odd = True
            keepGoing = False
    if even_before_odd:
        num_event += 1

print(num_event/num_simulations)

```

    0.0514


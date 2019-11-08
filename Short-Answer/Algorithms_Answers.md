#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)


b) O(n^2)


c) O(1)

## Exercise II

The first step is understanding what we're trying to figure out.  We want to determine the floor number (f) that yeilds the least amount of broken eggs and also the least amount of eggs dropped. I would approach this problem by putting in real values. 

So for example, if we drop x amount of eggs and x = 20.  This means that depending on the value of f (floor number) will determine # of broken eggs.  We want to minimize the number of eggs broken.  So if f = 4 (in my example), then 10 eggs break, so on and so forth:

f = 4 (10 eggs break)
f = 3 (5 eggs break)
f = 2 (3 eggs break)
f = 1 (1 eggs break)

if we add amount dropped, we get something like this:
# Total dropped + broken

f = 30
f = 25
f = 23
f = 21

In this example, to resolve the best case - f = 1. 

def best(pass in amount of eggs, {"floor num", num of eggs broke}):
    loop through dict:
        amount of eggs + broken amaount
        append a list of list [floor num, total amount]
        return the list
    run sorting algorith on list (selection)
    return lowest value

Runtime Complexity: O(n^2)
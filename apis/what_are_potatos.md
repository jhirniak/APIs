
# The story of potato picture

When looking up for description of potatos in [this picture](https://upload.wikimedia.org/wikipedia/commons/a/ab/Patates.jpg) I got few different responses from [CloudSightAPI](http://cloudsightapi.com/), some within 30-40 minutes between requests.

1. orange brown and red oval fruits
2. purple brown and maroon potato
3. orange brown and red oval stones
4. brown red and orange oval stones
5. brown beige yellow beans
6. sweet potatoes
7. brown beige and pink potatoes
8. brown oval root crops
9. brown yellow and purple pebble
10. brown red and purple potatoes
11. brown beans
12. different colors of sweet potatoes
13. brown oval root crops
14. brown purple red and yellow vegetables
15. different colors of potatoes stack
16. assorted potatoes

The answer seems clearly to change with time, it can go from right to totally unexpected answer at the beginning, in the middle getting similar description, but some not that much expected (e.g. beans or crops), at the end getting one answer repeatedly, but which also changes (at the end I was getting 200 sweet potatoes, which then changed to assorted potatoes).

This is quite interesting how many responses I got within 2 days and the convergance to one answer, but it is worth noting that in general the quality of the answer improved.

# Observations

* The service just returns token immediately for the request, so the request for answer may need to be done few times with a short delay to get the description and not `None`. The credit is taken for submitting the request and not fetching it (verified with `creditation_experiment.py`).
* Acceptable answer was recievved at the beginning, but on the way many unexpected answers occurred like pebbles, stones, beans, crops, etc. However, looking at the picture it can be clear why they could be read as those objects.
* As time went answer seemed to improve at the end arriving at very close description, but losing some content. At the beginning we got clear description of colors what at the end was replaced with word assorted (i.e. giving very human-like description).
* I query resulted in 16 different answer.
* It is unclear from the observation how the service works as results can change e.g. from potatoes to stones and from stones to crops in a metter of a minute. However, after many requests service seems to arrive at good and stable answer. CloudSightAPI is said to use MechanicalTurk, so it may explain how the answer improves with time. However, short-timed changes are more unexpected.

# Last, but not least...

... and here is a picture of the potatos ;).

![Potatos](https://upload.wikimedia.org/wikipedia/commons/a/ab/Patates.jpg)

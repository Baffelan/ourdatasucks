---
title: "The story of the sneaky zeros"
tags: blog, null values, zero-values
date: 2025-01-02
---

# The story of the sneaky zeros

For my master’s project, I was using a dataset which provided me with a large collection of LLM output text, alongside a numerical label indicating how significant of a hallucination was contained in the text (the consistency rating) for some of the entries. It was a neatly organised table (or so it appeared), with columns dedicated to all sorts of interesting metrics. Everything seemed fine at first glance. But first glances can apparently be very deceptive!

The goal was simple: calculate the average consistency rating for each category and draw some profound insights. Sounds easy, right? I wrote the SQL query with the confidence of someone who had yet to be betrayed by their own dataset. Seconds later, the results appeared, and something looked... off.

One category had an average consistency rating so low that it felt like the LLM had been purposely trying to spread disinformation. “Surely that can’t be right,” I thought. But who was I to argue with the numbers?

# The suspicion sets in

After double-checking my query and confirming I had the right column, the confusion began to set in. Not wanting to accept defeat, I began looking through the dataset thoroughly. Row by row, everything was looking perfect, until I spotted them: the zeros. Now you may be thinking "Well zeros are normal, right? They mean no consistency." But as I kept scrolling, something clicked. Why were some entries NULL and others explictly zero? And why were entries which seemed to be factually correct being marked with a zero consistency rating? What kind of prank was this? Who thought it would be a good idea to mix NULLs and zeros like that and set out to ruin my computation?

# The aftermath

For those unfamiliar with the subtle art of SQL averages, here's the twist: NULL values are ignored in calculations, while zeros are not. So when my dataset tossed in a few stealthy zeros alongside the NULLs, it dragged the average consistency rating straight into the abyss. Sadly, since there were some legitimate zero-consistency examples in the database, I had to abandon the dataset in favour of a smaller, but more functional, dataset.

# Lessons learned

1. **Never blindly trust your data.** It can be out to get you!
2. **Zeros and NULLs are not the same.** They may look innocent, but one will quietly step aside while the other ruins your calculations.
3. **Manual inspection can be very valuable.** Even a quick skim-through of the dataset can sometimes reveal important information about your dataset.

# Data Snippet

| Text                                                                                  | Consistency |
|---------------------------------------------------------------------------------------|-------------|
| Usain Bolt will compete at the relay championship on May 2 and 3 ...                  | 1.67        |
| Serena Williams beat Sara Errani 4-6 7-6 ...                                          | 2.67        |
| Buckingham Palace guard slipped on manhole cover in front of hundreds ...             | 0           |
| Brazilian coach Ze Maria was fired on Wednesday after poor run ...                    | 2.33        |
| Chipotle has decided to tap into the $70 billion food delivery market ...             | NULL        |

The statement "Buckingham Palace guard slipped on manhole cover..." is in fact consistent (should be NULL)! See: https://www.youtube.com/watch?v=cqmG5JWLRag


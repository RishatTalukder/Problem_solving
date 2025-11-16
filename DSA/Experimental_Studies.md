# Experimental_Studies

This is the process where we find try to find the genuine run time of a program. But this comes with its own set of drawbacks because the run time of a program is dependent on the `hardware` and the `software` used to run the program.

We can find the run time of a program by using the `time` module in python.

```python
# time_measurement.py
import time
start = time.time() #returns the starting time in seconds

# algorithm function

end = time.time() #returns the ending time in seconds
elapsed_time = end - start # we get the run time
print(elapsed_time)

```
<a href="time_measurement.py">time_measurement.py</a>

Although the time module is used to measure the run time of a program, but it is different for different machines. So, we might not get the same efficiency every time but what we can do is test out the run time for different inputs and `plot` the graph to get the average run time.

Let's say for `n` (10,100,1000,10000,100000) we get the `run time` (t1,t2,t3,t4,t5) and if we plot the time in the `x` axis and `n` in the `y` axis then we can get the `graph`.

Even though the run time can be different the plotting of the graph will not change and we would surely get understanding of the algorithm. 

The main drawbacks of this method is:

1. Comparing two algorithms is difficult unless both algorithms are executed on the same hardware.

2. Experiments can only be done in limited set of test inputs and not in all possible inputs. The important input may be important to the algorithm.

3. An algorithm must be fully implemented before the test starts.

The last drawback can be a the most serious drawback. It would be foolish to spend a significant amount of time testing an algorithm that could easily be deemed inferior using other `higher-level` analysis.

So, we need to fix these issues.
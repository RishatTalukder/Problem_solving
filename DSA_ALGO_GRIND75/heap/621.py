import collections

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # make a counter of the tasks
        # n_temp = n+1
        # while the counter is not empty
        # loop through the counter and decrement the count of the task and also decrement n_temp
        # if the count of the task is 0, remove it from the counter
        # if n_temp is greater than 0, add the idle time to the counter
        # return the total time taken

        counter = collections.Counter(tasks)

        idle_time = 0
        while counter:
            n_temp = n+1
            for task, _ in counter.most_common(n_temp):
                counter[task] -= 1
                if counter[task] == 0:
                    del counter[task]
                n_temp -= 1
                # if not counter:
                #     break

            if not counter:
                break
            else:
                idle_time += n_temp

        return len(tasks) + idle_time

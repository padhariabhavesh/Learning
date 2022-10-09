"""
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.
"""


class Solution:
    from collections import Counter
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if tasks is None or len(tasks) == 0:
            return None
        # if no idle time is needed, the time is the number of tasks
        if n == 0:
            return len(tasks)
            # count_set will return Counter({'A':3, 'B':3})
        count_set = Counter(tasks)
        # extract the dictionary from the counter object
        tasks_dict = dict(count_set)
        # returns the count of the most common task
        # The 'if count_set else None' prevents an error
        most_common_task = count_set.most_common(1)[0] if count_set else None

        if most_common_task is None:
            return len(tasks)

        num_most_common = most_common_task[1] - 1
        # multiply that number * the required cooldown time
        idle_units = num_most_common * n
        # no idle needed at the end, so get rid of that first item
        tasks_dict.pop(most_common_task[0])

        for key, value in tasks_dict.items():
            idle_units -= min(value, num_most_common)

        if idle_units < 0:
            return len(tasks)

        return len(tasks) + idle_units
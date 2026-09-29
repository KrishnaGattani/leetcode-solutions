class Solution:
    def leastInterval(self, tasks, n):
        count = {}

        for task in tasks:
            count[task] = count.get(task, 0) + 1

        max_count = max(count.values())

        max_tasks = 0
        for value in count.values():
            if value == max_count:
                max_tasks += 1

        answer = (max_count - 1) * (n + 1) + max_tasks

        return max(answer, len(tasks))
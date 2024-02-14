class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort()

        stack = [intervals[0]]

        for i in intervals[1:]:
            if stack[-1][0] <= i[0] <= stack[-1][1]:
                stack[-1][1] = max(i[1],stack[-1][1])

            else:
                stack.append(i)
        return stack



shit_list = []

print(shit_list)

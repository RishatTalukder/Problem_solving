class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        merged_meetings= [meetings[0]]

        for start, end in meetings[1:]:
            if merged_meetings[-1][0] <= start <= merged_meetings[-1][1]:
                merged_meetings[-1][1] = max(merged_meetings[-1][1], end)
            else:
                merged_meetings.append([start, end])

        count = 0
        for start, end in merged_meetings:
            count += (end - start + 1)

        return days - count
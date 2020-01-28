from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        start, end = 0, 1
        intervals.sort(key=lambda meeting: meeting[start])
        for index in range(1, len(intervals)):
            meeting, previous_meeting = intervals[index], intervals[index - 1]
            if meeting[start] < previous_meeting[end]:
                return False
        return True

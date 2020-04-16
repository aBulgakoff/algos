from itertools import accumulate


class Solution:  # two pass
    def checkValidString(self, s: str) -> bool:
        left_balance = right_balance = 0
        for ch in s:
            if ch in ('(', '*'):
                left_balance += 1
            else:
                left_balance -= 1

            if left_balance < 0:
                return False

        if not left_balance:
            return True

        for ch in reversed(s):
            if ch in (')', '*'):
                right_balance += 1
            else:
                right_balance -= 1

            if right_balance < 0:
                return False
        return True


class Solution2:  # two pass iterator
    def checkValidString(self, s: str) -> bool:
        return all(l >= 0 and r >= 0
                   for l, r
                   in zip(accumulate(map(lambda x: -1 if x == ')' else 1, s)),
                          accumulate(map(lambda x: -1 if x == '(' else 1, s[::-1])))
                   )


class Solution3:  # greedy
    def checkValidString(self, s: str) -> bool:
        low_bound = high_bound = 0

        for symbol in s:
            if symbol == '(':
                low_bound += 1
                high_bound += 1
            elif symbol == ')':
                low_bound -= 1
                high_bound -= 1
            elif symbol == '*':
                low_bound -= 1
                high_bound += 1

            if high_bound < 0:
                return False

            if low_bound < 0:
                low_bound = 0

        return low_bound == 0


class Solution4:  # greedy with lambda
    def checkValidString(self, s: str) -> bool:
        low_bound = high_bound = 0

        match = {
            '(': lambda: (low_bound + 1, high_bound + 1),
            ')': lambda: (low_bound - 1, high_bound - 1),
            '*': lambda: (low_bound - 1, high_bound + 1)
        }
        for symbol in s:
            low_bound, high_bound = match[symbol]()

            if low_bound < 0:
                low_bound = 0

            if high_bound < 0:
                return False

        return low_bound == 0


class Solution5:  # greedy with lambda
    def checkValidString(self, s: str) -> bool:
        bounds = (0, 0)
        match = {
            '(': lambda l, r: (l + 1, r + 1),
            ')': lambda l, r: (l - 1 if l > 0 else l, r - 1),
            '*': lambda l, r: (l - 1 if l > 0 else l, r + 1)
        }
        for symbol in s:
            bounds = match[symbol](*bounds)

            if bounds[1] < 0:
                return False

        return bounds[0] == 0


class Solution6:  # greedy with lambda
    def checkValidString(self, s: str) -> bool:
        match = {'(': lambda l, r: (l + 1, r + 1),
                 ')': lambda l, r: (l - 1 if l > 0 else l, r - 1),
                 '*': lambda l, r: (l - 1 if l > 0 else l, r + 1)}
        matched = [*accumulate(s, lambda b, ch: match[ch](*b), initial=(0, 0))]
        return all(r >= 0 for l, r in matched) and matched[-1][0] == 0

class Solution:  # greedy
    def balancedStringSplit(self, s: str) -> int:
        str_count = 0
        symbol_count = {'L': 0, 'R': 0}
        for symbol in s:
            symbol_count[symbol] += 1
            if symbol_count['L'] == symbol_count['R']:
                str_count += 1
                symbol_count['L'] = 0
                symbol_count['R'] = 0
        return str_count


class Solution2:  # greedy
    def balancedStringSplit(self, s: str) -> int:
        count = str_count = 0
        for ch in s:
            count += ch == 'L'
            count -= ch == 'R'
            str_count += count == 0
        return str_count


class Solution3:
    def balancedStringSplit(self, s: str) -> int:
        count = str_count = 0
        marker = {'L': 1, 'R': -1}
        for ch in s:
            count += marker[ch]
            str_count += count == 0
        return str_count

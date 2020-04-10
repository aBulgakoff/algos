from itertools import zip_longest


def pop_before_sharp(text: str) -> str:
    result = []
    for symbol in text:
        if symbol == '#':
            result.pop() if result else ''
            continue
        result.append(symbol)
    return ''.join(result)


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return pop_before_sharp(S) == pop_before_sharp(T)


def generate_excluding_sharp(text):
    qty_symbols_skip = 0
    for symbol in reversed(text):
        if symbol == '#':
            qty_symbols_skip += 1
        elif qty_symbols_skip:
            qty_symbols_skip -= 1
        else:
            yield symbol


class Solution2:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return all(s_symbol == t_symbol
                   for s_symbol, t_symbol
                   in zip_longest(generate_excluding_sharp(S),
                                  generate_excluding_sharp(T))
                   )

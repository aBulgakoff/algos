class Solution:
    def isHappy(self, n: int) -> bool:
        n_str,n_str_log = str(n), set()
        while n_str != '1':
            n_sum = 0
            for base in n_str:
                n_sum += pow(int(base), 2)
            if (n_str:=str(n_sum)) in n_str_log:
                return False
            n_str_log.add(n_str)
        return True


from operator import add
from functools import reduce


class Solution2:
    def isHappy(self, n: int) -> bool:
        n_str, n_str_log = str(n), set()
        while n_str != '1':
            if (n_str:= str(reduce(add,map(lambda base: pow(int(base), 2),n_str)))) in n_str_log:
                return False
            n_str_log.add(n_str)
        return True

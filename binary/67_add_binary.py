class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return f'{int(a, 2) + int(b, 2):b}'


class Solution2:
    def addBinary(self, a: str, b: str) -> str:
        a_num, b_num = int(a, 2), int(b, 2)
        while b_num:
            answer = a_num ^ b_num
            carry = (a_num & b_num) << 1
            a_num, b_num = answer, carry
        return bin(a_num)[2:]

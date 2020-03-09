class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.storage = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.storage[number] = self.storage.get(number, 0) + 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        return list(
            filter(
                lambda x: value - x in self.storage and (x != value - x or self.storage[x] > 1),
                self.storage
            )
        )

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)

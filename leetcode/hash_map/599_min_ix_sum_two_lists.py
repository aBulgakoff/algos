from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict1 = {name: ix for ix, name in enumerate(list1)}
        dict2 = {name: ix for ix, name in enumerate(list2)}

        product = {name: dict1[name] + dict2[name] for name in dict1.keys() & dict2.keys()}
        least_ix_sum = min(product.values())

        return list(filter(lambda name: product[name] == least_ix_sum, product))

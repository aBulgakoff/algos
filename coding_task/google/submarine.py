from typing import List

# air in submarines [10, 6, 2, 1]
# people to allocate 6


def allocate(submarine: List[int], people: int) -> List[int]:
    init_ratio = sum(submarine) / people
    subs_priority = list(map(lambda capacity: capacity if capacity >= init_ratio else 0, submarine))
    final_ratio = sum(subs_priority) / people
    return list(map(lambda x: round(x / final_ratio), subs_priority))


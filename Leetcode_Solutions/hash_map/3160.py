from collections import defaultdict
from typing import List

class Solution:
    """
    This class provides a method to process a series of queries and return the number of unique balances after each query.

    Method:
    - queryResults(limit, queries): Processes the queries and returns a list of the number of unique balances after each query.

    Pseudo Code:
    1. Initialize a dictionary `balance_map` to store the balance for each key.
    2. Initialize a defaultdict `balance_count` to count occurrences of each balance.
    3. Initialize a list `results` to store the number of unique balances after each query.
    4. Iterate through each query:
        a. Extract `key` and `value` from the query.
        b. If `key` is not in `balance_map`, add it with the `value`.
        c. If `key` is already in `balance_map`, update its balance:
            i. Decrease the count of the old balance in `balance_count`.
            ii. If the count of the old balance becomes zero, remove it from `balance_count`.
            iii. Update the balance for the `key` in `balance_map`.
        d. Increase the count of the new balance in `balance_count`.
        e. Append the number of unique balances to `results`.
    5. Return `results`.
    """

    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balance_map = {}
        balance_count = defaultdict(int)
        results = []

        for key, value in queries:
            if key in balance_map:
                old_balance = balance_map[key]
                balance_count[old_balance] -= 1
                if balance_count[old_balance] == 0:
                    del balance_count[old_balance]

            balance_map[key] = value
            balance_count[value] += 1
            results.append(len(balance_count))
    
        return results
class Solution:
    """
    A class used to determine if a frog can cross a river by jumping on stones.
    Methods
    -------
    canCross(stones: List[int]) -> bool
        Determines if the frog can cross the river given the positions of stones.
    Pseudocode:
    1. Initialize a hash_map where each stone position maps to an empty set.
    2. Add a jump distance of 0 to the starting stone (position 0).
    3. Iterate through each stone in the stones list.
        a. For each stone, iterate through its possible previous jump distances.
        b. For each previous jump distance, calculate the next possible jump distances (prev_jump_distance - 1, prev_jump_distance, prev_jump_distance + 1).
        c. If the next jump distance is positive and the stone at the next position exists in the hash_map, add the next jump distance to the set of the next stone.
    4. Return True if there are any jump distances in the set of the last stone, otherwise return False.
    """
    def canCross(self, stones) -> bool:
        hash_map = {stone : set() for stone in stones}
        hash_map[0].add(0)

        for stone in stones:
            for prev_jump_distance in hash_map[stone]:
                for next_jump_distance in [prev_jump_distance - 1, prev_jump_distance, prev_jump_distance + 1]:
                    if next_jump_distance > 0 and stone + next_jump_distance in hash_map:
                        hash_map[stone + next_jump_distance].add(next_jump_distance)

        
        return len(hash_map[stones[-1]]) > 0


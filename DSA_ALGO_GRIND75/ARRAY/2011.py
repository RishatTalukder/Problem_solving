class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        dic = {
            "X++":1,"++X":1,
            "X--":-1,"--X":-1
        }

        initial = 0

        for operation in operations:
            initial = initial + dic[operation]

        return initial
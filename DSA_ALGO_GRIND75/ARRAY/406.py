class Solution:
    """
    A class used to reconstruct a queue based on people's heights and the number of people in front of them who have a height greater than or equal to theirs.

    Methods
    -------
    reconstructQueue(people: List[List[int]]) -> List[List[int]]:
        Reconstructs the queue based on the given list of people.
    """
    
    """
        Reconstructs the queue based on the given list of people.

        Parameters
        ----------
        people : List[List[int]]
            A list of lists where each sublist contains two integers. The first integer represents the height of a person, and the second integer represents the number of people in front of this person who have a height greater than or equal to theirs.

        Returns
        -------
        List[List[int]]
            The reconstructed queue as a list of lists, where each sublist contains two integers representing the height of a person and the number of people in front of them who have a height greater than or equal to theirs.
        
        Example
        -------
        >>> sol = Solution()
        >>> sol.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])
        [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
    """
    def reconstructQueue(self, people):
        people.sort(key= lambda x : (-x[0], x[1]))
        res = []
        for i in people:
            res.insert(i[1],i)
        return res
    

sol = Solution()
print(sol.reconstructQueue([[7,1],[4,4],[7,0],[5,0],[6,1],[5,2]])) # [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
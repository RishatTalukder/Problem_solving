from collections import deque

class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        
        # Histogram heights for each column
        heights = [0] * (cols + 1)  # +1 sentinel column
        max_area = 0

        # Process row by row
        for row in range(rows):
            # Monotonic increasing stack (stores column indices)
            stack = [-1]

            for col in range(cols + 1):
                # Update histogram heights
                if col < cols and matrix[row][col] == '1':
                    heights[col] += 1
                else:
                    heights[col] = 0

                # Maintain increasing stack
                while stack[-1] != -1 and heights[stack[-1]] > heights[col]:
                    height = heights[stack.pop()]
                    width = col - stack[-1] - 1
                    max_area = max(max_area, height * width)

                stack.append(col)

        return max_area


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix and not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        max_area = 0
        heights = [0]*(cols+1)

        for i in range(rows):
            stack = [-1]
            for j in range(cols+1):
                if j < cols and matrix[i][j] == '1':
                    heights[j] += 1

                else:
                    heights[j] = 0

                
                while stack[-1] != -1 and heights[stack[-1]] > heights[j]:
                    height = heights[stack.pop()]
                    width = j - stack[-1] -1

                    max_area= max(max_area, height*width)

                stack.append(j)

        return max_area

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        heights = [0]*(cols+1)

        max_area = 0

        for i in range(rows):
            stack = [-1]

            for j in range(cols+1):
                if j < cols and matrix[i][j] == '1':
                    heights[j] += 1

                else:
                    heights[j] = 0

                while stack[-1] != -1 and heights[stack[-1]] > heights[j]:
                    height = heights[stack.pop()]
                    width = j - stack[-1] -1
                    max_area = max(max_area, height*width)

                stack.append(j)

        return max_area
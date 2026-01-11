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

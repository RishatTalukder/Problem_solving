from collections import defaultdict

from collections import deque, defaultdict

def canFinish(numCourses, prerequisites):
    # Step 1: Build the graph
    graph = defaultdict(list)
    in_degree = [0] * numCourses

    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course)
        in_degree[course] += 1

    # Step 2: Initialize the queue with nodes having in-degree 0
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

    # Step 3: Process the courses in topological order
    visited_courses = 0

    while queue:
        current = queue.popleft()
        visited_courses += 1

        # Decrease in-degree of neighbors and add them to the queue if in-degree becomes 0
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If all courses are visited, return True
    return visited_courses == numCourses

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)

        for course, prereq in prerequisites:
            adj_list[prereq].append(course)

        visited = set()

        def dfs(course):
            if course in visited:
                return False

            if adj_list[course] == []:
                return True

            visited.add(course)

            for neighbor in adj_list[course]:
                if not dfs(neighbor):
                    return False

            visited.remove(course)
            adj_list[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
            
        return True
    





from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for course, pre in prerequisites:
            adj_list[pre] = course

        vigited = set()

        def dfs(course):
            if course in vigited:
                return False
            
            if adj_list[course] == []:
                return True
            
            vigited.add(course)

            for neighbor in adj_list[course]:
                if dfs(neighbor) == False:
                    return False
            
            vigited.remove(course)
            adj_list[course] = []

            return True
        
        for course in range(numCourses):
            if dfs(course) == False:
                return False
            
        
        return True
        

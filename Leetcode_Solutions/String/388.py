class Solution:
    def lengthLongestPath(self, input: str) -> int:
        paths = input.split("\n")
        level = {0:0}
        maxx = 0

        for path in paths:
            name = path.lstrip("\t")
            depth = len(path) - len(name)

            is_file = "." in name

            if is_file:
                maxx = max(maxx, level[depth]+len(name))
            
            else:
                level[depth+1] = level[depth]+len(name)+1

        return maxx
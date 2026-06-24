string = list("aabc")

res = set()


def dfs(string, current_ind):
    if current_ind == len(string):
        print(string)
        return
    
    for i in range(current_ind, len(string)):

        string[i], string[current_ind] = string[current_ind], string[i]

        dfs(string, current_ind+1)

        string[i], string[current_ind] = string[current_ind], string[i]

    
dfs(string, 0)

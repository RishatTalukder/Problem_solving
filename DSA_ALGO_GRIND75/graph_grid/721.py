class DSU:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    # Find operation with path compression
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    # Union operation with union by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Attach smaller tree under larger tree
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

    # Add an element to the DSU
    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0


from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU()
        email_to_name = {}

        for account in accounts:
            name = account[0]
            first_mail = account[1]
            for email in account[1:]:
                dsu.add(email)
                dsu.union(first_mail,email)
                email_to_name[email] = name

            
        email_group = defaultdict(list)
        for email in email_to_name.keys():
            parent = dsu.find(email)
            email_group[parent].append(email)

        merged_emails = []
        for parent,emails in email_group.items():
            merged_emails.append([email_to_name[parent]]+sorted(emails))

        return merged_emails 
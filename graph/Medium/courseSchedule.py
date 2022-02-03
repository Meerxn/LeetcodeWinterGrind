class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hasher = {i:[] for i in range(numCourses)}
        for course,preq in prerequisites:
            hasher[course].append(preq)
        visited = set()
        def dfs(node):

            if node in visited:
                return False
            if hasher[node] == []:
                return True
            visited.add(node)
            for pre in hasher[node]:
                if dfs(pre) == False:
                    return False
            visited.remove(node)
            hasher[node] = []
        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True
    
        
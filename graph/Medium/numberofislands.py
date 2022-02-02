class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        grid2 = [list( map(int,i) ) for i in grid]
        counter = 0 
       
        def dfs(i,j):
            if i > 0 and grid2[i-1][j] == 1:
                grid2[i][j] = 0
                dfs(i-1,j)
            if i < len(grid2) - 1 and grid2[i+1][j] == 1:
                grid2[i][j] = 0
                dfs(i+1,j)
            if j < len(grid2[0]) - 1 and grid2[i][j+1] == 1:
                grid2[i][j] = 0
                dfs(i,j+1)
            if j > 0 and grid2[i][j-1] == 1:
                grid2[i][j] = 0
                dfs(i,j-1)
            else:
                grid2[i][j] = 0 
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1:
                    counter+=1
                    dfs(i,j)
        return counter
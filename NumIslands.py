class Solution:
    def explore(self, grid, visited, i, j):
        """
        given i,j, explore all neighbors if they connect to island, then mark as visited

        """
        m = len(visited) # numrows
        n = len(visited[0]) #numcols
        #check if out of bounds
        if (i < 0 or i >= m) or (j < 0  or j >= n):
            return
        if visited[i][j] or grid[i][j] == "0":
            return
        
        # not out of bounds, so label as visited
        visited[i][j] = True
        self.explore(grid, visited, i-1, j) #top
        self.explore(grid, visited, i+1, j) # bottom
        self.explore(grid, visited, i, j-1) #left
        self.explore(grid, visited, i, j+1) #right
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        how can we do this?
        maybe depth first search? go deep, return, onto the next?
        hold visited and explore neighbors. If 1, then explore other possibilities, label them as visited.
        go through list like this. Since next time we visit a land, we will know whether it was already counted as an island if we marked it

        visited[m][n]: T/F whether visited or not, all false initially
        num islands counter
        then iterate through all items
        if not visited and land, increase num islands

        length of list holds rows (that's the first index)
        length of the list in the list should hold cols (second index)
        """
        m = len(grid) # numrows
        n = len(grid[0]) #numcols
        visited = [[False] * n for _ in range(m)]
        num_islands = 0

        for i in range(m):
            for j in range(n):
                # If not visited and land
                if not visited[i][j] and grid[i][j] == "1":
                    num_islands += 1
                    self.explore(grid, visited, i, j)
        
        return num_islands
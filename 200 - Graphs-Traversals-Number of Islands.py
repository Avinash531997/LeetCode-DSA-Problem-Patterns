class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows,cols = len(grid), len(grid[0])
        visit=set()
        islands=0
        def bfs(row,col):
            q=collections.deque()
            visit.add((row,col))
            q.append((row,col))
            while q:
                r,c=q.popleft()
                directions = [[1,0], [-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    nr,nc = r+dr, c+dc
                    if (nr in range(rows) and nc in range(cols) and grid[nr][nc]=='1' and (nr,nc) not in visit):
                        q.append((nr,nc))
                        visit.add((nr,nc))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col]=='1' and (row,col) not in visit:
                    islands+=1
                    bfs(row,col)
                    
        return islands
        

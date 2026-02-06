class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid) , len(grid[0])
        visited = set()
        island = 0

        def bfs(r,c):
            q = deque()
            q.append((r, c))

            while q:
                row, col = q.popleft()
                dirs = [(0,1),(0,-1),(1,0),(-1,0)]

                for dr, dc in dirs:
                    r , c = row + dr, col + dc
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1" and (r, c) not in visited:
                        q.append((r,c))
                        visited.add((r,c))



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    island += 1
                    visited.add((r,c))
                    bfs(r, c)

        return island

O(r*C)

########################################################
994. rotten oranges

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = grid
        q = collections.deque()
        countFreshOrange = 0
        for i in range(m):
            for j in range(n):
                if visited[i][j] == 2:
                    q.append((i, j))
                if visited[i][j] == 1:
                    countFreshOrange += 1
        if countFreshOrange == 0:
            return 0
        if not q:
            return -1
        
        minutes = -1
        dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        while q:
            size = len(q)
            while size > 0:
                x, y = q.popleft()
                size -= 1
                for dx, dy in dirs:
                    i, j = x + dx, y + dy
                    if 0 <= i < m and 0 <= j < n and visited[i][j] == 1:
                        visited[i][j] = 2
                        countFreshOrange -= 1
                        q.append((i, j))
            minutes += 1
        
        if countFreshOrange == 0:
            return minutes
        return -1
#####################################

542. 01 Matrix
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = float('inf')

        while queue:
            row, col = queue.popleft()

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if 0 <= new_row < rows and 0 <= new_col < cols and mat[new_row][new_col] > mat[row][col] + 1:
                    mat[new_row][new_col] = mat[row][col] + 1
                    queue.append((new_row, new_col))

        return mat        


        
        

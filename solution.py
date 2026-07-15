from collections import deque
from typing import List

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Edge case: If the start or end cell contains a thief, the safeness factor is immediately 0
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0
            
        # --------------------------------------------------
        # Phase 1: Compute Minimum Manhattan Distance Grid
        # --------------------------------------------------
        dist = [[float('inf')] * n for _ in range(n)]
        queue = deque()
        
        # Initialize the queue with all thief positions
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    queue.append((r, c))
                    
        # Multi-source BFS to calculate the shortest distance from any cell to the nearest thief
        while queue:
            r, c = queue.popleft()
            for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == float('inf'):
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))

        # --------------------------------------------------
        # Phase 2: Guided Traversal via "Look-Ahead Radar"
        # --------------------------------------------------
        max_safe_reached = [[-1] * n for _ in range(n)]
        explorer_queue = deque([(0, 0, dist[0][0])])
        max_safe_reached[0][0] = dist[0][0]
        
        while explorer_queue:
            r, c, current_path_safe = explorer_queue.popleft()
            
            # Skip if a safer or equal path has already visited this cell
            if current_path_safe < max_safe_reached[r][c]:
                continue
                
            best_step_weight = -1
            candidates = []
            
            # A) Scan the four primary orthogonal directions
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    step_weight = dist[nr][nc]
                    actual_safe = min(current_path_safe, step_weight)
                    
                    if actual_safe > max_safe_reached[nr][nc]:
                        candidates.append((step_weight, actual_safe, nr, nc))
                        if step_weight > best_step_weight:
                            best_step_weight = step_weight
                        
            # B) Look-ahead check for diagonal directions (using bridge cells)
            for dr, dc in [(1,1), (1,-1), (-1,1), (-1,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    best_bridge_val = max(dist[r + dr][c], dist[r][c + dc])
                    step_weight = min(best_bridge_val, dist[nr][nc])
                    actual_safe = min(current_path_safe, step_weight)
                    
                    if actual_safe > max_safe_reached[nr][nc]:
                        candidates.append((step_weight, actual_safe, nr, nc))
                        if step_weight > best_step_weight:
                            best_step_weight = step_weight
                        
            # C) Branch expansion utilizing the optimal local movement weight
            if best_step_weight != -1:
                for s_weight, a_safe, nr, nc in candidates:
                    if s_weight == best_step_weight and a_safe > max_safe_reached[nr][nc]:
                        max_safe_reached[nr][nc] = a_safe
                        explorer_queue.append((nr, nc, a_safe))
                            
        # The final result is the maximum safeness factor reached at the bottom-right corner
        return max_safe_reached[n-1][n-1] if max_safe_reached[n-1][n-1] != -1 else 0

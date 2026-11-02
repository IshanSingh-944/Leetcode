from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        q = deque()
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        total = 0
        fresh = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        print("Initial Queue:", list(q))
        print("Initial Fresh:", fresh)

        while q and fresh > 0:

            print(f"\n===== Minute {total} =====")
            print("Queue at start:", list(q))
            print("Fresh oranges left:", fresh)

            for _ in range(len(q)):

                r, c = q.popleft()

                print(f"\nProcessing rotten orange: ({r}, {c})")

                for dr, dc in dir:

                    nr = r + dr
                    nc = c + dc

                    print(f"  Checking neighbor: ({nr}, {nc})")

                    if nr < 0 or nc < 0 or nr >= row or nc >= col:
                        print("    Out of bounds")
                        continue

                    if grid[nr][nc] == 0:
                        print("    Empty cell")
                        continue

                    if grid[nr][nc] == 2:
                        print("    Already rotten")
                        continue

                    if grid[nr][nc] == 1:
                        print(f"    Fresh -> Rotten at ({nr}, {nc})")

                        grid[nr][nc] = 2
                        fresh -= 1

                        print("    Fresh remaining:", fresh)

                        q.append((nr, nc))
                        print("    Added to queue")

            total += 1

            print("\nEnd of minute")
            print("Queue for next minute:", list(q))
            print("Fresh left:", fresh)

        print("\n===== Final State =====")
        print("Minutes:", total)
        print("Fresh:", fresh)

        return total if fresh == 0 else -1
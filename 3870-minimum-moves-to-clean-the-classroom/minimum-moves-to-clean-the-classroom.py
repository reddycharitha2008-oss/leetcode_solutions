from collections import deque

class Solution:
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])

        start = None
        litter_id = {}
        k = 0

        # Find start and assign IDs to litter
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)

                elif classroom[i][j] == 'L':
                    litter_id[(i, j)] = k
                    k += 1

        full_mask = (1 << k) - 1

        if k == 0:
            return 0

        queue = deque()
        queue.append((start[0], start[1], 0, energy, 0))

        # Maximum energy seen for (row, col, mask)
        best = {}
        best[(start[0], start[1], 0)] = energy

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c, mask, remaining, moves = queue.popleft()

            if mask == full_mask:
                return moves

            # Cannot make another move without energy
            if remaining == 0:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                new_energy = remaining - 1
                new_mask = mask

                # Collect litter
                if (nr, nc) in litter_id:
                    idx = litter_id[(nr, nc)]
                    new_mask |= (1 << idx)

                # Reset energy
                if classroom[nr][nc] == 'R':
                    new_energy = energy

                key = (nr, nc, new_mask)

                # Skip if we already reached this state
                # with equal or more energy
                if key in best and best[key] >= new_energy:
                    continue

                best[key] = new_energy
                queue.append(
                    (nr, nc, new_mask, new_energy, moves + 1)
                )

        return -1
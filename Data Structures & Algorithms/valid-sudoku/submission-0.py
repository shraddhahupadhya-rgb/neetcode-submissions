

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create Hash Sets using defaultdict to track seen numbers
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)  # Key: (r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Skip empty cells
                if val == ".":
                    continue
                
                # Compute box coordinates
                box_key = (r // 3, c // 3)

                # Check for duplicates in current row, column, or sub-box
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in squares[box_key]):
                    return False

                # Store value in sets
                rows[r].add(val)
                cols[c].add(val)
                squares[box_key].add(val)

        return True
        
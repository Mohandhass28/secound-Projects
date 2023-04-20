class Solution(object):
    boad = None
    Dp = None

    def exist(self, board, word):
        if self.boad == None:
            self.boad = board
        if self.Dp == None:
            self.Dp = [[False for _ in range(len(self.boad[0]))] for _ in range(len(self.boad))]
        rowlen = len(board)-1
        collen = len(board[0])-1
        roco = self.findword(word)
        if roco == False:
            return False
        ro,co = roco
        def Dfs(ind, row, col, word):
            if ind == len(word):
                return True
            if col > collen:
                return False
            elif row > rowlen:
                return False
            elif col < 0:
                return False
            elif row < 0:
                return False
            elif board[row][col] != word[ind]:
                return False
            self.boad[row][col] = '#'
            ans = (
                Dfs(ind + 1, row + 1, col, word) or
                Dfs(ind + 1, row - 1, col, word) or
                Dfs(ind + 1, row, col + 1, word) or
                Dfs(ind + 1, row, col - 1, word)
            )
            self.boad[row][col] = word[ind]
            return ans
        if Dfs(0,ro,co,word):
            return True
        return self.exist(self.boad,word)

    def findword(self, word):
        Dp = self.Dp
        boad = self.boad
        for i in range(len(boad)):
            for j in range(len(boad[i])):
                if boad[i][j] == word[0] and Dp[i][j] == False:
                    Dp[i][j] = True
                    return (i, j)
        return False

# board = [["A","B","C","E"],
#          ["S","F","C","S"],
#          ["A","D","E","E"]]
# word = "SEE"
# board = [["A","B","C","E"],
#          ["S","F","C","S"],
#          ["A","D","E","E"]]
# word = "ABCCED"
# board = [["C","A","A"],
#          ["A","A","A"],
#          ["B","C","D"]]
# word = "AAB"
board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word = "ABCB"
s = Solution()
p = s.exist(board,word)
print(p)
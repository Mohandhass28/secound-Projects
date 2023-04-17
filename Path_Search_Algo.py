class path(object):
    def __init__(self,maze):
        self.maze = maze
    def find_path(self):
        maze = self.maze
        end = 'x'
        qoueu = []
        star_pos = self.find_start()
        path = []
        path = path + [star_pos]
        qoueu.append((star_pos,path))
        visit = set()
        while len(qoueu) != 0:
            po = qoueu.pop(0)
            rowcol,path = po
            r,c = rowcol
            if maze[r][c] == end:
                return self.printpath(path)
            naighbours = self.getnaibo(rowcol)
            for naib in naighbours:
                if naib in visit:
                    continue
                r,c = naib
                if maze[r][c] == '#':
                    continue
                visit.add(naib)
                pathn = path + [naib]
                qoueu.append((naib,pathn))

    def find_start(self):
        star = 'O'
        maz = self.maze
        for i in range(len(maz)):
            for j in range(len(maz[i])):
                if maz[i][j] == star:
                    return (i,j)
    def getnaibo(self,rowcol):
        naighbour = []
        maze = self.maze
        row,col = rowcol
        if row+1 < len(maze):
            naighbour.append((row+1,col))
        if row > 0 :
            naighbour.append((row-1,col))
        if col > 0 :
            naighbour.append((row,col-1))
        if col+1 < len(maze[0]):
            naighbour.append((row,col+1))

        return naighbour

    def printpath(self,path):

        maxe = self.maze
        for r,c in path:
            maxe[r][c] = '@'
        return maxe


maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "x", "#"]
]
if __name__ == "__main__":
    s = path(maze).find_path()
    print(s)


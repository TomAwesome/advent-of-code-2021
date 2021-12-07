from io import TextIOWrapper

class space:
    value:int = 0
    marked:bool = False
    def __init__(self, value:int):
        self.value = value
    def Hit(self):
        self.marked = True
    def __repr__(self) -> str:
        return f'{self.value}:{self.marked}'
        
class bingoBoard:
    board:list[list[space]]
    lastNumberHit:int
    bingo:bool = False
    def __init__(self, board:list[list[space]]) -> None:
        self.board = board

    def checkNumber(self, number:int) -> bool:
        hit:bool = False
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j].value == number:
                    self.board[i][j].Hit()
                    hit = True
                    self.lastNumberHit = number
        return hit

    def hasBingo(self) -> bool:
        for i in range(5):
            bingo:bool = True
            for j in range(5):
                bingo = self.board[i][j].marked and bingo
            if bingo:
                self.bingo = True
                return True
        if bingo :
            self.bingo = True
            return True

        for i in range(5):
            bingo:bool = True
            for j in range(5):
                bingo = self.board[j][i].marked and bingo
            if bingo:
                self.bingo = True
                return True
        
        self.bingo = bingo
        return bingo

    def computeScore(self) -> int:
        notMarkedSum:int = 0
        for i in range(5):
            for j in range(5):
                if not self.board[i][j].marked:
                    notMarkedSum += self.board[i][j].value

        print(f'{notMarkedSum}*{self.lastNumberHit}')
        return notMarkedSum * self.lastNumberHit
                

    def __repr__(self) -> str:
        return self.board.__str__()
        

def buildBoards(reader: TextIOWrapper) -> list[bingoBoard]: 
    reader.readline()
    boards:list[bingoBoard] = []
    boardInputs = list(map(lambda x: x.replace('\n', ''), reader.readlines()))

    board:list[space] = []
    for line in boardInputs:
        if line == '':
            boards.append(bingoBoard(board))
            board = []
            continue
        spaces = list(map(lambda x: space(int(x.strip())), filter(str.strip, line.split())))
        board.append(spaces)

    boards.append(bingoBoard(board))
    return boards

fileStream = open("day4input.txt", 'r')

numbers = list(map(lambda x: int(x), fileStream.readline().replace('\n', '').split(','))) 

boards = buildBoards(fileStream)
losingboard:bingoBoard = None
winningOrder:list[bingoBoard] = []
for number in numbers:
    for board in boards:
        if not board.bingo and board.checkNumber(number) and board.hasBingo():
            winningOrder.append(board)

losingboard = winningOrder.pop()
score = losingboard.computeScore()
print(score)
print(losingboard)
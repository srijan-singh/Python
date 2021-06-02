def chessBoardMaker(dim = 8):
    chessBoard = []
    for i in range(dim):
        for j in range(dim):
            chessBoard.append([i,j])
    return chessBoard

def printBoard(chessBoard):
    print("\n")
    for i in range(len(chessBoard)):
        if (i%8==0 and i!=0):
            print("\n")
        print(chessBoard[i], end=" ")
    print("\n")

def knightMoves(x,y):

    movesList = [0,0,0,0,0,0,0,0]

    movesList[0] = [int(x+1),int(y+2)]
    movesList[1] = [int(x-1),int(y+2)]
    movesList[2] = [int(x-1),int(y-2)]
    movesList[3] = [int(x+1),int(y-2)]
    movesList[4] = [int(x+2),int(y+1)]
    movesList[5] = [int(x-2),int(y+1)]
    movesList[6] = [int(x-2),int(y-1)]
    movesList[7] = [int(x+2),int(y-1)]

    movesList.sort()

    return movesList

def moveDisplay(x,y, chessBoard=chessBoardMaker(), source="Knight", move="CanMove"):
    movesList = knightMoves(x,y)

    for i in range(len(chessBoard)):
        
        for moves in movesList:
            
            if chessBoard[i] == [x,y]:
                chessBoard[i] = source

            if chessBoard[i] == moves:
                chessBoard[i] = move
    
    return chessBoard

source = moveDisplay(0,0, chessBoardMaker(), "Source")
destination = moveDisplay(4,2,source,"Dstn") 
printBoard(destination)




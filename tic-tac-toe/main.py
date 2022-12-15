board = [[' ',' ',' ']
        ,[' ',' ',' ']
        ,[' ',' ',' ']]

turn = True
winner = None

def displayboard():
  for i in range(3):
    print(board[i][0]+"|"+board[i][1]+"|"+board[i][2])

def getPlayer(turn):
  if turn:
    return "X"
  return "O"

while True:
  if turn:
    print("X's turn")
    row = int(input("Enter Row (0-2): "))
    col = int(input("Enter Column (0-2): "))
    if board[row][col] != " ":
      print("Space occupied.")
      continue
    board[row][col] = "X"
    displayboard()
  
  else:
    print("O's turn")
    row = int(input("Enter Row (0-2): "))
    col = int(input("Enter Column (0-2): "))
    if board[row][col] != " ":
      print("Space occupied.")
      continue
    board[row][col] = "O"
    
    displayboard()
  # Check Winner.

  # Horizontal
  for i in range(3):
    if board[i][0] == board[i][1] == board[i][2] != ' ':
      print(getPlayer(turn) + " is the winner!")
      winner = turn
      break

  #Vertical
  for i in range(3):
    if board[0][i] == board[1][i] == board[2][i] != ' ':
      print(getPlayer(turn) + " is the winner!")
      winner = turn
      break

  # Diagonal 
  if board[0][0] == board[1][1] == board[2][2] != ' ':
    print(getPlayer(turn) + " is the winner!")
    winner = turn
    
  if board[0][1] == board[1][1] == board[2][0] != ' ':
    print(getPlayer(turn) + " is the winner!")
    winner = turn

  if winner is not None:
    winner = None
    board = [[' ',' ',' ']
          ,[' ',' ',' ']
          ,[' ',' ',' ']]
    displayboard()
  else:
    # Check tie
    tie = True
    for i in range(3):
      for j in range(3):
        if board[i][j] == ' ':
          tie = False
    if tie:
      board = [[' ',' ',' ']
          ,[' ',' ',' ']
          ,[' ',' ',' ']]
      print("Tie!")
      displayboard()
    else:
      turn = not turn
    
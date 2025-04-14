extends Node2D

var NEW_BOARD:Array = [
	"-", "-", "-",
	"-", "-", "-",
	"-", "-", "-"
]

var board:Array = [
	"-", "-", "-",
	"-", "-", "-",
	"-", "-", "-"
]

var WINNING_COMBINATIONS = [
	[0,1,2], [3,4,5], [6,7,8],
	[0,3,6], [1,4,7], [2,5,8],
	[0,4,8], [2,4,6]
]


func pop_icon(pos:int) -> void:
	#pops icon for mobs, etc.
	board.insert(pos, "-")

func clear() -> void:
	#clears the grid for new levels but keeps score
	board = NEW_BOARD.duplicate(true)

func new_game() -> void:
	#resets everthing to start a new game
	clear() #clears board
	#clear score
	pass

func win(icons:String) -> void:
	var squares:Array = []
	
	for dummy_index in range(len(board)): #Done
		#creates the squares array
		if board[dummy_index] == icons:
			squares.append(dummy_index)

	for combo in WINNING_COMBINATIONS: #one pretty mych a subset
		if combo[0] in squares and combo[1] in squares and combo[2] in squares:
			#Wins
			clear()
			get_tree().call_group("Icons", "remove_icon")
		
	print(squares)


####################################################################

var mario = preload("res://assets/Circle.png")
var wario = preload("res://assets/X.png")

var icon:Texture = null
var player_icon:String = ""

func coin_flip() -> void: #not done
	#put this in ready func
	#change icon
	#puts sound of mario or wario
	#put timmer to start mob
	pass
	
func start() -> void: #not done
	#put in ready func
	#start animation
	#start mob
	pass

func end_turn(pos:int) -> void:
	#changes and sets icon, checks game if won
	if icon == mario:
		icon = wario
		player_icon = "x"
	else:
		icon = mario
		player_icon = "o"
	
	board[pos] = player_icon #set player_icon in board
	
	#debuging
	print("")
	print(board.slice(0,2))
	print(board.slice(3,5))
	print(board.slice(6,8))
	
	win(player_icon) #checks if game won
	
func _ready():
	pass

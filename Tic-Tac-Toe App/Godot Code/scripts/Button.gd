extends Button


func remove_icon() -> void: #only time use is for mobs or items
	#add sound and animation
	self.icon = null #removes button icon
	Board.pop_icon(int(self.name)) #pops icon from grid


func _on_Button_pressed():
	if self.icon != null:
		return
	
	#add sound
	Board.end_turn(int(self.name))
	set_button_icon(Board.icon) #sets icon
	pass

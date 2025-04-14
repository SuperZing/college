extends TouchScreenButton



func remove_icon() -> void: #only time use is for mobs or items
	#add sound and animation
	self.normal = null #removes button icon
	#Board.pop_icon(int(self.name)) #pops icon from grid


#func _on_Button_pressed():
#	if self.icon != null:
#		return
#
#	#add sound
#	Board.end_turn(int(self.name))
#	set_button_icon(Board.icon) #sets icon
#	pass
#

func _on_touch_pressed():
	if self.normal != null: #will not reicon an existing icon
		return

	#add sound
	Board.end_turn(int(self.name))
	set_texture(Board.icon)
	#set_button_icon(Board.icon) #sets icon
	pass

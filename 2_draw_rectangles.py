import arcade
arcade.open_window(600,600,'Rectangle')   #opens a window with required width and length
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
arcade.start_render()     #Get Ready to Draw
arcade.draw_lrtb_rectangle_filled(5,300,590,370,arcade.color.BITTER_LIME)    #LEFT,RIGHT,TOP,BOTTOM,The numbers are in Pixels.
arcade.finish_render()
arcade.run()

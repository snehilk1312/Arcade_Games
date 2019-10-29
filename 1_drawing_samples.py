import arcade
arcade.open_window(600,600,"Drawing Example")
# Set the background color
arcade.set_background_color(arcade.color.AQUAMARINE)
arcade.set_background_color((189, 55, 180))
# Get ready to draw
arcade.start_render()
# Finish drawing
arcade.finish_render()
# Keep the window up until someone closes it.
arcade.run()

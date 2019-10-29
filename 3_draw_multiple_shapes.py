import arcade
arcade.open_window(600,600,"Multiple Images")
arcade.set_background_color(arcade.color.SAPPHIRE_BLUE)
arcade.start_render()
#arcade.draw_arc_filled(center_x: float, center_y: float, width: float, height: float,
# color: Union[Tuple[int, int, int], List[int], Tuple[int, int, int, int]], start_angle: float,
# end_angle: float, tilt_angle: float = 0, num_segments: int = 128)
arcade.draw_arc_filled(300,300,80,80,(123,2,34),0,60)
arcade.draw_arc_outline(150,300,80,80,(123,2,34),0,60)
#arcade.draw_polygon_outline(point_list: Sequence[Union[Tuple[float, float]
#, List[float]]], color: Union[Tuple[int, int, int], List[int]
#, Tuple[int, int, int, int]], line_width: float = 1)
arcade.draw_polygon_outline([[0,0],[100,0],[90,90],[123,45],[80,60]],(123,2,34), 5)
arcade.finish_render()
arcade.run()

'''
Related to lab 2
'''
import arcade
arcade.open_window(600,600,'Lab2')
arcade.set_background_color(arcade.color.BABY_BLUE)
arcade.start_render()
arcade.draw_lrtb_rectangle_filled(0,600,200,0,arcade.color.GREEN)
arcade.draw_lrtb_rectangle_filled(390,510,135,80,arcade.color.GRAY)
arcade.draw_lrtb_rectangle_filled(410,490,110,80,arcade.color.BLACK)
arcade.draw_lrtb_rectangle_filled(430,440,180,135,arcade.color.BLACK)
arcade.draw_circle_filled(350,100,13,(255, 0, 0),128)
arcade.draw_circle_outline(350,100,26,(255,255,255),30,128)
arcade.draw_circle_outline(350,100,35,(90,90,90),9,128)
arcade.draw_circle_outline(350,100,40,(0,0,0),5,128)
arcade.draw_circle_filled(500,80,7,(255, 0, 0),128)
arcade.draw_circle_outline(500,80,12,(255,255,255),12,128)
arcade.draw_circle_outline(500,80,17,(90,90,90),5,128)
arcade.draw_circle_outline(500,80,20,(0,0,0),3,128)
arcade.draw_lrtb_rectangle_filled(20,280,215,180,arcade.color.MINT_CREAM)
arcade.draw_lrtb_rectangle_filled(20,280,350,215,arcade.color.OU_CRIMSON_RED)
arcade.draw_polygon_filled([[10,350],[84,450],[149,470],[214,450],[290,350]],arcade.color.OU_CRIMSON_RED)
arcade.draw_lrtb_rectangle_filled(110,190,280,190,arcade.color.DARK_BROWN)
arcade.draw_line(90,280,210,280,arcade.color.WHITE,4)
arcade.draw_lrtb_rectangle_outline(138,162,324,284,arcade.color.WHITE,4)
arcade.draw_lrtb_rectangle_filled(35,59,283,257,(255,255,255))
arcade.draw_lrtb_rectangle_filled(38,56,280,260,(0,0,0))
arcade.draw_lrtb_rectangle_filled(241,265,283,257,(255,255,255))
arcade.draw_lrtb_rectangle_filled(244,262,280,260,(0,0,0))
arcade.finish_render()
arcade.run()
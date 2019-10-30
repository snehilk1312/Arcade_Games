import arcade as ar
ar.open_window(600,600,'SNOWMAN')
ar.set_background_color(ar.color.BLUE)
ar.start_render()
ar.draw_lrtb_rectangle_filled(0,600,200,0,ar.color.BABY_BLUE)
col_1=ar.color.WHITE
col_2=ar.color.BLACK
def gola(x,y,r,rang):
    ar.draw_circle_filled(x,y,r,rang)
gola(250,200,60,col_1)
gola(250,287,50,col_1)
gola(250,360,40,col_1)
gola(235,370,5,col_2)
gola(265,370,5,col_2)
ar.finish_render()
ar.run()

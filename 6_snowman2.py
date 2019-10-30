import arcade as ar


def draw_grass():
    ar.draw_lrtb_rectangle_filled(0, 800, 200, 0, ar.color.BABY_BLUE)


def draw_snowperson(x, y):
    col_1 = ar.color.WHITE
    col_2 = ar.color.BLACK
    gola(250 + x, 200 + y, 60, col_1)
    gola(250 + x, 287 + y, 50, col_1)
    gola(250 + x, 360 + y, 40, col_1)
    gola(235 + x, 370 + y, 5, col_2)
    gola(265 + x, 370 + y, 5, col_2)


def gola(x, y, r, rang):
    ar.draw_circle_filled(x, y, r, rang)


def on_draw(delta_time):
    ar.start_render()
    draw_grass()
    draw_snowperson(on_draw.snowperson1_x, 0)
    # draw_snowperson(150, 100)
    draw_snowperson(on_draw.snowperson2_x, 100)
    on_draw.snowperson1_x += 2
    on_draw.snowperson2_x += 1


'''
These are doubts and explanations related to basic scope resolution concepts

def on_draw(delta_time):
    ar.start_render()
    draw_grass()
    draw_snowperson(on_draw.snowperson1_x, 0)
    # draw_snowperson(150, 100)
    draw_snowperson(on_draw.snowperson2_x, 100)
    on_draw.snowperson1_x += 2
    on_draw.snowperson2_x += 1
    

on_draw.snowperson1_x = 0 # if we don't use on_draw along with snowperson1_x,it will be of main function
on_draw.snowperson2_x = 150 # so,then it can be used in function on_draw(delta_time)
#but there would be a limitation. Although we don't have to use on_draw. in line 36 and 38,but then while incrementing
#on line we will getting an error,since snowperson1_x and snowperson2_x will be of main function and not of 
#on_draw function


REFERENCE EXAMPLE:

def rough():
    x=2
    print(x)
    print(z)
    # z=z+1
    # print(z)

def new(y):
    print(new.x)
    print('lola')
new.x=3
x=1
y=rough
#print(type(y))
new(y)
z=1
rough()

'''

on_draw.snowperson1_x = 0
on_draw.snowperson2_x = 150
ar.open_window(800, 600, 'SNOWMAN')
ar.set_background_color(ar.color.BLUE)
# Call on_draw every 60th of a second.
# arcade.schedule(function_pointer: Callable, interval: numbers.Number)[source]
# Schedule a function to be automatically called every interval seconds.
ar.schedule(on_draw, 1/60)
ar.run()
# draw_grass()
# draw_snowperson(150,100)
# draw_snowperson(0,0)
# ar.finish_render()

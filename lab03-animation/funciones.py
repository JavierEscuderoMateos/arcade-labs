import arcade
def draw_amogus(x, y, color):
    # cabeza
    arcade.draw_circle_filled(400+x, 500+y, 100, color)
    arcade.draw_circle_outline(400+x, 500+y, 100, arcade.color.BLACK)
    # cuerpo
    arcade.draw_rectangle_filled(400+x, 400+y, 200, 200, color)
    arcade.draw_rectangle_outline(400+x, 400+y, 200, 200, arcade.color.BLACK)
    arcade.draw_rectangle_filled(400+x, 500+y, 200, 10, color)
    # visor
    arcade.draw_rectangle_filled(475+x, 475+y, 150, 80, arcade.color.CYAN)
    arcade.draw_rectangle_outline(475+x, 475+y, 150, 80, arcade.color.BLACK)
    # mochila
    arcade.draw_rectangle_filled(275+x, 425+y, 50, 150, color)
    arcade.draw_rectangle_outline(275+x, 425+y, 50, 150, arcade.color.BLACK)
    # pies
    arcade.draw_circle_filled(340+x, 300+y, 40, color)
    arcade.draw_circle_outline(340+x, 300+y, 40, arcade.color.BLACK)

    arcade.draw_circle_filled(460+x, 300+y, 40, color)
    arcade.draw_circle_outline(460+x, 300+y, 40, arcade.color.BLACK)

    arcade.draw_rectangle_filled(400+x, 320+y, 198, 39, color)

def draw_grass():
    arcade.draw_rectangle_filled(900,100,300, arcade.color.GREEN)



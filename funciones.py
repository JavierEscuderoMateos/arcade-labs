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
    arcade.draw_rectangle_filled(900, 100, 300, 100, arcade.color.GREEN)


def draw_tree(x, y, type):
    if type == "oak":
        arcade.draw_rectangle_filled(x, y, 10, 50, arcade.color.WOOD_BROWN)
        arcade.draw_circle_filled(x, y+40, 20, arcade.color.APPLE_GREEN)


def draw_background(code):
    if code == "oak_forest":
        arcade.draw_rectangle_filled(500, 250, 1000, 500,arcade.color.SKY_BLUE)
        arcade.draw_rectangle_filled(500, 100, 1000, 200, arcade.color.FOREST_GREEN)
        draw_tree(40, 80, "oak")
        draw_tree(383, 80, "oak")
        draw_tree(200, 120, "oak")
        draw_tree(120, 120, "oak")
        draw_tree(434, 74, "oak")
        draw_tree(92, 200, "oak")
        draw_tree(961, 220, "oak")
        draw_tree(145, 81, "oak")
        draw_tree(836, 17, "oak")
        draw_tree(476, 128, "oak")
        draw_tree(275, 18, "oak")
        draw_tree(120, 120, "oak")

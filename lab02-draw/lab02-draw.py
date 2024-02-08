import arcade

arcade.open_window(800, 600, "Amogus")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

#cabeza
arcade.draw_circle_filled(400, 500, 100, arcade.color.RED)
arcade.draw_circle_outline(400, 500, 100, arcade.color.BLACK)
#cuerpo
arcade.draw_rectangle_filled(400, 400, 200, 200, arcade.color.RED)
arcade.draw_rectangle_outline(400, 400, 200, 200, arcade.color.BLACK)
arcade.draw_rectangle_filled(400, 500, 200, 10, arcade.color.RED)
#visor
arcade.draw_rectangle_filled(475, 475, 150, 80, arcade.color.CYAN)
arcade.draw_rectangle_outline(475, 475, 150, 80, arcade.color.BLACK)
#mochila
arcade.draw_rectangle_filled(275, 425, 50, 150, arcade.color.RED)
arcade.draw_rectangle_outline(275, 425, 50, 150, arcade.color.BLACK)
#pies
arcade.draw_circle_filled(340, 300, 40, arcade.color.RED)
arcade.draw_circle_outline(340, 300, 40, arcade.color.BLACK)

arcade.draw_circle_filled(460, 300, 40, arcade.color.RED)
arcade.draw_circle_outline(460, 300, 40, arcade.color.BLACK)

arcade.draw_rectangle_filled(400, 320, 198, 39, arcade.color.RED)

arcade.finish_render()
arcade.run()
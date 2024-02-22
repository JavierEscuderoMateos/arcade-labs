import arcade
import funciones

arcade.open_window(1000, 500, "Game")
arcade.start_render()


funciones.draw_background("oak_forest")


arcade.finish_render()
arcade.run()
import arcade
import funciones

arcade.open_window(1920, 1080, "Amogus")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()


funciones.draw_amogus(-60,90,arcade.color.PINK)
funciones.draw_amogus(250,90,arcade.color.YELLOW)
funciones.draw_amogus(600,90,arcade.color.AIR_SUPERIORITY_BLUE)

arcade.finish_render()
arcade.run()
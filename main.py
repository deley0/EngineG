import arcade
import arcade.gui
import math
from package.paraButton import *
from package.cam import *

resolution = (900, 900)


def rect(x, y, sx, sy, color):  # Более удобное рисование квадратов, sx = size x
    arcade.draw_rectangle_filled(x, y, sx, sy, color=(int(color[0]), int(color[1]), int(color[2])))


class MyGame(arcade.Window):
    """ Главный класс приложения. """

    def __init__(self, width, height):
        super().__init__(width, height)
        self.manager = arcade.gui.UIManager()

        self.manager.enable()
        self.v_box = arcade.gui.UIBoxLayout()
        self.but = ParaButton(x = 900/2-200, y = 900/2-200, width=200, height=100, text="Quit")
        self.manager.add(self.but)



    def setup(self):
        global cam
        global resolution
        cam = Cam(resolution = resolution)
        self.t = 0

    def on_key_press(self, symbol, modifiers):
        global cam
        if modifiers and symbol == 119:
            cam.scale -= 0.1

        elif symbol == 115:
            cam.scale += 0.1


        cam.position.x = 100
        cam.position.y = 100
        cam.use()
    def on_draw(self):
        """ Отрендерить этот экран. """
        global h
        global camPoint1
        global camPoint2
        self.clear()
        cam.zoom2()

        arcade.start_render()
        self.but.draw()

        self.t += 1

    def on_mouse_motion(self, x, y, dx, dy):
        pass

    def update(self, delta_time):
        pass



def main():
    global resolution
    game = MyGame(resolution[0], resolution[1])
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()

import math
import arcade.gui
from arcade.gui.property import bind

def para(x, y, sx, sy, color1, color2, sd):
    arcade.draw_polygon_filled(((x, y), (x + sd, y + sy), (x + sx + sd, y + sy), (x + sx, y), (x, y), (x + sd, y + sy)),
                               color1)
    arcade.draw_polygon_outline(
        ((x, y), (x + sd, y + sy), (x + sx + sd, y + sy), (x + sx, y), (x, y), (x + sd, y + sy)), color2, line_width=10)

class ParaButton(arcade.gui.UIFlatButton):
    def __init__(
        self,
        *,
        x: float = 0,
        y: float = 0,
        width: float,
        height: float,
        color1: list = [145, 145, 145],
        color2: list = [56, 56, 56],
        size_hint=None,
        size_hint_min=None,
        size_hint_max=None,
        **kwargs,
    ):
        super().__init__(
            x=x,
            y=y,
            width=width,
            height=height,
            size_hint=size_hint,
            size_hint_min=size_hint_min,
            size_hint_max=size_hint_max,
            **kwargs,
        )
        self.register_event_type("on_click")

        bind(self, "pressed", self.trigger_render)
        bind(self, "hovered", self.trigger_render)
        bind(self, "disabled", self.trigger_render)
        self.anim = math.pi*10
        self.blink = 0
        self.color1 = color1
        self.color2 = color2

    def on_click(self, event: arcade.gui.UIOnClickEvent):
        pass
    def on_update(self, dt):

        if self.pressed:
            self.blink = 50
        if not self.hovered:
            self.anim -= 3
        else:
            self.anim += 3
        if self.anim < 0:
            self.anim = 0
        if self.anim > math.pi*10:
            self.anim = math.pi*10
        if self.blink > 0:
            self.blink-=3
    def draw(self):
        para(self.x, self.y, self.width, self.height,
             (self.color1[0] - self.blink, self.color1[1] - self.blink, self.color1[2] - self.blink),
             (self.color2[0] + int(self.anim * 1.5), self.color2[1] + int(self.anim * 2.5), self.color2[2] + int(self.anim * 2.5)),
             math.cos(self.anim / 20) * (self.width/6))
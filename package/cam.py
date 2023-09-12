from pyglet.math import Mat4, Vec2, Vec3
from typing import Optional, Tuple, Union, List, TYPE_CHECKING
import arcade.camera

FourIntTuple = Tuple[int, int, int, int]
FourFloatTuple = Tuple[float, float, float, float]

class Cam(arcade.Camera):
    def __init__(
            self, *,
            viewport: Optional[FourIntTuple] = None,
            projection: Optional[FourFloatTuple] = None,
            zoom: float = 1.0,
            resolution: list = [900,900],
            rotation: float = 0.0,
            anchor: Optional[Tuple[float, float]] = None,
            window: Optional["arcade.Window"] = None,
    ):

        # Zoom
        self._zoom: float = zoom

        # Near and Far
        self._near: int = -1
        self._far: int = 1

        # Shake
        self.shake_velocity: Vec2 = Vec2()
        self.shake_offset: Vec2 = Vec2()
        self.shake_speed: float = 0.0
        self.shake_damping: float = 0.0
        self.shaking: bool = False

        # Call init from superclass here, previous attributes are needed before this call
        super().__init__(viewport=viewport, projection=projection, window=window)

        # Rotation
        self._rotation: float = rotation  # in degrees
        self._anchor: Optional[Tuple[float, float]] = anchor  # (x, y) to anchor the camera rotation

        # Matrixes
        # Rotation matrix holds the matrix used to compute the rotation set in window.ctx.view_matrix_2d
        self._rotation_matrix: Mat4 = Mat4()

        # Init matrixes
        # This will precompute the rotaion matrix
        self._set_rotation_matrix()
        self.scale = 1
        self.size=50
        self.ratio = resolution[0]/resolution[1]
        self.resolution = resolution

    def zoom2(self):
        self.set_viewport((self.position.x+(-self.size * self.scale*self.ratio)+self.resolution[0]/4, self.position.y+(-self.size * self.scale)+self.resolution[1]/4, self.position.x+self.size * self.scale*self.ratio*2+self.resolution[0]/4, self.position.y+self.size * self.scale*2+self.resolution[1]/4))


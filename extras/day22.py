from manim import *


# class ExamplePrism(ThreeDScene):
#     def construct(self):
#         self.set_camera_orientation(phi=90 * DEGREES, theta=150 * DEGREES)
#         prismSmall = Prism(dimensions=[1, 2, 3]).rotate(PI / 2)
#         prismLarge = Prism(dimensions=[1.5, 3, 4.5]).move_to([2, 0, 0])
#         # self.add(prismLarge)
#         p0 = Prism(dimensions=[3, 6, 49]).move_to([34, 33, -30]).scale(0.0001)
#         p1 = Prism(dimensions=[3, 29, 4]).move_to([34, 4, 0]).scale(0.0001)
#         # self.add(prism0)
#         # self.add(prismSmall, prismLarge)
#         # prism0 = Prism(dimensions=[3, 6, 18]).move_to([0, 0, 0])
#         # prism1 = Prism(dimensions=[3, 2, 4]).move_to([1, 0, 0]).scale(0.01)
#         self.add(p0, p1)

#         # self.play(Create(prismSmall), run_time=1)
#         # self.play(Create(prismLarge), run_time=1)
#         # self.wait()


class ExamplePrism(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=150 * DEGREES)
        # prismSmall = Prism(dimensions=[1, 2, 3]).rotate(PI / 2)
        # prismLarge = Prism(dimensions=[1.5, 3, 4.5]).move_to([2, 0, 0])
        # self.add(prismLarge)
        p0 = Prism(dimensions=[3, 6, 49]).move_to([34, 33, -30]).scale(0.0001)
        p1 = Prism(dimensions=[3, 29, 4]).move_to([34, 4, 0]).scale(0.0001)
        self.add(p0, p1)

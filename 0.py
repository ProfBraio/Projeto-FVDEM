from manim import *

class parte0(Scene):
    def construct(self):
        title = Tex(r'Relacionando Trigonometria à Proporção Áurea:\\Um curta no Manim').shift(UP*2)
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#343434"
        ds_m = MathTex(r"\mathbb{M}", fill_color=logo_black).scale(7)
        ds_m.shift(2.25 * LEFT + 1.5 * UP)
        circle = Circle(color=logo_green, fill_opacity=1).shift(LEFT)
        square = Square(color=logo_blue, fill_opacity=1).shift(UP)
        triangle = Triangle(color=logo_red, fill_opacity=1).shift(RIGHT)
        logo = VGroup(triangle, square, circle, ds_m)  # order matters
        logo.next_to(title, DOWN)

        self.play(Write(title))
        self.wait()
        self.play(FadeIn(logo, lag_ratio = 0))
        self.wait(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()
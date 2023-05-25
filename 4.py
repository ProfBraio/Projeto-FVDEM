from manim import *

class parte4(Scene):
    def construct(self):
        lei = MathTex(r"b^2+a^2-2ab\cdot cos(\alpha)=c^2",
                       color = RED).scale(.75)
        Lei = Tex("Lei dos Cossenos", color = GREEN)
        LEI = VGroup(Lei, lei).arrange(DOWN).scale(.5).to_corner(UL)
        af0 = MathTex(r"sen(\alpha+\beta)=cos(\alpha)sen(\beta)+cos(\beta)sen(\alpha)", color = RED).scale(.55).shift(UP*2+RIGHT*.5)
        af1 = MathTex(r"cos(\alpha+\beta)=cos(\alpha)cos(\beta)-sen(\alpha)sen(\beta)", color = RED).scale(.55).next_to(af0, DOWN)
        af2 = Tex("Seno e Cosseno da Soma de Arcos", color = GREEN).next_to(af0, UP).scale(.8)
        SOMA = VGroup(af0,af1,af2).scale(.5).next_to(LEI, DOWN)
        

        prop0 = Tex("Proporção Áurea", color = GREEN)
        prop1 = Tex(r"Duas medidas \emph{a} e \emph{b} estão sob a proporção áurea se:").shift(UP).scale(.75)
        prop2 = MathTex(r"\frac{a+b}{a}=\frac{a}{b}", color = RED).scale(.75)
        prop3 = MathTex(r"\frac{a+b}{a}","=",r"\frac{a}{b}","="r"\varphi", color = RED).scale(.75)
        prop4 = MathTex(r"a=b\varphi", color = RED).next_to(prop3, DOWN).scale(.75)
        prop5 = MathTex(r"\frac{b+b\varphi}{b\varphi}=\frac{b\varphi}{b}", color = RED).next_to(prop4, DOWN).scale(.75)
        prop6 = MathTex(r"\frac{1+\varphi}{\varphi}=\varphi", color = RED).next_to(prop4, DOWN).scale(.75)

        xy = NumberPlane()

        Vertices = []

        for i in range(5):
            k = xy.c2p(2*np.cos(2*PI*i/5+PI/2-2*PI/5), 2*np.sin(2*PI*i/5+PI/2-2*PI/5))
            Vertices.append(k)
        
        pentagono = Polygon(*Vertices, color = PURE_GREEN, stroke_width = 1)

        a0 = MathTex("a", color = PURE_GREEN).scale(.75).next_to(Line(Vertices[0], Vertices[1]), RIGHT, buff = -.8)
        a1 = MathTex("a", color = PURE_GREEN).scale(.75).next_to(Line(Vertices[1], Vertices[2]), LEFT, buff = -.8)
        a2 = MathTex("a", color = PURE_GREEN).scale(.75).next_to(Line(Vertices[2], Vertices[3]), LEFT, buff = -.3)
        a3 = MathTex("a", color = PURE_GREEN).scale(.75).next_to(Line(Vertices[3], Vertices[4]), DOWN)
        a4 = MathTex("a", color = PURE_GREEN).scale(.75).next_to(Line(Vertices[4], Vertices[0]), RIGHT, buff = -.3)

        pentagrama = VGroup()
        for i in range(5):
            k = Line(Vertices[i], Vertices[(i+2)%5], stroke_width = 1, color = PURE_GREEN)
            pentagrama.add(k)

        ang0 = Angle(Line(Vertices[1], Vertices[3]), Line(Vertices[1], Vertices[4]),
                     color = PURE_RED, radius = .5, stroke_width = 1.5)
        ang1 = Angle(Line(Vertices[3], Vertices[1]), Line(Vertices[3], Vertices[2]),
                     color = PURE_RED, radius = .5, stroke_width = 1.5)
        Redang = MathTex(r"\angle",r"=36^{\circ}").to_corner(UR)
        Redang[0].set(color = PURE_RED)

        ang2 = Angle(Line(Vertices[3], Vertices[4]), Line(Vertices[3], Vertices[1]),
                     color = DARK_BLUE, radius = .5, stroke_width = 1.5)
        ang3 = Angle(Line(Vertices[4], Vertices[1]), Line(Vertices[4], Vertices[3]),
                     color = DARK_BLUE, radius = .5, stroke_width = 1.5)
        ang4 = Angle(Line(Vertices[2], Vertices[3]), Line(Vertices[2], Vertices[0]),
                     color = DARK_BLUE, radius = .5, stroke_width = 1.5)
        ang5 = Angle(Line(xy.c2p(-.45,.62),Vertices[2]), Line(xy.c2p(-.45,.62), Vertices[3]),
                     color = DARK_BLUE, radius = .5, stroke_width = 1.5)
        
        Bluang = MathTex(r"\angle",r"=72^{\circ}").next_to(Redang, DOWN)
        Bluang[0].set(color = DARK_BLUE)

        tri0 = Polygon(Vertices[1], Vertices[3], Vertices[4], color = RED, fill_opacity = .75)
        Tri0 = VGroup()
        Tri0.add(tri0, ang0.copy(), ang2.copy(), ang3.copy(), a3.copy())
        Tri0.add(MathTex("a+b").rotate(2*PI/5).scale(.75).next_to(Tri0, LEFT, buff = -.3))
        tri1 = Polygon(Vertices[2], Vertices[3], xy.c2p(-.45,.62), color = BLUE, fill_opacity = .75)
        Tri1 = VGroup()
        Tri1.add(tri1, ang1.copy(), ang4.copy(), ang5.copy(), a2.copy())
        Tri1.add(MathTex("b").scale(.75).next_to(Tri1, UP))

        eq0 = MathTex(r"\frac{a+b}{a}",r"=\frac{a}{b}").scale(.75).next_to(Bluang, DOWN)
        eq1 = MathTex(r"a=b\varphi").scale(.75).next_to(eq0, DOWN)
        
        conta0 = MathTex(r"(b\varphi)^2=b^2+(b\varphi)^2-2b\cdot b\varphi \cdot cos(72^{\circ})").scale(.75).shift(UP*3+RIGHT)
        conta1 = MathTex(r"\Rightarrow cos(72^{\circ})=\frac{1}{2}\cdot\frac{1}{\varphi}").scale(.75).next_to(conta0, DOWN)
        conta2 = MathTex(r"\Rightarrow cos(72^{\circ})=\frac{1}{2}\cdot(\varphi-1)").scale(.75).next_to(conta1, DOWN)
        conta3 = MathTex(r"\Rightarrow 2cos^2(36^{\circ})-1=\frac{1}{2}\cdot(\varphi-1)").scale(.75).next_to(conta2, DOWN)
        conta4 = MathTex(r"\Rightarrow cos^2(36^{\circ})=\frac{\varphi+1}{4}").scale(.75).next_to(conta3, DOWN)
        conta5 = MathTex(r"\Rightarrow cos^2(36^{\circ})=\frac{\varphi^2}{4}").scale(.75).next_to(conta4, DOWN)
        conta6 = MathTex(r"cos(36^{\circ})=\frac{\varphi}{2}").scale(.75).next_to(conta5, DOWN)

        self.add(LEI, SOMA)
        self.play(Write(prop0))
        self.play(prop0.animate.shift(UP*2))
        self.play(Write(prop1))
        self.play(Write(prop2))
        self.wait()
        self.play(FadeOut(prop1, shift = UP), prop2.animate.shift(UP))
        self.play(Write(prop3))
        self.play(Circumscribe(prop3[2:5]))
        self.play(Circumscribe(prop3[2:5]))
        self.play(Write(prop4))
        self.play(Circumscribe(prop3[0:3]))
        self.play(Circumscribe(prop3[0:3]))
        self.play(Write(prop5))
        self.wait()
        self.play(ReplacementTransform(prop5,prop6))
        self.play(FadeOut(prop2), FadeOut(prop4))
        self.wait()
        self.play(prop0.animate.scale(.5).next_to(SOMA, DOWN))
        self.play(prop3.animate.scale(.5).next_to(prop0, DOWN))
        self.play(prop6.animate.scale(.5).next_to(prop3, DOWN))
        self.play(Create(pentagono))
        self.play(Write(a0), Write(a1), Write(a2), Write(a3), Write(a4))
        self.play(Create(pentagrama))
        self.play(Create(ang0), Create(ang1))
        self.play(Write(Redang))
        self.wait()
        self.play(Create(ang2), Create(ang3), Create(ang4), Create(ang5))
        self.play(Write(Bluang))
        self.wait()
        self.play(Create(Tri0), Create(Tri1))
        self.play(FadeOut(pentagrama), FadeOut(pentagono), FadeOut(a0),
                  FadeOut(a1), FadeOut(a2), FadeOut(a3), FadeOut(a4),
                  FadeOut(ang0), FadeOut(ang1), FadeOut(ang2), FadeOut(ang3),
                  FadeOut(ang4), FadeOut(ang5), Tri0.animate.shift(RIGHT*2), Rotate(Tri1, PI))
        self.play(Rotate(Tri1[4], PI), Rotate(Tri1[5], PI))
        self.wait()
        self.play(Circumscribe(Tri0[4]), Circumscribe(Tri0[5]))
        self.play(Circumscribe(Tri0[4]), Circumscribe(Tri0[5]))
        self.play(Write(eq0[0]))
        self.play(Circumscribe(Tri1[4]), Circumscribe(Tri1[5]))
        self.play(Circumscribe(Tri1[4]), Circumscribe(Tri1[5]))
        self.play(Write(eq0[1]))
        self.wait()
        self.play(FadeOut(Tri0), Tri1.animate.shift(LEFT*2))
        self.play(Circumscribe(eq0), Circumscribe(prop3))
        self.play(Circumscribe(eq0), Circumscribe(prop3))
        self.play(Write(eq1))
        x= MathTex(r"b\varphi").scale(.75).next_to(Tri1, RIGHT, buff = -.2)
        self.play(ReplacementTransform(Tri1[4],x ))
        self.play(Circumscribe(LEI))
        self.play(Circumscribe(LEI))
        self.play(Write(conta0))
        self.wait()
        self.play(Write(conta1))
        self.wait()
        self.play(Circumscribe(prop6))
        self.play(Circumscribe(prop6))
        self.play(Write(conta2))
        self.wait()
        self.play(Circumscribe(SOMA))
        self.play(Circumscribe(SOMA))
        self.play(Write(conta3))
        self.wait()
        self.play(Write(conta4))
        self.play(Circumscribe(prop6))
        self.play(Circumscribe(prop6))
        self.play(Write(conta5))
        self.wait()
        self.play(Write(conta6))
        self.wait(3)
        self.play(FadeOut(conta0), FadeOut(conta1), FadeOut(conta2),
                  FadeOut(conta3), FadeOut(conta4), FadeOut(conta5), 
                  FadeOut(Tri1), FadeOut(x), FadeOut(Redang), 
                  FadeOut(Bluang), FadeOut(eq0), FadeOut(eq1),
                  FadeOut(LEI), FadeOut(SOMA), FadeOut(prop0),
                  FadeOut(prop3), FadeOut(prop6))
        self.play(conta6.animate.move_to(xy.c2p(0,0)), run_time = 3)
        tempo = ValueTracker(0)
        theta = DecimalNumber().to_corner(DL)
        theta.set(color = BLACK)
        theta.add_updater(lambda x: x.set_value(tempo.get_value()))
        aurea = always_redraw(lambda: VGroup(prop0.copy(), prop3.copy(), prop6.copy()).arrange(DOWN).move_to(xy.c2p(3*np.cos(2*PI/3+theta.get_value()),3*np.sin(2*PI/3+theta.get_value()))))
        LEI0 = always_redraw(lambda: LEI.copy().move_to(xy.c2p(3*np.cos(4*PI/3+theta.get_value()),3*np.sin(4*PI/3+theta.get_value()))))
        SOMA0 = always_redraw(lambda: SOMA.copy().move_to(xy.c2p(3*np.cos(6*PI/3+theta.get_value()),3*np.sin(6*PI/3+theta.get_value()))))
        self.play(FadeIn(theta), FadeIn(aurea), FadeIn(LEI0), FadeIn(SOMA0))
        self.play(tempo.animate.set_value(6*PI), rate_func = linear, run_time = 10)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()
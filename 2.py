from manim import *

class parte2(Scene):
    def construct(self):
        xy = NumberPlane()

        A = xy.c2p(-2,0)
        B = xy.c2p(0,2)
        C = xy.c2p(3,0)
        K = xy.c2p(0,0)

        figura0 = VGroup()

        figura0.add(Polygon(A,B,C, color = PURE_GREEN)) #0
        figura0.add(MathTex("a", color = PURE_GREEN).next_to(figura0[0],DOWN)) #1 labels
        figura0.add(MathTex("b", color = PURE_GREEN).next_to(figura0[0],LEFT, buff = -.5)) #2
        figura0.add(MathTex("c", color = PURE_GREEN).next_to(figura0[0],RIGHT, buff = -1)) #3

        figura0.add(Angle(Line(A,C), Line(A,B), color = PURE_GREEN, radius = .5)) #4 angulo
        figura0.add(MathTex(r"\alpha", color = PURE_GREEN).move_to(Angle(Line(A,C), Line(A,B), color = PURE_GREEN, radius = .5+.3))) #5
        figura0.save_state()

        figura0.add(DashedLine(K,B, color = PURE_GREEN)) #6
        figura0.add(Angle(Line(K,B), Line(K,A), elbow = True, color = PURE_GREEN, radius = 0.3)) #7
        figura0.add(Angle(Line(K,C), Line(K,B), elbow = True, color = PURE_GREEN, radius = 0.3)) #8
        figura0.add(MathTex("h", color = PURE_GREEN).next_to(figura0[6], RIGHT)) #9

        figura0.add(MathTex("m").move_to(xy.c2p(-1,-.5))) #10
        figura0.add(MathTex("a-m").move_to(xy.c2p(1.5,-.5))) #11

        tex0 = MathTex(r"sen(\alpha)",r"=\frac{h}{b}").shift(RIGHT+UP*2).scale(.75)
        tex1 = MathTex(r"\Rightarrow b\cdot sen(\alpha)=h").next_to(tex0, DOWN).scale(.75)

        tex2 = MathTex(r"cos(\alpha)",r"=\frac{m}{b}").next_to(tex0, RIGHT, buff = 2).scale(.75)
        tex3 = MathTex(r"\Rightarrow b\cdot cos(\alpha)=m").next_to(tex2, DOWN).scale(.75)

        teo0 = MathTex(r"h^2+(a-m)^2=c^2", color = RED).scale(.75).shift(RIGHT*2.5)
        teo1 = MathTex(r"\Rightarrow",r"h^2","+",r"a^2-",r"2am+m^2",r"=c^2", color = RED).scale(.75).next_to(teo0, DOWN)
        teo2 = MathTex(r"\Rightarrow",
                       r"(b\cdot sen(\alpha))^2",
                       "+",
                       r"a^2-",
                       r"2ab\cdot cos(\alpha)+(b\cdot cos(\alpha))^2",
                       r"=c^2", color = RED).scale(.75).next_to(teo1, DOWN)
        teo3 = teo2.copy()
        teo4 = MathTex(r"\Rightarrow (b\cdot sen(\alpha))^2+(b\cdot cos(\alpha))^2+a^2-2ab\cdot cos(\alpha)=c^2",
                       color = RED).scale(.75).next_to(teo2, DOWN)
        teo5 = MathTex(r"\Rightarrow b^2\cdot sen^2(\alpha)+b^2\cdot cos^2(\alpha)+a^2-2ab\cdot cos(\alpha)=c^2",
                       color = RED).scale(.75).next_to(teo4, DOWN)
        teo6 = MathTex(r"\Rightarrow b^2\cdot(sen^2(\alpha)+ cos^2(\alpha))+a^2-2ab\cdot cos(\alpha)=c^2",
                       color = RED).scale(.75).next_to(teo5, DOWN)
        
        lei = MathTex(r"b^2+a^2-2ab\cdot cos(\alpha)=c^2",
                       color = RED).scale(.75).next_to(teo5, DOWN)
        Lei = Tex("Lei dos Cossenos", color = GREEN)
        



        self.play(Create(figura0[0]))
        self.play(Create(figura0[1]), Create(figura0[2]),
                  Create(figura0[3]))
        self.play(Create(figura0[4]))
        self.play(Create(figura0[5]))
        self.play(Create(figura0[6]))
        self.play(Create(figura0[7]), Create(figura0[8]))
        self.play(Create(figura0[9]))
        self.play(figura0[1].animate.shift(DOWN*.75))
        self.play(FadeIn(figura0[10]), FadeIn(figura0[11]))
        self.wait()
        self.play(figura0.animate.shift(LEFT*4))
        self.wait()
        self.play(Write(tex0[0]))
        self.wait()
        self.play(Indicate(figura0[2]),Indicate(figura0[9]), Circumscribe(figura0[2]), Circumscribe(figura0[9]))
        self.play(Indicate(figura0[2]),Indicate(figura0[9]), Circumscribe(figura0[2]), Circumscribe(figura0[9]))
        self.play(Indicate(figura0[2]),Indicate(figura0[9]), Circumscribe(figura0[2]), Circumscribe(figura0[9]))
        self.wait()
        self.play(Write(tex0[1]))
        self.wait()
        self.play(Write(tex1))
        self.wait()
        self.play(Write(tex2[0]))
        self.wait()
        self.play(Indicate(figura0[2]),Indicate(figura0[10]), Circumscribe(figura0[2]), Circumscribe(figura0[10]))
        self.play(Indicate(figura0[2]),Indicate(figura0[10]), Circumscribe(figura0[2]), Circumscribe(figura0[10]))
        self.play(Indicate(figura0[2]),Indicate(figura0[10]), Circumscribe(figura0[2]), Circumscribe(figura0[10]))
        self.wait()
        self.play(Write(tex2[1]))
        self.wait()
        self.play(Write(tex3))
        self.wait()
        self.play(Indicate(figura0[3]), Indicate(figura0[9]), Indicate(figura0[11]),
                  Circumscribe(figura0[3]), Circumscribe(figura0[9]), Circumscribe(figura0[11]))
        self.play(Indicate(figura0[3]), Indicate(figura0[9]), Indicate(figura0[11]),
                  Circumscribe(figura0[3]), Circumscribe(figura0[9]), Circumscribe(figura0[11]))
        self.play(Indicate(figura0[3]), Indicate(figura0[9]), Indicate(figura0[11]),
                  Circumscribe(figura0[3]), Circumscribe(figura0[9]), Circumscribe(figura0[11]))
        self.wait()
        self.play(Write(teo0))
        self.wait(3)
        self.play(Write(teo1))
        self.wait()
        self.play(Write(teo2[0]))
        self.play(Circumscribe(tex1), Circumscribe(teo1[1]))
        self.play(Circumscribe(tex1), Circumscribe(teo1[1]))
        self.wait()
        self.play(Write(teo2[1]))
        self.wait()
        self.play(Write(teo2[2:4]))
        self.play(Circumscribe(tex3), Circumscribe(teo1[4]))
        self.play(Circumscribe(tex3), Circumscribe(teo1[4]))
        self.wait()
        self.play(Write(teo2[4]))
        self.wait(3)
        self.play(Write(teo2[5]))
        self.wait()
        self.play(teo3.animate.next_to(teo2, DOWN))
        self.wait(3)
        self.play(ReplacementTransform(teo3, teo4))
        self.wait(3)
        self.play(Write(teo5))
        self.wait(3)
        self.play(Write(teo6))
        self.wait(3)
        self.play(ReplacementTransform(teo6, lei))
        self.wait(5)
        self.play(FadeOut(tex0), FadeOut(tex1), FadeOut(tex2), FadeOut(tex3),
                  FadeOut(teo0), FadeOut(teo1), FadeOut(teo2), FadeOut(teo4), FadeOut(teo5), FadeOut(lei))
        self.play(Restore(figura0))
        LEI = VGroup(Lei, lei).arrange(DOWN).next_to(figura0, DOWN)
        self.play(Write(LEI))
        self.wait(5)
        self.play(FadeOut(figura0), LEI.animate.scale(.5).to_corner(UL))
        self.wait()
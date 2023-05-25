from manim import *

class parte3(Scene):
    def construct(self):
        lei = MathTex(r"b^2+a^2-2ab\cdot cos(\alpha)=c^2",
                       color = RED).scale(.75)
        Lei = Tex("Lei dos Cossenos", color = GREEN)
        LEI = VGroup(Lei, lei).arrange(DOWN).scale(.5).to_corner(UL)
        xy = NumberPlane()

        A = xy.c2p(-2,-2)
        B = xy.c2p(2,-2)
        C = xy.c2p(2,3)
        D = xy.c2p(-2,3)
        K = xy.c2p(2,1)
        J = xy.c2p(.5,3)

        figura0 = VGroup()

        figura0.add(Polygon(A,K,J, color = PURE_GREEN)) #0
        figura0.add(Angle(Line(K,J), Line(K,A), elbow = True, color = PURE_GREEN, radius = 0.3)) #1
        figura0.add(Angle(Line(A,K), Line(A,J), color = PURE_GREEN, radius = 0.5)) #2
        figura0.add(MathTex('1', color = PURE_GREEN).next_to(figura0[0], LEFT, buff = -1)) #3
        figura0.add(MathTex(r"\alpha", color = PURE_GREEN).move_to(Angle(Line(A,K), Line(A,J), color = PURE_GREEN, radius = 0.5+.3))) #4

        figura0.add(MathTex(r"cos(\alpha)").rotate(np.arctan(3/4)).next_to(figura0[0], DOWN, buff = -1.6).scale(.75)) #5
        figura0.add(MathTex(r"sin(\alpha)").rotate(np.arctan(-2/1.5)).next_to(figura0[0], RIGHT+UP, buff = -1.2).scale(.75)) #6

        figura0.add(Polygon(K,B,A, color = PURE_GREEN)) #7
        figura0.add(Angle(Line(B,K), Line(B,A), elbow = True, color = PURE_GREEN, radius = 0.3)) #8
        figura0.add(Angle(Line(A,B), Line(A,K), color = PURE_GREEN, radius = 0.6)) #9
        figura0.add(MathTex(r"\beta", color = PURE_GREEN).move_to(Angle(Line(A,B), Line(A,K), color = PURE_GREEN, radius = 0.6+.3))) #10

        figura0.add(MathTex(r"cos(\alpha)cos(\beta)").next_to(figura0[7], DOWN).scale(.75)) #11
        figura0.add(MathTex(r"cos(\alpha)sen(\beta)").rotate(-PI/2).next_to(figura0[7], RIGHT).scale(.65)) #12

        figura0.add(Angle(Line(K,A), Line(K,B), color = BLUE, radius = 0.5)) #13

        tex0 = MathTex(r"\angle", r"=90^{\circ}-\beta").to_corner(UR).scale(.75)
        tex0[0].set(color = BLUE)
        
        figura0.add(Polygon(K,C,J, color = PURE_GREEN)) #14
        figura0.add(Angle(Line(C,J), Line(C,K), elbow = True, color = PURE_GREEN, radius = 0.3)) #15
        figura0.add(Angle(Line(K,C), Line(K,J), color = YELLOW, radius = 0.5)) #16

        tex1 = MathTex(r"\angle", r"=\beta").next_to(tex0, DOWN).scale(.75)
        tex1[0].set(color = YELLOW)

        figura0.add(MathTex(r"cos(\beta)sen(\alpha)").rotate(-PI/2).scale(.65).next_to(figura0[14], RIGHT)) #17
        figura0.add(MathTex(r"sen(\alpha)sen(\beta)").scale(.65).next_to(figura0[14], UP)) #18

        figura0.add(Angle(Line(J,K), Line(J,C), color = BLUE, radius = 0.3)) #19
        figura0.add(Angle(Line(J,A), Line(J,K), color = PURE_RED, radius = 0.5)) #20

        tex2 = MathTex(r"\angle", r"=90^{\circ}-\alpha").next_to(tex1, DOWN).scale(.75)
        tex2[0].set(color = PURE_RED)

        figura0.add(Polygon(J,D,A, color = PURE_GREEN)) #21
        figura0.add(Angle(Line(D,A), Line(D,J), color = PURE_GREEN, elbow = True, radius = 0.3)) #22

        figura0.add(Angle(Line(J,D), Line(J,A), color = LIGHT_PINK, radius = 0.5)) #23

        tex3 = MathTex(r"\angle","+",r"\angle","+",r"\angle",r"=180^{\circ}").next_to(tex2, DOWN).scale(.75)
        tex3[0].set(color = BLUE)
        tex3[2].set(color = PURE_RED)
        tex3[4].set(color = LIGHT_PINK)

        tex4 = MathTex(r"\angle",r"=\alpha+\beta").next_to(tex2, DOWN).scale(.75)
        tex4[0].set(color = LIGHT_PINK)
        
        figura0.add(MathTex(r"sen(\alpha+\beta)").rotate(PI/2).next_to(figura0[21], LEFT).scale(.75)) #24
        figura0.add(MathTex(r"cos(\alpha+\beta)").scale(.65).next_to(figura0[21], UP)) #25

        af0 = MathTex(r"sen(\alpha+\beta)=cos(\alpha)sen(\beta)+cos(\beta)sen(\alpha)", color = RED).scale(.55).shift(UP*2+RIGHT*.5)
        af1 = MathTex(r"cos(\alpha+\beta)=cos(\alpha)cos(\beta)-sen(\alpha)sen(\beta)", color = RED).scale(.55).next_to(af0, DOWN)
        af2 = Tex("Seno e Cosseno da Soma de Arcos", color = GREEN).next_to(af0, UP).scale(.8)
        SOMA = VGroup(af0,af1,af2)


        self.add(LEI)
        self.play(Create(figura0[0]), Create(figura0[1]))
        self.play(Create(figura0[2]), Create(figura0[3]))
        self.play(Create(figura0[4]))
        self.wait()
        self.play(Create(figura0[5]))
        self.play(Create(figura0[6]))
        self.play(Create(figura0[7]))
        self.play(Create(figura0[8]), Create(figura0[9]), Create(figura0[10]))
        self.wait()
        self.play(Create(figura0[11]))
        self.play(Create(figura0[12]))
        self.wait(2)
        self.play(Create(figura0[13]))
        self.play(Write(tex0))
        self.wait(2)
        self.play(Create(figura0[14]))
        self.play(Create(figura0[15]))
        self.play(Create(figura0[16]))
        self.play(Write(tex1))
        self.wait(2)
        self.play(Create(figura0[17]))
        self.play(Create(figura0[18]))
        self.wait(2)
        self.play(Create(figura0[19]))
        self.play(Create(figura0[20]))
        self.play(Write(tex2))
        self.wait(2)
        self.play(Create(figura0[21]))
        self.play(Create(figura0[22]))
        self.play(Create(figura0[23]))
        self.play(Write(tex3))
        self.wait()
        self.play(ReplacementTransform(tex3,tex4))
        self.wait()
        self.play(Create(figura0[24]))
        self.play(Create(figura0[25]))
        self.wait(3)
        self.play(figura0.animate.scale(.65).to_corner(DL), FadeOut(tex0),
                  FadeOut(tex1), FadeOut(tex2), FadeOut(tex4))
        self.play(Indicate(figura0[24]), Indicate(figura0[12]), Indicate(figura0[17]))
        self.play(Indicate(figura0[24]), Indicate(figura0[12]), Indicate(figura0[17]))
        self.play(Indicate(figura0[24]), Indicate(figura0[12]), Indicate(figura0[17]))
        self.play(Write(SOMA[0]))
        self.wait()
        self.play(Indicate(figura0[25]), Indicate(figura0[18]), Indicate(figura0[11]))
        self.play(Indicate(figura0[25]), Indicate(figura0[18]), Indicate(figura0[11]))
        self.play(Indicate(figura0[25]), Indicate(figura0[18]), Indicate(figura0[11]))
        self.play(Write(SOMA[1]))
        self.wait()
        self.play(Write(SOMA[2]))
        self.wait()
        self.play(FadeOut(figura0), SOMA.animate.scale(.5).next_to(LEI, DOWN))
        self.wait(2)
from manim import *

class parte5(Scene):
    def construct(self):
        prod = Tex("Produção:")
        nome = Tex("Braian Henzel Barcelos", color = YELLOW)
        prog = Tex("Programa Utilizado:")
        manim = Tex("Manim", color = YELLOW)
        code = Tex("Código Disponível Em:")
        git = Tex("https://github.com/ProfBraio/Projeto-FVDEM/tree/main", color = YELLOW)
        music = Tex("Áudio:")
        you = Tex("Biblioteca de Áudio do YouTube", color = YELLOW)
        cerd = VGroup(prod, nome, prog, manim, code, git, music, you).arrange(DOWN).to_edge(UP)

        self.play(Write(cerd, lag_ratio = 1, run_time = 9))
        self.wait()
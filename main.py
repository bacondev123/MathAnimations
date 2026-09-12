from manim import *

# 3b1b dark charcoal background
config.background_color = "#171717"

class DemoScene(Scene):
    def construct(self):
        # Create shapes
        circle = Circle(radius=1.5, color=BLUE)
        square = Square(side_length=2.5, color=YELLOW)
        
        # Text
        text = Text("3Blue1Brown with AI", font_size=36, color=WHITE).to_edge(UP)

        # Animation sequence
        self.play(Write(text))
        self.play(Create(circle))
        self.wait(0.5)
        # Morph circle into square
        self.play(ReplacementTransform(circle, square))
        self.wait(1)
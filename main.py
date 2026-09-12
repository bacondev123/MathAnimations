from manim import *

# 3Blue1Brown aesthetic background
config.background_color = "#171717"

class ShadowMeasurement(Scene):
    def construct(self):
        thai_font = "Tahoma"

        # ----------------------------------------------------
        # 1. Title
        # ----------------------------------------------------
        title = Text("ความคล้าย: การวัดความสูงด้วยเงา", font=thai_font, font_size=32, color=WHITE).to_edge(UP)
        subtitle = Text("Similar Triangles & Shadow Reckoning", font_size=18, color=GRAY).next_to(title, DOWN, buff=0.15)
        
        self.play(Write(title), FadeIn(subtitle))
        self.wait(1)

        # ----------------------------------------------------
        # 2. Ground & Sun
        # ----------------------------------------------------
        ground_y = -2.2
        ground = Line(LEFT * 7, RIGHT * 7, color=GRAY_B).shift(UP * ground_y)
        
        # Sun at top left
        sun_pos = LEFT * 5.5 + UP * 2.8
        sun = Dot(sun_pos, radius=0.35, color=YELLOW)
        sun_glow = Circle(radius=0.55, color=YELLOW, stroke_opacity=0.5).move_to(sun_pos)
        sun_label = Text("ดวงอาทิตย์", font=thai_font, font_size=16, color=YELLOW).next_to(sun, DOWN, buff=0.2)

        self.play(Create(ground), FadeIn(sun, sun_glow, sun_label))

        # ----------------------------------------------------
        # 3. Objects: Stick (เสา) and Tree (ต้นไม้)
        # ----------------------------------------------------
        # Positions
        stick_x = -3.5
        stick_h = 1.5   # stick height
        stick_s = 2.0   # stick shadow length

        tree_x = 0.5
        tree_h = 3.0    # tree height
        tree_s = 4.0    # tree shadow length

        # Stick
        stick = Line(
            [stick_x, ground_y, 0], 
            [stick_x, ground_y + stick_h, 0], 
            color=LIGHT_BROWN, stroke_width=6
        )
        stick_label = Text("เสา (1.5 ม.)", font=thai_font, font_size=18, color=LIGHT_PINK).next_to(stick, LEFT, buff=0.2)

        # Tree (Trunk + Foliage)
        trunk = Line(
            [tree_x, ground_y, 0], 
            [tree_x, ground_y + 1.2, 0], 
            color=DARK_BROWN, stroke_width=8
        )
        foliage = Triangle(color=GREEN, fill_color=GREEN, fill_opacity=0.7).scale(1.1).move_to([tree_x, ground_y + 2.1, 0])
        tree_label = Text("ต้นไม้ (H = ?)", font=thai_font, font_size=18, color=YELLOW).next_to(foliage, UP, buff=0.2)

        self.play(Create(stick), Write(stick_label))
        self.play(Create(trunk), Create(foliage), Write(tree_label))
        self.wait(1)

        # ----------------------------------------------------
        # 4. Sunlight Rays & Shadows
        # ----------------------------------------------------
        # Sun rays pass through the tops of both objects at the exact same angle
        ray_stick = DashedLine(
            sun_pos, 
            [stick_x + stick_s, ground_y, 0], 
            color=YELLOW_B, stroke_width=2
        )
        ray_tree = DashedLine(
            sun_pos, 
            [tree_x + tree_s, ground_y, 0], 
            color=YELLOW_B, stroke_width=2
        )

        # Shadows on the ground
        shadow_stick = Line([stick_x, ground_y, 0], [stick_x + stick_s, ground_y, 0], color=BLUE_C, stroke_width=8)
        shadow_tree = Line([tree_x, ground_y, 0], [tree_x + tree_s, ground_y, 0], color=ORANGE, stroke_width=8)

        lbl_s_stick = Text("เงา = 2 ม.", font=thai_font, font_size=16, color=BLUE_C).next_to(shadow_stick, DOWN, buff=0.15)
        lbl_s_tree = Text("เงา = 6 ม.", font=thai_font, font_size=16, color=ORANGE).next_to(shadow_tree, DOWN, buff=0.15)

        self.play(Create(ray_stick), Create(ray_tree))
        self.play(
            Create(shadow_stick), Write(lbl_s_stick),
            Create(shadow_tree), Write(lbl_s_tree)
        )
        self.wait(1.5)

        # ----------------------------------------------------
        # 5. Highlight Similar Triangles
        # ----------------------------------------------------
        # Small triangle (Stick)
        tri_small = Polygon(
            [stick_x, ground_y, 0],
            [stick_x, ground_y + stick_h, 0],
            [stick_x + stick_s, ground_y, 0],
            color=BLUE, fill_color=BLUE, fill_opacity=0.25, stroke_width=3
        )
        
        # Large triangle (Tree)
        tri_large = Polygon(
            [tree_x, ground_y, 0],
            [tree_x, ground_y + tree_h, 0],
            [tree_x + tree_s, ground_y, 0],
            color=YELLOW, fill_color=YELLOW, fill_opacity=0.2, stroke_width=3
        )

        self.play(FadeIn(tri_small), FadeIn(tri_large))

        similarity_note = Text(
            "แสงแดดส่องขนานกัน → ทำมุมเท่ากัน → สามเหลี่ยมคล้ายกัน!", 
            font=thai_font, font_size=20, color=GOLD
        ).to_edge(UP).shift(DOWN * 0.8)
        
        self.play(FadeOut(subtitle), Write(similarity_note))
        self.wait(2)

        # ----------------------------------------------------
        # 6. Mathematical Proportions & Solution
        # ----------------------------------------------------
        # Clear top note and show calculation box
        self.play(FadeOut(similarity_note))

        eq1 = Text("ความสูงต้นไม้ / เงาต้นไม้  =  ความสูงเสา / เงาเสา", font=thai_font, font_size=20, color=WHITE)
        eq2 = Text("H / 6  =  1.5 / 2", font_size=24, color=YELLOW)
        eq3 = Text("H  =  (1.5 × 6) / 2", font_size=24, color=WHITE)
        ans = Text("H  =  4.5 เมตร!", font=thai_font, font_size=28, color=GREEN)

        eq_group = VGroup(eq1, eq2, eq3, ans).arrange(DOWN, buff=0.25).to_corner(UL).shift(RIGHT * 0.5)

        self.play(Write(eq1))
        self.wait(1)
        self.play(Write(eq2))
        self.wait(1)
        self.play(Write(eq3))
        self.wait(1)
        self.play(Write(ans))

        # Highlight final answer
        box = SurroundingRectangle(ans, color=GREEN, buff=0.15)
        self.play(Create(box))
        self.wait(3)
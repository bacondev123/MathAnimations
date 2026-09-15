from manim import *

# ====================================================================
# 9:16 VERTICAL CONFIGURATION (1080 x 1920)
# ====================================================================
config.background_color = "#171717"
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9.0
config.frame_height = 16.0

# ====================================================================
# MEASUREMENT DATA
# ====================================================================
STICK_HEIGHT_M = 1.6    # ความสูงคน (167 ซม. / 1.6 ม.)
STICK_SHADOW_M = 1.9    # ความยาวเงาคน (194 ซม. / 1.9 ม.)
POLE_SHADOW_M  = 12.6   # ความยาวเงาเสาธง: 400 + 400 + 400 + 60 = 1260 ซม. (12.6 ม.)

POLE_HEIGHT_M = (STICK_HEIGHT_M * POLE_SHADOW_M) / STICK_SHADOW_M


class FlagpoleShadowMeasurement(Scene):
    def construct(self):
        thai_font = "Tahoma"

        # ----------------------------------------------------
        # 1. Title & Header (Top Section) (~4.0s)
        # ----------------------------------------------------
        title = Text("การวัดความสูงเสาธงด้วยเงา", font=thai_font, font_size=26, color=WHITE).to_edge(UP, buff=0.8)
        subtitle = Text("การประยุกต์ใช้เรื่องความคล้าย (Similar Triangles)", font=thai_font, font_size=14, color=GRAY_B).next_to(title, DOWN, buff=0.15)

        self.play(Write(title, run_time=1.5), FadeIn(subtitle, run_time=1.5))
        self.wait(2.5)

        # ----------------------------------------------------
        # 2. Ground & Sun (Bottom/Middle Section) (~3.0s)
        # ----------------------------------------------------
        ground_y = -3.8
        ground = Line(LEFT * 4.2, RIGHT * 4.2, color=GRAY_C).shift(UP * ground_y)

        sun_pos = LEFT * 2.8 + UP * 1.5
        sun = Dot(sun_pos, radius=0.25, color=YELLOW)
        sun_glow = Circle(radius=0.42, color=YELLOW, stroke_opacity=0.35).move_to(sun_pos)
        sun_label = Text("ดวงอาทิตย์", font=thai_font, font_size=12, color=YELLOW).next_to(sun, UP, buff=0.1)

        self.play(Create(ground), FadeIn(sun, sun_glow, sun_label), run_time=1.5)
        self.wait(1.5)

        # ----------------------------------------------------
        # 3. Reference Person & Flagpole (~7.0s)
        # ----------------------------------------------------
        stick_x = -2.8
        stick_draw_h = 1.1
        stick_draw_s = 1.3

        pole_x = 0.5
        pole_draw_h = 2.6
        pole_draw_s = 3.2

        # --- Reference Person ---
        stick = Line([stick_x, ground_y, 0], [stick_x, ground_y + stick_draw_h, 0], color=LIGHT_BROWN, stroke_width=5.5)
        stick_label = Text(f"คน ({STICK_HEIGHT_M:.1f} ม.)", font=thai_font, font_size=13, color=LIGHT_PINK).next_to(stick, LEFT, buff=0.1)

        # --- Flagpole ---
        pole_base = Rectangle(width=0.35, height=0.12, color=GRAY, fill_color=GRAY, fill_opacity=1).move_to([pole_x, ground_y + 0.06, 0])
        pole_body = Line([pole_x, ground_y, 0], [pole_x, ground_y + pole_draw_h, 0], color=WHITE, stroke_width=4.5)
        pole_finial = Dot([pole_x, ground_y + pole_draw_h, 0], radius=0.07, color=GOLD)

        # Thai National Flag
        flag_w = 0.65
        flag_stripes = VGroup(
            Rectangle(width=flag_w, height=0.07, color=RED, fill_color=RED, fill_opacity=1, stroke_width=0),
            Rectangle(width=flag_w, height=0.07, color=WHITE, fill_color=WHITE, fill_opacity=1, stroke_width=0),
            Rectangle(width=flag_w, height=0.14, color=BLUE_E, fill_color=BLUE_E, fill_opacity=1, stroke_width=0),
            Rectangle(width=flag_w, height=0.07, color=WHITE, fill_color=WHITE, fill_opacity=1, stroke_width=0),
            Rectangle(width=flag_w, height=0.07, color=RED, fill_color=RED, fill_opacity=1, stroke_width=0),
        ).arrange(DOWN, buff=0).next_to([pole_x, ground_y + pole_draw_h - 0.22, 0], RIGHT, buff=0)

        flagpole_group = VGroup(pole_base, pole_body, pole_finial, flag_stripes)
        pole_label = Text("เสาธง (H = ?)", font=thai_font, font_size=14, color=YELLOW).next_to(pole_finial, UP, buff=0.12)

        self.play(Create(stick), Write(stick_label), run_time=1.5)
        self.wait(1.5)
        self.play(Create(flagpole_group), Write(pole_label), run_time=1.5)
        self.wait(2.5)

        # ----------------------------------------------------
        # 4. Sunlight Rays & Shadows (~9.0s)
        # ----------------------------------------------------
        ray_stick = DashedLine(sun_pos, [stick_x + stick_draw_s, ground_y, 0], color=YELLOW_B, stroke_width=2)
        ray_pole  = DashedLine(sun_pos, [pole_x + pole_draw_s, ground_y, 0], color=YELLOW_B, stroke_width=2)

        shadow_stick = Line([stick_x, ground_y, 0], [stick_x + stick_draw_s, ground_y, 0], color=BLUE_C, stroke_width=7)
        shadow_pole  = Line([pole_x, ground_y, 0], [pole_x + pole_draw_s, ground_y, 0], color=ORANGE, stroke_width=7)

        lbl_s_stick = Text(f"เงาคน = {STICK_SHADOW_M} ม.", font=thai_font, font_size=12, color=BLUE_C).next_to(shadow_stick, DOWN, buff=0.12)
        lbl_s_pole = Text("เงาเสาธง = 1,260 ซม. (12.6 ม.)", font=thai_font, font_size=12, color=ORANGE).next_to(shadow_pole, DOWN, buff=0.12)
        lbl_s_segments = Text("(400 + 400 + 400 + 60 ซม.)", font=thai_font, font_size=10, color=GRAY).next_to(lbl_s_pole, DOWN, buff=0.06)

        self.play(Create(ray_stick), Create(ray_pole), run_time=1.5)
        self.wait(1.5)
        self.play(
            Create(shadow_stick), Write(lbl_s_stick),
            Create(shadow_pole), Write(lbl_s_pole), FadeIn(lbl_s_segments),
            run_time=2.0
        )
        self.wait(4.0)

        # ----------------------------------------------------
        # 5. Triangle Emergence & Similarity Principle (~9.0s)
        # ----------------------------------------------------
        tri_stick = Polygon(
            [stick_x, ground_y, 0],
            [stick_x, ground_y + stick_draw_h, 0],
            [stick_x + stick_draw_s, ground_y, 0],
            color=BLUE, fill_color=BLUE, fill_opacity=0.25, stroke_width=2.2
        )

        tri_pole = Polygon(
            [pole_x, ground_y, 0],
            [pole_x, ground_y + pole_draw_h, 0],
            [pole_x + pole_draw_s, ground_y, 0],
            color=YELLOW, fill_color=YELLOW, fill_opacity=0.2, stroke_width=2.2
        )

        self.play(FadeIn(tri_stick), FadeIn(tri_pole), run_time=1.5)
        self.wait(2.0)

        # Centered explanation in the upper area
        concept_note = Text(
            "แสงแดดขนานกัน → มุมเท่ากัน\n→ สามเหลี่ยมคล้ายกัน (ม.ม.)", 
            font=thai_font, font_size=14, color=GOLD, line_spacing=0.8
        ).move_to([0, 3.8, 0])

        self.play(FadeOut(subtitle), Write(concept_note), run_time=1.5)
        self.wait(4.0)

        # ----------------------------------------------------
        # 6. Smooth Transition to Math (Upper Card) (~28.0s)
        # ----------------------------------------------------
        self.play(
            FadeOut(concept_note),
            FadeOut(ray_stick),
            FadeOut(ray_pole),
            run_time=1.0
        )

        calc_header = Text("คำนวณความสูงเสาธงด้วยอัตราส่วน:", font=thai_font, font_size=14, color=BLUE_B)
        eq1 = Text("ความสูงเสาธง / เงาเสาธง  =  ความสูงคน / เงาคน", font=thai_font, font_size=13, color=WHITE)
        eq2 = Text(f"H / {POLE_SHADOW_M}  =  {STICK_HEIGHT_M} / {STICK_SHADOW_M}", font=thai_font, font_size=17, color=YELLOW)
        eq3 = Text(f"H  =  ({STICK_HEIGHT_M} × {POLE_SHADOW_M}) / {STICK_SHADOW_M}", font=thai_font, font_size=17, color=WHITE)
        ans = Text(f"H  =  {POLE_HEIGHT_M:.1f} เมตร (หรือ {int(POLE_HEIGHT_M * 100)} ซม.)", font=thai_font, font_size=19, color=GREEN)

        calc_group = VGroup(calc_header, eq1, eq2, eq3, ans).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        calc_group.move_to([0, 3.8, 0])

        # Sleek dark background card sized for 9:16
        calc_card = RoundedRectangle(
            corner_radius=0.15,
            width=calc_group.width + 0.5,
            height=calc_group.height + 0.35,
            color=GRAY_D,
            fill_color="#181818",
            fill_opacity=0.92,
            stroke_width=1.5
        ).move_to(calc_group)

        self.play(FadeIn(calc_card), Write(calc_header), run_time=1.2)
        self.wait(1.5)

        self.play(Write(eq1), run_time=1.5)
        self.wait(3.0)

        self.play(Write(eq2), run_time=1.5)
        self.wait(3.0)

        self.play(Write(eq3), run_time=1.5)
        self.wait(3.0)

        self.play(Write(ans), run_time=1.5)
        self.wait(1.5)

        # Green highlight box for the final answer
        box = SurroundingRectangle(ans, color=GREEN, buff=0.08)
        self.play(Create(box), run_time=1.0)
        self.wait(6.0)
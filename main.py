from manim import *

# 3Blue1Brown aesthetic background
config.background_color = "#171717"

# ====================================================================
# MEASUREMENT DATA (แก้ไขค่าตัวเลขจริงตรงนี้ได้เลย)
# ====================================================================
STICK_HEIGHT_M = 1.6    # ความสูงไม้เมตร (167 ซม. / 1.6 ม.) 
STICK_SHADOW_M = 1.9    # ความยาวเงาไม้ (194 ซม. / 1.9 ม.) 
POLE_SHADOW_M  = 12.6   # ความยาวเงาเสาธง: 400 + 400 + 400 + 60 = 1260 ซม. (12.6 ม.)

# คำนวณความสูงเสาธงอัตโนมัติ: H = (h_stick * s_pole) / s_stick
POLE_HEIGHT_M = (STICK_HEIGHT_M * POLE_SHADOW_M) / STICK_SHADOW_M


class FlagpoleShadowMeasurement(Scene):
    def construct(self):
        thai_font = "Tahoma"

        # ----------------------------------------------------
        # 1. Title & Intro
        # ----------------------------------------------------
        title = Text("การวัดความสูงเสาธงด้วยเงา", font=thai_font, font_size=30, color=WHITE).to_edge(UP, buff=0.35)
        subtitle = Text("การประยุกต์ใช้เรื่องความคล้าย (Similar Triangles)", font=thai_font, font_size=16, color=GRAY_B).next_to(title, DOWN, buff=0.12)
        
        self.play(Write(title), FadeIn(subtitle))
        self.wait(1)

        # ----------------------------------------------------
        # 2. Ground & Sun (Tucked into the far upper-left corner)
        # ----------------------------------------------------
        ground_y = -2.2
        ground = Line(LEFT * 7.2, RIGHT * 7.2, color=GRAY_C).shift(UP * ground_y)
        
        sun_pos = LEFT * 6.0 + UP * 3.2
        sun = Dot(sun_pos, radius=0.28, color=YELLOW)
        sun_glow = Circle(radius=0.48, color=YELLOW, stroke_opacity=0.35).move_to(sun_pos)
        sun_label = Text("ดวงอาทิตย์", font=thai_font, font_size=13, color=YELLOW).next_to(sun, DOWN, buff=0.1)

        self.play(Create(ground), FadeIn(sun, sun_glow, sun_label))

        # ----------------------------------------------------
        # 3. Reference Stick & Flagpole
        # ----------------------------------------------------
        stick_x = -4.0
        stick_draw_h = 1.15
        stick_draw_s = 1.6

        pole_x = 0.8
        pole_draw_h = 2.9
        pole_draw_s = 4.0

        # --- Reference Stick ---
        stick = Line([stick_x, ground_y, 0], [stick_x, ground_y + stick_draw_h, 0], color=LIGHT_BROWN, stroke_width=6)
        stick_label = Text(f"คน ({STICK_HEIGHT_M:.1f} ม.)", font=thai_font, font_size=15, color=LIGHT_PINK).next_to(stick, LEFT, buff=0.15)

        # --- Flagpole Construction ---
        pole_base = Rectangle(width=0.4, height=0.15, color=GRAY, fill_color=GRAY, fill_opacity=1).move_to([pole_x, ground_y + 0.075, 0])
        pole_body = Line([pole_x, ground_y, 0], [pole_x, ground_y + pole_draw_h, 0], color=WHITE, stroke_width=5)
        pole_finial = Dot([pole_x, ground_y + pole_draw_h, 0], radius=0.08, color=GOLD)

        # Thai National Flag (ธงไตรรงค์)
        flag_w = 0.75
        flag_stripes = VGroup(
            Rectangle(width=flag_w, height=0.08, color=RED, fill_color=RED, fill_opacity=1, stroke_width=0),
            Rectangle(width=flag_w, height=0.08, color=WHITE, fill_color=WHITE, fill_opacity=1, stroke_width=0),
            Rectangle(width=flag_w, height=0.16, color=BLUE_E, fill_color=BLUE_E, fill_opacity=1, stroke_width=0),
            Rectangle(width=flag_w, height=0.08, color=WHITE, fill_color=WHITE, fill_opacity=1, stroke_width=0),
            Rectangle(width=flag_w, height=0.08, color=RED, fill_color=RED, fill_opacity=1, stroke_width=0),
        ).arrange(DOWN, buff=0).next_to([pole_x, ground_y + pole_draw_h - 0.25, 0], RIGHT, buff=0)

        flagpole_group = VGroup(pole_base, pole_body, pole_finial, flag_stripes)
        pole_label = Text("เสาธง (H = ?)", font=thai_font, font_size=17, color=YELLOW).next_to(pole_finial, UP, buff=0.15)

        self.play(Create(stick), Write(stick_label))
        self.play(Create(flagpole_group), Write(pole_label))
        self.wait(1)

        # ----------------------------------------------------
        # 4. Sunlight Rays & Shadows
        # ----------------------------------------------------
        ray_stick = DashedLine(sun_pos, [stick_x + stick_draw_s, ground_y, 0], color=YELLOW_B, stroke_width=2)
        ray_pole  = DashedLine(sun_pos, [pole_x + pole_draw_s, ground_y, 0], color=YELLOW_B, stroke_width=2)

        shadow_stick = Line([stick_x, ground_y, 0], [stick_x + stick_draw_s, ground_y, 0], color=BLUE_C, stroke_width=8)
        shadow_pole  = Line([pole_x, ground_y, 0], [pole_x + pole_draw_s, ground_y, 0], color=ORANGE, stroke_width=8)

        lbl_s_stick = Text(f"เงาคน = {STICK_SHADOW_M} ม.", font=thai_font, font_size=15, color=BLUE_C).next_to(shadow_stick, DOWN, buff=0.15)
        lbl_s_pole = Text("เงาเสาธง = 1,260 ซม. (12.6 ม.)", font=thai_font, font_size=15, color=ORANGE).next_to(shadow_pole, DOWN, buff=0.15)
        lbl_s_segments = Text("(400 + 400 + 400 + 60 ซม.)", font=thai_font, font_size=13, color=GRAY).next_to(lbl_s_pole, DOWN, buff=0.08)

        self.play(Create(ray_stick), Create(ray_pole))
        self.play(
            Create(shadow_stick), Write(lbl_s_stick),
            Create(shadow_pole), Write(lbl_s_pole), FadeIn(lbl_s_segments)
        )
        self.wait(1.5)

        # ----------------------------------------------------
        # 5. Triangle Emergence & Similarity Principle
        # ----------------------------------------------------
        tri_stick = Polygon(
            [stick_x, ground_y, 0],
            [stick_x, ground_y + stick_draw_h, 0],
            [stick_x + stick_draw_s, ground_y, 0],
            color=BLUE, fill_color=BLUE, fill_opacity=0.25, stroke_width=2.5
        )

        tri_pole = Polygon(
            [pole_x, ground_y, 0],
            [pole_x, ground_y + pole_draw_h, 0],
            [pole_x + pole_draw_s, ground_y, 0],
            color=YELLOW, fill_color=YELLOW, fill_opacity=0.2, stroke_width=2.5
        )

        self.play(FadeIn(tri_stick), FadeIn(tri_pole))

        concept_note = Text(
            "แสงแดดขนานกัน → มุมเท่ากัน → สามเหลี่ยมคล้ายกัน (ม.ม.)", 
            font=thai_font, font_size=16, color=GOLD
        ).next_to(title, DOWN, buff=0.15)

        self.play(FadeOut(subtitle), Write(concept_note))
        self.wait(2)

        # ----------------------------------------------------
        # 6. Smooth Transition to Math (Clear clutter)
        # ----------------------------------------------------
        # Fade out title, notes, and the slicing ray to free the upper screen
        self.play(
            FadeOut(title), 
            FadeOut(concept_note),
            FadeOut(ray_stick),
            FadeOut(ray_pole)
        )

        # Calculation group with clean typography
        calc_header = Text("คำนวณความสูงเสาธงด้วยอัตราส่วน:", font=thai_font, font_size=16, color=BLUE_B)
        eq1 = Text("ความสูงเสาธง / เงาเสาธง  =  ความสูงคน / เงาคน", font=thai_font, font_size=16, color=WHITE)
        eq2 = Text(f"H / {POLE_SHADOW_M}  =  {STICK_HEIGHT_M} / {STICK_SHADOW_M}", font=thai_font, font_size=20, color=YELLOW)
        eq3 = Text(f"H  =  ({STICK_HEIGHT_M} × {POLE_SHADOW_M}) / {STICK_SHADOW_M}", font=thai_font, font_size=20, color=WHITE)
        ans = Text(f"H  =  {POLE_HEIGHT_M:.1f} เมตร (หรือ {int(POLE_HEIGHT_M * 100)} ซม.)", font=thai_font, font_size=22, color=GREEN)

        calc_group = VGroup(calc_header, eq1, eq2, eq3, ans).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        calc_group.to_edge(UP, buff=0.35).shift(LEFT * 0.4)

        # Sleek dark background card so it pops cleanly
        calc_card = RoundedRectangle(
            corner_radius=0.15,
            width=calc_group.width + 0.6,
            height=calc_group.height + 0.4,
            color=GRAY_D,
            fill_color="#181818",
            fill_opacity=0.88,
            stroke_width=1.5
        ).move_to(calc_group)

        self.play(FadeIn(calc_card), Write(calc_header))
        self.play(Write(eq1))
        self.wait(1)
        self.play(Write(eq2))
        self.wait(1)
        self.play(Write(eq3))
        self.wait(1)
        self.play(Write(ans))

        # Green highlight box for the final answer
        box = SurroundingRectangle(ans, color=GREEN, buff=0.1)
        self.play(Create(box))
        self.wait(3)
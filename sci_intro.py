from manim import *
import numpy as np

# ตั้งค่าอัตราส่วนแนวตั้ง 9:16 (รองรับทั้ง -pql และ -pqh อัตโนมัติ)
if config.pixel_width > config.pixel_height:
    config.pixel_width, config.pixel_height = config.pixel_height, config.pixel_width
config.frame_width = 9.0
config.frame_height = 16.0


class EcosystemIntro(Scene):
    def construct(self):
        # 1. ตั้งค่าสีพื้นหลังและฟอนต์ภาษาไทย
        self.camera.background_color = "#071717"
        THAI_FONT = "Leelawadee UI"  # เปลี่ยนเป็น "Sarabun", "Kanit" หรือ "Tahoma" ได้

        # ==========================================================
        # ส่วนที่ 1: พื้นหลังแนววิทยาศาสตร์ (Grid + Ambient Particles)
        # ==========================================================
        grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-9, 9, 1],
            background_line_style={
                "stroke_color": TEAL_E,
                "stroke_width": 1,
                "stroke_opacity": 0.18,
            },
            axis_config={"stroke_opacity": 0},
        )

        # สร้างละอองแสงทั่วเฟรมแนวตั้ง
        rng = np.random.default_rng(42)
        particles = VGroup()
        for _ in range(36):
            x = rng.uniform(-4.2, 4.2)
            y = rng.uniform(-7.5, 7.5)
            r = rng.uniform(0.025, 0.065)
            color = rng.choice([TEAL_A, GREEN_B, YELLOW_B])
            dot = Dot(point=[x, y, 0], radius=r, color=color).set_opacity(rng.uniform(0.25, 0.65))
            particles.add(dot)

        self.play(FadeIn(grid, run_time=0.8), FadeIn(particles, run_time=1.0))

        # ==========================================================
        # ส่วนที่ 2: โดมจำลองระบบนิเวศ (Ecosystem Terrarium)
        # ==========================================================
        dome_center = UP * 2.1
        dome_radius = 1.95

        # ขอบแก้วทรงกลม 2 ชั้น
        glass_outer = Circle(radius=dome_radius + 0.10, color=TEAL_B, stroke_width=2).set_stroke(opacity=0.45)
        glass_inner = Circle(radius=dome_radius, color=TEAL_A, stroke_width=4)
        glass_outer.move_to(dome_center)
        glass_inner.move_to(dome_center)

        # ชั้นดินและชั้นน้ำด้านล่างของโดม
        soil_rect = Rectangle(width=5.0, height=1.5).move_to(dome_center + DOWN * 1.55)
        soil_layer = Intersection(glass_inner.copy(), soil_rect)
        soil_layer.set_fill("#4A3525", opacity=0.95).set_stroke(width=0)

        water_rect = Rectangle(width=5.0, height=0.40).move_to(dome_center + DOWN * 0.65)
        water_layer = Intersection(glass_inner.copy(), water_rect)
        water_layer.set_fill("#1E7898", opacity=0.75).set_stroke(width=0)

        # ต้นกล้า (ผู้ผลิต)
        stem_start = dome_center + DOWN * 0.60
        stem_end = dome_center + UP * 0.45
        stem = CubicBezier(
            stem_start,
            stem_start + UP * 0.40 + LEFT * 0.10,
            stem_end + DOWN * 0.35 + RIGHT * 0.10,
            stem_end,
            color=GREEN_C,
            stroke_width=7,
        )

        # ใบไม้ซ้าย-ขวา-บน
        def make_leaf(scale=0.55, color=GREEN_B):
            c1 = Circle(radius=scale).shift(UP * scale * 0.5)
            c2 = Circle(radius=scale).shift(DOWN * scale * 0.5)
            leaf = Intersection(c1, c2)
            leaf.set_fill(color, opacity=1).set_stroke(GREEN_A, width=1.5)
            return leaf

        leaf_left = make_leaf(0.55, GREEN_B).rotate(35 * DEGREES).move_to(stem_end + LEFT * 0.30 + DOWN * 0.15)
        leaf_right = make_leaf(0.62, GREEN_C).rotate(-35 * DEGREES).move_to(stem_end + RIGHT * 0.34 + UP * 0.06)
        leaf_top = make_leaf(0.38, "#7CFC00").rotate(85 * DEGREES).move_to(stem_end + UP * 0.22)

        # ดวงอาทิตย์ (แหล่งพลังงาน)
        sun_pos = dome_center + RIGHT * 0.90 + UP * 0.85
        sun_core = Circle(radius=0.26, color=YELLOW_B, fill_opacity=1, stroke_width=0).move_to(sun_pos)
        sun_rays = VGroup()
        for i in range(8):
            angle = i * (PI / 4)
            ray = Line(
                start=sun_pos + 0.36 * np.array([np.cos(angle), np.sin(angle), 0]),
                end=sun_pos + 0.52 * np.array([np.cos(angle), np.sin(angle), 0]),
                color=YELLOW_A,
                stroke_width=3.5,
            )
            sun_rays.add(ray)
        sun_group = VGroup(sun_core, sun_rays)

        # วงแหวนวัฏจักรพลังงานรอบโดม
        orbit_ring = DashedVMobject(
            Circle(radius=dome_radius + 0.38, color=GREEN_A, stroke_width=2.5),
            num_dashes=40,
        )
        orbit_ring.set_stroke(opacity=0.6).move_to(dome_center)

        # จุดโหนดวัฏจักร 3 จุดรอบวงโคจร
        node_angles = [60 * DEGREES, 180 * DEGREES, 300 * DEGREES]
        node_colors = [YELLOW_B, GREEN_B, TEAL_A]
        orbit_nodes = VGroup()
        for ang, col in zip(node_angles, node_colors):
            pos = dome_center + (dome_radius + 0.38) * np.array([np.cos(ang), np.sin(ang), 0])
            node = Dot(point=pos, radius=0.11, color=col)
            glow = Circle(radius=0.20, color=col, stroke_width=1.5).set_stroke(opacity=0.5).move_to(pos)
            orbit_nodes.add(VGroup(glow, node))

        # แอนิเมชันสร้างโดมและระบบนิเวศ
        self.play(
            Create(glass_inner),
            FadeIn(glass_outer),
            run_time=1.0,
        )
        self.play(
            FadeIn(soil_layer, shift=UP * 0.2),
            FadeIn(water_layer, shift=UP * 0.2),
            run_time=0.8,
        )
        self.play(
            Create(stem),
            GrowFromCenter(sun_group),
            run_time=0.9,
        )
        self.play(
            GrowFromCenter(leaf_left),
            GrowFromCenter(leaf_right),
            GrowFromCenter(leaf_top),
            Create(orbit_ring),
            FadeIn(orbit_nodes, scale=0.5),
            run_time=0.9,
        )

        # หมุนรังสีดวงอาทิตย์และวงโคจรต่อเนื่อง
        sun_rays.add_updater(lambda m, dt: m.rotate(0.6 * dt, about_point=sun_pos))
        orbit_ring.add_updater(lambda m, dt: m.rotate(-0.25 * dt, about_point=dome_center))

        # ==========================================================
        # ส่วนที่ 3: ข้อความหัวข้อการทดลอง (Title & Badge)
        # ==========================================================
        badge_text = Text(
            "การทดลองวิทยาศาสตร์",
            font=THAI_FONT,
            font_size=32,
            color=TEAL_A,
            weight=BOLD,
        )
        badge_box = SurroundingRectangle(
            badge_text,
            color=TEAL_B,
            buff=0.20,
            corner_radius=0.22,
            stroke_width=2.5,
        ).set_fill(TEAL_E, opacity=0.28)
        badge = VGroup(badge_box, badge_text).move_to(DOWN * 1.45)

        main_title = Text(
            "ระบบนิเวศ",
            font=THAI_FONT,
            font_size=82,
            weight=BOLD,
        ).set_color_by_gradient(GREEN_A, TEAL_A, WHITE)
        main_title.next_to(badge, DOWN, buff=0.40)

        sub_title = Text(
            "ECOSYSTEM SCIENCE EXPERIMENT",
            font="Segoe UI",
            font_size=22,
            color=GREY_B,
        ).next_to(main_title, DOWN, buff=0.35)

        line_left = Line(LEFT * 0.9, ORIGIN, color=GREEN_C, stroke_width=2.5).next_to(sub_title, LEFT, buff=0.22)
        line_right = Line(ORIGIN, RIGHT * 0.9, color=GREEN_C, stroke_width=2.5).next_to(sub_title, RIGHT, buff=0.22)

        self.play(
            FadeIn(badge, shift=UP * 0.25),
            run_time=0.7,
        )
        self.play(
            FadeIn(main_title, shift=UP * 0.25, scale=0.92),
            run_time=0.9,
        )
        self.play(
            FadeIn(sub_title),
            Create(line_left),
            Create(line_right),
            run_time=0.8,
        )

        self.wait(2.2)

        # ==========================================================
        # ส่วนที่ 4: จบ Intro เพื่อตัดเข้าสู่วิดีโอการทดลอง
        # ==========================================================
        sun_rays.clear_updaters()
        orbit_ring.clear_updaters()

        all_objects = VGroup(
            grid,
            particles,
            glass_outer,
            glass_inner,
            soil_layer,
            water_layer,
            stem,
            leaf_left,
            leaf_right,
            leaf_top,
            sun_group,
            orbit_ring,
            orbit_nodes,
            badge,
            main_title,
            sub_title,
            line_left,
            line_right,
        )
        self.play(FadeOut(all_objects, scale=1.05), run_time=1.0)
        self.wait(0.3)
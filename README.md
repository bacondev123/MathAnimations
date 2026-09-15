# 🎬 Math Animations with Manim

A boilerplate and workspace for creating 3Blue1Brown-style mathematical animations using Python and the **Manim Community Edition (ManimCE)** engine.

---

## 📽️ Showcase

<video src="https://github.com/user-attachments/assets/8e0d0ad1-9e24-4d3d-8dcc-3ae370d36f1a" controls="controls" style="max-width: 100%;"></video>

---

## 🛠️ Prerequisites

Before running the animations, ensure you have the following installed:

1. **Python 3.10+**
2. **FFmpeg** (Required for video encoding):
   * **Windows (via winget):**
     ```powershell
     winget install Gyan.FFmpeg
     ```
   * **macOS (via Homebrew):**
     ```bash
     brew install ffmpeg
     ```
   * **Linux (Ubuntu/Debian):**
     ```bash
     sudo apt install ffmpeg
     ```

---

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🎥 Rendering Animations

To render a scene from your Python file:

### Fast Preview (Low Quality - 480p, 15fps)
Ideal for testing alignments, timing, and layout:
```bash
python -m manim -pql main.py <SceneName>
```

### Final Export (High Quality - 1080p, 60fps)
Use this when you are ready to publish:
```bash
python -m manim -pqh main.py <SceneName>
```

> **Flags explanation:**
> * `-p`: Preview the video immediately after rendering finishes.
> * `-ql`: Quality Low (fast render).
> * `-qh`: Quality High (production ready).

Output video files are saved automatically in the `media/videos/` directory.

---

## 📂 Project Structure

```text
├── .gitignore          # Excludes media/, cache, and virtual environments
├── LICENSE             # Open-source license
├── README.md           # Project documentation and instructions
├── requirements.txt    # Python dependencies
└── main.py             # Animation scripts and scene definitions
```

# Math Animations with Manim

A starter template for creating mathematical animations using Python and [Manim Community Edition](https://www.manim.community/).

## Showcase

<video src="https://github.com/user-attachments/assets/8e0d0ad1-9e24-4d3d-8dcc-3ae370d36f1a" controls style="max-width: 100%;"></video>

## Prerequisites

- **Python 3.10+**
- **FFmpeg**:
  - macOS: `brew install ffmpeg`
  - Linux: `sudo apt install ffmpeg`
  - Windows: `winget install Gyan.FFmpeg`

## Setup

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
pip install -r requirements.txt
```

## Rendering

Run `manim` targeting the script and scene class:

```bash
# Preview (480p, 15 fps)
manim -pql main.py SceneName

# Production export (1080p, 60 fps)
manim -pqh main.py SceneName
```

Common flags:
- `-p`: Automatically play video once finished
- `-ql`: Low quality (fast preview)
- `-qh`: High quality (1080p)

Rendered videos are saved to `media/videos/`.

## Project Structure

```text
├── main.py             # Animation scenes
├── requirements.txt    # Dependencies
└── media/              # Rendered output (gitignored)
```

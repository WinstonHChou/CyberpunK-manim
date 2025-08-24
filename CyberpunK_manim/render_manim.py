from pathlib import Path
from manim_slides import Slide
from manim import config, tempconfig
import importlib.util
import sys
import subprocess

def render_and_convert_to_pptx(scene_file: str, scene_name: str, output_pptx: str, theme_layout: str = None):
    """
    Renders a Manim Slides scene using subprocess, then converts the result to PPTX using convert.py.
    Args:
        scene_file: Path to the .py file containing the Slide class (e.g., 'basic_example/example.py')
        scene_name: Name of the Slide class (e.g., 'BasicExample')
        output_pptx: Path to output PPTX file
        theme_layout: Path to theme layout PPTX (optional)
    """
    # 1. Render the slide using manim-slides CLI
    render_cmd = [
        "manim-slides", "render", scene_file, scene_name
    ]
    print(f"Running: {' '.join(render_cmd)}")
    subprocess.run(render_cmd, check=True)

    # 2. Convert to PPTX using convert.py
    convert_cmd = [
        "CyberpunK-manim", "convert", scene_name, output_pptx, "--to", "pptx"
    ]
    if theme_layout:
        convert_cmd.extend(["--use-layout", theme_layout])
    print(f"Running: {' '.join(convert_cmd)}")
    subprocess.run(convert_cmd, check=True)

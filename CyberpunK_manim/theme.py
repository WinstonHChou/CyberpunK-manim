from pptx import Presentation
from pathlib import Path
import os

# Parent directory of the current script
dir_path = os.path.dirname(os.path.abspath(__file__))
default_layout_path = f"{dir_path}/theme/CyberpunK-theme.pptx"

def get_pptx_presentation(layout_path: str | Path = None) -> Presentation:
    """
    Load and return a pptx.Presentation object for the given layout file.
    If layout_path is None, use the default layout.
    """
    if layout_path is None:
        layout_path = default_layout_path
    return Presentation(str(layout_path))

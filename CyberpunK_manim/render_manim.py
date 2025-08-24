import mimetypes
import subprocess
from collections import deque
from enum import Enum
from pathlib import Path
from typing import Optional, Union

import av
import pptx
from lxml import etree
from PIL import Image
from tqdm import tqdm
import subprocess

import pptx
from manim_slides.present import get_scenes_presentation_config
from manim_slides.config import PresentationConfig

class FrameIndex(str, Enum):
    first = "first"
    last = "last"

    def __repr__(self) -> str:
        return self.value
    
# From GitHub issue comment:
# - https://github.com/scanny/python-pptx/issues/427#issuecomment-856724440
def auto_play_media(
    media: pptx.shapes.picture.Movie, loop: bool = False
) -> None:
    el_id = xpath(media.element, ".//p:cNvPr")[0].attrib["id"]
    el_cnt = xpath(
        media.element.getparent().getparent().getparent(),
        f'.//p:timing//p:video//p:spTgt[@spid="{el_id}"]',
    )[0]
    cond = xpath(el_cnt.getparent().getparent(), ".//p:cond")[0]
    cond.set("delay", "0")

    if loop:
        ctn = xpath(el_cnt.getparent().getparent(), ".//p:cTn")[0]
        ctn.set("repeatCount", "indefinite")

def xpath(el: etree.Element, query: str) -> etree.XPath:
    nsmap = {"p": "http://schemas.openxmlformats.org/presentationml/2006/main"}
    return etree.ElementBase.xpath(el, query, namespaces=nsmap)

def read_image_from_video_file(file: Path, frame_index: "FrameIndex") -> Image:
    """Read a image from a video file at a given index."""
    with av.open(str(file)) as container:
        frames = container.decode(video=0)

        if frame_index == FrameIndex.last:
            (frame,) = deque(frames, 1)
        else:
            frame = next(frames)

        return frame.to_image()
    
class VideoData:
    def __init__(
        self,
        file: Path,
        mime_type: str,
        notes: Optional[str] = None,
        loop: bool = True,
        poster_frame: Union[FrameIndex, Image.Image] = FrameIndex.first,
    ):
        self.file = file
        self.mime_type = mime_type
        self.notes = notes
        self.loop = loop

        if isinstance(poster_frame, FrameIndex):
            self.poster_frame_image = read_image_from_video_file(file, poster_frame)
        else:
            self.poster_frame_image = poster_frame


def extract_embedded_videos(presentation_configs: list[PresentationConfig]):
    """
    Extracts video info from presentation configs and returns a list of VideoData objects.
    """
    videos = []
    for i, presentation_config in enumerate(presentation_configs):
        for slide_config in tqdm(
            presentation_config.slides,
            desc=f"Extracting video info for config {i + 1}",
            leave=False,
        ):
            file = slide_config.file
            mime_type = mimetypes.guess_type(file)[0]
            notes_text = slide_config.notes
            loop = getattr(slide_config, "loop", False)
            poster_frame = FrameIndex.first
            video = VideoData(
                file=file,
                mime_type=mime_type,
                notes=notes_text,
                loop=loop,
                poster_frame=poster_frame,
            )
            videos.append(video)
    return videos

def render_and_extract(scene_file: str, scene_name: str):
    """
    Renders a Manim Slides scene using subprocess, then converts the result to PPTX using convert.py.
    Args:
        scene_file: Path to the .py file containing the Slide class (e.g., 'basic_example/example.py')
        scene_name: Name of the Slide class (e.g., 'BasicExample')
    """
    # 1. Render the slide using manim-slides CLI (subprocess is fine for this)
    render_cmd = [
        "manim-slides", "render", scene_file, scene_name
    ]
    print(f"Running: {' '.join(render_cmd)}")
    subprocess.run(render_cmd, check=True)

    # 2. Get presentation configs
    folder = Path(scene_file).parent / "slides"
    scenes = [scene_name]
    presentation_configs = get_scenes_presentation_config(scenes, folder)

    # 3. Extract video info and return
    return extract_embedded_videos(presentation_configs)

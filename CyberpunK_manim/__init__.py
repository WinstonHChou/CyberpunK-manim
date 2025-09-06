# Expose main API
from .render_manim import render_and_extract, add_animation
from .theme import get_pptx_presentation, Color
from .pptx_slide_create import *

from pptx.util import *
from pptx.enum.text import PP_ALIGN
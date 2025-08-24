from CyberpunK_manim.render_manim import render_and_extract, auto_play_media
from CyberpunK_manim.theme import get_pptx_presentation

prs = get_pptx_presentation()

# Add a cover slide
cover = prs.slides[0]
cover.shapes.title.text = 'Cover Slide Title'
cover.shapes.placeholders[1].text = 'Cover Slide Content'

# Add a bullet slide
bullet_slide_layout = prs.slide_layouts[1]
slide = prs.slides.add_slide(bullet_slide_layout)
shapes = slide.shapes
title_shape = shapes.title
body_shape = shapes.placeholders[1]
title_shape.text = 'Adding a Bullet Slide'
tf = body_shape.text_frame
tf.text = 'Find the bullet slide layout'
p = tf.add_paragraph()
p.text = 'Use _TextFrame.text for first bullet'
p.level = 1
p = tf.add_paragraph()
p.text = 'Use _TextFrame.add_paragraph() for subsequent bullets'
p.level = 2

# Get animation videos from render_and_extract
videos = render_and_extract(
    scene_file="example_animation.py",
    scene_name="BasicExample"
)

# Add each video to a new blank slide and embed as movie
blank_slide_layout = prs.slide_layouts[1]
import tempfile
for video in videos:
    anim_slide = prs.slides.add_slide(blank_slide_layout)
    # Save poster frame image to a temporary file
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp_img:
        video.poster_frame_image.save(tmp_img.name)
        poster_frame_path = tmp_img.name
    # Embed the movie in the slide
    movie = anim_slide.shapes.add_movie(
        str(video.file),
        0, 0, prs.slide_width, prs.slide_height,
        poster_frame_image=poster_frame_path,
        mime_type=video.mime_type,
    )
    if video.notes != "":
        anim_slide.notes_slide.notes_text_frame.text = video.notes

    auto_play_media(movie, loop=video.loop)

prs.save('test.pptx')
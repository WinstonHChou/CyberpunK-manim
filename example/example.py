from CyberpunK_manim import render_and_extract, add_animation, get_pptx_presentation

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
    scene_name=["BasicExample", "BasicExample2"]
)

# Add each video to a new blank slide and embed as movie
blank_slide_layout = prs.slide_layouts[1]
for video in videos:
    anim_slide = prs.slides.add_slide(blank_slide_layout)
    add_animation(anim_slide, video, prs.slide_width/2, prs.slide_width/8, prs.slide_width/2, prs.slide_height/2)

prs.save('example.pptx')
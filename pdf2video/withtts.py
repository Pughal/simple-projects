# Step 1: Convert PDF Pages to Images
from pdf2image import convert_from_path
pdf_path = 'test.pdf'
images = convert_from_path(pdf_path, dpi=200, poppler_path=r'\.venv\poppler-24.08.0\Library\bin')
for i, image in enumerate(images):
    image.save(f'page_{i}.png', 'PNG')

# Step 2: Extract Text from PDF
import fitz  # PyMuPDF
pdf_texts = []
with fitz.open(pdf_path) as doc:
    for page_num in range(doc.page_count):
        text = doc[page_num].get_text("text")
        pdf_texts.append(text)

# Step 3: Convert Text to Audio
from gtts import gTTS
for i, text in enumerate(pdf_texts):
    tts = gTTS(text, lang='en')
    tts.save(f"audio_page_{i}.mp3")

# Step 4: Combine Images and Audio into Video
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
video_clips = []
for i in range(len(images)):
    image_clip = ImageClip(f'page_{i}.png').set_duration(5)
    audio_clip = AudioFileClip(f"audio_page_{i}.mp3")
    image_clip = image_clip.set_audio(audio_clip).set_duration(audio_clip.duration)
    video_clips.append(image_clip)

final_video = concatenate_videoclips(video_clips, method="compose")
final_video.write_videofile("output_video_with_narration.mp4", codec="libx264", fps=24)


from pdf2image import convert_from_path

pdf_path = 'test.pdf'
images = convert_from_path(pdf_path, dpi=200, poppler_path=r'\.venv\poppler-24.08.0\Library\bin')  # Adjust DPI for quality
for i, image in enumerate(images):
    image.save(f'page_{i}.png', 'PNG')  # Save each page as an image



from moviepy.editor import ImageSequenceClip

# List all saved images in order
image_files = [f'page_{i}.png' for i in range(len(images))]
clip = ImageSequenceClip(image_files, fps=1)  # 1 fps means 1 image per second
clip.write_videofile('output_video.mp4', codec='libx264')



from moviepy.editor import AudioFileClip

# Load the audio file
audio_clip = AudioFileClip('background_audio.mp3')  # Replace with your audio file
# Set the audio to the video clip
clip = clip.set_audio(audio_clip)
# Write the video file
clip.write_videofile('output_video_with_audio.mp4', codec='libx264', fps=1)



from PIL import Image, ImageDraw, ImageFont

for i in range(len(images)):
    image = Image.open(f'page_{i}.png')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 20)  # Change font and size as needed
    draw.text((10, 10), f"Page {i+1}", fill="black", font=font)  # Text position and color
    image.save(f'annotated_page_{i}.png')  # Save the annotated image



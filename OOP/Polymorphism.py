# Poly means many, Morphe means forms
# Method Overriding (Polymorphism in Inheritance)

class MediaRenderer:
    def render(self):
        print("Rendering a generic media file...")

class VideoRenderer(MediaRenderer):
    def render(self):
        print("Rendering a high-resolution video file...")

class AudioRenderer(MediaRenderer):
    def render(self):
        print("Rendering an audio file with enhanced sound quality...")


# Creating objects
video = VideoRenderer()
audio = AudioRenderer()

# Directly calling render() – Polymorphism in action!
video.render()
audio.render()

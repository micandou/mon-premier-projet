from kivy.app import App
from kivy.uix.label import Label

class EmojiApp(App):
    def build(self):
        return Label(text="Je suis fort 💪", font_size='24sp')

if __name__ == "__main__":
    EmojiApp().run()
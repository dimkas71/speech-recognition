from kivy.app import App
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget


class VoiceDrawerWidget(Widget):
    counter = NumericProperty(0)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update_counter, 1)

    def update_counter(self, timeout):
        self.counter += int(timeout)


class VoiceDrawerApp(App):

    def build(self):
        return VoiceDrawerWidget()


if __name__ == '__main__':
    VoiceDrawerApp().run()

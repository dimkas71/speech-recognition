# Uncomment these lines to see all the messages
import random
import threading
import time
from typing import List

# from kivy.logger import Logger
# import logging
# Logger.setLevel(logging.INFO)

from kivy.app import App
from kivy.clock import mainthread
from kivy.graphics import Color, Rectangle, InstructionGroup
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout


class TaggedInstructionGroup(InstructionGroup):

    def __init__(self, tag, **kwargs):
        super().__init__(**kwargs)
        self.tag = tag


class VoiceWidget(BoxLayout):
    event = threading.Event()
    recognized_text = StringProperty("Recognized text")  #TODO: make a localization in the next release
    tagged_instructions = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids['voice_btn'].bind(on_press=self.on_press)
        self._background_thread = None

    def on_press(self, instance):
        if not self.event.is_set():
            self.event.set()
        self._background_thread = threading.Thread(target=self.recognize, args=(instance,))
        self._background_thread.start()

    def recognize(self, button):
        time.sleep(2)
        self.on_recognize()

    @mainthread
    def on_recognize(self):
        self.ids['voice_btn'].state = 'normal'
        self.recognized_text = f'You said: draw rectangle {random.randint(1, 100)}'

        tg = self._find_by_tag("hello")
        if not tg:
            group = TaggedInstructionGroup("hello")

            group.add(Color(0., 1., 0.5))
            group.add(Rectangle(pos=(random.randint(300, 800), random.randint(50, 200)), size=(20, 20)))
            self._add(group)

            tg = group

        with self.canvas:
            self.canvas.add(tg)

    #region operations with tagged instructions
    def _add(self, tagged_group):
        if not self._find_by_tag(tagged_group.tag):
            self.tagged_instructions.append(tagged_group)

    def _find_by_tag(self, tag):
        tagged_group = None
        for tg in self.tagged_instructions:
            if tg.tag != tag:
                continue
            tagged_group = tg
            break
        return tagged_group

    def _remove_with_tag(self, tag):
        for tg in self.tagged_instructions:
            if tg.tag != tag:
                continue
            self.tagged_instructions.remove(tg)
            break
    def _remove_all(self):
        self.tagged_instructions.clear()
    #end region


class VoiceDrawerApp(App):

    def build(self):
        return VoiceWidget()


if __name__ == '__main__':
    VoiceDrawerApp().run()

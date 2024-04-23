# Uncomment these lines to see all the messages
import logging
import threading
import time

from kivy.logger import Logger

from src.command import CommandResolver
from voice_recognition import GoogleVoiceRecognizer

Logger.setLevel(logging.INFO)

from kivy.app import App
from kivy.clock import mainthread
from kivy.graphics import InstructionGroup
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
        self._voice_recognizer = GoogleVoiceRecognizer() #TODO: Add DI support to inject recognizer here...

    def on_press(self, instance):
        if not self.event.is_set():
            self.event.set()
        self._background_thread = threading.Thread(target=self.recognize)
        self._background_thread.start()

    def recognize(self):
        time.sleep(2)
        #text = self._voice_recognizer.recognize()
        text = self.ids['emul_txt'].text
        self.on_recognize(text)

    @mainthread
    def on_recognize(self, rec_text):
        Logger.info(f"Command: {rec_text}")
        command = CommandResolver.resolve(rec_text)
        self._set_btn_state_to_normal()
        self._update_recognized_text(f'You said: {rec_text}')
        #
        # tg = self._find_by_tag("hello")
        # if not tg:
        #     group = TaggedInstructionGroup("hello")
        #
        #     group.add(Color(0., 1., 0.5))
        #     group.add(Rectangle(pos=(random.randint(300, 800), random.randint(50, 200)), size=(20, 20)))
        #     self._add(group)
        #
        #     tg = group
        #
        # with self.canvas:
        #     self.canvas.add(tg)
        command.execute(self.canvas)

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

    #endregion

    #region internal handlers
    def _set_btn_state_to_normal(self):
        self.ids['voice_btn'].state = 'normal'

    def _update_recognized_text(self, new_text):
        self.recognized_text = new_text
    #endregion


class VoiceDrawerApp(App):

    def build(self):
        return VoiceWidget()


if __name__ == '__main__':
    VoiceDrawerApp().run()

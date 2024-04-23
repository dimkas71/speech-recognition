import os
from abc import ABCMeta, abstractmethod

import speech_recognition as sp

from speech_recognition import UnknownValueError, RequestError
from pocketsphinx import LiveSpeech

import logging
from kivy.logger import Logger

Logger.setLevel(logging.INFO)


class Recognizer(metaclass=ABCMeta):

    @abstractmethod
    def recognize(self) -> str:
        ...


class VoskVoiceRecognizer(Recognizer):
    #TODO: add Vosk based implemetation Of Recognizer

    def recognize(self) -> str:
        pass


class SphinxVoiceRecognizer(Recognizer):
    UNRECOGNIZED_TEXT = "Unrecognized text"

    def __init__(self):
        os.environ['POCKETSPHINX_DATA'] = '/home/dimkas71/tmp/pocketsphinx/model'

    def recognize(self) -> str:
        phrases = LiveSpeech()
        if not phrases[-1]:
            return self.UNRECOGNIZED_TEXT
        return phrases[-1]

class GoogleVoiceRecognizer(Recognizer):
    UNRECOGNIZED_TEXT = "Unrecognized text"

    def __init__(self):
        super().__init__()
        self._recognizer = sp.Recognizer()
        self._microphone = sp.Microphone()

    def recognize(self) -> str:
        with self._microphone as m:
            self._recognizer.adjust_for_ambient_noise(m)
        try:
            audio = None
            with self._microphone as m:
                audio = self._recognizer.listen(m)
            recognized_text = self._recognizer.recognize_google(audio)
            return recognized_text
        except (UnknownValueError, RequestError) as e:
            Logger.info(f"Error message {e.args[0]}")
            return self.UNRECOGNIZED_TEXT

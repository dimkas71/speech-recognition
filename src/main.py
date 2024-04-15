from kivy.app import App
from kivy.clock import Clock
from kivy.event import EventDispatcher
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget


class CounterUpdateDispatcher(EventDispatcher):
    counter = NumericProperty(0)

    def __init__(self, *args, **kwargs):
        self.register_event_type('on_counter_updated')
        super(CounterUpdateDispatcher, self).__init__(*args, **kwargs)
        Clock.schedule_interval(self.update_counter, 1)

    def update_counter(self, timeout):
        self.counter += timeout
        self.dispatch('on_counter_updated', self.counter)


    def on_counter_updated(self, *args):
        ...


class VoiceDrawerWidget(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._dispatcher = CounterUpdateDispatcher()
        self._dispatcher.bind(on_counter_updated=self.on_counter_updated)

    def on_counter_updated(self, *args):
        if args[1]:
            self.ids['lbl'].text = 'Current tick: {}'.format(int(args[1]))


class VoiceDrawerApp(App):

    def build(self):
        return VoiceDrawerWidget()


if __name__ == '__main__':
    VoiceDrawerApp().run()

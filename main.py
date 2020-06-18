import kivy
from kivy.app import App
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
from time import strftime


class StopWatch(App):
    starting_seconds = 0 #to start at zero seconds
    watch_started = False #So is does not start automatically
    Window.size = (300,500)

    def on_start(self):
        Clock.schedule_interval(self.update, 0)

    def update(self, nap):
        if self.watch_started:
            self.starting_seconds += nap

        self.root.ids.time.text = strftime('[b]%H[/b]:%M:%S')

        m, s = divmod(self.starting_seconds, 60)
        self.root.ids.stopwatch.text = ('%02d:%02d.[size=40]%02d[/size]' %
                                        (int(m), int(s), int(s * 100 % 100)))

    def start_stop(self):
        self.root.ids.start_stop.text = 'Start' if self.watch_started else 'Stop'
        self.watch_started = not self.watch_started

    def reset_button(self):
        if self.watch_started:
            self.root.ids.start_stop.text = 'Start'
            self.watch_started = False

        self.starting_seconds = 0

if __name__ == '__main__':
    StopWatch().run()

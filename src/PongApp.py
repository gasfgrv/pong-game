from kivy.app import App
from kivy.clock import Clock

from src.PongGame import PongGame


class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

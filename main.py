from model.game import ReversiGame
from view.game_console_view import GameConsoleView
from controller.game_controller import GameController


model = ReversiGame()
view = GameConsoleView(model)
controller = GameController(model, view)

controller.run_game()


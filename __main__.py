import random
from game.director import Director
from game.actor import Actor
from game.squares import Squares
from game.draw_squares import DrawSquares
from game.location import Location
from game.input_service import InputService
from game.output_service import OutputService
from game.clear_squares import ClearSquares
from game.choose_square import ChooseSquare
from game.handle_selection_squares import HandleSelectionSquare
from asciimatics.screen import Screen

def main(screen):
    cast = {}
    script = {}

    input_service = InputService(screen)
    output_service = OutputService(screen)
    draw_squares = DrawSquares(output_service)
    clear_squares = ClearSquares()
    choose_square = ChooseSquare
    handle_selection_square = HandleSelectionSquare()
    

    script['input'] = [choose_square]
    script['update'] = [clear_squares, handle_selection_square]
    script['output'] = [draw_squares]

    director = Director(cast, script)
    director.start_game()
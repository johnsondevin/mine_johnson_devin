import random
from game.director import Director
from game.actor import Actor
from game.squares import Squares
from game.draw_squares import DrawSquares
from game.location import Location
from game.input_service import InputService
from game.output_service import OutputService
from game.clear_squares import ClearSquares
from asciimatics.screen import Screen

def main(screen):
    cast = {}
    script = {}

    input_service = InputService(screen)
    output_service = OutputService(screen)
    draw_squares = DrawSquares()
    clear_squares = ClearSquares(output_service)
    

    script['input'] = []
    script['update'] = []
    script['output'] = []

    director = Director(cast, script)
    director.start_game()
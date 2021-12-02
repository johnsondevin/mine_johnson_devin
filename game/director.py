class Director:
    def __init__(self):
        pass

    def start_game(self):
        while True:
            self._cue_action('input')
            self._cue_action('update')
            self._cue_action('output')

    def _cue_action(self, tag):
        for action in self._script[tag]:
            action.execute(self._cast)
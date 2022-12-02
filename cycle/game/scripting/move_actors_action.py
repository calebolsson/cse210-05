from game.scripting.action import Action


class MoveActorsAction(Action):
    """
    An update action that handles the movement of each actor on the stage.

    Attributes:
        * none for now
    """

    def __init__(self) -> None:
        super().__init__()

    def execute(self, cast, script):
        actors = cast.get_all_actors()
        for actor in actors:
            actor.move_next()
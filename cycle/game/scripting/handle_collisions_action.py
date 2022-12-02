import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point


class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.

    The responsibility of HandleCollisionsAction is to handle the situation when the cycle collides
    with the upgrade, or the cycle collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_upgrade_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _handle_upgrade_collision(self, cast):
        """Updates the score nd moves the upgrade if the cycle collides with the upgrade.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        scores = cast.get_actors("scores")
        upgrade = cast.get_first_actor("upgrades")
        cycles = cast.get_actors("cycles")
        head = [cycles[0].get_head(), cycles[1].get_head()]

        for x in [0, 1]:
            cycles[x].grow_tail(1)
            scores[x].add_points(1)
            if head[x].get_position().equals(upgrade.get_position()):
                points = upgrade.get_points()
                cycles[x].grow_tail(points)
                scores[x].add_points(points)
                upgrade.reset()

    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the cycle collides with one of its segments.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        cycles = cast.get_actors("cycles")
        head = [cycles[0].get_segments()[0], cycles[1].get_segments()[0]]
        segments = cycles[0].get_segments()[1:] + cycles[1].get_segments()[1:]

        for segment in segments:
            if head[0].get_position().equals(segment.get_position()):
                self._is_game_over = True
                pass
            if head[1].get_position().equals(segment.get_position()):
                self._is_game_over = True
                pass

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the cycle and upgrade white if the game is over.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            cycles = cast.get_actors("cycles")
            segments = cycles[0].get_segments() + cycles[1].get_segments()
            upgrade = cast.get_first_actor("upgrades")

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments:
                segment.set_color(constants.WHITE)
            upgrade.set_color(constants.WHITE)

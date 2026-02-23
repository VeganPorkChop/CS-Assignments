"""
Author: Graham Gilbert-Schroeer
Starting Date: 2/22/26

Contraption definitions for Cats vs Homework
"""

from src.managers import GameManager, Actor, Tile
from src.cats import Cat


class Contraption(Actor):
    """
    Base class that represents all contraptions
    """

    _cost: int
    """
    Cost (in batteries) to place this contraption
    """

    def __init__(self, image_name: str, cost: int):
        """
        Initializes this contraption with a positive cost
        """
        super().__init__(image_name)
        assert isinstance(cost, int) and cost >= 0
        self._cost = cost

    def cost(self) -> int:
        """
        Returns the cost in batteries for this contraption
        """
        return self._cost

    def place(self, tile: 'Tile'):
        """
        Places this contraption on the board
        """
        assert isinstance(tile, Tile)
        GameManager.manager().add_contraption(self)
        self.teleport(tile)

    def end_round(self):
        """
        Takes some action as a contraption
        By default, a contraption does nothing at the end of the round
        """
        pass

    def interact(self):
        """
        A cat interacts with this contraption
        Any interaction immediately knocks the base contraption over
          and removes it from the board
        """
        self.tile().clear_actor()
        self._tile = None
        GameManager.manager().remove_contraption(self)


class LaserPointer(Contraption):
    """
    Each round, points a laser to attempt to distract the first cat in its lane
    """

    def __init__(self):
        """
        The constructor for a LaserPointer
        Laser pointers have an image name 'laser' and cost 7 batteries
        """
        super().__init__('laser', 7)

    def end_round(self):
        """
        A laser pointer distracts the first cat in its lane
        """
        next = self._tile.entrance()
        while next is not None:
            if isinstance(next.actor(), Cat):
                next.actor().distract(1)
                return  # we can simply return when we find a cat
            next = next.entrance()

# Part 1: "Basic Contraptions"


class SnackDispenser(Contraption):
    """
    A Snack dispenser does nothing by itself, but can be interacted with
      a total of 5 times before being knocked over
    """

    _uses: int

    def __init__(self):
        """
        The constructor for a SnackDispenser
        Snack dispensers have an image name of 'snacks' and cost 4 batteries
        """
        super().__init__('snacks', 4)
        self._uses = 0

    def interact(self):
        self._uses+=1
        if self._uses >= 5:
            self._tile = None
            GameManager.manager().remove_contraption(self)
            


class BatteryCharger(Contraption):
    """
    Every other round, charges a new battery
    Does not charge a battery the round it is placed
    """
    _ready: bool

    def __init__(self):
        """
        The constructor for a BatteryCharger
        Battery chargers have an image name 'charger' and cost 3 batteries
        """
        super().__init__("charger", 3)
        self._ready = False

    def end_round(self):
        """
        A laser pointer distracts the first cat in its lane
        """
        self._ready != self._ready
        if self._ready:
            GameManager.manager().add_batteries(1)
        next = self._tile.entrance()
        while next is not None:
            if isinstance(next.actor(), Cat):
                self._tile = None
                GameManager.manager().remove_contraption(self)
                return  # we can simply return when we find a cat
            next = next.entrance() 

class BallThrower(Contraption):
    """
    Each round, throws a ball to distract the nearest Cat within 3 spaces
    If there is no such Cat, this contraption does nothing
    """

    def __init__(self):
        """
        The constructor for a BallThrower
        Ball throwers have an image name 'thrower' and cost 3 batteries
        """
        # TODO: Implement me!
        super().__init__('empty', 100)

    # TODO: potentially override more methods of Contraption

# Part 3: "Advanced Contraptions"
# We recommend adding more Cats before implementing these contraptions


class TripleLaserPointer(Contraption):
    """
    Each round, points a laser to attempt to distract the first cat in its lane
      _and_ a cat in both the lane above and below this contraption
    """

    def __init__(self):
        """
        The constructor for a TripleLaserPointer
        Triple laser pointers have an image name 'triple_laser' and cost 12 batteries
        """
        # TODO: Implement me!
        super().__init__('empty', 100)

    # TODO: potentially override more methods of Contraption


class ColorfulBallThrower(Contraption):
    """
    Each round, throws a ball to distract the nearest Cat within 3 spaces
    If there is no such Cat, adds a colorful ball to the furthest empty space
      within the 3-space range of this colorful ball thrower
    """

    def __init__(self):
        """
        The constructor for a ColorfulBallThrower
        Colorful ball throwers have an image name 'colorful_thrower' and cost 5 batteries
        """
        # TODO: Implement me!
        super().__init__('empty', 100)

    # TODO: potentially override more methods of Contraption and/or update Cat
    # Note that you are permitted to change this to be a child class of BallThrower
    #   though this may or may not be easier than just keeping this directly inheriting from Contraption

    # Hint: consider creating a new Actor class to represent the colorful ball that gets placed
    # Note that a colorful ball has the image name colorful_ball
    # Specifically note the set_actor and clear_actor methods in Tile


class SpaceHeater(Contraption):
    """
    This Contraption, by itself, does nothing
    However, any cat that ends a move within a range of two of this Contraption
      is distracted for exactly one point
    """

    def __init__(self):
        """
        The constructor for a SpaceHeater
        Space heaters have an image name 'heater' and cost 4 batteries
        """
        # TODO: Implement me!
        super().__init__('empty', 100)

    # TODO: potentially update Cat to work with the space heater
    # Note that the space heater does not distract the cat during its action...

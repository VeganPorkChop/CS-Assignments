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
        self._uses += 1
        if self._uses >= 5:
            # Call parent's interact to properly remove
            super().interact()
            


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
        if self._ready:
            GameManager.manager().add_batteries(1)
        next = self._tile.entrance()
        while next is not None:
            if isinstance(next.actor(), Cat):
                # Use interact() to properly remove
                self.interact()
                return  # we can simply return when we find a cat
            next = next.entrance() 
        self._ready = not self._ready

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
        super().__init__('thrower', 3)

    def end_round(self):
        location = self._tile
        for _ in range(3):
            location = location.entrance()
            if location is None:
                return
            if isinstance(location.actor(), Cat):
                location.actor().distract(1)
                return

             

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
        super().__init__('triple_laser', 12)

    def end_round(self):
        """
        A laser pointer distracts the first cat in its lane
        """
        next = [self._tile.entrance(),self._tile.above().entrance(),self._tile.below().entrance()]
        for i in range(len(next)):
            while next[i] is not None:
                if isinstance(next[i].actor(), Cat):
                    next[i].actor().distract(1)
                    return
                next[i] = next[i].entrance()

class ColorfulBall(Contraption):
    def __init__(self):
        # colorful balls are temporary contraptions with no cost
        super().__init__('colorful_ball', 0)

    def interact(self):
        if not self.is_on_board():
            return
        target_tile = self.tile()
        entrance_tile = target_tile.entrance()
        if entrance_tile is not None and isinstance(entrance_tile.actor(), Cat):
            cat = entrance_tile.actor()
            cat.distract(1)
            # remove the ball first, then teleport the cat into this tile
            super().interact()
            cat.teleport(target_tile)

    


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
        super().__init__('colorful_thrower', 5)
    
    def end_round(self):
        location = self._tile
        furthest_empty = None
        for _ in range(3):
            location = location.entrance()
            if location is None:
                break
            if location.is_empty():
                furthest_empty = location
            if isinstance(location.actor(), Cat):
                location.actor().distract(1)
                return
        if furthest_empty is not None:
            ColorfulBall().place(furthest_empty)

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
        super().__init__('heater', 4)

    # TODO: potentially update Cat to work with the space heater
    # Note that the space heater does not distract the cat during its action...

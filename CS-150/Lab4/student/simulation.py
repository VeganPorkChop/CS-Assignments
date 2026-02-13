"""
Author: YOUR NAME HERE
Starting Date: YOUR STARTING DATE HERE

Initial creation by Dietrich Geisler on 10/25/2025

Implementation of a simple traffic stop simulation
"""

# Imports and constant definitions
import random

# How much time it takes to go from one light to the next
TRAVEL_TIME = 15

# Travel variation to account for faster or slower cars
TRAVEL_VARIATION = 5

# The random variation (in time steps) between when cars enter the simulation
SPAWN_VARIATION = 3


# Part 1: Light
# ----------------------------------------------

class Light:
    """
    Defines a traffic light with a queue of waiting cars

    Attributes:
        id: A unique id for this Light (1-indexed)
        is_green: True if this light is green, and False otherwise
        max_countdown: How many total timesteps between each light switch
        countdown: How many timesteps until this light switches between Red and Green
        queue: A queue of Cars looking to pass through this traffic light
    """
    _NEXT_ID = 1
    id: int
    is_green: bool
    max_countdown: int
    countdown: int
    queue: list['Car']

    def __init__(self, max_countdown: int, initial_countdown: int):
        """Constructor for Light

        Initially sets this light to be Red (is_green to False)
        As well as the queue to be empty

        Arguments:
            max_countdown: How many total timesteps between each light switch
                           Must be a positive non-zero number
            initial_countdown: How many timesteps until the first light switch
                               Must be a positive non-zero number
        """
        assert type(max_countdown) == int
        assert type(initial_countdown) == int
        assert max_countdown > 0
        assert initial_countdown > 0

        self.id = Light._NEXT_ID
        Light._NEXT_ID += 1

        self.is_green = False
        self.max_countdown = max_countdown
        self.countdown = initial_countdown
        self.queue = []

    @staticmethod
    def reset_ids():
        """Reset Light ids back to 1 (useful for deterministic tests)."""
        Light._NEXT_ID = 1

    def __str__(self) -> str:
        """Returns a string representation of this Light"""

        color = 'Green' if self.is_green else 'Red'
        return f'Light (id: {self.id}): {color}'

    def __repr__(self) -> str:
        """Returns a debugging-friendly representation of this Light"""

        return f'Light(id={self.id}, is_green={self.is_green}, ' + \
            f'max_countdown={self.max_countdown}, ' + \
            f'countdown={self.countdown}, ' + \
            f'queue_length={self.queue_length()})'

    def add_car_to_queue(self, car: 'Car'):
        """Adds a Car to the queue of Cars waiting at this Light"""
        # TODO: Implement me!

        return

    def queue_length(self) -> int:
        """Returns the number of Cars waiting in this Light's queue"""
        # TODO: Implement me!

        return

    def advance_queue(self) -> 'Car':
        """Advances the queue of this Light by one and returns the passing car

        Recall that a queue allows the car that arrived first to pass through first
        This function errors if there are no Cars in the queue

        HINT: you can use an assert to error explicitly,
              or you can call a built-in list function that produces
              an error when the queue is empty

        Returns:
            The Car that was removed from the queue
        """
        # TODO: Implement me!

        return Car()

    def can_go(self) -> bool:
        """Indicates whether or not cars can pass through this Light

        Cars can only pass through this Light if the Light is green _and_
        at least one timestep has passed since this Light turned green

        This delay is meant to simulate the reaction time of drivers
          who (by casual observation) take ~3 seconds to start driving

        Returns:
            True if Cars can pass through this Light, and False otherwise
        """
        # TODO: Implement me!

        return False

    def timestep(self):
        """Advances time for this Light by a single timestep (3 seconds of real time)

        Specifically, all of the following happen:
        1. the countdown of this Light decreases by one
        2. if the countdown has reached zero:
           a. this light changes color
           b. the countdown is reset to max_countdown
        """
        # TODO: Implement me!

        return


# Part 2: Car
# ----------------------------------------------

class Car:
    """Represents a single Car driving through traffic lights

    Note that a Car keeps track of all Lights it must travel through
    Distance between each Light is stored as a number of timesteps
    (That is, we don't model any physics of a real car, just time spent moving)

    Attributes:
        id: A unique id for this Car (1-indexed)
        current_light: The Light this Car is currently stopped at,
                       Or None if this Car is currently traveling to the next Light

        remaining_lights: An ordered list of all Lights this Car must still pass through
                          NOTE: the first light in this list is the first light this Car reaches
                          That is, this list is ordered from closest to furthest Light

        travel_time: The number of timesteps until this Car reaches the next Light
                     When this Car is stopped at a Light, this can be any number
    """
    _NEXT_ID = 1
    id: int
    current_light: Light | None
    remaining_lights: list[Light]
    travel_time: int

    def __init__(self, lights: list[Light]):
        """Constructor for the Car object

        This Car is initially not at a Light, but is setup to reach
          the first Light after exactly one timestep

        Arguments:
            lights: the ordered list of Lights this Car must pass through
                    note that this list may be modified by Car

        """
        assert isinstance(lights, list)
        for light in lights:
            assert isinstance(light, Light)

        self.id = Car._NEXT_ID
        Car._NEXT_ID += 1

        self.current_light = None
        self.remaining_lights = lights
        self.travel_time = 1

    @staticmethod
    def reset_ids():
        """Reset Car ids back to 1 (useful for deterministic tests)."""
        Car._NEXT_ID = 1

    def __str__(self) -> str:
        """Returns a string representation of this Car"""

        return f'Car (id: {self.id})'

    def __repr__(self) -> str:
        """Returns a debugging-friendly representation of this Car"""

        return f'Car(id={self.id}, current_light={self.current_light}, ' + \
            f'num_remaining_lights={len(self.remaining_lights)}, ' + \
            f'travel_time={self.travel_time})'

    def number_of_lights(self) -> int:
        """Returns the number of Lights this Car must still pass through"""
        # TODO: Implement me!

        return 0

    def is_at_light(self) -> bool:
        """Returns whether or not this Car is currently stopped at a Light

        Returns:
            True if this Car is stopped at a Light, or False otherwise
        """

        # TODO: Implement me!

        return False

    def start_going(self):
        """Updates this Car to stop waiting at the current Light
           so that it can start traveling to the next Light

        This also sets the number of timesteps until this Car reaches the next Light
        The number of timesteps is based on the two constants defined above:
            TRAVEL_TIME
            TRAVEL_VARIATION

        Specifically, the travel time for this Car is set to a random integer in the range:
          [TRAVEL_TIME, TRAVEL_TIME + TRAVEL_VARIATION] (inclusive)

        HINT: Recall that Python provides a function for this in random.randint
        """
        # TODO: Implement me!

        return

    def timestep(self):
        """Advances time for this Car by a single timestep (3 seconds of real time)

        Specifically, all of the following happen:
        1. if this Car is at a light, nothing changes
        2. Otherwise, reduce travel_time by one
        3. If travel time reaches zero, then the following occur
           a. This Car removes that light from its list of remaining_lights
           b. This Car stops at that light
           c. This Car is added to back of the queue of the Light it stopped at

        NOTE: if this Car would reach a Light in this timestep, but has no remaining lights,
              then this function raises an error

        HINT: you can use an assert to error explicitly,
              or you can call a built-in list function that produces
              an error when the list of lights is empty
        """

        # TODO: Implement me!

        return


# Part 3: Simulation
# ----------------------------------------------

class Simulation:
    """Represents and controls a single traffic light simulation

    For a description of the Simulation behavior, see the lab4.md document

    Can be stepped through for a single timestep using the timestep() method
    Or can be run for a fixed number of timesteps using the run() method

    Attributes:
        lights: an ordered list of all Lights in this simulation
                lights are ordered so that the closest to our incoming Cars
                  is in front of the list, while the furthest is in the back of the list

        cars: an unordered list of Cars

        timestep_count: how many timesteps have passed in this Simulation

        spawn_time: how many (baseline) timesteps pass before a new Car is added
    """
    lights: list[Light]
    cars: list[Car]
    timestep_count: int
    spawn_time: int

    def __init__(self, light_count, light_change_length, light_offset, spawn_time):
        """Constructor for a new Simulation

        Arguments:
            light_count: the number of lights in this simulation
            light_change_length: how many timesteps pass before a Light changes color
            light_offset: how far "offset" each light starts
                          for example, if offset is 1, then each light starts 
                            its countdown 1 timestep earlier than the light before
            spawn_time: how many (baseline) timesteps pass before a new Car is added
        """
        self.lights = []
        for index in range(light_count):
            light_countdown = ((index * light_offset) %
                               light_change_length) + 1
            self.lights.append(Light(light_change_length, light_countdown))
        self.spawn_time = spawn_time
        self.cars = []
        self.spawn_countdown = 1
        self.timestep_count = 0

    def __str__(self) -> str:
        """Returns a formatted string representation of this Simulation

        This string representation is best understood by example
        See the attached .txt examples as illustrations of this representation
        """

        # Build up a string starting wih the simulation
        result = f'Simulation of {len(self.lights)} light(s)\n'
        result += f'Timestep: {self.timestep_count}\n'
        result += '========================\n\n'
        result += 'START\n'
        for index in range(len(self.lights)):
            # First, get the cars that haven't yet reached the next light
            target_light_count = len(self.lights) - index
            for car in self.cars:
                if not car.is_at_light() and car.number_of_lights() == target_light_count:
                    result += f'{car}\n'

            # Add spacing between the cars and the light
            result += '\n...\n\n'

            # For each light, get the light string and each car at the light
            light = self.lights[index]
            for car in light.queue:
                result += f'{car}\n'
            result += f'{light}\n---\n'

        result += 'FINISH\n'
        return result

    def __repr__(self) -> str:
        """Returns a debugging-friendly representation of this Simulation"""

        return f'Simulation(num_lights={len(self.lights)}, ' + \
            f'num_cars={len(self.cars)}' + \
            f'spawn_time={self.spawn_time}' + \
            f'spawn_countdown={self.spawn_countdown})'

    def number_of_lights(self) -> int:
        """Returns the number of lights managed by this Simulation"""

        # TODO: Implement me!

        return 0

    def active_cars(self) -> int:
        """Returns the number of Cars currently tracked by this simulation"""

        # TODO: Implement me!

        return 0

    def waiting_car_count(self) -> int:
        """Returns the total number of Cars currently waiting at traffic lights in this Simulation

        This number includes all Cars waiting at all traffic lights
        But does not include Cars traveling between traffic lights
        """

        # TODO: Implement me!

        return 0

    def car_counts(self) -> list[int]:
        """Calculates the number of Cars waiting at each traffic light

        For example, if there are 3 traffic lights in this Simulation
        Then the returned list would have the following values:
            [Number of Cars at the 1st traffic light,
             Number of Cars at the 2nd traffic light,
             Number of Cars at the 3rd traffic light]

        Returns:
            A list where each index i is the number of Cars waiting at the (i+1)th traffic light
        """
        # TODO: Implement me!

        return []

    def timestep(self):
        """Advances this Simulation by exactly 1 timestep

        When a timestep (3 real seconds) advances, the following occur:
        1. timestep_count increases by 1
        2. For each Light, the following occur
           a. Advances that Light by one timestep
           b. If a Car can go through the Light and the Light has a Car queued up, 
              permits the first Car in the Light queue through the Light
           c. If a Car passes through the last Light, removes that Car from self.cars
              (it is no longer being tracked by this simulation)
        3. After advancing each Light, advance each Car by one timestep
        4. After advancing each Car, reduce spawn_countdown by one
        5. If spawn_countdown reaches zero, the following occur
           a. Creates a new Car and add it to the list of Cars
           b. Set the spawn countdown to start waiting for a new Car

        The number of timesteps to wait for spawning a new car is based on the following two values:
            self.spawn_time
            SPAWN_VARIATION (a constant defined above)

        Specifically, the spawn time for a new Car is set to a random integer
          such that the number of steps is in the range:
          [self.spawn_time, self.spawn_time + SPAWN_VARIATION] (inclusive)

        HINT: when creating a new Car, recall that Cars may adjust the list you provide
              you may want to be careful about passing in self.lights directly...
        """

        # TODO: Implement me!

        return

    def run(self, timesteps: int):
        """Advances this simulation by a fixed number of timesteps

        Each timestep is applied as described in the timestep() method

        Arguments:
            timesteps: the number of timesteps to advance this simulation
        """

        # TODO: Implement me!

        return


# Simulation Demonstration
# ----------------------------------------------

def main():
    """A demonstration of the working simulation

    Writes the result of this simulation to the local file 'simulation_result.txt'
    """

    # A rather powerful operation that "fixes" randomness for random.randint and related functions
    # This allows us to have consistent (though not predictable) results when testing
    random.seed(0)

    # Get user input
    light_count = int(input('Give a number of lights: '))
    light_change_length = int(
        input('Give a number of timesteps before lights change: '))
    light_offset = int(
        input('Give the timestep "offset" between the starting lights: '))
    spawn_length = int(
        input('Give the timestep count between each car spawning: '))
    timesteps = int(
        input('Give the number of timesteps to run the simulation: '))

    # Create and run the simulation
    simulation = Simulation(
        light_count, light_change_length, light_offset, spawn_length)
    simulation.run(timesteps)

    # Write the simulation state to 'simulation_result.txt'
    with open('simulation_result.txt', 'w') as f:
        f.write(str(simulation))


if __name__ == "__main__":
    main()

"""
Author: YOUR NAME HERE
Starting Date: YOUR STARTING DATE HERE

Test cases for the Traffic Simulation
"""

import simulation

# A bit of a tricky hack here
# What we're doing is fixing the constants used for randomness to be 0
# This allows us to have simple consistent testing while still having
#   simulation randomness be applied
simulation.TRAVEL_VARIATION = 0
simulation.SPAWN_VARIATION = 0

# Reset ids so tests are deterministic, even if re-run
def reset_ids():
    simulation.Light.reset_ids()
    simulation.Car.reset_ids()

# Part 1 Tests: Light
# ----------------------------------------------


def test_light_equal(expected: simulation.Light, result: simulation.Light, fn_name: str):
    """Tests if two lights are equal

    That is, this tests if two lights have exactly the same values

    If any values differ, print an appropriate error
    """

    error_message = f'while testing {fn_name}\n\texpected\t{repr(expected)}\n\tgot\t\t{repr(result)}'
    assert expected.is_green == result.is_green, error_message
    assert expected.max_countdown == result.max_countdown, error_message
    assert expected.countdown == result.countdown, error_message
    assert expected.queue == result.queue, error_message


def test_light_constructor():
    """Test cases for the Light constructor"""

    reset_ids()
    fn_name = 'Light constructor'

    light = simulation.Light(5, 3)

    # Test that each attribute was set correctly by the constructor
    result = light.is_green
    expected = False
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = light.max_countdown
    expected = 5
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = light.countdown
    expected = 3
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = light.queue
    expected = []
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    print(f'{fn_name} tests passed')


def test_light_queue():
    """Test cases for Light queue methods"""

    reset_ids()
    fn_name = 'Light queue'

    # Basic test of queue size as we add/remove a car

    # First create a new Light (the parameters don't matter here)
    light1 = simulation.Light(5, 3)

    # Initially, the queue should have zero elements
    result = light1.queue_length()
    expected = 0
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    # Add a single car to the queue (the Car parameters just contain this light)
    car1 = simulation.Car([light1])
    light1.add_car_to_queue(car1)

    # The queue should now have one element in it
    result = light1.queue_length()
    expected = 1
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    # Now, advance the queue of the light, and then we should have zero elements left
    light1.advance_queue()
    result = light1.queue_length()
    expected = 0
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    # Test of the queue returning things in the right order

    # Create a new light and some cars
    light2 = simulation.Light(5, 3)
    first_car = simulation.Car([light2])
    second_car = simulation.Car([light2])

    # Add each car to the light2 in sequence
    light2.add_car_to_queue(first_car)
    light2.add_car_to_queue(second_car)

    # There should be two elements in this queue
    result = light2.queue_length()
    expected = 2
    error_message = f'while testing {fn_name}, expected {repr(expected)} got {repr(result)}'
    assert expected == result, error_message

    # Now, advance the queue and make sure the first car is returned first
    result = light2.advance_queue()
    expected = first_car
    error_message = f'while testing {fn_name}, expected {repr(expected)} got {repr(result)}'
    # compare the cars by id
    assert expected.id == result.id, error_message

    # Now, advance the queue again and make sure the second car is returned
    result = light2.advance_queue()
    expected = second_car
    error_message = f'while testing {fn_name}, expected {repr(expected)} got {repr(result)}'
    # compare the cars by id
    assert expected.id == result.id, error_message

    # TODO: Add a new test about the light queues here!
    # You can use existing lights or make new ones

    print(f'{fn_name} tests passed')


def test_light_timestep():
    """Test cases for Light.timestep"""

    reset_ids()
    fn_name = 'Light.timestep'

    # Basic test cases for now, will add more later

    light = simulation.Light(3, 1)

    # Initially red
    result = light.is_green
    expected = False
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    # Turns green after one timestep
    light.timestep()
    result = light.is_green
    expected = True
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    # Still green after counting down by one
    light.timestep()
    result = light.is_green
    expected = True
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    # Switches back to red after three timesteps
    light.timestep()
    light.timestep()
    result = light.is_green
    expected = False
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    # TODO: Add a new test about the light timestep here
    # You can use an existing light or make new ones

    print(f'{fn_name} tests passed')


def test_light_can_go():
    """Test cases for Light.can_go"""

    reset_ids()
    fn_name = 'Light.can_go'

    # Basic test cases for now, will add more later

    light = simulation.Light(3, 1)

    # Initially red
    result = light.can_go()
    expected = False
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    # The light turned green, but cars haven't started moving yet
    light.timestep()
    result = light.can_go()
    expected = False
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    # Now cars start crossing the intersection go
    light.timestep()
    result = light.can_go()
    expected = True
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    # The light turned red, so cars can no longer go
    light.timestep()
    light.timestep()
    result = light.can_go()
    expected = False
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    # TODO: Add a new test about the light can_go method here
    # You can use an existing light or make new ones

    print(f'{fn_name} tests passed')


# Part 2 Tests: Car
# ----------------------------------------------


def test_car_constructor():
    """Test cases for the Car constructor"""

    reset_ids()
    fn_name = 'Car constructor'

    car = simulation.Car([simulation.Light(5, 3)])

    # Test that each attribute was set correctly by the constructor
    result = car.current_light
    error_message = f'while testing {fn_name}, expected None got {result}'
    assert result is None, error_message

    result = len(car.remaining_lights)
    expected = 1
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = car.remaining_lights
    test_light_equal(car.remaining_lights[0], simulation.Light(5, 3), fn_name)

    result = car.travel_time
    expected = 1
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    print(f'{fn_name} tests passed')


def test_car_light_updates():
    """Test cases for Car light update methods

    Specifically tests all the (related) following methods:
      timestep
      is_at_light
      number_of_lights
      car_start_going
    """

    reset_ids()
    fn_name = 'Car light updates'

    # Test based on timestep
    # Setup a simple light that will allow us to go for exactly one step
    light1 = simulation.Light(2, 1)
    # And a second light we don't reach in this basic setup
    # Note that it takes TRAVEL_TIME steps to reach this second light, which is a while
    light2 = simulation.Light(2, 1)

    car = simulation.Car([light1, light2])

    # Initially, we have 2 lights remaining and are not at a light
    result = car.number_of_lights()
    expected = 2
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = car.is_at_light()
    expected = False
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    # Advance the car, which means we should reach the first light
    # Note that cars start with one countdown
    car.timestep()

    result = car.number_of_lights()
    expected = 1
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = car.is_at_light()
    expected = True
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    # Now, tell the car to start going again
    car.start_going()
    result = car.number_of_lights()
    expected = 1
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = car.is_at_light()
    expected = False
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    # After going again, we should have exactly the max travel time (since we removed random variation)
    result = car.travel_time
    expected = simulation.TRAVEL_TIME
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    # TODO: Add a new test about the car timestep or light information here
    # You can use the existing car or make a new one

    print(f'{fn_name} tests passed')


# Part 3 Tests: Simulation
# ----------------------------------------------

def test_simulation_constructor():
    """Test cases for the Simulation constructor"""

    reset_ids()
    fn_name = 'Simulation constructor'

    sim = simulation.Simulation(3, 5, 2, 4)

    result = len(sim.lights)
    expected = 3
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = sim.spawn_time
    expected = 4
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = sim.cars
    expected = []
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = sim.spawn_countdown
    expected = 1
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = sim.timestep_count
    expected = 0
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    print(f'{fn_name} tests passed')


def test_simulation_number_of_lights():
    """Test cases for Simulation.number_of_lights"""

    reset_ids()
    fn_name = 'Simulation.number_of_lights'

    simulation1 = simulation.Simulation(1, 1, 1, 1)
    result = simulation1.number_of_lights()
    expected = 1
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    simulation2 = simulation.Simulation(5, 1, 1, 1)
    result = simulation2.number_of_lights()
    expected = 5
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    # TODO: Add a new test about the simulation number of lights here
    # You should likely make a new simulation here

    print(f'{fn_name} tests passed')


def test_simulation_timestep_information():
    """Test cases for Simulation.active_cars"""

    reset_ids()
    fn_name = 'Simulation timestep information'

    # Setup a simulation to spawn cars each step
    sim = simulation.Simulation(5, 5, 3, 1)

    # The simulation string output is meant to be read from START (top/incoming)
    # down to FINISH (bottom/after the last light).
    sim_str = str(sim)
    assert 'START' in sim_str, f'while testing {fn_name}, expected START marker in output'
    assert 'FINISH' in sim_str, f'while testing {fn_name}, expected FINISH marker in output'

    # No cars waiting or active
    result = sim.waiting_car_count()
    expected = 0
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = sim.active_cars()
    expected = 0
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = sim.car_counts()
    expected = [0, 0, 0, 0, 0]
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    # After one timestep, we should have one car active, but no cars waiting
    sim.timestep()
    result = sim.waiting_car_count()
    expected = 0
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = sim.active_cars()
    expected = 1
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = sim.car_counts()
    expected = [0, 0, 0, 0, 0]
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    # After two timesteps, we should have two car actives, and one car at the first light
    sim.timestep()
    result = sim.waiting_car_count()
    expected = 1
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = sim.active_cars()
    expected = 2
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = sim.car_counts()
    expected = [1, 0, 0, 0, 0]
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    # TODO: Add a new test about the simulation timesteps
    # You can use the current simulation or make a new one

    print(f'Simulation timestep information tests passed')


def test_all():
    # Light tests
    test_light_constructor()
    test_light_queue()
    test_light_timestep()
    test_light_can_go()
    print()

    # Car tests
    test_car_constructor()
    test_car_light_updates()
    print()

    # Simulation tests
    test_simulation_constructor()
    test_simulation_number_of_lights()
    test_simulation_timestep_information()
    print()
    
    print('All tests passed!')


if __name__ == "__main__":
    test_all()

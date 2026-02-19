"""
Author: Graham Gilbert-Schroeer 
Starting Date: 02/13/26

Test cases for the Traffic Simulation
"""

import simulation

simulation.TRAVEL_VARIATION = 0
simulation.SPAWN_VARIATION = 0

def reset_ids():
    simulation.Light.reset_ids()
    simulation.Car.reset_ids()

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

    light1 = simulation.Light(5, 3)

    result = light1.queue_length()
    expected = 0
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    car1 = simulation.Car([light1])
    light1.add_car_to_queue(car1)

    result = light1.queue_length()
    expected = 1
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    light1.advance_queue()
    result = light1.queue_length()
    expected = 0
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    light2 = simulation.Light(5, 3)
    first_car = simulation.Car([light2])
    second_car = simulation.Car([light2])

    light2.add_car_to_queue(first_car)
    light2.add_car_to_queue(second_car)

    result = light2.queue_length()
    expected = 2
    error_message = f'while testing {fn_name}, expected {repr(expected)} got {repr(result)}'
    assert expected == result, error_message

    result = light2.advance_queue()
    expected = first_car
    error_message = f'while testing {fn_name}, expected {repr(expected)} got {repr(result)}'
    assert expected.id == result.id, error_message

    result = light2.advance_queue()
    expected = second_car
    error_message = f'while testing {fn_name}, expected {repr(expected)} got {repr(result)}'
    assert expected.id == result.id, error_message

    light3 = simulation.Light(5, 3)
    a = simulation.Car([light3])
    b = simulation.Car([light3])
    c = simulation.Car([light3])
    light3.add_car_to_queue(a)
    light3.add_car_to_queue(b)
    light3.add_car_to_queue(c)

    result = light3.queue_length()
    expected = 3
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = light3.advance_queue()
    expected = a
    error_message = f'while testing {fn_name}, expected {repr(expected)} got {repr(result)}'
    assert expected.id == result.id, error_message

    result = light3.queue_length()
    expected = 2
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = light3.advance_queue()
    expected = b
    error_message = f'while testing {fn_name}, expected {repr(expected)} got {repr(result)}'
    assert expected.id == result.id, error_message

    result = light3.advance_queue()
    expected = c
    error_message = f'while testing {fn_name}, expected {repr(expected)} got {repr(result)}'
    assert expected.id == result.id, error_message

    result = light3.queue_length()
    expected = 0
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    print(f'{fn_name} tests passed')


def test_light_timestep():
    """Test cases for Light.timestep"""

    reset_ids()
    fn_name = 'Light.timestep'

    light = simulation.Light(3, 1)

    result = light.is_green
    expected = False
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    light.timestep()
    result = light.is_green
    expected = True
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    light.timestep()
    result = light.is_green
    expected = True
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    light.timestep()
    light.timestep()
    result = light.is_green
    expected = False
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    light2 = simulation.Light(4, 2)
    result = (light2.is_green, light2.countdown)
    expected = (False, 2)
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    light2.timestep()
    result = (light2.is_green, light2.countdown)
    expected = (False, 1)
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    light2.timestep()
    result = (light2.is_green, light2.countdown)
    expected = (True, 4)
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    light2.timestep()
    result = (light2.is_green, light2.countdown)
    expected = (True, 3)
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    print(f'{fn_name} tests passed')


def test_light_can_go():
    """Test cases for Light.can_go"""

    reset_ids()
    fn_name = 'Light.can_go'

    light = simulation.Light(3, 1)

    result = light.can_go()
    expected = False
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    light.timestep()
    result = light.can_go()
    expected = False
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    light.timestep()
    result = light.can_go()
    expected = True
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    light.timestep()
    light.timestep()
    result = light.can_go()
    expected = False
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    light2 = simulation.Light(5, 1)
    light2.timestep()
    result = light2.can_go()
    expected = False
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    light2.timestep()
    result = light2.can_go()
    expected = True
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    light2.timestep()
    light2.timestep()
    light2.timestep()
    light2.timestep()
    result = light2.can_go()
    expected = False
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    print(f'{fn_name} tests passed')


def test_car_constructor():
    """Test cases for the Car constructor"""

    reset_ids()
    fn_name = 'Car constructor'

    car = simulation.Car([simulation.Light(5, 3)])

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

    light1 = simulation.Light(2, 1)
    light2 = simulation.Light(2, 1)

    car = simulation.Car([light1, light2])

    result = car.number_of_lights()
    expected = 2
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = car.is_at_light()
    expected = False
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    car.timestep()

    result = car.number_of_lights()
    expected = 1
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = car.is_at_light()
    expected = True
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    car.start_going()
    result = car.number_of_lights()
    expected = 1
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = car.is_at_light()
    expected = False
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = car.travel_time
    expected = simulation.TRAVEL_TIME
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    for _ in range(simulation.TRAVEL_TIME - 1):
        car.timestep()

    result = car.is_at_light()
    expected = False
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    car.timestep()
    result = car.is_at_light()
    expected = True
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = car.number_of_lights()
    expected = 0
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = light2.queue_length()
    expected = 1
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    print(f'{fn_name} tests passed')


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

    simulation3 = simulation.Simulation(3, 7, 2, 9)
    result = simulation3.number_of_lights()
    expected = 3
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    print(f'{fn_name} tests passed')


def test_simulation_timestep_information():
    """Test cases for Simulation.active_cars"""

    reset_ids()
    fn_name = 'Simulation timestep information'

    sim = simulation.Simulation(5, 5, 3, 1)

    sim_str = str(sim)
    assert 'START' in sim_str, f'while testing {fn_name}, expected START marker in output'
    assert 'FINISH' in sim_str, f'while testing {fn_name}, expected FINISH marker in output'

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

    for _ in range(simulation.TRAVEL_TIME - 1):
        sim.timestep()

    result = sim.waiting_car_count()
    expected = 8
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = sim.active_cars()
    expected = simulation.TRAVEL_TIME + 1
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    counts = sim.car_counts()
    result = counts[0]
    expected = 8
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = sum(counts)
    expected = sim.waiting_car_count()
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    print(f'Simulation timestep information tests passed')


def test_all():
    test_light_constructor()
    test_light_queue()
    test_light_timestep()
    test_light_can_go()
    print()

    test_car_constructor()
    test_car_light_updates()
    print()

    test_simulation_constructor()
    test_simulation_number_of_lights()
    test_simulation_timestep_information()
    print()
    
    print('All tests passed!')


if __name__ == "__main__":
    test_all()

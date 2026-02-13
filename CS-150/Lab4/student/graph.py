"""
Author: YOUR NAME HERE
Starting Date: YOUR STARTING DATE HERE

Initial creation by Dietrich Geisler on 10/25/2025

Functions to explore traffic simulation results (e.g., print summary data).
"""

import simulation


def graph_waiting_cars():
    """Print summary of the number of waiting cars over time.

    For each timestep, reports the number of waiting cars at each light.
    """

    # Set constants on top of the function for easy modification
    SIMULATION_LENGTH = 300
    LIGHT_COUNT = 3
    LIGHT_CHANGE_LENGTH = 30
    LIGHT_OFFSET = 3
    SPAWN_LENGTH = 5

    # Create the simulation
    sim = simulation.Simulation(LIGHT_COUNT,
                                LIGHT_CHANGE_LENGTH,
                                LIGHT_OFFSET,
                                SPAWN_LENGTH)

    # Setup lists for data collection
    light_values = []
    for _ in range(LIGHT_COUNT):
        light_values.append([])

    # Run the simulation, recording data each step
    for timestep in range(SIMULATION_LENGTH):
        car_counts = sim.car_counts()
        for index in range(len(car_counts)):
            light_values[index].append(car_counts[index])
        sim.timestep()

    print('Simulation finished')

    # Print summary: average waiting cars per light over the run
    print(f'\nTraffic simulation with {LIGHT_COUNT} lights')
    print('Average waiting cars per light over the run:')
    for index in range(LIGHT_COUNT):
        avg = sum(light_values[index]) / len(light_values[index])
        print(f'  Light {index + 1}: {avg:.2f}')


def graph_by_light_count():
    """Print average waiting cars for varying numbers of lights."""

    SIMULATION_LENGTH = 500
    LIGHT_CHANGE_LENGTH = 20
    LIGHT_OFFSET = 3
    SPAWN_LENGTH = 5
    MAX_LIGHTS = 5

    print('Number of lights -> average waiting cars')
    for light_count in range(1, MAX_LIGHTS + 1):
        sim = simulation.Simulation(light_count,
                                    LIGHT_CHANGE_LENGTH,
                                    LIGHT_OFFSET,
                                    SPAWN_LENGTH)
        waiting_cars = 0
        for _ in range(SIMULATION_LENGTH):
            waiting_cars += sim.waiting_car_count()
            sim.timestep()
        average_waiting = waiting_cars / SIMULATION_LENGTH
        print(f'  {light_count} -> {average_waiting:.2f}')
        print(f'Simulation of {light_count} lights finished')


def main():
    """Choose which experiment to run."""

    graph_waiting_cars()
    # graph_by_light_count()


if __name__ == "__main__":
    main()

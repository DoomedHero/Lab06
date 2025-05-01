import turtle
from Solar_System import SolarSystem
from Sun import Sun
from Planet import Planet

class Simulation:
    def __init__(self, solar_system, width: int, height: int, num_periods: int):
        self._solar_system = solar_system
        self._width = width
        self._height = height
        self._num_periods = num_periods
        self._t = turtle.Turtle()
        self._t.hideturtle()
        self._t.speed(1)
        self._screen = turtle.Screen()
        self._screen.setup(width=self._width, height=self._height)
        self._screen.bgcolor("black")
        self._t.clear()

    def run(self):
        self._solar_system.show_planets()
        for a_move in range(self._num_periods):
            self._solar_system.move_planets()
            self._solar_system.show_planets()
        self.freeze()


    def freeze(self):
        self._screen.exitonclick()

if __name__ == '__main__':
    solar_system = SolarSystem()
    simulation = Simulation(solar_system, 500,500, 2000000)

#Assume the variables for Jupiter are 1.

    sol = Sun("SOL", 9.74, 1047.56, 5800,  0, 0)
    solar_system.add_sun(sol)

    mercury = Planet("MERCURY", 0.0341, 0.000174, 0, 0, 25, 25, "grey")
    solar_system.add_planet(mercury)

    simulation.run()
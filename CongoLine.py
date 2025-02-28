"""
Congo Line
Filename: CongoLine.py
Author: Anh Tran
Date: February 18, 2024
Collaborator: Tommy Shoemaker
Resources: https://stackoverflow.com/questions/5228383/how-do-i-find-the-distance-between-two-points

"""

from __future__ import annotations

# always import 'future' at beginning
import dudraw
import random


class Dancer:
    # implement fps improve animation visualize
    fps = 120

    def __init__(self, x_pos: int = None, y_pos: int = None, radius=1.5):
        """
        Function creates instances that allow access among class function.
        parameters: (self, x_pos, y_pos, radius)
        return: values of 'self' parameter when being called.
        """
        self.k = 10
        # k values recognize as velocity changer of how fast circles follow, move around.
        self.dancer_size = radius

        # Defaut values automatic creates values with random method
        if x_pos == None:
            self.x_position = random.randint(-10, 110)
        if y_pos == None:
            self.y_position = random.randint(-10, 110)
        # random color genrator range between (0 to 255)
        self.color = dudraw.Color(
            random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        )

    def __str__(self):
        """
        Function purpose to print values causing program crash
        parameters: (self)
        return: values of k to recognize values determine velocity of x & y.
        """
        # 2.- __str__ function for debugging purpose
        return f"{self.k}"

    def redraw_dancer(self):
        """
        Function purpose to draw amount of circles Class being called in main
        parameters: (self)
        return: draw the amount of circles in the list.
        """
        # convert rgb choices into dudraw.color allow pasting to set_pen_color without rgb
        dudraw.set_pen_color(self.color)
        dudraw.filled_circle(self.x_position, self.y_position, self.dancer_size)

    def velocity_x(self, target_x: float = None):
        """
        Function purpose finding velocity of x where circle follow target or cursor.
        parameters: (self, target_X)
        return: velocity where x move next base on previous circle in the list
        """
        if target_x == None:
            return self.k * (dudraw.mouse_x() - self.x_position) / Dancer.fps
        # calculate velocity using two vector, take target(cursor, or a circle)
        # subtract for x-coordinate of the next circle in the list.
        return self.k * (target_x - self.x_position) / self.fps

    def velocity_y(self, target_y: float = None):
        """
        Function purpose finding velocity of y where circle follow target or cursor.
        parameters: (self, target_y)
        return: velocity where circles will move in y-coordinate direction.
        """
        if target_y == None:
            # divide fps lessen time, make animation faster, provide better quality.
            return self.k * (dudraw.mouse_y() - self.y_position) / Dancer.fps
        return self.k * (target_y - self.y_position) / Dancer.fps

    def move_dancer(self, target_x: float = None, target_y: float = None):
        """
        Function purpose changing x and y position after calculate velocity
        The effect of velocity will move circles around horizontally.
        parameters: (self, target_x, target_y)
        return: continuously update the canvas with new circle position following target
        """
        self.x_position += self.velocity_x(target_x)
        self.y_position += self.velocity_y(target_y)

    def increase_velocity(self, increase_amount: float = 5):
        """
        Function purpose to increase velocity of circles movement
        parameters: (self, increase_amount)
        return: new value of self.k when user input 'f' key
        """
        self.k += increase_amount

    def stop_velocity(self, stop_cirle: float):
        """
        Function purpose stop all circles movement.
        parameters: (self, stop_circle)
        return: convert k into 0 to save the circle in the same position without moving
        """
        self.k = stop_cirle


def main():
    """ """
    dudraw.set_canvas_size(400, 400)
    dudraw.clear(dudraw.LIGHT_GRAY)
    dudraw.set_x_scale(0, 100)
    dudraw.set_y_scale(0, 100)

    key = ""
    dancer_list = []

    while key != "q":
        dudraw.clear(dudraw.BLACK)
        if dudraw.mouse_clicked():
            # called 20 times of Dancer class, each index have a dancer.
            dancer_list = [Dancer() for _ in range(20)]

        # checking if dancer_list empty == true
        if dancer_list:
            for i in range(len(dancer_list)):
                # Dancer 1 follow cursor, index 0 is first dancer
                if i == 0:
                    dancer_list[0].move_dancer()
                # the rest dancer will follow previous one
                # called move_dancer append two value x & y
                # will be pass to calculate velocity/ distance of previous circle
                elif i > 0:
                    dancer_list[i].move_dancer(
                        dancer_list[i - 1].x_position, dancer_list[i - 1].y_position
                    )
                dancer_list[i].redraw_dancer()

        dudraw.show(1000 / Dancer.fps)

        # append new circle one every key_type
        if key == "n":
            dancer_list.append(Dancer())

        # increase movement of the circles, and closer distance
        if key == "f":
            for dancer in dancer_list:
                dancer.increase_velocity()
        # stop dancers from dancing where.
        if key == "s":
            for dancer in dancer_list:
                dancer.stop_velocity(0)
        # making 100 dancers at once like a crumble colorful ball
        if key == "c":
            for i in range(1000):
                dancer_list.append(Dancer())
        key = dudraw.next_key_typed()


if __name__ == "__main__":
    main()

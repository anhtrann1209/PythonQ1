"""
Sand Fall Stimulation Part 2
Filename: SandGameP2.py
Author: Anh Tran
Date: February 9, 2024
Resources: 
github.com - https://github.com/Antiochian/Falling-Sand
stackoverflow - https://stackoverflow.com/questions/71257560/how-to-correctly-update-the-grid-in-falling-sand-simulation
stanford.edu -https://web.stanford.edu/class/archive/cs/cs106a/cs106a.1212/assn/sand-handout.html

"""

import dudraw
from random import randint
import random


class Sandbox:
    def __init__(self):
        """
        Function make instances which are class 'self' parameter
        parameters: (self)
        return: setting up canvas, creating 2D list
        """
        self.canvas_size = 300
        # number of box per row and column
        self.box_size = 150
        # how much space each box take up
        self.square_size = self.canvas_size / self.box_size
        # create a 2D list of 0 represent air
        self.sand_list = [
            [0 for row in range(self.box_size)] for col in range(self.box_size)
        ]

    def update_pixel(self):
        """
        Function updates sand block, move down the grid, and check position left and right if open as 0.
        parameters: (self))
        return: sand squares falling down the grid, checking left anf right box finding 0 and replace.
        """
        # color for sand
        dudraw.set_pen_color_rgb(174, 155, 125)

        # iterate over rows start=1 to stop sand from falling further.
        for row in range(self.box_size - 1):
            # iterate over columns
            for col in range(self.box_size):
                # check where mouse change list content equal 1
                if self.sand_list[row][col] == 1:
                    dudraw.filled_square(
                        col * self.square_size, row * self.square_size, 1
                    )

                    # swaping values as sand move to lowest empty box and make value in list = 1
                    if row > 0 and self.sand_list[row - 1][col] == 0:
                        self.sand_list[row][col], self.sand_list[row - 1][col] = (
                            self.sand_list[row - 1][col],
                            self.sand_list[row][col],
                        )

                    # allows sand to move to the left giving open slot = 0
                    elif (
                        col > 0
                        and self.sand_list[row][col - 1] == 0
                        and self.sand_list[row - 1][col - 1] == 0
                    ):
                        self.sand_list[row][col], self.sand_list[row - 1][col - 1] = (
                            self.sand_list[row - 1][col - 1],
                            self.sand_list[row][col],
                        )

                    # allows sand to move to the left giving open slot
                    elif (
                        col < self.box_size - 1
                        and self.sand_list[row][col + 1] == 0
                        and self.sand_list[row - 1][col + 1] == 0
                    ):
                        self.sand_list[row][col], self.sand_list[row - 1][col + 1] = (
                            self.sand_list[row - 1][col + 1],
                            self.sand_list[row][col],
                        )

    def place_sand(self):
        """
        Function take x and y position, change it to 1 represent sand, but cannot change floor numbers in list.
        parameters: (self)
        return: position around x and y and change value at list to 1 if it not 2 = Floor
        """
        # function mouse_x gives back a float, therefore cast it into integer
        # divide square_size scale down to fit grid pixel structure
        x, y = int(dudraw.mouse_x() / self.square_size), int(
            dudraw.mouse_y() / self.square_size
        )

        if 0 <= x < self.box_size and 0 <= y < self.box_size:
            for sand_drop in range(randint(5, 10)):
                random_x = x + randint(-2, 2)
                random_y = y + randint(-2, 2)

                # choices less than max x value but greater than 0
                if 0 <= random_x < self.box_size and 0 <= random_y < self.box_size:
                    # set value in list equal to 1
                    if self.sand_list[random_y][random_x] != 2:
                        self.sand_list[random_y][random_x] = 1

    def place_floor(self):
        """
        Function take in x and y position around, and passed it mainly to update_floor.
        parameters: (self)
        return: position around x and y, change value in list to 2 if mouse position not sand
        """
        # function mouse_x gives back a float, therefore cast it into integer
        # divide square_size scale down to fit grid pixel structure
        x, y = int(dudraw.mouse_x() / self.square_size), int(
            dudraw.mouse_y() / self.square_size
        )

        if 0 <= x < self.box_size and 0 <= y < self.box_size:
            # drop sand in same row
            for sand_drop in range(randint(5, 10)):
                random_x = x + randint(-1, 1)
                random_y = y + randint(-1, 1)

                if 0 <= random_x < self.box_size and 0 <= random_y < self.box_size:
                    if self.sand_list[random_y][random_x] != 1:
                        self.sand_list[random_y][random_x] = 2

    def update_floor(self):
        """
        Function draw brown block where list is 2 represent floor, and does not move.
        parameters: (self)
        return: Draw brown square represent bridge, but it does not have movement.
        """

        dudraw.set_pen_color_rgb(109, 79, 75)
        for row in range(1, self.box_size):
            # iterate over columns
            for col in range(self.box_size):
                # check if the list contain 1 == 'sand'
                if self.sand_list[row][col] == 2:
                    dudraw.filled_square(
                        col * self.square_size, row * self.square_size, 1
                    )

    def remove(self):
        """
        Function change all values back to 0's which remove all block water, floor, and sand.
        parameters: (self)
        return: x and y position where list contains value 1, 2, 3 and convert back to 0.
        """

        x, y = int(dudraw.mouse_x() / self.square_size), int(
            dudraw.mouse_y() / self.square_size
        )

        if 0 <= x < self.box_size and 0 <= y < self.box_size:
            # remove sand or floor in the same row
            for _ in range(randint(5, 10)):
                random_x = x + randint(-4, 4)
                random_y = y + randint(-4, 4)

                if 0 <= random_x < self.box_size and 0 <= random_y < self.box_size:

                    if (
                        self.sand_list[random_y][random_x] == 1
                        or self.sand_list[random_y][random_x] == 2
                        or self.sand_list[random_y][random_x] == 3
                    ):
                        # set value at specific grid equal to 0
                        self.sand_list[random_y][random_x] = 0

    def water(self):
        """
        Function locate position around x and y and pass to update_water function.
        parameters: (self)
        return: position around x and y, change it to 3 for water function if not floor.
        """

        x, y = int(dudraw.mouse_x() / self.square_size), int(
            dudraw.mouse_y() / self.square_size
        )

        if 0 <= x < self.box_size and 0 <= y < self.box_size:
            # remove sand or floor in the same row
            for _ in range(randint(5, 10)):
                random_x = x + randint(-1, 1)
                random_y = y + randint(-1, 1)

                if 0 <= random_x < self.box_size and 0 <= random_y < self.box_size:
                    if (
                        self.sand_list[random_y][random_x] != 2
                        or self.sand_list[random_y][random_x] == 1
                    ):
                        # set value to 3 to fill in water
                        self.sand_list[random_y][random_x] = 3

    def update_water(self):
        """
        Function to update the water simulation.
        parameters: (self)
        return: water block which move left and right simultaneously.
        """
        dudraw.set_pen_color_rgb(3, 71, 112)

        # looping through the last row in list
        for row in range(self.box_size - 1):
            for col in range(self.box_size):
                # x and y will pass the position where water was storage as 3
                if self.sand_list[row][col] == 3:
                    dudraw.filled_square(
                        col * self.square_size, row * self.square_size, 1
                    )

                    # check if slot open
                    if row < self.box_size - 1 and self.sand_list[row - 1][col] == 0:
                        self.sand_list[row][col], self.sand_list[row - 1][col] = (
                            self.sand_list[row - 1][col],
                            self.sand_list[row][col],
                        )
                    else:
                        # random.choice pick -1 for left and 1 for right (water stimulation)
                        direction = random.choice([-1, 1])
                        new_col = col + direction

                        # critical to check canvas boundaries
                        if 0 <= new_col < self.box_size:
                            # Check if the new cell is open
                            if self.sand_list[row][new_col] == 0:
                                (
                                    self.sand_list[row][col],
                                    self.sand_list[row][new_col],
                                ) = (
                                    self.sand_list[row][new_col],
                                    self.sand_list[row][col],
                                )
                        # when column beyond limits, it will stay at current column
                        else:
                            # Check if the current cell is open
                            if self.sand_list[row][col] == 0:
                                self.sand_list[row][col], self.sand_list[row][col] = (
                                    self.sand_list[row][col],
                                    self.sand_list[row][col],
                                )

    def main(self):
        """
        Function take constructor instances.
        parameters: (self)
        return: function activate base on linking 'key' type.
        """
        dudraw.set_canvas_size(600, 600)
        dudraw.set_x_scale(0, self.canvas_size)
        dudraw.set_y_scale(0, self.canvas_size)

        key = "s"
        while key != "q":
            dudraw.clear_rgb(173, 216, 230)

            if key == "s":
                # place canvas set up inside choosen key to avoid overlap.
                dudraw.set_pen_color(dudraw.BLACK)
                dudraw.filled_rectangle(150, 270, 100, 20)
                dudraw.set_pen_color(dudraw.WHITE)
                dudraw.set_font_size(50)
                dudraw.text(150, 270, "Sand")

                # consistently pass update floor 2D list storage, and drawing placement.
                self.update_floor()
                self.update_water()

                if dudraw.mouse_is_pressed():
                    self.place_sand()
                self.update_pixel()

            if key == "f":
                dudraw.set_pen_color(dudraw.BLACK)
                dudraw.filled_rectangle(150, 270, 100, 20)
                dudraw.set_pen_color(dudraw.WHITE)
                dudraw.set_font_size(50)
                dudraw.text(150, 270, "Floor")
                self.update_pixel()
                self.update_water()

                if dudraw.mouse_is_pressed():

                    self.place_floor()
                # Draw the floor after drawing the sand
                self.update_floor()

            if key == "r":
                dudraw.set_pen_color(dudraw.BLACK)
                dudraw.filled_rectangle(150, 270, 100, 20)
                dudraw.set_pen_color(dudraw.WHITE)
                dudraw.set_font_size(50)
                dudraw.text(150, 270, "Remove")

                self.update_pixel()
                self.update_floor()
                self.update_water()

                # remove function does it once and convert back to 0, no neadd for update.
                if dudraw.mouse_is_pressed():
                    self.remove()

            if key == "w":
                dudraw.set_pen_color(dudraw.BLACK)
                dudraw.filled_rectangle(150, 270, 100, 20)
                dudraw.set_pen_color(dudraw.WHITE)
                dudraw.set_font_size(50)
                dudraw.text(150, 270, "Water")

                self.update_pixel()
                self.update_floor()

                if dudraw.mouse_is_pressed():
                    self.water()
                self.update_water()

            if dudraw.has_next_key_typed():
                key = dudraw.next_key_typed()

            dudraw.show(10)

        else:
            key == "q"


if __name__ == "__main__":
    sandbox = Sandbox()
    sandbox.main()

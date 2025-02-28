"""
Sand Fall Stimulation Part 1
Filename: SandGameP1.py
Author: Anh Tran
Date: January 30, 2024
Resources: 
github.com - https://github.com/Antiochian/Falling-Sand
stackoverflow - https://stackoverflow.com/questions/71257560/how-to-correctly-update-the-grid-in-falling-sand-simulation
stanford.edu -https://web.stanford.edu/class/archive/cs/cs106a/cs106a.1212/assn/sand-handout.html

"""

import dudraw
from random import randint


class Sandbox:
    def __init__(self):
        self.canvas_size = 300
        # number of box per row and column
        self.box_size = 150
        # how much space each box take up
        self.square_size = self.canvas_size / self.box_size
        # create a 2D list of 0 represent air
        self.sand_list = [
            [0 for row in range(self.box_size)] for col in range(self.box_size)
        ]
        self.gravity = 1

    def update_pixel(self):
        # color for sand
        dudraw.set_pen_color_rgb(174, 155, 125)

        # box_size = 50
        # iterate over rows start=1 to stop sand from falling further.
        for row in range(1, self.box_size):
            # iterate over columns
            for col in range(self.box_size):
                # check if the list contain 1 == 'sand'
                if self.sand_list[row][col] == 1:
                    dudraw.filled_square(
                        col * self.square_size, row * self.square_size, 1
                    )

                    if row > 0 and self.sand_list[row - 1][col] == 0:
                        # swaping values to clear out the sand as it move to lowest empty box
                        self.sand_list[row][col], self.sand_list[row - 1][col] = (
                            self.sand_list[row - 1][col],
                            self.sand_list[row][col],
                        )

                    # if the sand == 1, and column and row on the left == 0 then move it down
                    elif (
                        col > 0
                        and self.sand_list[row][col - 1] == 0
                        and self.sand_list[row - 1][col - 1] == 0
                    ):
                        self.sand_list[row][col], self.sand_list[row - 1][col - 1] = (
                            self.sand_list[row - 1][col - 1],
                            self.sand_list[row][col],
                        )

                    # if the sand == 1, and column and row on the right == 0 then move sand down diagonally
                    # minus 1 because start with 0 in the loop
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
        # function mouse_x gives back a float, therefore cast it into integer
        # divide square_size scale down to fit grid pixel structure
        x, y = int(dudraw.mouse_x() / self.square_size), int(
            dudraw.mouse_y() / self.square_size
        )

        if 0 <= x < self.box_size and 0 <= y < self.box_size:
            # drop sand in same row
            for sand_drop in range(randint(5, 10)):
                random_x = x + randint(-2, 2)
                random_y = y + randint(-2, 2)

                # check if random choice is valid to be place in the grid
                if 0 <= random_x < self.box_size and 0 <= random_y < self.box_size:
                    # set value at specific grid equal to 1
                    self.sand_list[random_y][random_x] = 1

    def main(self):
        dudraw.set_canvas_size(600, 600)
        dudraw.set_x_scale(0, self.canvas_size)
        dudraw.set_y_scale(0, self.canvas_size)

        key = "s"
        while key != "q":
            dudraw.clear_rgb(173, 216, 230)
            key = dudraw.next_key_typed()
            dudraw.set_font_size(50)
            dudraw.text(40, 280, "Sand")

            if dudraw.mouse_is_pressed():
                self.place_sand()

            # update new list values change
            self.update_pixel()
            dudraw.show(10)


if __name__ == "__main__":
    sandbox = Sandbox()
    sandbox.main()

"""
    Purpose: Draws a recursive Sierpinski Triangle using Dudraw.
    Filename: SierpinskiTriangleDraw.py
    Author: Anh Tran
    Date: Jan 13, 2024
    Assignment: Sierpinski Recursive Drawing
    Collaborators: None
    Internet Source: 
"""

import dudraw

def draw_sierpinski(left: float, bottom: float, right: float, top: float, min_size: float, color_scale: float):
    # Base case: If the size of the triangle is small enough, draw it
    if (right - left) < min_size:
        dudraw.set_pen_color_rgb(
            int(left * color_scale * 256), 
            int(bottom * color_scale * 256), 
            150
        )
        dudraw.filled_triangle(left, bottom, right, bottom, (right + left) / 2, top)
    else:
        # Recursive case: Split the triangle into 3 smaller triangles
        mid_left = (left + right) / 2
        mid_bottom = (bottom + top) / 2
        mid_right = (right + left) / 2
        draw_sierpinski(left, bottom, mid_left, mid_bottom, min_size, color_scale)
        draw_sierpinski(mid_left, bottom, right, mid_bottom, min_size, color_scale)
        draw_sierpinski(left + (right - left) / 4, (top + bottom) / 2, right - (right - left) / 4, top, min_size, color_scale)


def main():    
    dudraw.set_canvas_size(800, 800)
    # Minimum size to stop drawing triangles
    min_size = 0.002  
    # Controls the intensity of the colors based on the position
    color_scale = 0.5  
    # Initial values for a unit square
    draw_sierpinski(0, 0, 1, 1, min_size, color_scale) 
    dudraw.show(10000)


if __name__ == "__main__":
    main()



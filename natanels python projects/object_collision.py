import pygame


# use this function to find the out if an object has been clicked
def button_clicked(button_coordinates_x, button_coordinates_y, width, height, mouse_position):
    if button_coordinates_x + height > mouse_position[0] > button_coordinates_x and button_coordinates_y + width > \
            mouse_position[1] > button_coordinates_y:
        button_clicked = True
        return button_clicked


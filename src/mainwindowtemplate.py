import pygame
import dubercomponent
import brushes as brush


def main():
    pygame.init()
    pygame.display.set_caption("Duber Paint")
    logo = pygame.image.load("./assets/duberpaint.png")
    pygame.display.set_icon(logo)

    # screen size subject to change
    window = pygame.display.set_mode((1080, 720))
    brush_icon = pygame.image.load("./assets/BrushIcon.png")
    eraser_icon = pygame.image.load("./assets/EraserIcon.png")
    line_icon = pygame.image.load("./assets/LineIcon.png")
    rectangle_icon = pygame.image.load("./assets/RectangleIcon.png")
    ellipse_icon = pygame.image.load("./assets/EllipseIcon.png")

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.fill((0, 0, 0))

        font_1 = pygame.font.Font(None, 32)

        # project logo
        window.blit(pygame.transform.scale(logo, (166, 115)), (0, 0))

        # drawing tool customization
        colour_selection_area = dubercomponent.DuberComponent(
            240, 10, 160, 95, (128, 128, 128))  # not complete
        brush_selection_area = dubercomponent.DuberComponent(
            420, 10, 136, 95, (128, 128, 128))  # not complete
        shape_selection_area = dubercomponent.DuberComponent(
            576, 10, 265, 95, (128, 128, 128))  # not complete

        join_code = "XXXXXX"
        join_code_area = dubercomponent.DuberTextBox(
            861, 10, 130, 55, (128, 128, 128), "Join Code:", font_1, (255, 255, 255))
        window.blit(font_1.render(join_code, True, (255, 255, 255)), (866, 34))

        export_button = dubercomponent.DuberTextBox(
            861, 73, 130, 32, (128, 128, 128), "Export", font_1, (0, 128, 0))

        kick_button = dubercomponent.DuberTextBox(
            20, 670, 160, 40, (255, 0, 0), "Kick User", font_1, (255, 0, 0))

        # list of users
        window.blit(font_1.render('Users:', True, (255, 255, 255)), (20, 130))
        pygame.draw.rect(window, (128, 128, 128), (20, 170, 160, 40), True)
        pygame.draw.rect(window, (128, 128, 128), (20, 210, 160, 40), True)
        pygame.draw.rect(window, (128, 128, 128), (20, 250, 160, 40), True)
        pygame.draw.rect(window, (128, 128, 128), (20, 290, 160, 40), True)
        pygame.draw.rect(window, (128, 128, 128), (20, 330, 160, 40), True)
        pygame.draw.rect(window, (128, 128, 128), (20, 370, 160, 40), True)
        pygame.draw.rect(window, (128, 128, 128), (20, 410, 160, 40), True)
        pygame.draw.rect(window, (128, 128, 128), (20, 450, 160, 40), True)
        pygame.draw.rect(window, (128, 128, 128), (20, 490, 160, 40), True)
        pygame.draw.rect(window, (128, 128, 128), (20, 530, 160, 40), True)
        pygame.draw.rect(window, (128, 128, 128), (20, 570, 160, 40), True)
        pygame.draw.rect(window, (128, 128, 128), (20, 610, 160, 40), True)

        export_button.draw(window)
        colour_selection_area.draw(window)
        brush_selection_area.draw(window)
        shape_selection_area.draw(window)
        join_code_area.draw(window)
        kick_button.draw(window)
        # top part of interface
        pygame.draw.rect(window, (255, 255, 255), (0, 0, 1080, 115), True)

        # left part of interface
        pygame.draw.rect(window, (255, 255, 255), (0, 0, 200, 720), True)

        # canvas
        pygame.draw.rect(window, (255, 255, 255), (200, 115, 880, 605), False)

        # positions for colour buttons

        # row 1
        pygame.draw.rect(window, (128, 128, 128), (250, 18, 20, 20), 0)
        pygame.draw.rect(window, (128, 128, 128), (280, 18, 20, 20), 0)
        pygame.draw.rect(window, (128, 128, 128), (310, 18, 20, 20), 0)
        pygame.draw.rect(window, (128, 128, 128), (340, 18, 20, 20), 0)
        pygame.draw.rect(window, (128, 128, 128), (370, 18, 20, 20), 0)

        # row 2
        pygame.draw.rect(window, (128, 128, 128), (250, 48, 20, 20), 0)
        pygame.draw.rect(window, (128, 128, 128), (280, 48, 20, 20), 0)
        pygame.draw.rect(window, (128, 128, 128), (310, 48, 20, 20), 0)
        pygame.draw.rect(window, (128, 128, 128), (340, 48, 20, 20), 0)
        pygame.draw.rect(window, (128, 128, 128), (370, 48, 20, 20), 0)

        # row 3
        pygame.draw.rect(window, (128, 128, 128), (250, 78, 20, 20), 0)
        pygame.draw.rect(window, (128, 128, 128), (280, 78, 20, 20), 0)
        pygame.draw.rect(window, (128, 128, 128), (310, 78, 20, 20), 0)
        pygame.draw.rect(window, (128, 128, 128), (340, 78, 20, 20), 0)
        pygame.draw.rect(window, (128, 128, 128), (370, 78, 20, 20), 0)

        # positions for brush buttons
        """
        # row 1
        pygame.draw.rect(window, (128, 128, 128), (430, 20, 32, 32), 0)
        pygame.draw.rect(window, (128, 128, 128), (472, 20, 32, 32), 0)
        pygame.draw.rect(window, (128, 128, 128), (514, 20, 32, 32), 0)

        # row 2
        pygame.draw.rect(window, (128, 128, 128), (430, 62, 32, 32), 0)
        pygame.draw.rect(window, (128, 128, 128), (472, 62, 32, 32), 0)
        pygame.draw.rect(window, (128, 128, 128), (514, 62, 32, 32), 0)

        # positions for shape buttons
        pygame.draw.rect(window, (128, 128, 128), (586, 20, 75, 75), 0)
        pygame.draw.rect(window, (128, 128, 128), (671, 20, 75, 75), 0)
        pygame.draw.rect(window, (128, 128, 128), (756, 20, 75, 75), 0)
        """
        colour_selection_area.draw(window)
        # canvas
        pygame.draw.rect(window, (255, 255, 255), (200, 115, 880, 605), False)

        colour_list = []
        # row1
        colour_list.append(
            dubercomponent.DuberColourButton(
                250, 18, (255, 0, 0)))
        colour_list.append(
            dubercomponent.DuberColourButton(
                280, 18, (255, 165, 0)))
        colour_list.append(
            dubercomponent.DuberColourButton(
                310, 18, (255, 255, 0)))
        colour_list.append(
            dubercomponent.DuberColourButton(
                340, 18, (0, 128, 0)))
        colour_list.append(
            dubercomponent.DuberColourButton(
                370, 18, (0, 0, 255)))

        # row 2
        colour_list.append(
            dubercomponent.DuberColourButton(
                250, 48, (128, 0, 128)))
        colour_list.append(
            dubercomponent.DuberColourButton(
                280, 48, (0, 0, 0)))
        colour_list.append(
            dubercomponent.DuberColourButton(
                310, 48, (255, 255, 255)))
        colour_list.append(
            dubercomponent.DuberColourButton(
                340, 48, (139, 69, 19)))
        colour_list.append(
            dubercomponent.DuberColourButton(
                370, 48, (128, 128, 128)))

        # row 3
        colour_list.append(
            dubercomponent.DuberColourButton(
                250, 78, (255, 255, 255)))
        colour_list.append(
            dubercomponent.DuberColourButton(
                280, 78, (255, 255, 255)))
        colour_list.append(
            dubercomponent.DuberColourButton(
                310, 78, (255, 255, 255)))
        colour_list.append(
            dubercomponent.DuberColourButton(
                340, 78, (255, 255, 255)))
        colour_list.append(
            dubercomponent.DuberColourButton(
                370, 78, (255, 255, 255)))

        for colours in colour_list:
            colours.draw(window)

        brush_icon = pygame.image.load("./assets/BrushIcon.png")

        brush_list = []
        # adding buttons to the list of brush buttons

        # row 1
        brush_list.append(
            dubercomponent.DuberBrushButton(
                430, 20, pygame.transform.scale(
                    brush_icon, (32, 32)), brush.Brush(
                    (0, 0, 0), 10)))
        brush_list.append(
            dubercomponent.DuberBrushButton(
                472, 20, pygame.transform.scale(
                    brush_icon, (32, 32)), brush.Brush(
                    (0, 0, 0), 10)))
        brush_list.append(
            dubercomponent.DuberBrushButton(
                514, 20, pygame.transform.scale(
                    brush_icon, (32, 32)), brush.Brush(
                    (0, 0, 0), 10)))

        # row 2
        brush_list.append(
            dubercomponent.DuberBrushButton(
                430, 62, pygame.transform.scale(
                    brush_icon, (32, 32)), brush.Brush(
                    (0, 0, 0), 10)))
        brush_list.append(
            dubercomponent.DuberBrushButton(
                472, 62, pygame.transform.scale(
                    brush_icon, (32, 32)), brush.Brush(
                    (0, 0, 0), 10)))
        brush_list.append(
            dubercomponent.DuberBrushButton(
                514, 62, pygame.transform.scale(
                    eraser_icon, (32, 32)), brush.Eraser(10)))

        shape_list = []
        # adding buttons to the list of shape buttons
        shape_list.append(
            dubercomponent.DuberShapeButton(
                586, 20, pygame.transform.scale(
                    rectangle_icon, (75, 75))))
        shape_list.append(
            dubercomponent.DuberShapeButton(
                671, 20, pygame.transform.scale(
                    ellipse_icon, (75, 75))))
        shape_list.append(
            dubercomponent.DuberShapeButton(
                756, 20, pygame.transform.scale(
                    line_icon, (75, 75))))

        for brushes in brush_list:
            brushes.draw(window)

        for shapes in shape_list:
            shapes.draw(window)

        pygame.display.flip()

    """
    Colours:

    Red: (255,0,0)
    Orange: (255,165)
    Yellow: (255,255,255)
    Green: (0,128,0)
    Blue: (0,0,255)
    Purple: (128,0,128)
    Black: (0,0,0)
    White: (255,255,255)
    Brown: (139,69,19)
    Grey: (128,128,128)


    """


if __name__ == "__main__":
    main()

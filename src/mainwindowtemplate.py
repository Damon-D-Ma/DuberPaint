import pygame
import dubercomponent


def main():
    pygame.init()
    pygame.display.set_caption("Duber Paint")
    logo = pygame.image.load("./assets/duberpaint.png")
    pygame.display.set_icon(logo)

    # screen size subject to change
    window = pygame.display.set_mode((1080, 720))

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
        window.fill((0,0,0))






        font_1= pygame.font.Font(None,32)

        #project logo
        window.blit(pygame.transform.scale(logo, (166,115)), (0,0))

        #drawing tool customization
        colour_selection_area = dubercomponent.DuberTextBox(240, 10, 300, 95, (128,128,128), "Colours here", font_1, (255,255,255))#not complete
        brush_selection_area = dubercomponent.DuberTextBox(560, 10, 150, 95, (128,128,128), "Brushes here", font_1, (255,255,255))#not complete
        shape_selection_area = dubercomponent.DuberTextBox(730, 10, 200, 95, (128,128,128), "Shapes here", font_1, (255,255,255))#not complete
        
        #leave/disconnect button
        leave_button = dubercomponent.DuberTextBox(20, 670, 160, 40, (255,0,0), "LEAVE", font_1, (255,0,0))
        

        #list of users
        window.blit(font_1.render('Users:', True, (255, 255, 255)), (20, 130))
        pygame.draw.rect(window, (128,128,128), (20, 170, 160, 40), True)
        pygame.draw.rect(window, (128,128,128), (20, 210, 160, 40), True)
        pygame.draw.rect(window, (128,128,128), (20, 250, 160, 40), True)
        pygame.draw.rect(window, (128,128,128), (20, 290, 160, 40), True)
        pygame.draw.rect(window, (128,128,128), (20, 330, 160, 40), True)
        pygame.draw.rect(window, (128,128,128), (20, 370, 160, 40), True)
        pygame.draw.rect(window, (128,128,128), (20, 410, 160, 40), True)
        pygame.draw.rect(window, (128,128,128), (20, 450, 160, 40), True)
        pygame.draw.rect(window, (128,128,128), (20, 490, 160, 40), True)
        pygame.draw.rect(window, (128,128,128), (20, 530, 160, 40), True)
        pygame.draw.rect(window, (128,128,128), (20, 570, 160, 40), True)
        pygame.draw.rect(window, (128,128,128), (20, 610, 160, 40), True)

        leave_button.draw(window)

        colour_selection_area.draw(window)
        brush_selection_area.draw(window)
        shape_selection_area.draw(window)

        #top part of interface
        pygame.draw.rect(window, (255,255,255), (0,0, 1080, 115), True)

        #left part of interface
        pygame.draw.rect(window, (255,255,255), (0,0, 200, 720), True)

        #canvas
        pygame.draw.rect(window, (255,255,255), (200,115, 880,605), False)

        


        pygame.display.flip()




if __name__ == "__main__":
    main()



from Parameters import *
need_input = False
input_text = '|'
input_tick = 30


def print_text(message, x, y, font_color=(30, 255, 50), font_type='Art-Metropol.ttf', font_size=35):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    screen.blit(text, (x, y))

def get_input(x, y):
    global need_input, input_text, input_tick
    input_rect = pygame.Rect(x, y, 250, 70)

    pygame.draw.rect(screen, (255,255,255), input_rect)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if input_rect.collidepoint(mouse[0], mouse[1]) and click[0]:
        need_input = True

    if need_input:
        for event in pygame.event.get():
            if need_input and event.type == pygame.KEYDOWN:
                input_text = input_text.replace('|', '')
                input_tick = 30

                if event.key == pygame.K_RETURN:
                    need_input = False
                    message = input_text
                    input_text = ''
                    return message
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    if len(input_text) < 16:
                        input_text += event.unicode
                input_text += '|'

    print_text(message = input_text, x = x, y = y , font_size = 50)

    input_tick -= 1
    if input_tick == 0:
        input_text = input_text[:-1]
    if input_tick == -30:
        input_text += '|'

    return  None
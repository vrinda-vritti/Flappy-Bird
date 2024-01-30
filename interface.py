import pygame
import random
import sys
from tkinter import *
from PIL import Image, ImageTk
import os

def main_window():
    window = Tk()
    window.geometry("288x512")
    window.title("Flappy's Trap")
    icon = PhotoImage(file='yellowbird.png')
    window.iconphoto(True, icon)
    window.config(background="#86DC3D")


    def instructions():
        root = Tk()
        root.geometry("288x512")
        root.configure(bg="#86DC3D")
        root.title("Instructions")
        c1 = Canvas(root,width = 288, height= 512, bg="#86DC3D")
        c1.create_text(140,150,text = """1.Pass the Flappy Bird through
        the pipes.""",font= ('Arial', 13, 'bold'), fill= 'yellow')
        c1.create_text(125, 220, text="""2.If you fail to pass the
        Flappy through the pipes
        you will be challenged
        with the questions.""",font=('Arial', 13, 'bold'), fill='yellow')
        c1.grid()
        root.mainloop()

    def play_quiz():
        os.system('python quiz.py')


    def start_game():
        pygame.init()
        time = pygame.time.Clock()

        fly = 0.19
        bird_movement = 0

        screen = pygame.display.set_mode((288, 512))
        screen_icon = pygame.image.load('yellowbird.png')
        pygame.display.set_icon(screen_icon)
        caption = pygame.display.set_caption("Flappy's Trap !")

        # background:
        background = pygame.image.load("night.png").convert_alpha()

        # bird:
        bird = pygame.image.load("yellowbird.png").convert()
        bird_rect = bird.get_rect(center=(50, 290))

        # floor:
        floor = pygame.image.load("base.png").convert()
        floor_x_pos = 0

        # message:
        message = pygame.image.load("message.png").convert_alpha()
        message_rect = message.get_rect(center=(140, 190))

        # pipes:
        pipe_surface = pygame.image.load("pipe.png").convert()
        pipe_list = []

        pipe_spawn = pygame.USEREVENT
        pygame.time.set_timer(pipe_spawn, 1200)
        pipe_height = [200, 300, 400]

        # game sound :
        game_sound1 = pygame.mixer.Sound("audio_wing.wav")
        game_sound2 = pygame.mixer.Sound("audio_die.wav")

        def game_base():
            screen.blit(floor, (floor_x_pos, 450))
            screen.blit(floor, (floor_x_pos + 288, 450))

        def check_collision(pipes):
            for pipe in pipes:
                if bird_rect.colliderect(pipe):
                    game_sound2.play()
                    return False
                if bird_rect.top <= -100 or bird_rect.bottom >= 450:
                    game_sound2.play()
                    return False
            return True

        def create_pipe():
            random_pipe_pos = random.choice(pipe_height)
            top_pipe = pipe_surface.get_rect(midbottom=(500, random_pipe_pos - 100))
            bottom_pipe = pipe_surface.get_rect(midtop=(500, random_pipe_pos))
            return bottom_pipe, top_pipe

        def move_pipes(pipes):
            for pipe in pipes:
                pipe.centerx -= 5
            return pipes

        def draw_pipes(pipes):
            for pipe in pipes:
                if pipe.bottom >= 512:
                    screen.blit(pipe_surface, pipe)
                else:
                    flip_pipe = pygame.transform.flip(pipe_surface, False, True)
                    screen.blit(flip_pipe, pipe)

        # main loop
        game_active = True

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and game_active:
                        bird_movement = 0
                        bird_movement -= 3
                        game_sound1.play()
                    if event.key == pygame.K_SPACE and game_active == False:
                        if event.key == pygame.K_SPACE:
                            bird_rect.center = (50, 290)
                            bird_movement = 0
                            pipe_list.clear()
                            game_active = True
                if event.type == pipe_spawn and game_active:
                    pipe_list.extend(create_pipe())

            screen.blit(background, (0, 0))
            if game_active:
                bird_movement += fly
                bird_rect.centery += bird_movement
                screen.blit(bird, bird_rect)

                pipe_list = move_pipes(pipe_list)
                draw_pipes(pipe_list)
                game_active = check_collision(pipe_list)
            else:
                screen.blit(message, message_rect)
                play_quiz()
                break

            floor_x_pos -= 1
            game_base()

            if floor_x_pos <= -288:
                floor_x_pos = 0

            pygame.display.update()
            time.tick(90)


    label_1 = Label(window, text=" Welcome To Flappy's Trap !", font=('Arial', 15, 'bold'), fg="green",
                    bg="yellow",
                    relief=RAISED,
                    bd = 4,
                    padx= 5,
                    pady = 5)
    button_1 = Button(window, text="Click here to play !", font=('Arial', 18, 'bold'), fg="green", bg="yellow",
                    relief=RAISED,
                    bd = 4,
                    padx= 5,
                    pady= 5, command= start_game)

    button_2 = Button(window, text="Instructions", font=('Arial', 18, 'bold'), fg="green", bg="yellow",
                    relief=RAISED,
                    bd = 4,
                    padx=4,
                    pady= 4, command= instructions)

    img = Image.open("yellowbird.png")
    resize = img.resize((90, 90), Image.ANTIALIAS)

    photo = ImageTk.PhotoImage(resize, master=window)
    Label(window, text="", bg="#86DC3D").grid(row=13, column=1)
    Label(window, text="", bg="#86DC3D").grid(row=14, column=1)
    Label(window, image=photo).grid(row=15, column=1)

    label_1.grid(row=2, column=1)
    Label(window, text="", bg="#86DC3D").grid(row=0, column=1)
    Label(window, text="", bg="#86DC3D").grid(row=1, column=1)
    Label(window, text="", bg="#86DC3D").grid(row=3, column=1)

    button_1.grid(row=6, column=1)
    Label(window, text="", bg="#86DC3D").grid(row=4, column=1)
    Label(window, text="", bg="#86DC3D").grid(row=5, column=1)
    Label(window, text="", bg="#86DC3D").grid(row=1, column=1)

    button_2.grid(row=10, column=1)
    Label(window, text="", bg="#86DC3D").grid(row=7, column=1)
    Label(window, text="", bg="#86DC3D").grid(row=8, column=1)
    Label(window, text="", bg="#86DC3D").grid(row=9, column=1)

    window.mainloop()

main_window()
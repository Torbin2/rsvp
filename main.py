import pygame as py
from time import sleep
py.init()

SCALE = 2
STANDART_FPS = 15 #make false to ask on startup
#COLORS = ["#517121", "#ae8ede"]
COLORS = ["#141c08","#5b5959"]
font = py.font.Font(("fonts/1.0.ttf"), 200 * SCALE) #1.0-1.2


with open("input.txt", "r") as f:
    lines = f.readlines()

words = []
for line in lines:
    line.removesuffix("\n")
    line = line.split(" ")
    for i in line: words.append(i)



py.display.set_caption('rapid serial visual presentation')

fps = STANDART_FPS
while not fps:
    try:
        fps = int(int(input("wpm : ")) / 60)
    except ValueError: pass
    print(fps)

    
screen = py.display.set_mode((1600 *SCALE, 900*SCALE))
clock = py.time.Clock()

word_num = 0

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()
    screen.fill(COLORS[0])

    render_wrd = font.render(f"{words[word_num]}", False, (COLORS[1]))
    wrd_rect = render_wrd.get_rect(center=(800 * SCALE, 450 * SCALE))
    screen.blit(render_wrd, wrd_rect)
    if words[word_num][-1] in ".,":
        sleep(0.1)

    word_num += 1

    clock.tick(fps)
    py.display.update()
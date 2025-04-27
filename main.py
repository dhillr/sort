import math
import random
import time
import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("sorting algorithm -_-")

class Sort:
    def __init__(self, arr, anim_values=None):
        self.arr = arr
        self.anim_values = anim_values

    def get(self): return self.arr

def sort(arr: list) -> Sort:
    digits = math.floor(math.log10(max(arr)) + 1)
    vals = [arr]

    for d in range(digits):
        buckets = [[] for _ in range(10)]

        for item in arr:
            buckets[digitLSD(d, item)].append(item)
        
        arr = []

        for bucket in buckets:
            for bucket_item in bucket:
                arr.append(bucket_item)

        vals.append(arr)
    return Sort(arr, anim_values=vals)

def digitLSD(digit, num) -> int:
    return (num // (10 ** digit)) % 10

def gen(len):
    res = []
    for i in range(len): res.append(i+1)
    random.shuffle(res)
    return res

unsorted = gen(128)
sorted = sort(unsorted)
l = len(sorted.get())

start_time = time.time()
millis = 0

DELAY = 10

while True:
    screen.fill((255, 255, 255))

    scale = (screen.get_width()/l, screen.get_height()/l)

    val = sorted.anim_values[(int(millis//DELAY)//l)%len(sorted.anim_values)]
    val_p = sorted.anim_values[(int(millis//DELAY)//l-1)%len(sorted.anim_values)]
    
    current = int(millis//DELAY)%l

    for i in range(current):
        elem = val[i]
        pygame.draw.rect(screen, (elem*(255/l), elem*(127/l), elem*(200/l)), (i*scale[0], screen.get_height()-elem*scale[1], scale[0], 720))
    for i in range(current, l):
        elem = val_p[i]
        pygame.draw.rect(screen, (elem*(255/l), elem*(127/l), elem*(200/l)), (i*scale[0], screen.get_height()-elem*scale[1], scale[0], 720))

    element = val[current]
    pygame.draw.rect(screen, (255, 0, 0), (current*scale[0], screen.get_height()-element*scale[1], scale[0], 720))

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()

    pygame.display.flip()
    millis = 1000 * (time.time() - start_time)
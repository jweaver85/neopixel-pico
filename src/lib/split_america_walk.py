from .utils import walk, render

COLOR01 = (255, 0, 0)  # RED
COLOR02 = (255, 255, 255)  # WHITE
COLOR03 = (0, 0, 255)  # BLUE


def split_america_walk(options):
    if len(options.buffer) == 0:
        walk(COLOR01, COLOR02, options)
        walk(COLOR02, COLOR03, options)
        walk(COLOR03, COLOR02, options)
        walk(COLOR02, COLOR01, options)

    start = int(0)
    left_middle = int(len(options.colors) / 2 - 1)
    right_middle = int(left_middle + 1)
    end = int(len(options.colors) - 1)

    popped = options.buffer.pop()
    options.buffer.push(popped)

    options.colors.remove(start)
    options.colors.insert(left_middle, popped)

    options.colors.remove(end)
    options.colors.insert(right_middle, popped)
    render(options)

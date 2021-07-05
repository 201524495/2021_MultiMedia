from pynput import mouse


# Mouse Clicked Point
def on_click(x, y, button, pressed):
    if pressed == False:
        print(x, y)


with mouse.Listener(on_click=on_click) as listener:
    listener.join()



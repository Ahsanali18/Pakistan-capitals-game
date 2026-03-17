from turtle import Screen

screen = Screen()
screen.bgpic("map.gif")

def get_mouse_click_coor(x, y):
    print(x, y)

screen.onscreenclick(get_mouse_click_coor)

screen.mainloop()
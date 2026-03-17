from turtle import Turtle, Screen
import pandas as pd


screen = Screen()
t = Turtle()

screen.title("Pakistan Capital Game")
screen.setup(width=800, height=600)
image = "map.gif"

screen.addshape(image)
t.shape(image)

data = pd.read_csv("pakistan_capitals.csv")
capital_cities = data.City.to_list()

guessed_cities = []

while len(guessed_cities) < 7:
    answer_city = screen.textinput(title=f"{len(guessed_cities)}/50 City Correct", prompt="What's another capital city's name?").title()
    
    if answer_city == 'Exit':
        missing_cities = []
        for city in capital_cities:
            if city not in guessed_cities:
                missing_cities.append(city)
        new_data = pd.DataFrame(missing_cities)
        new_data.to_csv("cities_to_learn.csv")
        break
    if answer_city in capital_cities:
        guessed_cities.append(answer_city)
        new_turtle = Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()

        city_data = data[data.City == answer_city]

        x_coordinate = int(city_data.x.item())
        y_coordinate = int(city_data.y.item())

        new_turtle.goto(x_coordinate, y_coordinate)
        new_turtle.write(answer_city)

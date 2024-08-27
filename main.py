import turtle
import pandas

screen = turtle.Screen()
screen.title("Asian Country Game")
image = "asian_country.gif"
screen.addshape(image)
turtle.shape(image)
correct_guess = []
while len(correct_guess) < 50:
    answer_country = screen.textinput(title=f"{len(correct_guess)}/50 country correct", prompt="What's the another country's name?")
    answer = answer_country.title()

    data = pandas.read_csv("asian_country.csv")
    if answer == "Exit":
        missing_country = []
        for country in data["Country"]:
            if country not in correct_guess:
                missing_country.append(country)
        print(f"The missed countries {missing_country}")
        new_data = pandas.DataFrame(missing_country)
        new_data.to_csv("stated_to_learn.csv")
        break
    if answer in data["Country"].tolist() and answer not in correct_guess:
        correct_guess.append(answer)

        county_data = data[data.Country == answer]
        x_cor = float(county_data["x"].iloc[0])
        y_cor = float(county_data["y"].iloc[0])
        writer_turtle = turtle.Turtle()
        writer_turtle.penup()
        writer_turtle.hideturtle()
        writer_turtle.goto(x_cor, y_cor)
        writer_turtle.write(answer, align="center", font=("Arial", 12, "normal"))





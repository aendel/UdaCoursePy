def welcome_message(name):
#Prints out a personalised welcome message
    return "Welcome to this Python script, " + name + "!"

#Call the welcome message function with the input "Udacity Student"
#and print the output
print(welcome_message("Udacity Student"))

how_many_snakes = 1
snake_string = """
Welcome to Python3!

             ____
            / . .\\
            \  ---<
             \  /
   __________/ /
-=:___________/

<3, Philip and Charlie
"""


print(snake_string * how_many_snakes)

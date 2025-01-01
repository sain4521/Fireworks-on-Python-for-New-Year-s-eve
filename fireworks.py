# first setups
import turtle
name = "Everyone"

# initialization
scrn = turtle.Screen()
scrn.bgcolor("#000")
scrn.title("New Year 2025!")
scrn.setup(width = 1.0, height = 1.0)
canvas = scrn.getcanvas()
root = canvas.winfo_toplevel()
root.overrideredirect(1)
firework = turtle.Turtle()
firework.pensize(5)
firework.shape("turtle")
size = 20
firework.stamp
firework.speed(100)
firework.left(90)

# first pattern
firework.color("#ff0000")
for step in range(40):
  firework.forward(100)
  firework.left(180)
  firework.forward(100)
  firework.left(9)
  
# second pattern
firework.color("#ff9100")
for step in range(36):
  firework.forward(130)
  firework.left(180)
  firework.forward(130)
  firework.left(10)
  
# third patern
firework.color("#0400ff")
for step in range(20):
  firework.forward(150)
  firework.left(180)
  firework.forward(150)
  firework.left(18)

# forth pattern
firework.color("#bb00ff")
for step in range(15):
  firework.forward(180)
  firework.left(180)
  firework.forward(180)
  firework.left(25)

# last pattern
firework.color("#fce808")
for stamps in range(12):
  firework.penup()
  firework.forward(170)
  firework.pendown()
  firework.forward(10)
  firework.penup()
  firework.forward(10)
  firework.stamp()
  firework.right(30)
  firework.penup()
  firework.setpos(0, 0)

text = turtle.Turtle()
text.color("#fff")
text.penup()
text.setpos(0, -240)
text.write("Happy New Year 2025, " + str(name) + "!", True, align="center", font=("Arial", 20, "normal"))
text.setpos(0, -330)
text.write("Best wishes for the next year!", True, align="center", font=("Arial", 17, "normal"))
text.setpos(0, -350)

scrn.mainloop()
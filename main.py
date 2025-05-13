from tkinter import *

FONT = "Courier"
BG_YELLOW = "#FFF7D1"

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=BG_YELLOW)

canvas = Canvas(width=200, height=224, bg=BG_YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato )
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT, 35, "bold"))
canvas.pack()



window.mainloop()
from tkinter import *

FONT = "Courier"
BG_YELLOW = "#FFF7D1"
FG_GREEN = "#79AC78"

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=BG_YELLOW)


timer_label = Label(text="Timer", font=(FONT, 70, "bold"), bg=BG_YELLOW, fg=FG_GREEN)
timer_label.grid(column=1, row=0)



canvas = Canvas(width=200, height=224, bg=BG_YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato )
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT, 35, "bold") )
canvas.grid(column=1, row=1)

start_button = Button(text="START", font=(FONT, 35, "bold") ,bg=BG_YELLOW,highlightthickness=0)
start_button.grid(column=0, row=2)


reset_button = Button(text="RESET", font=(FONT, 35, "bold"), bg=BG_YELLOW, highlightthickness=0)
reset_button.grid(column=2, row=2)

check_mark = Label(text="🍅", font=(FONT, 35, "bold"), bg=BG_YELLOW)
check_mark.grid(column=1, row=3)


window.mainloop()
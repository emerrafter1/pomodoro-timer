from tkinter import *
import math

FONT = "Courier"
BG_YELLOW = "#FFF7D1"
FG_GREEN = "#79AC78"
WORKING_MINUTES = 25
SHORT_BREAK = 5
LONG_BREAK = 20
reps = 0
timer = None


window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=BG_YELLOW)

timer_label = Label(text=f"Timer", font=(FONT, 70, "bold"), bg=BG_YELLOW, fg=FG_GREEN)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=BG_YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato )
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT, 35, "bold") )
canvas.grid(column=1, row=1)



def count_down(count):

    count_minutes = math.floor(count / 60)
    count_seconds = count % 60

    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1 )
    else:
        start_timer()
        progress_mark_text = ""
        completed_sessions = math.floor(reps/2)
        for _ in range(completed_sessions):
            progress_mark_text += "🍅"

        progress_mark.config(text=progress_mark_text)


def start_timer():
    global reps
    reps += 1

    work_seconds = WORKING_MINUTES * 60
    short_break_seconds = SHORT_BREAK * 60
    long_break_seconds = LONG_BREAK * 60

    if reps % 8 == 0:
        count_down(long_break_seconds)
        timer_label.config(text="Break!")
    elif reps % 2 == 0:
        count_down(short_break_seconds)
        timer_label.config(text="Break!")
    else:
        count_down(work_seconds)
        timer_label.config(text="Work!")

def reset_timer():
    global timer
    global reps
    reps = 0
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    progress_mark.config(text="")


start_button = Button(text="START", font=(FONT, 35, "bold") ,bg=BG_YELLOW,highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="RESET", font=(FONT, 35, "bold"), bg=BG_YELLOW, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

progress_mark = Label( font=(FONT, 35, "bold"), bg=BG_YELLOW)
progress_mark.grid(column=1, row=3)



window.mainloop()
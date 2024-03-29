
from tkinter import *
import math
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.05
SHORT_BREAK_MIN = 0.05
LONG_BREAK_MIN = 20
reps = 0
timer = None

# Timer Reset

def timer_reset():
    global timer
    global reps
    window.after_cancel(timer)
    reps = 0
    time_label.configure(text="Timer", fg = GREEN)
    check_marks.configure(text='')
    canvas.itemconfig(timer_text, text="00:00")

# Timer Mechanism

def start_timer():
    global reps
    reps += 1
    work_secs = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps == 8:
        countdown(long_break)
        reps = 0
        time_label.configure(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break)
        time_label.configure(text="Break", fg=PINK)
        marks = ""
        work_sessions = math.floor(reps / 2)
        for m in range(work_sessions):
            marks += "✔"
        check_marks.configure(text = marks)
    else:
        countdown(work_secs)
        time_label.configure(text="Work", fg=GREEN)

# Countdown Mechanism


def countdown(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10 or count_sec == 0:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()


# UI Set up
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

time_label = Label(text="Timer", font=(FONT_NAME, 35), bg=YELLOW, fg=GREEN)
time_label.grid(column=2, row=1,)

start_button = Button(text="Start", command=start_timer, highlightbackground=YELLOW)
start_button.grid(column=1, row=3)
start_button = Button(text="Reset", command=timer_reset, highlightbackground=YELLOW)
start_button.grid(column=3, row=3)

check_marks = Label(bg=YELLOW, fg=GREEN)
check_marks.grid(column=2, row=4)

window.mainloop()
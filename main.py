from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier New"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_marks.config(text="")
    start.configure(state=NORMAL)


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    start.configure(state=DISABLED)
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break", fg=RED)
        window.lift()
        window.attributes('-topmost', True)
        window.after_idle(window.attributes, '-topmost', False)
        window.iconify()
        window.update()
        window.deiconify()
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Short Break", fg=PINK)
        window.lift()
        window.attributes('-topmost', True)
        window.after_idle(window.attributes, '-topmost', False)
        window.iconify()
        window.update()
        window.deiconify()
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)
        window.attributes('-topmost', True)
        window.after_idle(window.attributes, '-topmost', False)
        window.iconify()
        window.update()
        window.deiconify()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=30, bg=YELLOW)
window.iconbitmap('icon.ico')
window.resizable(0, 0)

# Label
timer_label = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pomodoro_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=pomodoro_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# Buttons
start_photo = PhotoImage(file="start.png")
reset_photo = PhotoImage(file="reset.png")
start = Button(image=start_photo, border=0, highlightthickness=0, command=start_timer)
reset = Button(image=reset_photo, border=0, highlightthickness=0, command=reset_timer)
start.grid(column=0, row=2)
reset.grid(column=2, row=2)

# Check Marks
check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

# Holding Screen
window.mainloop()

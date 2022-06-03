from tkinter import *
import time

root = Tk()
root.configure(background=("black"))
root.title("Stopwatch")
root.geometry("500x200")


Grid.columnconfigure(root, index=(0, 2, 4), weight=1)
Grid.rowconfigure(root, index=0, weight=1)

time_elapsed1 = -1
time_elapsed2 = 0
time_elapsed3 = 0
time1 = 0
time2 = 0
i = 0
j = 0

middleframe = Frame(root)
middleframe.grid(row=3, column=0, columnspan=5)
middleframe.configure(background="black")


def create_label(text, _x, _y):
    label = Label(middleframe, text=text, fg="white", bg="black", font=("default", 10, "bold"))
    label.pack(side=LEFT, padx=2)


def start():
    start_button.grid_forget()
    resume_button.grid_forget()
    stop_button.grid(row=1, column=0, sticky="nsew")
    global time_elapsed1, time_elapsed2, time_elapsed3, time1, self_job, time2
    time2 = int(time.time())
    if time2 != time1:
        time1 = time2
        if time_elapsed1 < 59:
            time_elapsed1 += 1
            clock_frame.config(text=(str(time_elapsed3).zfill(2) + ":" + str(time_elapsed2).zfill(2) + ":" + str(
                time_elapsed1).zfill(2)))
        else:
            time_elapsed1 = 0

            if time_elapsed2 < 59:
                time_elapsed2 += 1
                clock_frame.config(text=(str(time_elapsed3).zfill(2) + ":" + str(time_elapsed2).zfill(2) + ":" + str(
                    time_elapsed1).zfill(2)))
            else:
                time_elapsed2 = 0
                time_elapsed3 += 1
                if time_elapsed3 >= 24:
                    time_elapsed1 = 0
                    time_elapsed2 = 0
                    time_elapsed3 = 0
                else:
                    time_elapsed3 += 1
                    clock_frame.config(text=(
                                str(time_elapsed3).zfill(2) + ":" + str(time_elapsed2).zfill(2) + ":" + str(
                            time_elapsed1).zfill(2)))
    self_job = root.after(900, start)


def stop():
    global self_job
    if self_job is not None:
        root.after_cancel(self_job)
        self_job = None
    stop_button.grid_forget()
    resume_button.grid(row=1, column=0, sticky="nsew")


def resume():
    start_button.grid_forget()
    resume_button.grid_forget()
    stop_button.grid(row=1, column=0, sticky="nsew")
    global time_elapsed1, time_elapsed2, time_elapsed3, time1, self_job, time2
    time2 = int(time.time())
    if time2 != time1:
        time1 = time2
        if time_elapsed1 < 59:
            time_elapsed1 += 1
            clock_frame.config(text=(str(time_elapsed3).zfill(2) + ":" + str(time_elapsed2).zfill(2) + ":" + str(
                time_elapsed3).zfill(2)))
        else:
            time_elapsed1 = 0
            time_elapsed2 += 1
            if time_elapsed2 < 59:
                time_elapsed2 += 1
                clock_frame.config(text=(str(time_elapsed3).zfill(2) + ":" + str(time_elapsed2).zfill(2) + ":" + str(
                    time_elapsed1).zfill(2)))
            else:
                time_elapsed2 = 0
                time_elapsed3 += 1
                if time_elapsed3 >= 24:
                    time_elapsed1 = 0
                    time_elapsed2 = 0
                    time_elapsed3 = 0
                else:
                    time_elapsed3 += 1
                    clock_frame.config(text=(
                                str(time_elapsed3).zfill(2) + ":" + str(time_elapsed2).zfill(2) + ":" + str(
                            time_elapsed1).zfill(2)))
    self_job = root.after(900, start)


def clear():
    global time_elapsed1, time_elapsed2, time_elapsed3, time1, self_job, time2, label, i, j
    try:
        stop()
    except:
        start()
        stop()
    clock_frame.config(text="00:00:00")
    time_elapsed1 = -1
    time_elapsed2 = 0
    time_elapsed3 = 0
    time_1 = 0
    time_2 = 0
    i = 0
    j = 0
    wig = middleframe.winfo_children()
    for b in wig:
        b.pack_forget()
        resume_button.grid_forget()
    start_button.grid(row=1, column=0, sticky="nsew", padx=2)
    reset_button.grid(row=1, column=2, sticky="nsew", padx=2)
    lap_button.grid(row=1, column=4, sticky="nsew", padx=2)
    clock_frame.grid(row=0, column=0, columnspan=5, sticky="nsew")


def lap():
    global time_elapsed1, time_elapsed2, time_elapsed3, time1, self_job, time2, i, j
    if i < 9:
        create_label(
            (str(time_elapsed3).zfill(2) + ":" + str(time_elapsed2).zfill(2) + ":" + str(time_elapsed1).zfill(2)),
            20 + (110 * i), 400 + (j * 50))
    else:
        j += 1
        i = 0
        create_label(
            (str(time_elapsed3).zfill(2) + ":" + str(time_elapsed2).zfill(2) + ":" + str(time_elapsed1).zfill(2)),
            20 + (110 * i), 400 + (j * 50))
    i += 1


def resize(e):
    size = e.width / 10
    start_button.config(font=("monotxt", int(size), "bold"))
    stop_button.config(font=("monotxt", int(size), "bold"))
    resume_button.config(font=("monotxt", int(size), "bold"))
    lap_button.config(font=("monotxt", int(size), "bold"))
    reset_button.config(font=("monotxt", int(size), "bold"))

    height_size = e.height - 10
    if e.height <= 300:
        clock_frame.config(font=("monotxt", height_size, "bold"))

def button_hover(e):
    start_button["bg"] = "#ff004c"
    start_button["fg"] = "black"
def button_hover_leave(e):
    start_button["bg"] = "black"
    start_button["fg"] = "#ff004c"

def button_hover1(e):
    stop_button["bg"] = "#ff004c"
    stop_button["fg"] = "black"
def button_hover_leave1(e):
    stop_button["bg"] = "black"
    stop_button["fg"] = "#ff004c"

def button_hover2(e):
    resume_button["bg"] = "#ff004c"
    resume_button["fg"] = "black"
def button_hover_leave2(e):
    resume_button["bg"] = "black"
    resume_button["fg"] = "#ff004c"

def button_hover3(e):
    reset_button["bg"] = "#00fff7"
    reset_button["fg"] = "black"
def button_hover_leave3(e):
    reset_button["bg"] = "black"
    reset_button["fg"] = "#00fff7"

def button_hover4(e):
    lap_button["bg"] = "#fffb00"
    lap_button["fg"] = "black"
def button_hover_leave4(e):
    lap_button["bg"] = "black"
    lap_button["fg"] = "#fffb00"

clock_frame = Label(text="00:00:00", bg="black", fg="white")
start_button = Button(text="START", bg="black", fg="#ff004c", borderwidth=0, command=start)
stop_button = Button(text="PAUSE", bg="black", fg="#ff004c", borderwidth=0, command=stop)
resume_button = Button(text="RESUME", bg="black", fg="#ff004c", borderwidth=0, command=start)
reset_button = Button(text="RESET", bg="black", fg="#00fff7", borderwidth=0, command=clear)
lap_button = Button(text="LAP", bg="black", fg="#fffb00", borderwidth=0, command=lap)

start_button.grid(row=1, column=0, sticky="nsew", padx=2)
reset_button.grid(row=1, column=2, sticky="nsew", padx=2)
lap_button.grid(row=1, column=4, sticky="nsew", padx=2)
clock_frame.grid(row=0, column=0, columnspan=5, sticky="nsew")

start_button.bind("<Enter>", button_hover)
start_button.bind("<Leave>", button_hover_leave)
stop_button.bind("<Enter>", button_hover1)
stop_button.bind("<Leave>", button_hover_leave1)
resume_button.bind("<Enter>", button_hover2)
resume_button.bind("<Leave>", button_hover_leave2)
reset_button.bind("<Enter>", button_hover3)
reset_button.bind("<Leave>", button_hover_leave3)
lap_button.bind("<Enter>", button_hover4)
lap_button.bind("<Leave>", button_hover_leave4)

root.bind('<Configure>', resize)

root.mainloop()

from tkinter import *
import time

root=Tk()
root.configure(background=("white"))
root.title("Stopwatch")
root.geometry("980x480")

time_elapsed1=-1
time_elapsed2=0
time_elapsed3=0
time1=0
time2=0
i=0
j=0

def create_label(text,_x,_y):
    label=Label(root, text=text, fg="white", bg="white", font=("default", 10, "bold"))
    label.place(x=_x, y=_y, width=100, height=45)

def start():
    start_button.place_forget()
    resume_button.place_forget()
    stop_button.place(x=20, y=300, width=300, height=100)
    global time_elapsed1, time_elapsed2, time_elapsed3, time1, self_job, time2
    time2=int(time.time())
    if time2!=time1:
        time1=time2
        if time_elapsed1<59:
            time_elapsed1+=1
            clock_frame.config(text=(str(time_elapsed3).zfill(2)+":"+str(time_elapsed2).zfill(2)+":"+str(time_elapsed1).zfill(2)))
        else:
            time_elapsed1=0
            
            if time_elapsed2<59:
                time_elapsed2+=1
                clock_frame.config(text=(str(time_elapsed3).zfill(2)+":"+str(time_elapsed2).zfill(2)+":"+str(time_elapsed1).zfill(2)))
            else:
                time_elapsed2=0
                time_elapsed3+=1
                if time_elapsed3>=24:
                    time_elapsed1=0
                    time_elapsed2=0
                    time_elapsed3=0
                else:
                    time_elapsed3+=1
                    clock_frame.config(text=(str(time_elapsed3).zfill(2)+":"+str(time_elapsed2).zfill(2)+":"+str(time_elapsed1).zfill(2)))
    self_job=root.after(900,start)

def stop():
    global self_job
    if self_job is not None:
        root.after_cancel(self_job)
        self_job=None
    stop_button.place_forget()
    resume_button.place(x=20, y=300, width=300, height=100)

def resume():
    start_button.place_forget()
    resume_button.place_forget()
    stop_button.place(x=20, y=300, width=300, height=100)
    global time_elapsed1, time_elapsed2, time_elapsed3, time1, self_job, time2
    time2=int(time.time())
    if time2!=time1:
        time1=time2
        if time_elapsed1<59:
            time_elapsed1+=1
            clock_frame.config(text=(str(time_elapsed3).zfill(2)+":"+str(time_elapsed2).zfill(2)+":"+str(time_elapsed3).zfill(2)))
        else:
            time_elapsed1=0
            time_elapsed2+=1
            if time_elapsed2<59:
                time_elapsed2+=1
                clock_frame.config(text=(str(time_elapsed3).zfill(2)+":"+str(time_elapsed2).zfill(2)+":"+str(time_elapsed1).zfill(2)))
            else:
                time_elapsed2=0
                time_elapsed3+=1
                if time_elapsed3>=24:
                    time_elapsed1=0
                    time_elapsed2=0
                    time_elapsed3=0
                else:
                    time_elapsed3+=1
                    clock_frame.config(text=(str(time_elapsed3).zfill(2)+":"+str(time_elapsed2).zfill(2)+":"+str(time_elapsed1).zfill(2)))
    self_job=root.after(900,start)

def clear():
      global time_elapsed1, time_elapsed2, time_elapsed3, time1, self_job, time2, label, i, j
      try: 
          stop()
      except:
          start()
          stop()
      clock_frame.config(text="00:00:00")
      time_elapsed1=-1
      time_elapsed2=0
      time_elapsed3=0
      time_1=0
      time_2=0
      i=0
      j=0
      wig=root.winfo_children()
      for b in wig:
          b.place_forget()
          resume_button.place_forget()
      start_button.place(x=20, y=300, width=300, height=100)
      lap_button.place(x=660, y=300, width=300, height=100)
      reset_button.place(x=340, y=300, width=300, height=100)
      clock_frame.place(x=200, y=50, width=600, height=200)

def lap():
    global time_elapsed1, time_elapsed2, time_elapsed3, time1, self_job, time2, i, j
    if i<9:
        create_label((str(time_elapsed3).zfill(2)+":"+str(time_elapsed2).zfill(2)+":"+str(time_elapsed1).zfill(2)),20+(110*i),400+(j*50))
    else:
        j+=1
        i=0
        create_label((str(time_elapsed3).zfill(2)+":"+str(time_elapsed2).zfill(2)+":"+str(time_elapsed1).zfill(2)), 20+(110*i), 400+(j*50))
    i+=1

clock_frame=Label(text="00:00:00", bg="white", fg="black", font=("monotxt", 75, "bold"))
start_button=Button(text="START", bg="pink", fg="black", borderwidth=10, command=start, font=("monotxt", 30, "bold"))
stop_button=Button(text="STOP", bg="pink", fg="black", borderwidth=10, command=stop, font=("monotxt", 30, "bold"))
resume_button=Button(text="RESUME", bg="pink", fg="black", borderwidth=10, command=start, font=("monotxt", 30, "bold"))
lap_button=Button(text="LAP", bg="pink", fg="black", borderwidth=10, command=lap, font=("monotxt", 30, "bold"))
reset_button=Button(text="RESET", bg="pink", fg="black", borderwidth=10, command=clear, font=("monotxt", 30, "bold"))

start_button.place(x=20, y=300, width=300, height=100)
lap_button.place(x=660, y=300, width=300, height=100)
reset_button.place(x=340, y=300, width=300, height=100)
clock_frame.place(x=200, y=50, width=600, height=200)

root.mainloop()




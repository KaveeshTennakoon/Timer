import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time

def countdown():
    try:
        hours = int(hours_entry.get())
        minutes = int(minutes_entry.get())
        seconds = int(seconds_entry.get())

        total_seconds = (hours * 3600) + (minutes * 60) + seconds

        # Hide the input frame and show the timer frame
        input_frame.pack_forget()
        timer_frame.pack()

        while total_seconds >= 0:
            mins, secs = divmod(total_seconds, 60)
            hours, mins = divmod(mins, 60)
            timeformat = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
            
            # Change text color to red if remaining time is less than 3 seconds
            if total_seconds <= 3:
                timer_label.config(text=timeformat, fg="red")
            else:
                timer_label.config(text=timeformat, fg="black")
            
            root.update()
            time.sleep(1)
            total_seconds -= 1

        choice = messagebox.askquestion("Timer", "Time's up! Do you want to enter another time?")
        
        if choice == 'yes':
            input_frame.pack()  # Show the input frame again
            timer_frame.pack_forget()  # Hide the timer frame
            clear_entries()
        else:
            root.quit()  # Quit the program

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid values for hours, minutes, and seconds.")

def clear_entries():
    hours_entry.delete(0, tk.END)
    minutes_entry.delete(0, tk.END)
    seconds_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Countdown Timer")

notebook = ttk.Notebook(root)
notebook.pack(padx=20, pady=20)

input_frame = ttk.Frame(notebook)
timer_frame = ttk.Frame(notebook)

notebook.add(input_frame, text="Input")

hours_label = tk.Label(input_frame, text="Hours:")
hours_label.pack()
hours_entry = tk.Entry(input_frame)
hours_entry.pack()

minutes_label = tk.Label(input_frame, text="Minutes:")
minutes_label.pack()
minutes_entry = tk.Entry(input_frame)
minutes_entry.pack()

seconds_label = tk.Label(input_frame, text="Seconds:")
seconds_label.pack()
seconds_entry = tk.Entry(input_frame)
seconds_entry.pack()

start_button = tk.Button(input_frame, text="Start Timer", command=countdown)
start_button.pack()

timer_label = tk.Label(timer_frame, font=("Arial", 24))
timer_label.pack(padx=20, pady=20)

root.mainloop()



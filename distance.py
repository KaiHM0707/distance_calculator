from tkinter import *

scr = Tk()
scr.geometry("300x200")
scr.title("Distance Calculator")

top_frame = Frame(scr, bg="lightblue")
top_frame.pack(fill=BOTH, expand=True)

bottom_frame = Frame(scr, bg="lightgreen")
bottom_frame.pack(fill=BOTH, expand=True)

Label(top_frame, text="How many hours?", bg="lightblue").pack(pady=5)
time_entry = Entry(top_frame)
time_entry.pack(pady=5)

Label(top_frame, text="How fast? (km/h)", bg="lightblue").pack(pady=5)
speed_entry = Entry(top_frame)
speed_entry.pack(pady=5)

def calculate_distance():
    time = time_entry.get()
    speed = speed_entry.get()

    if time.isdigit() and speed.isdigit():
        time = float(time)
        speed = float(speed)
        distance = time * speed
        result_label.config(text=f"Total distance: {distance} km")
    else:
        result_label.config(text="Enter valid numbers.")


Button(bottom_frame, text="Calculate", command=calculate_distance, bg="blue", fg="white").pack(pady=10)

result_label = Label(bottom_frame, text="Total distance: 0.00 km", bg="lightgreen")
result_label.pack(pady=10)

scr.mainloop()

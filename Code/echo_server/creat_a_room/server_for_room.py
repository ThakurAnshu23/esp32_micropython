import tkinter as tk

# Create a window
window = tk.Tk()
window.title("Virtual Room")

# Define the dimensions of the room
room_width = 800
room_height = 600

# Create a canvas to represent the room
canvas = tk.Canvas(window, width=room_width, height=room_height, bg="#f0f0f0")
canvas.pack()

# Add elements to the room
canvas.create_text(room_width // 2, room_height // 2, text="Welcome to the Virtual Room", font=("Arial", 20))
canvas.create_text(room_width // 2, room_height // 2 + 30, text="This is a virtual room created using Tkinter.", font=("Arial", 12))

# Run the Tkinter event loop
window.mainloop()

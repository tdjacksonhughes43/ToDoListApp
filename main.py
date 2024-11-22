import tkinter as tk

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Task Tracker")
    root.geometry("400x400")  # Set the size of the window

    # Add a label to the main window
    title_label = tk.Label(root, text="Task Tracker", font=("Helvetica", 16))
    title_label.pack(pady=20)

    # Add a button to close the app
    exit_button = tk.Button(root, text="Exit", command=root.quit)
    exit_button.pack(pady=10)

    # Start the Tkinter main loop
    root.mainloop()

if __name__ == "__main__":
    main()

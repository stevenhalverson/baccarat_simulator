import tkinter as tk
from tkinter import messagebox
from simulation import BaccaratSimulation
import pandas as pd
from data_access import *

class BaccaratGUI:
    def __init__(self, root):
        self.root = root
        root.title("Baccarat Simulation")
        root.geometry("800x600")

        # Entry for number of shoes
        shoes_label = tk.Label(root, text="Enter Number of Shoes:")
        shoes_label.pack()
        self.shoes_entry = tk.Entry(root)
        self.shoes_entry.pack()

        # Button to start simulation
        start_button = tk.Button(root, text="Start Simulation", command=self.start_simulation)
        start_button.pack(pady=10)

        # Button to exit
        exit_button = tk.Button(root, text="Exit", command=root.destroy)
        exit_button.pack(pady=10)

    def start_simulation(self):
        try:
            num_shoes = int(self.shoes_entry.get())
            sim = BaccaratSimulation()
            sim.begin_simulation(shoes=num_shoes)
            sim.get_csv()
            sim.save_to_sqlite_db()
            messagebox.showinfo("Success", "Simulation completed and data saved.")
        except ValueError:
            messagebox.showerror("Error", "Invalid number of shoes. Please enter a valid number.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BaccaratGUI(root)
    root.mainloop()

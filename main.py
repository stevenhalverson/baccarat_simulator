import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from simulation import BaccaratSimulation
import pandas as pd
from data_access import *
import threading
import queue

class BaccaratGUI:
    MIN_SHOES = 1
    MAX_SHOES = 15000
    
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

        #Progress bar
        self.progress_queue = queue.Queue()
        self.progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=20)

        self.simulation_complete = threading.Event()

    def start_simulation(self):
        try:
            num_shoes = int(self.shoes_entry.get())

            if not self.MIN_SHOES <= num_shoes <= self.MAX_SHOES:
                raise ValueError(f"Please enter a number between {self.MIN_SHOES} and {self.MAX_SHOES}.")
            
            sim = BaccaratSimulation(progress_queue=self.progress_queue, completion_flag=self.simulation_complete)
            simulation_thread = threading.Thread(target=self.run_simulation, args=(sim, num_shoes))
            simulation_thread.start()
            
        except ValueError as e:
            messagebox.showerror("Error", str(e))

        self.check_progress() #should this go here?

    def check_progress(self):
        try:
            progress = self.progress_queue.get_nowait()
            self.progress["value"] = progress

        except queue.Empty:
            pass
        
        if self.simulation_complete.is_set():
            self.progress["value"] = 100
            pass
        else:
            self.root.after(100, self.check_progress)
    
    def run_simulation(self, sim, num_shoes):
            sim.begin_simulation(shoes=num_shoes)
            sim.get_csv()
            sim.save_to_sqlite_db()
            messagebox.showinfo("Success", "Simulation completed and data saved.")


if __name__ == "__main__":
    root = tk.Tk()
    app = BaccaratGUI(root)
    root.mainloop()
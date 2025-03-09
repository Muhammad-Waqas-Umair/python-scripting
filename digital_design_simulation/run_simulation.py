import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
import threading

class VerilogSimGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Verilog Simulation GUI")
        self.root.geometry("600x400")

        # Variables to store file paths
        self.module_file = ""
        self.testbench_file = ""

        # Create GUI components
        self.create_widgets()

    def create_widgets(self):
        # File selection for Verilog files
        self.select_module_button = tk.Button(self.root, text="Select Module File", command=self.select_module_file)
        self.select_module_button.pack(pady=20)

        self.select_testbench_button = tk.Button(self.root, text="Select Testbench File", command=self.select_testbench_file)
        self.select_testbench_button.pack(pady=20)

        # Compile and run buttons
        self.compile_button = tk.Button(self.root, text="Compile and Run Simulation", command=self.compile_and_run)
        self.compile_button.pack(pady=20)

        # Output display area
        self.output_text = tk.Text(self.root, height=10, width=70)
        self.output_text.pack(pady=20)

    def select_module_file(self):
        """Open file dialog to select the module file."""
        self.module_file = filedialog.askopenfilename(title="Select Module File", filetypes=(("Verilog Files", "*.v"), ("All Files", "*.*")))
        if self.module_file:
            self.output_text.insert(tk.END, f"Selected Module File: {self.module_file}\n")

    def select_testbench_file(self):
        """Open file dialog to select the testbench file."""
        self.testbench_file = filedialog.askopenfilename(title="Select Testbench File", filetypes=(("Verilog Files", "*.v"), ("All Files", "*.*")))
        if self.testbench_file:
            self.output_text.insert(tk.END, f"Selected Testbench File: {self.testbench_file}\n")

    def compile_and_run(self):
        """Compile and run the Verilog files using Icarus Verilog."""
        if not self.module_file or not self.testbench_file:
            messagebox.showerror("Error", "Please select both module and testbench files.")
            return

        # Clear previous output
        self.output_text.delete(1.0, tk.END)

        # Step 1: Compile Verilog files using iverilog
        compile_command = f"iverilog -o simulation_output.vvp {self.module_file} {self.testbench_file}"
        compilation_result = subprocess.run(compile_command, shell=True, capture_output=True, text=True)

        if compilation_result.returncode != 0:
            self.output_text.insert(tk.END, f"Compilation failed with error: {compilation_result.stderr}\n")
            return
        else:
            self.output_text.insert(tk.END, "Compilation successful!\n")

        # Step 2: Run the simulation using vvp
        run_command = "vvp simulation_output.vvp"
        simulation_result = subprocess.run(run_command, shell=True, capture_output=True, text=True)

        if simulation_result.returncode != 0:
            self.output_text.insert(tk.END, f"Simulation failed with error: {simulation_result.stderr}\n")
        else:
            self.output_text.insert(tk.END, "Simulation successful!\n")
            self.output_text.insert(tk.END, "Simulation Output:\n")
            self.output_text.insert(tk.END, simulation_result.stdout)

            # Visualize the output using matplotlib
            self.visualize_circuit(faulty_circuit="example_circuit", faulty_nodes=["example_node"])

    def visualize_circuit(self, faulty_circuit, faulty_nodes):
        """Function to visualize a circuit (or simulation output)"""
        # Enable interactive mode
        plt.ion()

        # Example of plotting a simple faulty circuit visualization (you can replace this with your logic)
        fig, ax = plt.subplots()
        ax.plot([0, 1, 2], [0, 1, 0], label='Circuit Output')

        # Highlight faulty nodes (for example purposes, using a simple annotation)
        for node in faulty_nodes:
            ax.annotate(f"Faulty: {node}", xy=(1, 1), xytext=(2, 1),
                        arrowprops=dict(facecolor='red', shrink=0.05))

        ax.set_title(f"Visualization of Faults in {faulty_circuit}")
        ax.set_xlabel('Time')
        ax.set_ylabel('Signal')
        ax.legend()

        # Use threading to avoid blocking the GUI's mainloop
        threading.Thread(target=self.display_plot, args=(fig,)).start()

    def display_plot(self, fig):
        """Threaded function to display the plot without blocking the Tkinter GUI"""
        # Ensure plt.show() is called from the main thread
        self.root.after(0, self._show_plot, fig)

    def _show_plot(self, fig):
        """Helper function to display the plot in the main thread"""
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = VerilogSimGUI(root)
    root.mainloop()

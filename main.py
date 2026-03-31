import tkinter as tk
import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("360x580")
        self.root.resizable(False, False)
        self.root.configure(bg="#121212")  
        
        self.current_input = ""
        self.full_operation = ""
        self.ans = 0
        
        self.create_display()
        
        self.create_buttons()
    
    def create_display(self):
        display_frame = tk.Frame(self.root, bg="#121212", bd=0, relief=tk.FLAT)
        display_frame.pack(padx=10, pady=10, fill=tk.X)
        
        self.operation_display = tk.Label(display_frame, text="", bg="#121212", fg="#8E8E93", 
                                         font=("Arial", 14), anchor=tk.E, wraplength=340)
        self.operation_display.pack(fill=tk.X, pady=(5, 0))
        
        self.display = tk.Label(display_frame, text="0", bg="#121212", fg="#FFFFFF", 
                               font=("Arial", 48, "bold"), anchor=tk.E, padx=10, pady=10)
        self.display.pack(fill=tk.X)
    
    def create_buttons(self):
        main_frame = tk.Frame(self.root, bg="#121212")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        buttons_grid = tk.Frame(main_frame, bg="#121212")
        buttons_grid.pack(fill=tk.BOTH, expand=True)
        
        for i in range(4):
            buttons_grid.grid_columnconfigure(i, weight=1, uniform="col")
        for i in range(9):
            buttons_grid.grid_rowconfigure(i, weight=1, uniform="row")
        
        buttons = [
            {"text": "AC", "row": 0, "col": 0, "bg": "#FF5252", "fg": "#FFFFFF", "cmd": self.clear_all},
            {"text": "DEL", "row": 0, "col": 1, "bg": "#FF5252", "fg": "#FFFFFF", "cmd": self.delete},
            {"text": "(", "row": 0, "col": 2, "bg": "#424242", "cmd": lambda: self.add_to_input("(")},
            {"text": ")", "row": 0, "col": 3, "bg": "#424242", "cmd": lambda: self.add_to_input(")")},
            
            {"text": "sin", "row": 1, "col": 0, "bg": "#424242", "cmd": lambda: self.add_to_input("sin(")},
            {"text": "cos", "row": 1, "col": 1, "bg": "#424242", "cmd": lambda: self.add_to_input("cos(")},
            {"text": "tan", "row": 1, "col": 2, "bg": "#424242", "cmd": lambda: self.add_to_input("tan(")},
            {"text": "÷", "row": 1, "col": 3, "bg": "#FF9800", "cmd": lambda: self.add_to_input("/")},
            
            {"text": "π", "row": 2, "col": 0, "bg": "#424242", "cmd": lambda: self.add_to_input("π")},
            {"text": "e", "row": 2, "col": 1, "bg": "#424242", "cmd": lambda: self.add_to_input("e")},
            {"text": "log", "row": 2, "col": 2, "bg": "#424242", "cmd": lambda: self.add_to_input("log(")},
            {"text": "×", "row": 2, "col": 3, "bg": "#FF9800", "cmd": lambda: self.add_to_input("*")},
            
            {"text": "7", "row": 3, "col": 0, "bg": "#212121", "cmd": lambda: self.add_to_input("7")},
            {"text": "8", "row": 3, "col": 1, "bg": "#212121", "cmd": lambda: self.add_to_input("8")},
            {"text": "9", "row": 3, "col": 2, "bg": "#212121", "cmd": lambda: self.add_to_input("9")},
            {"text": "−", "row": 3, "col": 3, "bg": "#FF9800", "cmd": lambda: self.add_to_input("-")},
            
            {"text": "4", "row": 4, "col": 0, "bg": "#212121", "cmd": lambda: self.add_to_input("4")},
            {"text": "5", "row": 4, "col": 1, "bg": "#212121", "cmd": lambda: self.add_to_input("5")},
            {"text": "6", "row": 4, "col": 2, "bg": "#212121", "cmd": lambda: self.add_to_input("6")},
            {"text": "+", "row": 4, "col": 3, "bg": "#FF9800", "cmd": lambda: self.add_to_input("+")},
            
            {"text": "1", "row": 5, "col": 0, "bg": "#212121", "cmd": lambda: self.add_to_input("1")},
            {"text": "2", "row": 5, "col": 1, "bg": "#212121", "cmd": lambda: self.add_to_input("2")},
            {"text": "3", "row": 5, "col": 2, "bg": "#212121", "cmd": lambda: self.add_to_input("3")},
            {"text": "x^n", "row": 5, "col": 3, "bg": "#424242", "cmd": lambda: self.add_to_input("^")},
            
            {"text": "0", "row": 6, "col": 0, "bg": "#212121", "cmd": lambda: self.add_to_input("0")},
            {"text": "00", "row": 6, "col": 1, "bg": "#212121", "cmd": lambda: self.add_to_input("00")},
            {"text": ".", "row": 6, "col": 2, "bg": "#212121", "cmd": lambda: self.add_to_input(".")},
            {"text": "√", "row": 6, "col": 3, "bg": "#424242", "cmd": lambda: self.add_to_input("√(")},
            
            {"text": "%", "row": 7, "col": 0, "bg": "#424242", "cmd": lambda: self.add_to_input("%")},
            {"text": "ln", "row": 7, "col": 1, "bg": "#424242", "cmd": lambda: self.add_to_input("ln(")},
            {"text": "ANS", "row": 7, "col": 2, "bg": "#424242", "cmd": lambda: self.add_to_input(str(self.ans))},
            {"text": "=", "row": 7, "col": 3, "bg": "#8E2DE2", "cmd": self.calculate},
        ]
        
        for btn in buttons:
            self.create_cool_button(
                buttons_grid, 
                btn["text"], 
                btn["row"], 
                btn["col"], 
                bg=btn["bg"], 
                fg=btn.get("fg", "#FFFFFF"), 
                command=btn["cmd"]
            )
        
        self.create_cool_button(
            buttons_grid, 
            "B→D", 
            8, 0, 
            colspan=2, 
            bg="#6A11CB", 
            command=self.bin_to_dec
        )
        
        self.create_cool_button(
            buttons_grid, 
            "D→B", 
            8, 2, 
            colspan=2, 
            bg="#6A11CB", 
            command=self.dec_to_bin
        )
        
        self.create_cool_button(
            buttons_grid, 
            "Plot", 
            9, 0, 
            colspan=4, 
            bg="#6A11CB", 
            command=self.open_plot_window
        )
    
    def create_cool_button(self, parent, text, row, column, colspan=1, bg="#212121", fg="#FFFFFF", command=None):
        frame = tk.Frame(parent, bg="#121212")
        frame.grid(row=row, column=column, columnspan=colspan, sticky="nsew", padx=4, pady=4)
        
        button = tk.Button(
            frame, 
            text=text, 
            bg=bg, 
            fg=fg, 
            font=("Arial", 16, "bold"), 
            relief=tk.FLAT, 
            bd=0, 
            command=command,
            activebackground="#666666", 
            activeforeground="#FFFFFF"
        )
        button.pack(fill=tk.BOTH, expand=True)
        
        button.bind("<Enter>", lambda e, b=button, c=bg: self.on_hover(b, c))
        button.bind("<Leave>", lambda e, b=button, c=bg: self.on_leave(b, c))
        
        return button
    
    def on_hover(self, button, original_color):
        r, g, b = button.winfo_rgb(original_color)
        r = min(65535, r + 8000)
        g = min(65535, g + 8000)
        b = min(65535, b + 8000)
        hover_color = f"#{r//256:02x}{g//256:02x}{b//256:02x}"
        button.config(bg=hover_color)
    
    def on_leave(self, button, original_color):
        button.config(bg=original_color)
    
    def add_to_input(self, value):
        if value == "π":
            self.current_input += str(math.pi)
        elif value == "e":
            self.current_input += str(math.e)
        else:
            self.current_input += value
        
        self.display.config(text=self.current_input)
    
    def bin_to_dec(self):
        try:
            if self.current_input.strip():
                binary = ''.join(c for c in self.current_input if c in '01')
                decimal = int(binary, 2)
                self.current_input = str(decimal)
                self.display.config(text=self.current_input)
                self.ans = decimal
        except Exception as e:
            self.display.config(text="Error")
            self.current_input = ""
    
    def dec_to_bin(self):
        try:
            if self.current_input.strip():
                decimal = int(float(self.current_input))
                binary = bin(decimal)[2:]  
                self.current_input = binary
                self.display.config(text=self.current_input)
                self.ans = binary
        except Exception as e:
            self.display.config(text="Error")
            self.current_input = ""
    
    def clear_all(self):
        self.current_input = ""
        self.full_operation = ""
        self.display.config(text="0")
        self.operation_display.config(text="")
    
    def delete(self):
        self.current_input = self.current_input[:-1]
        if not self.current_input:
            self.display.config(text="0")
        else:
            self.display.config(text=self.current_input)
    
    def calculate(self):
        try:
            self.full_operation = self.current_input
            
            expression = self.current_input
            expression = expression.replace("π", str(math.pi))
            expression = expression.replace("e", str(math.e))
            expression = expression.replace("^", "")
            expression = expression.replace("√(", "math.sqrt(")
            expression = expression.replace("sin(", "math.sin(")
            expression = expression.replace("cos(", "math.cos(")
            expression = expression.replace("tan(", "math.tan(")
            expression = expression.replace("log(", "math.log10(")
            expression = expression.replace("ln(", "math.log(")
            expression = expression.replace("%", "/100")
            
            result = eval(expression)
            
            formatted_result = f"{result:.10g}"
            
            self.operation_display.config(text=self.full_operation)
            self.display.config(text=formatted_result)
            
            self.ans = result
            self.current_input = formatted_result
            
        except Exception as e:
            self.display.config(text="Error")
            self.current_input = ""
    
    def open_plot_window(self):
        PlotWindow(self.root)

class PlotWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Function Plotter")
        self.window.geometry("800x600")
        self.window.configure(bg="#121212")
        
        input_frame = tk.Frame(self.window, bg="#121212")
        input_frame.pack(pady=10)
        
        functions_frame = tk.Frame(self.window, bg="#121212")
        functions_frame.pack(pady=5)
        
        tk.Label(functions_frame, text="Function 1:", bg="#121212", fg="#FFFFFF").pack(side=tk.LEFT, padx=5)
        self.function1_input = tk.Entry(functions_frame, width=30, bg="#212121", fg="#FFFFFF", insertbackground="#FFFFFF")
        self.function1_input.pack(side=tk.LEFT, padx=5)
        
        tk.Label(functions_frame, text="Function 2:", bg="#121212", fg="#FFFFFF").pack(side=tk.LEFT, padx=5)
        self.function2_input = tk.Entry(functions_frame, width=30, bg="#212121", fg="#FFFFFF", insertbackground="#FFFFFF")
        self.function2_input.pack(side=tk.LEFT, padx=5)
        
        range_frame = tk.Frame(self.window, bg="#121212")
        range_frame.pack(pady=5)
        
        tk.Label(range_frame, text="X Range:", bg="#121212", fg="#FFFFFF").pack(side=tk.LEFT, padx=5)
        self.x_min = tk.Entry(range_frame, width=10, bg="#212121", fg="#FFFFFF", insertbackground="#FFFFFF")
        self.x_min.pack(side=tk.LEFT, padx=5)
        self.x_min.insert(0, "-10")
        
        tk.Label(range_frame, text="to", bg="#121212", fg="#FFFFFF").pack(side=tk.LEFT, padx=5)
        self.x_max = tk.Entry(range_frame, width=10, bg="#212121", fg="#FFFFFF", insertbackground="#FFFFFF")
        self.x_max.pack(side=tk.LEFT, padx=5)
        self.x_max.insert(0, "10")
        
        plot_button = tk.Button(self.window, text="Plot", bg="#6A11CB", fg="#FFFFFF", 
                              command=self.plot_function, font=("Arial", 12, "bold"))
        plot_button.pack(pady=10)
        
        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        self.fig.patch.set_facecolor('#121212')
        self.ax.set_facecolor('#121212')
        self.ax.tick_params(colors='white')
        self.ax.spines['bottom'].set_color('white')
        self.ax.spines['top'].set_color('white')
        self.ax.spines['left'].set_color('white')
        self.ax.spines['right'].set_color('white')
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.window)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def plot_function(self):
        try:
            self.ax.clear()
            self.ax.set_facecolor('#121212')
            self.ax.tick_params(colors='white')
            self.ax.spines['bottom'].set_color('white')
            self.ax.spines['top'].set_color('white')
            self.ax.spines['left'].set_color('white')
            self.ax.spines['right'].set_color('white')
            
            x_min = float(self.x_min.get())
            x_max = float(self.x_max.get())
            
            x = np.linspace(x_min, x_max, 1000)
            
            colors = ['#8E2DE2', '#FF5252', '#4CAF50', '#FFC107']
            
            if self.function1_input.get().strip():
                function1 = self.function1_input.get()
                function1 = self._process_function(function1)
                y1 = eval(function1)
                self.ax.plot(x, y1, color=colors[0], label='Function 1')
            
            if self.function2_input.get().strip():
                function2 = self.function2_input.get()
                function2 = self._process_function(function2)
                y2 = eval(function2)
                self.ax.plot(x, y2, color=colors[1], label='Function 2')
            
            self.ax.grid(True, color='#424242', linestyle='--', alpha=0.3)
            self.ax.set_xlabel('x', color='white')
            self.ax.set_ylabel('y', color='white')
            self.ax.set_title('Function Plot', color='white')
            
            if self.function1_input.get().strip() or self.function2_input.get().strip():
                self.ax.legend(facecolor='#121212', edgecolor='white', labelcolor='white')
            
            self.canvas.draw()
            
        except Exception as e:
            tk.messagebox.showerror("Error", f"Invalid function or range: {str(e)}")
    
    def _process_function(self, function):
        replacements = {
            "sin": "np.sin",
            "cos": "np.cos",
            "tan": "np.tan",
            "log": "np.log10",
            "ln": "np.log",
            "π": "np.pi",
            "e": "np.e",
            "^": "",
            "√": "np.sqrt"
        }
        for old, new in replacements.items():
            function = function.replace(old, new)
        return function

if __name__ == "__main__":
    root = tk.Tk()
    app = ScientificCalculator(root)
    root.mainloop()
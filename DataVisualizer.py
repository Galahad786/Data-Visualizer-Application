import tkinter as tk             # For app
from tkinter import filedialog   
from PIL import Image, ImageTk   # For handling images
import customtkinter as ctk      # For advanced modification in app
import pandas as pd              # For Data Framing
import matplotlib.pyplot as plt  # For graph plotting

# for app appearance
ctk.set_appearance_mode("light")  # Options: system, light, dark
ctk.set_default_color_theme("blue")  # Options: blue, green, dark-blue

# Function to handle file upload
def upload_file():
    global data
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv"), ("Excel Files", "*.xlsx")])
    
    if file_path:
        try:
            if file_path.endswith('.csv'):      # Checking postfix for CSV file
                data = pd.read_csv(file_path)   # Reading CSV
            elif file_path.endswith('.xlsx'):   # Checking postfix for Excel file
                data = pd.read_excel(file_path) # Reading Excel file
            
            # Defining columns
            column_names = list(data.columns)
            column_select_x.configure(values=column_names)
            column_select_y.configure(values=column_names)
            status_label.configure(text="File loaded successfully!", text_color="green")
        except Exception as e:                  # In case of error
            status_label.configure(text=f"Error loading file: {e}", text_color="red")
    else:
        status_label.configure(text="No file selected.", text_color="orange")

# Function to plot the graph
def plot_graph():
    x_column = column_select_x.get() 
    y_column = column_select_y.get()
    graph_type = graph_dropdown.get()
    
    if not data.empty and x_column and y_column:
        try:
            plt.figure(figsize=(8, 6))
            if graph_type == "Bar Graph":
                plt.bar(data[x_column], data[y_column], color="lightblue")
            elif graph_type == "Line Graph":
                plt.plot(data[x_column], data[y_column], marker="o", color="orange")
            elif graph_type == "Histogram":
                plt.hist(data[y_column], bins=10, color="green", alpha=0.7)
            elif graph_type == "Scatter Plot":
                plt.scatter(data[x_column], data[y_column], color="purple", alpha=0.6)
            elif graph_type == "Pie Chart":
                plt.pie(data[y_column], labels=data[x_column], autopct="%1.1f%%", startangle=90)
            
            plt.xlabel(x_column)
            plt.ylabel(y_column)
            plt.title(f"{graph_type} of {x_column} vs {y_column}")
            plt.grid(True)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            status_label.configure(text=f"Error generating graph: {e}", text_color="red")
    else:
        status_label.configure(text="Please select valid columns and graph type.", text_color="red")

# Initialize the application window
app = ctk.CTk()
app.title("AI-Powered Data Visualizer")
app.geometry("1920x1080")

canvas = tk.Canvas(app, width=1920, height=1080)
canvas.pack(fill="both", expand=True)

# Add a heading with centered alignment and a more appealing font style
heading_label = ctk.CTkLabel(
    app,
    text="AI-Powered Data Visualizer 🚀",
    font=("Helvetica", 36, "bold"),
    text_color="#000000"  
)
heading_label_window = canvas.create_window(400, 80, window=heading_label, anchor="center")

# Add a styled sub-heading
subheading_label = ctk.CTkLabel(
    app,
    text="Created by:\n Abdul Basit Arshad | B23F0364AI181\n Abdullah Asad | B23F0336AI158\n Ayesha Mazhar | B23F0041AI165",
    font=("Helvetica", 14),
    text_color="#000000"  # Cyan color
)
subheading_label_window = canvas.create_window(400, 160, window=subheading_label, anchor="center")

# Upload file button with styling
upload_button = ctk.CTkButton(
    app,
    text="Upload CSV/Excel File",
    command=upload_file,
    fg_color="#4CAF50",  # Green color
    hover_color="#45A049",  # Darker green on hover
    text_color="black",
    font=("Helvetica", 14, "bold")
)
upload_button_window = canvas.create_window(400, 250, window=upload_button, anchor="center")

# Dropdown for selecting X-axis
column_select_x_label = ctk.CTkLabel(
    app, text="Select X-axis Column:", font=("Helvetica", 16), text_color="black"
)
column_select_x_label_window = canvas.create_window(400, 310, window=column_select_x_label, anchor="center")

column_select_x = ctk.CTkComboBox(app, state="readonly", width=400)
column_select_x_window = canvas.create_window(400, 340, window=column_select_x, anchor="center")

# Dropdown for selecting Y-axis
column_select_y_label = ctk.CTkLabel(
    app, text="Select Y-axis Column:", font=("Helvetica", 16), text_color="black"
)
column_select_y_label_window = canvas.create_window(400, 390, window=column_select_y_label, anchor="center")

column_select_y = ctk.CTkComboBox(app, state="readonly", width=400)
column_select_y_window = canvas.create_window(400, 420, window=column_select_y, anchor="center")

# Dropdown for selecting graph type
graph_label = ctk.CTkLabel(
    app, text="Select Graph Type:", font=("Helvetica", 16), text_color="black"
)
graph_label_window = canvas.create_window(400, 470, window=graph_label, anchor="center")

graph_dropdown = ctk.CTkComboBox(
    app, state="readonly", width=400, values=["Bar Graph", "Line Graph", "Histogram", "Scatter Plot", "Pie Chart"]
)
graph_dropdown_window = canvas.create_window(400, 500, window=graph_dropdown, anchor="center")

# Plot graph button with styling
plot_button = ctk.CTkButton(
    app,
    text="Plot Graph",
    command=plot_graph,
    fg_color="#4CAF50",  # Green
    hover_color="#45A049",
    text_color="black",
    font=("Helvetica", 14, "bold")
)
plot_button_window = canvas.create_window(400, 570, window=plot_button, anchor="center")

# Status label for feedback
status_label = ctk.CTkLabel(
    app, text="", font=("Helvetica", 12, "bold", "italic"), text_color="red"
)
status_label_window = canvas.create_window(400, 620, window=status_label, anchor="center")

# Run the application
app.mainloop()

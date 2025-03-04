
import tkinter as tk  # Import the Tkinter module for GUI development

# Create the main window
window = tk.Tk()
window.title("Simple calculator")  # Set the title of the window
window.configure(bg="#F0FFF0")  # Set the background color of the window
window.geometry("700x800")  # Set the size of the window
window.resizable(True, False)  # Allow horizontal resizing but not vertical

# Create a frame to hold the widgets
frame = tk.Frame(master=window, width=500,height=800,borderwidth=5, bg="#B4CDCD", relief=tk.RAISED)
frame.pack(ipady=20,ipadx=10,pady=40, padx=30)  # Add some vertical padding

def button_clear():
    """Clears the display entry."""
    display.delete(0, tk.END)

# Create an entry widget for displaying input and output
display = tk.Entry(master=frame, borderwidth=10, relief=tk.SUNKEN, bg="#F0FFF0", font=("Arial", 12))
display.grid(row=0, column=0, columnspan=4)  # Position the entry widget

# Initialize variables
operator = ""
num1, num2, num3, num4 = "", "", "", ""
result1 = ""

def button_click(numb):
    """Handles number and operator button clicks."""
    global num4
    num1 = display.get()  # Get the current value in the display
    display.delete(0, tk.END)  # Clear the display
    display.insert(0, str(num1) + str(numb))  # Append the clicked number/operator
    num4 = display.get()  # Store the updated value
    
def equal():
    """Evaluates the mathematical expression entered by the user."""
    global result1, operator, num2, num3, num4
    
    try:
        # Find the operator in the input
        for char in str(num4):
            if char in "+-*/=":  # Check for a valid operator
                operator = char
                break

        # Split the input into two operands
        if operator:
            num2, num3 = num4.split(operator)
        
        # Perform the operation based on the detected operator
        if operator == '+':
            result1 = int(num2) + int(num3)
        elif operator == '-':
            result1 = int(num2) - int(num3)
        elif operator == '*':
            result1 = int(num2) * int(num3)
        elif operator == '/':
            result1 = round(int(num2) / int(num3), 5)
        else:
            result1 = num4  # If no valid operator, return the same input
        
        display.insert(len(num4), "=")  # Show the equal sign
        display.insert(20, result1)  # Display the result
    
    except ZeroDivisionError:
        display.delete(0, tk.END)
        display.insert(0, "Error: Division by zero")
    except ValueError:
        display.delete(0, tk.END)
        display.insert(0, "Error: Invalid input")
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, f"Error: {str(e)}")  # Display unexpected errors


# Create number buttons

button_0 = tk.Button(master=frame, text="0", bg="#BCD2EE", font=("Arial", 12), command=lambda: button_click(0))
button_1 = tk.Button(master=frame, text="1", font=("Arial", 12), command=lambda: button_click(1))
button_2 = tk.Button(master=frame, text="2", font=("Arial", 12), command=lambda: button_click(2))
button_3 = tk.Button(master=frame, text="3", font=("Arial", 12), command=lambda: button_click(3))
button_4 = tk.Button(master=frame, text="4", font=("Arial", 12), command=lambda: button_click(4))
button_5 = tk.Button(master=frame, text="5", font=("Arial", 12), command=lambda: button_click(5))
button_6 = tk.Button(master=frame, text="6", font=("Arial", 12), command=lambda: button_click(6))
button_7 = tk.Button(master=frame, text="7", font=("Arial", 12), command=lambda: button_click(7))
button_8 = tk.Button(master=frame, text="8", font=("Arial", 12), command=lambda: button_click(8))
button_9 = tk.Button(master=frame, text="9", font=("Arial", 12), command=lambda: button_click(9))


# Create operator and control buttons
button_clear = tk.Button(master=frame, text="clear", font=("Arial", 12), command=button_clear)
button_add = tk.Button(master=frame, text="+", font=("Arial", 16), command=lambda: button_click("+"))
button_subtract = tk.Button(master=frame, text="-", font=("Arial", 16), command=lambda: button_click("-"))
button_multi = tk.Button(master=frame, text="×", font=("Arial", 16), command=lambda: button_click("*"))
button_div = tk.Button(master=frame, text="/", font=("Arial", 16), command=lambda: button_click("/"))
button_equal = tk.Button(master=frame, text="=", font=("Arial", 12), command=equal)

# Arrange buttons in the grid

button_0.grid(row=4, column=0, ipadx=10)
button_1.grid(row=3, column=0, ipadx=10)
button_2.grid(row=3, column=1, ipadx=10)
button_3.grid(row=3, column=2, ipadx=10)
button_4.grid(row=2, column=0, ipadx=10)
button_5.grid(row=2, column=1, ipadx=10)
button_6.grid(row=2, column=2, ipadx=10)
button_7.grid(row=1, column=0, ipadx=10)
button_8.grid(row=1, column=1, ipadx=10)
button_9.grid(row=1, column=2, ipadx=10)

button_add.grid(row=3, column=3, ipadx=8)
button_subtract.grid(row=2, column=3, ipadx=10)
button_multi.grid(row=1, column=3, ipadx=7)
button_div.grid(row=4, column=2, ipadx=10)
button_clear.grid(row=4, column=1, ipadx=1)
button_equal.grid(row=4, column=3, ipadx=10)

window.mainloop()

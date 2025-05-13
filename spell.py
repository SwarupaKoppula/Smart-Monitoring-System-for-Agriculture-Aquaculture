import tkinter
from tkinter import *
from textblob import TextBlob

# Initialize window
root = Tk()
root.title("Spelling Checker")
root.geometry("700x400")
root.config(background="#dae6f6")

# Function to check spelling
def check_spelling():
    word = enter_text.get()
    a = TextBlob(word)
    right = str(a.correct())

    # Display the corrected text
    cs = Label(root, text="Correct text is:", font=("poppins", 20), bg="#dae6f6", fg="#364971")
    cs.place(x=100, y=250)

    spell.config(text=right)

# Heading
heading = Label(root, text="Spelling Checker", font=("Trebuchet MS", 30, "bold"), bg="#dae6f6", fg="#364971")
heading.pack(pady=(50, 0))

# Text input field
enter_text = Entry(root, justify="center", width=30, font=("poppins", 25), bg="white", border=2)
enter_text.pack(pady=10)
enter_text.focus()

# Check button (with command added)
button = Button(root, text="Check", font=("arial", 20, "bold"), fg="white", bg="red", command=check_spelling)
button.pack()

# Label to display corrected spelling
spell = Label(root, font=("poppins", 20), bg="#dae6f6", fg="#364971")
spell.place(x=350, y=250)

# Run the Tkinter event loop
root.mainloop()

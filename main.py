from tkinter import *
from tkinter import messagebox

# List of possible key signatures
key_signatures = [
    "C", "C#", "Db", "D", "D#", "Eb", "E", "F", "F#", "Gb", "G", 
    "G#", "Ab", "A", "A#", "Bb", "B"
]

# Dictionary mapping key signatures to their corresponding keys
key_signature_map = {
    "C Major / A minor": ["C", "D", "E", "F", "G", "A", "B"],
    "G Major / E minor": ["G", "A", "B", "C", "D", "E", "F#"],
    "D Major / B minor": ["D", "E", "F#", "G", "A", "B", "C#"],
    "A Major / F# minor": ["A", "B", "C#", "D", "E", "F#", "G#"],
    "E Major / C# minor": ["E", "F#", "G#", "A", "B", "C#", "D#"],
    "B Major / G# minor": ["B", "C#", "D#", "E", "F#", "G#", "A#"],
    "F# Major / D# minor": ["F#", "G#", "A#", "B", "C#", "D#", "E#"],
    "C# Major / A# minor": ["C#", "D#", "E#", "F#", "G#", "A#", "B#"],
    "F Major / D minor": ["F", "G", "A", "Bb", "C", "D", "E"],
    "Bb Major / G minor": ["Bb", "C", "D", "Eb", "F", "G", "A"],
    "Eb Major / C minor": ["Eb", "F", "G", "Ab", "Bb", "C", "D"],
    "Ab Major / F minor": ["Ab", "Bb", "C", "Db", "Eb", "F", "G"],
    "Db Major / Bb minor": ["Db", "Eb", "F", "Gb", "Ab", "Bb", "C"],
    "Gb Major / Eb minor": ["Gb", "Ab", "Bb", "Cb", "Db", "Eb", "F"],
    "Cb Major / Ab minor": ["Cb", "Db", "Eb", "Fb", "Gb", "Ab", "Bb"]
}

# functions
def error_message():
    messagebox.showerror("Invalid entries", "Please try again.")
    lblResult.config(text="Error")

def get_key_signature():
    firstEntry = e1.get()
    secondEntry = e2.get()
    thirdEntry = e3.get()
    fourthEntry = e4.get()

    # check for empty or non-letter entries
    if firstEntry not in key_signatures:
        error_message()
    elif secondEntry not in key_signatures:
        error_message()
    elif thirdEntry not in key_signatures:
        error_message()
    elif fourthEntry not in key_signatures:
        error_message()
    else:
        finalResult = firstEntry + " " + secondEntry + " " + thirdEntry + " " + fourthEntry
        lblResult.config(text="Result: " + finalResult)

def remove_entries():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

# window properties
window = Tk()
window.title('Key Signature Finder')
icon = PhotoImage(file="icon.png")
window.iconphoto(True, icon)
window.resizable(False, False)

# configure monitor resolution
app_width = 375
app_height = 175
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width/2)-(app_width/2)
y = (screen_height/2)-(app_height/2)

# configure window size
window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
window.tk.call('tk', 'scaling', 2.0)

# header section
lblHeader = Label(window, text="Enter a musical key (for example C-sharp or E-flat):", font=('Arial', 8))
lblHeader.grid(column=0, row=0, pady=5)

# entries
e_frame = Frame(window)
e_frame.grid(column=0, row=1, pady=5)
e1 = Entry(e_frame, width=5)
e1.pack(side=LEFT, padx=3)
e2 = Entry(e_frame, width=5)
e2.pack(side=LEFT, padx=3)
e3 = Entry(e_frame, width=5)
e3.pack(side=LEFT, padx=3)
e4 = Entry(e_frame, width=5)
e4.pack(side=LEFT, padx=3)

# buttons
btn_frame = Frame(window)
btn_frame.grid(column=0, row=2, pady=5)
btnOk = Button(btn_frame, text="Ok", bg="light gray", width=10, command=get_key_signature)
btnOk.pack(side=LEFT, padx=3) 
btnReset = Button(btn_frame, text="Reset", bg="light gray", width=10, command=remove_entries)
btnReset.pack(side=LEFT, padx=3) 

# results
lblResult = Label(window, text="Results: ",font=('Arial', 8))
lblResult.grid(column=0, row=3, pady=5)

window.mainloop()
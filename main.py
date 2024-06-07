from tkinter import *
from tkinter import messagebox

# List of possible key signatures
key_notes = [
    "Cb", "C", "C#", "Db", "D", "D#", "Eb", "E", "E#", "Fb", "F", "F#", "Gb", "G", 
    "G#", "Ab", "A", "A#", "Bb", "B", "B#"
]

# Dictionary mapping key signatures to their corresponding keys
key_signature_map = {
    "Cb major | Ab minor": ["Cb", "Db", "Eb", "Fb", "Gb", "Ab", "Bb"],
    "Gb major | Eb minor": ["Gb", "Ab", "Bb", "Cb", "Db", "Eb", "F"],
    "Db major | Bb minor": ["Db", "Eb", "F", "Gb", "Ab", "Bb", "C"],
    "Ab major | F minor": ["Ab", "Bb", "C", "Db", "Eb", "F", "G"],
    "Eb major | C minor": ["Eb", "F", "G", "Ab", "Bb", "C", "D"],
    "Bb major | G minor": ["Bb", "C", "D", "Eb", "F", "G", "A"],
    "F major | D minor": ["F", "G", "A", "Bb", "C", "D", "E"],
    "C major | A minor": ["C", "D", "E", "F", "G", "A", "B"],
    "G major | E minor": ["G", "A", "B", "C", "D", "E", "F#"],
    "D major | B minor": ["D", "E", "F#", "G", "A", "B", "C#"],
    "A major | F# minor": ["A", "B", "C#", "D", "E", "F#", "G#"],
    "E major | C# minor": ["E", "F#", "G#", "A", "B", "C#", "D#"],
    "B major | G# minor": ["B", "C#", "D#", "E", "F#", "G#", "A#"],
    "F# major | D# minor": ["F#", "G#", "A#", "B", "C#", "D#", "E#"],
    "C# major | A# minor": ["C#", "D#", "E#", "F#", "G#", "A#", "B#"],
}

# functions
def error_message():
    messagebox.showerror("Invalid entries", "Please try again. \nUse capital letters, \nno spaces or numbers, \nand #/b for sharps and flats.")
    lblResult.config(text="Error")

def get_key_signature(event=None):
    firstEntry = e1.get()
    secondEntry = e2.get()
    thirdEntry = e3.get()
    fourthEntry = e4.get()

    entered_notes = [firstEntry, secondEntry, thirdEntry, fourthEntry]

    # Check if all entered keys are valid subsets of key signatures
    matching_signatures = []
    for signature, key_notes in key_signature_map.items():
        # Check if entered notes are a subset of the current key signature's notes
        if set(entered_notes).issubset(set(key_notes)):
            matching_signatures.append(signature)

    if matching_signatures:
        final_result = "\n".join(matching_signatures)
        lblResult.config(text="Matching Key Signatures:\n" + final_result)
    else:
        error_message()

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

# configure window size and position
app_width = 400
app_height = 250
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width/2)-(app_width/2)
y = (screen_height/2)-(app_height/2)
window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
window.tk.call('tk', 'scaling', 2.0)

# header section
lblHeader = Label(window, text="Enter a musical key (for example C#/Db/E):", font=('Helvetica', 10))
lblHeader.grid(column=0, row=0, sticky="nsew")

# entries
e_frame = Frame(window)
e_frame.grid(column=0, row=1, pady=5, ipadx=1, ipady=1)
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
btnOk = Button(btn_frame, text="Ok", font=('Helvetica', 10), bg="light gray", width=10, command=get_key_signature)
btnOk.pack(side=LEFT, padx=3) 
btnReset = Button(btn_frame, text="Reset", font=('Helvetica', 10), bg="light gray", width=10, command=remove_entries)
btnReset.pack(side=LEFT, padx=3) 

# results
lblResult = Label(window, text="Results: ", font=('Helvetica', 10))
lblResult.grid(column=0, row=3, pady=5)
window.bind("<Return>", get_key_signature)

# Center widgets in the window
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)
window.grid_columnconfigure(0, weight=1)

window.mainloop()
from tkinter import*
import tkinter.messagebox as messagebox 

def check_password_strength():
    """Check the strength of the password based onits length . """
    password= entrypassword.get()
    length=len(password)
    if length < 8:
        strength="weak"
    elif length>=8 and length <=12:
        else:
    strength="strong"
    messagebox.showinfo("Password Strength, f"Your password strength is: {strength})
    window=Tk()
    window.title("Password Strength Checker ")
    label_password=Label(window text = "Entry Password :")
    label_password.pack()
    entry_password= Entry(window,ahow="*")
    entry_password.pack()
    button_check =Button (window text = "Check strength ", command=check_password_strength)
    button_check.pack()

    window.mainloop()
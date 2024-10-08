import tkinter as tk

# Function to encrypt text using Caesar Cipher
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

# Function to decrypt text using Caesar Cipher
def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char
    return decrypted_text

# Function to handle the conversion based on the user's choice
def convert():
    message = input_box.get("1.0", "end-1c")  # Get the text from the input box
    shift = int(shift_box.get())  # Get the shift value
    if operation.get() == 'Encrypt':
        result = encrypt(message, shift)
    else:
        result = decrypt(message, shift)
    output_box.delete(1.0, tk.END)  # Clear the output box
    output_box.insert(tk.END, result)  # Insert the result in the output box

# Creating the main application window
root = tk.Tk()
root.title("Caesar Cipher")

# Label and text box for input message
tk.Label(root, text="Enter the message:").pack(pady=5)
input_box = tk.Text(root, height=5, width=40)
input_box.pack(pady=5)

# Label and entry for shift value
tk.Label(root, text="Enter the shift value (0-25):").pack(pady=5)
shift_box = tk.Entry(root)
shift_box.pack(pady=5)

# Radio buttons to select Encrypt or Decrypt
operation = tk.StringVar(value="Encrypt")
tk.Radiobutton(root, text="Encrypt", variable=operation, value="Encrypt").pack(pady=5)
tk.Radiobutton(root, text="Decrypt", variable=operation, value="Decrypt").pack(pady=5)

# Button to perform the conversion
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack(pady=10)

# Label and text box for the output message
tk.Label(root, text="Result:").pack(pady=5)
output_box = tk.Text(root, height=5, width=40)
output_box.pack(pady=5)

# Run the application
root.mainloop()

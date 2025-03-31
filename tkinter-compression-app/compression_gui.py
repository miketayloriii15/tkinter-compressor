import tkinter as tk
from compressmodule import compress, decompress
from tkinter import filedialog

# Open a file dialog and return the selected file path
def open_file():
    filename = filedialog.askopenfilename(
        initialdir='/', 
        title="Select a file"
    )
    return filename

# Call the compression function with input and fixed output file
def compression(input_path, output_path):
    """Compresses the selected input file and writes to output file."""
    if input_path:
        compress(input_path, output_path)

# Call the decompression function with input and fixed output file
def decompression(input_path, output_path):
    """Decompresses the selected input file and writes to output file."""
    if input_path:
        decompress(input_path, output_path)

# Main application window
window = tk.Tk()
window.title("Compression Engine")
window.geometry("600x400")

# Compression button
compress_button = tk.Button(
    window,
    text="Compress File",
    command=lambda: compression(open_file(), "compressed_output.txt")
)
compress_button.grid(row=2, column=1, pady=10)

# Decompression button
decompress_button = tk.Button(
    window,
    text="Decompress File",
    command=lambda: decompression(open_file(), "decompressed_output.txt")
)
decompress_button.grid(row=3, column=1, pady=10)

# Run the application
window.mainloop()

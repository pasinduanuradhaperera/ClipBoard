import tkinter as tk
import pyperclip
import threading
import time


class ClipboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clipboard Manager")
        self.root.geometry("400x400")
        self.root.resizable(False,False)

        self.history = []
        self.last_clipboard_content = ""
        self.max_history = 20  # Default limit

        # Label
        self.label = tk.Label(root, text="Enter Text to Copy:", font=("Arial", 12))
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Text Entry (Left side)
        self.entry = tk.Entry(root, font=("Arial", 12), width=30)
        self.entry.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry.bind("<Return>", self.handle_enter)

        # Copy to Clipboard button (Right side)
        self.copy_button = tk.Button(
            root, text="Copy to Clipboard", command=self.copy_to_clipboard, font=("Arial", 12)
        )
        self.copy_button.grid(row=1, column=1, padx=10, pady=5, sticky="e")

        # Limit Adjustment (Max History Size)
        self.limit_label = tk.Label(root, text="Max History Size:", font=("Arial", 12))
        self.limit_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.limit_spinbox = tk.Spinbox(
            root, from_=1, to=1000, font=("Arial", 12), width=5, command=self.update_limit
        )
        self.limit_spinbox.grid(row=2, column=1, padx=10, pady=5, sticky="e")
        self.limit_spinbox.delete(0, tk.END)
        self.limit_spinbox.insert(0, str(self.max_history))  # Set default value

        # Clear History button (Bottom left corner)
        self.clear_button = tk.Button(
            root, text="Clear History", command=self.clear_history, font=("Arial", 12)
        )
        self.clear_button.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        # Frame to hold the scrollable canvas
        self.history_frame = tk.Frame(root)
        self.history_frame.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Create canvas
        self.canvas = tk.Canvas(self.history_frame)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        # Create a frame inside the canvas to hold the history tiles
        self.history_canvas_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.history_canvas_frame, anchor="nw")

        # Update scroll region
        self.history_canvas_frame.bind(
            "<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        # Add mouse wheel scrolling to canvas
        self.canvas.bind_all("<MouseWheel>", self.on_mouse_wheel)

        # No History label
        self.no_history_label = tk.Label(
            root, text="No History Available", font=("Arial", 12), fg="gray"
        )
        self.no_history_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        self.no_history_label.grid_forget()  # Hide it initially

        # Start clipboard monitoring in a separate thread
        self.monitor_thread = threading.Thread(target=self.monitor_clipboard, daemon=True)
        self.monitor_thread.start()

    def copy_to_clipboard(self):
        """Copy text to clipboard and save it in history."""
        text = self.entry.get().strip()
        if text:
            pyperclip.copy(text)
            self.add_to_history(text)
            self.entry.delete(0, tk.END)

    def handle_enter(self, event):
        """Handle the Enter key to copy text."""
        self.copy_to_clipboard()

    def clear_history(self):
        """Clear clipboard history."""
        self.history = []
        self.update_history()

    def update_history(self):
        """Update the frame with the latest clipboard history tiles."""
        # Clear the existing history tiles
        for widget in self.history_canvas_frame.winfo_children():
            widget.destroy()

        # If history is empty, show the "No History Available" label
        if not self.history:
            self.no_history_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        else:
            self.no_history_label.grid_forget()  # Hide the label if history is available

            # Add new history tiles
            for index, item in enumerate(self.history, start=1):
                # Display only the first 20 characters
                display_text = f"{index}. {item[:20]}"  # Include the item number and first 20 characters
                tile = tk.Button(
                    self.history_canvas_frame, text=display_text, font=("Arial", 12), width=40, height=2, command=lambda text=item: self.copy_to_clipboard_from_tile(text)
                )
                tile.grid(row=index, column=0, padx=10, pady=5, sticky="w")

    def add_to_history(self, text):
        """Add new text to history if it is not a duplicate."""
        if text and (not self.history or self.history[0] != text):
            self.history.insert(0, text)
            if len(self.history) > self.max_history:
                self.history.pop()
            self.update_history()

    def copy_to_clipboard_from_tile(self, text):
        """Remove clicked tile from history and copy text to the clipboard."""
        # Remove the clicked tile from history
        self.history.remove(text)
        # Update the UI
        self.update_history()
        # Copy text to clipboard
        pyperclip.copy(text)

    def update_limit(self):
        """Update the maximum history limit from the spinbox."""
        try:
            self.max_history = int(self.limit_spinbox.get())
        except ValueError:
            self.max_history = 20  # Reset to default if invalid input

    def monitor_clipboard(self):
        """Monitor the clipboard for new content."""
        while True:
            try:
                content = pyperclip.paste().strip()
                if content and content != self.last_clipboard_content:
                    self.last_clipboard_content = content
                    self.add_to_history(content)
            except Exception as e:
                print(f"Error accessing clipboard: {e}")
            time.sleep(0.5)  # Check every 500ms

    def on_mouse_wheel(self, event):
        """Handle mouse wheel scrolling."""
        # Scroll the canvas vertically based on mouse wheel movement
        if event.delta > 0:
            self.canvas.yview_scroll(-1, "units")  # Scroll up
        else:
            self.canvas.yview_scroll(1, "units")  # Scroll down


if __name__ == "__main__":
    root = tk.Tk()
    app = ClipboardApp(root)
    root.mainloop()

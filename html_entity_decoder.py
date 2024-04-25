import tkinter as tk
import html
import pyperclip

class HTMLEntityDecoderApp:
    def __init__(self, root):
        self.root = root
        self.root.title('HTML Entity Decoder')

        tk.Label(self.root, text='Enter Encoded URL:').pack(pady=5)
        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack(pady=5)

        tk.Button(self.root, text='Decode', command=self.decode_url).pack(pady=5)
        self.result = tk.Text(self.root, height=4, width=50)
        self.result.pack(pady=5)

        tk.Button(self.root, text='Copy to Clipboard', command=self.copy_to_clipboard).pack(pady=5)
        tk.Button(self.root, text='Clear', command=self.clear_fields).pack(pady=5)

        self.status_label = tk.Label(self.root, text='', fg='red')
        self.status_label.pack(pady=5)

    def decode_url(self):
        encoded_url = self.entry.get()
        if encoded_url:
            decoded_url = html.unescape(encoded_url)
            self.result.delete(1.0, tk.END)
            self.result.insert(tk.END, decoded_url)
            self.status_label.config(text='URL decoded successfully', fg='green')
        else:
            self.status_label.config(text='Please enter an encoded URL', fg='red')

    def copy_to_clipboard(self):
        decoded_url = self.result.get(1.0, tk.END).strip()
        if decoded_url:
            pyperclip.copy(decoded_url)
            self.status_label.config(text='URL copied to clipboard', fg='green')
        else:
            self.status_label.config(text='No URL to copy', fg='red')

    def clear_fields(self):
        self.entry.delete(0, tk.END)
        self.result.delete(1.0, tk.END)
        self.status_label.config(text='')

if __name__ == "__main__":
    root = tk.Tk()
    app = HTMLEntityDecoderApp(root)
    root.mainloop()
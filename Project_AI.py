import tkinter as tk
import random

root = tk.Tk()
root.title("Chatbot")
responses = {
    "hi": ["hello", "hey there"],
    "how are you": ["I'm fine", "feeling good"],
    "apakah kamu seseorang yang pintar": ["ooohhh tentu saja"],
    "apakah kamu seseorang yang baik hati": ["ya, aku sangat baik hati"], 
    "bagaimana cuaca hari ini": ["tanya aja sama BMKG"],
    "dimana kamu berada sekarang": ["di dekatmu "],
    "siapa namamu": ["namaku adalah luckybot, aku adalah seorang robot yg jenius"],
    "berapa umur kamu": ["10 tahun"],
    "apakah kamu tau aku": ["hmmmm, tidak tauu"],
    "apakah kamu mau jadi teman aku": ["yeaaayyy, tentu saja"],
    
}
def respond(input):
    if input in responses:
        return random.choice(responses[input])
    else:
        return random.choice(responses["default"]) 
    
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

input_field = tk.Entry(input_frame, font=("Arial", 18))
input_field.pack(fill=tk.X, padx=10)

display_frame = tk.Frame(root)
display_frame.pack()

display_field = tk.Text(display_frame, height=10, font=("Arial", 18))
display_field.pack(fill=tk.X, padx=10)

def enter_pressed(event):
    input_get = input_field.get()
    display_field.insert(tk.END, "You: " + input_get + "\n\n")
    display_field.insert(tk.END, "Bot: " + respond(input_get.lower()) + "\n\n")
    input_field.delete(0, tk.END)

root.bind("<Return>", enter_pressed)
root.mainloop()



import tkinter as tk
from PIL import Image, ImageTk
import random

# Set up a dictionary with image paths, their labels, and explanations
# Updated dictionary with new image paths and explanations
images = {
    "D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\good and bad images\\good_touch1.jpg": {"label": "good", "explanation": "This is a friendly touch, like a pat on the back."},
    "D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\good and bad images\\good_touch2.jpg": {"label": "good", "explanation": "This is a safe touch, like a high-five with a friend."},
    "D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\good and bad images\\bad_touch1.jpg": {"label": "bad", "explanation": "This is an inappropriate touch and is not safe."},
    "D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\good and bad images\\bad_touch2.jpg": {"label": "bad", "explanation": "This is a touch that makes you uncomfortable, so it's considered bad."},
    
    # Additional images
    "D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\good and bad images\\bad_touch3.jpg": {"label": "bad", "explanation": "This shows an uncomfortable or unwanted touch. It's important to speak up in such situations."},
    "D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\good and bad images\\bad_touch4.jpg": {"label": "bad", "explanation": "An inappropriate or unsafe touch. Always tell a trusted adult if this happens."},
    "D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\good and bad images\\good_touch3.jpg": {"label": "good", "explanation": "A friendly handshake, which is generally considered a good and safe touch."},
    "D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\good and bad images\\good_touch4.jpg": {"label": "good", "explanation": "A safe hug between friends or family members, showing care and affection."}
}


# Function to load a new image and display it
def load_new_image():
    global current_image, current_label, current_explanation
    current_image, details = random.choice(list(images.items()))
    current_label = details["label"]
    current_explanation = details["explanation"]
    
    # Load and display the image
    img = Image.open(current_image)
    img = img.resize((300, 300))  # Resize image as needed
    img_tk = ImageTk.PhotoImage(img)
    image_label.config(image=img_tk)
    image_label.image = img_tk

# Function to check the answer and display a custom explanation window
def check_answer(answer):
    if (answer == "Bad" and current_label == "bad") or (answer == "Good" and current_label == "good"):
        result_text = "Correct! 😊"
        result_color = "#66FF66"
        icon_text = "👍"
    else:
        result_text = "Incorrect! 😔"
        result_color = "#FF6666"
        icon_text = "👎"
    
    show_explanation_window(result_text, result_color, icon_text, current_explanation)
    load_new_image()  # Load a new image after showing the explanation

# Function to create and display a custom explanation window
def show_explanation_window(result_text, result_color, icon_text, explanation_text):
    explanation_window = tk.Toplevel(root)
    explanation_window.title("Explanation")
    explanation_window.geometry("400x350")
    explanation_window.configure(bg="#FFF0E6")  # Soft peach background

    icon_label = tk.Label(
        explanation_window,
        text=icon_text,
        font=("Comic Sans MS", 48),
        bg="#FFF0E6"
    )
    icon_label.pack(pady=10)

    result_label = tk.Label(
        explanation_window,
        text=result_text,
        font=("Comic Sans MS", 24, "bold"),
        bg="#FFF0E6",
        fg=result_color
    )
    result_label.pack(pady=10)

    explanation_label = tk.Label(
        explanation_window,
        text=explanation_text,
        font=("Comic Sans MS", 14),
        bg="#FFF0E6",
        fg="#333333",
        wraplength=350,
        justify="center"
    )
    explanation_label.pack(pady=10)

    close_button = tk.Button(
        explanation_window,
        text="Got it!",
        font=("Comic Sans MS", 14, "bold"),
        bg="#FFB74D",
        fg="black",
        width=10,
        height=1,
        relief="ridge",
        bd=4,
        command=explanation_window.destroy,
        activebackground="#FF8A65",
        cursor="hand2"
    )
    close_button.pack(pady=20)

    explanation_window.transient(root)
    explanation_window.grab_set()
    root.wait_window(explanation_window)

# Initialize the main application window
root = tk.Tk()
root.title("Touch Identification Game")
root.geometry("500x600")
root.configure(bg="#FFEBB7")  # Light yellow for main background

# Title Label
title_label = tk.Label(
    root,
    text="Is this touch good or bad?",
    font=("Comic Sans MS", 22, "bold"),
    bg="#FFEBB7",
    fg="#0066CC"  # Soft blue text color
)
title_label.pack(pady=20)

# Display an image
image_label = tk.Label(root, bg="#FFEBB7")
image_label.pack(pady=20)

# Load the first image
current_image = None
current_label = None
current_explanation = None
load_new_image()

# Frame for buttons
button_frame = tk.Frame(root, bg="#FFEBB7")
button_frame.pack(pady=30)

# Style for the "Bad" button
bad_button = tk.Button(
    button_frame,
    text="❌ Bad Touch",
    command=lambda: check_answer("Bad"),
    font=("Comic Sans MS", 16, "bold"),
    bg="#FF6666",
    fg="white",
    width=12,
    height=2,
    relief="ridge",
    bd=5,
    cursor="hand2",
    activebackground="#FF7F7F"
)
bad_button.grid(row=0, column=0, padx=20)

# Style for the "Good" button
good_button = tk.Button(
    button_frame,
    text="✔️ Good Touch",
    command=lambda: check_answer("Good"),
    font=("Comic Sans MS", 16, "bold"),
    bg="#4CAF50",
    fg="white",
    width=12,
    height=2,
    relief="ridge",
    bd=5,
    cursor="hand2",
    activebackground="#66FF66"
)
good_button.grid(row=0, column=1, padx=20)

# Run the main loop
root.mainloop()

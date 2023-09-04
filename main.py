import tkinter as tk
from tkinter import ttk


# Create the main window
root = tk.Tk()
root.title("Pickleball Rules")

# Rules dictionary
rules = {
    "The Serve": "The server’s arm must be moving in an upward arc when the ball is struck.\n\n"
            "Paddle contact with the ball must not be made above the waist level."
            "The head of the paddle must not be above the highest part of the wrist at contact.\n\n"
            "A ‘drop serve’ is also permitted in which case none of the elements above apply.\n\n"
            "At the time the ball is struck, the server’s feet may not touch the court or outside the imaginary extension of the sideline or centerline and at least one foot must be behind the baseline on the playing surface or the ground behind the baseline.\n\n"
            "The serve is made diagonally crosscourt and must land within the confines of the opposite diagonal court.\n\n"
            "Only one serve attempt is allowed per server.",
    "Serve Sequence": "Both players on the serving doubles team have the opportunity to serve and score points until they commit a fault *(except for the first service sequence of each new game).\n\n"
            "The first serve of each side-out is made from the right/even court."
            "The head of the paddle must not be above the highest part of the wrist at contact.\n\n"
            "If a point is scored, the server switches sides and the server initiates the next serve from the left/odd court.\n\n"
            "As subsequent points are scored, the server continues switching back and forth until a fault is committed, and the first server loses the serve.\n\n"
            "When the first server loses the serve the partner then serves from their correct side of the court (except for the first service sequence of the game*).\n\n"
            "The second server continues serving until his team commits a fault and loses the serve to the opposing team.\n\n"
            "Once the service goes to the opposition (at side out), the first serve is from the right/even court and both players on that team have the opportunity to serve and score points until their team commits two faults.\n\n"
            "In singles the server serves from the right/even court when his or her score is even and from the left/odd when the score is odd.",
    "Scoring": "Points are scored only by the serving team.\n\n"
            "Games are normally played to 11 points, win by 2.\n\n"
            "Tournament games may be to 15 or 21, win by 2.\n\n"
            "When the serving team’s score is even (0, 2, 4, 6, 8, 10) the player who was the first server in the game for that team will be in the right/even court when serving or receiving; when odd (1, 3, 5, 7, 9) that player will be in the left/odd court when serving or receiving.",
    "Two-Bounce Rule": "When the ball is served, the receiving team must let it bounce before returning, and then the serving team must let it bounce before returning, thus two bounces.\n\n"
            "After the ball has bounced once in each team’s court, both teams may either volley the ball (hit the ball before it bounces) or play it off a bounce (ground stroke).\n\n"
            "The two-bounce rule eliminates the serve and volley advantage and extends rallies.",
    "Line Calls": "A ball contacting any part of any line, except the non-volley zone line on a serve, is considered “in.”\n\n"
            "A serve contacting the non-volley zone line is short and a fault.\n\n",
            "Non-Volley Zone": "The non-volley zone is the court area within 7 feet on both sides of the net.\n\n"
            "Volleying is prohibited within the non-volley zone. This rule prevents players from executing smashes from a position within the zone.\n\n"
            "It is a fault if, when volleying a ball, the player steps on the non-volley zone, including the line and/or when the player’s momentum causes them or anything they are wearing or carrying to touch the non-volley zone including the associated lines.\n\n"
            "It is a fault if, after volleying, a player is carried by momentum into or touches the non-volley zone, even if the volleyed ball is declared dead before this happens.\n\n"
            "A player may legally be in the non-volley zone any time other than when volleying a ball.\n\n"
            "The non-volley zone is commonly referred to as 'the kitchen.'",
    "Faults": "A fault is any action that stops play because of a rule violation.\n\n"
            "A fault by the receiving team results in a point for the serving team.\n\n"
            "A fault by the serving team results in the server’s loss of serve or side out.", 
    "Determining Serving Team": "Any fair method can be used to determine which player or team has first choice of side, service, or receive. (Example: coin flip)"

}


def display_rule(rule_name):
    rule_text.delete("1.0", tk.END)  # Clear the current content
    if rule_name != "Select a rule":
        rule_text.insert(tk.END, rules.get(rule_name, "Rule not found."))
        rule_text.yview_moveto(1.0)  # Scroll to the end

def quit_app():
    root.quit()

def toggle_dark_mode():
    dark_mode = dark_mode_var.get()
    if dark_mode:
        # Dark mode colors
        root.configure(bg="#1e1e1e")
        rule_text.configure(bg="#333333", fg="white", insertbackground="white")
        rule_menu.configure(background="#1e1e1e", foreground="white")
        quit_button.configure(background="#1e1e1e", foreground="white")
        font_size_label.configure(background="#1e1e1e", foreground="white")
        dark_mode_checkbox.configure(bg="#1e1e1e", fg="white", selectcolor="#1e1e1e")
        style.configure('DarkHorizontal.TScale', sliderbackground='white')  # Set sliderbackground to white for the thumb
        style.configure('Dark.Horizontal.TScrollbar', troughcolor="#1e1e1e", sliderbackground="white")  # Customize scrollbar style
    else:
        # Light mode colors
        root.configure(bg="white")
        rule_text.configure(bg="white", fg="black", insertbackground="black")
        rule_menu.configure(background="white", foreground="black")
        quit_button.configure(background="white", foreground="black")
        font_size_label.configure(background="white", foreground="black")
        dark_mode_checkbox.configure(bg="white", fg="black", selectcolor="white")
        style.configure('DarkHorizontal.TScale', sliderbackground='black')  # Set sliderbackground to black for the thumb
        style.configure('Dark.Horizontal.TScrollbar', troughcolor="lightgray", sliderbackground="black")  # Customize scrollbar style

# Create a custom style for the scrollbar in dark mode
style = ttk.Style()
style.configure('Dark.Horizontal.TScrollbar', troughcolor="#1e1e1e", sliderbackground="white")  # Customize scrollbar style



# Create a dark mode toggle checkbox
dark_mode_var = tk.BooleanVar()
dark_mode_var.set(False)  # Light mode by default
dark_mode_checkbox = tk.Checkbutton(root, text="Dark Mode", variable=dark_mode_var, command=toggle_dark_mode)
dark_mode_checkbox.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="w")

# Create a Text widget for displaying the rules
rule_text = tk.Text(root, wrap=tk.WORD, width=50, height=20)
rule_text.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")

# Create a scrollbar
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=rule_text.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
rule_text.config(yscrollcommand=scrollbar.set)

# Create the font size selector variable
selected_font_size = tk.IntVar()
selected_font_size.set(12)  # Set the default font size

# Function to update the font size
def update_font_size(value):
    new_font_size = selected_font_size.get()
    rule_text.config(font=("Arial", new_font_size))

# Create a Label for the font size
font_size_label = ttk.Label(root, text="Font Size:")
font_size_label.grid(row=2, column=0, padx=10, pady=(0, 5), sticky="w")

# Create a Scale widget for selecting the font size
font_size_slider = ttk.Scale(root, from_=10, to=20, variable=selected_font_size, orient="horizontal", command=update_font_size)
font_size_slider.grid(row=3, column=0, padx=10, pady=(0, 10), sticky="ew")

# Create a rule selection dropdown with a hint
rule_var = tk.StringVar()
rule_var.set("Select a rule")
rule_menu = tk.OptionMenu(root, rule_var, "Select a rule", *rules.keys(), command=lambda _: display_rule(rule_var.get()))
rule_menu.grid(row=4, column=0, padx=10, pady=(0, 5), sticky="ew")

# Button to quit the application
quit_button = tk.Button(root, text="Quit", command=quit_app)
quit_button.grid(row=5, column=0, padx=10, pady=(0, 10), sticky="ew")

# Configure grid row and column weights for resizing
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Run the Tkinter main loop
root.mainloop()

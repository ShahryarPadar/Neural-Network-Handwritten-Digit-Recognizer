from tkinter.ttk import Style

def apply_Dark_Theme_style():
    Dark_Theme_Style = Style()
    Dark_Theme_Style.theme_use("clam")

    Dark_Theme_Style.configure("TFrame",
                                background="#212121")

    Dark_Theme_Style.configure("TNotebook",
                               background="#994d00")

    Dark_Theme_Style.configure("TLabel",
                                background="#212121",
                                foreground="#ff8c1a",
                                font=("Arial Rounded MT Bold",13),
                                relief="solid",
                                  borderwidth=2)

    Dark_Theme_Style.configure("TButton",
                                background="#333333",
                                foreground="#ff8c1a",
                                  focusthickness=0,
                                    focuscolor="#ff8c1a",
                                    font=("Arial Rounded MT Bold",13))
    Dark_Theme_Style.map("TButton",
                         background=[("active", "#4d4d4d")],
                         foreground=[("active", "#ff8c1a")])

from tkinter import Canvas,ROUND
import tkinter.ttk as ttk
from tkinter.messagebox import showerror,showwarning,showinfo
from tkinter.filedialog import askopenfile,asksaveasfilename

from tkinterdnd2 import TkinterDnD, DND_FILES
from PIL import Image, ImageGrab, ImageOps, ImageTk
from numpy import array,argmax
from os import path


from Style_config import apply_Dark_Theme_style
from NN import predict




def start_paint(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def paint(event):
    global last_x, last_y

    if last_x and last_y:
        canvas.create_line(
                            last_x, last_y, event.x, event.y,
                            fill="white",
                            width=15,          # ضخامت قلم 
                            capstyle=ROUND,  # سر خط گرد
                            smooth=True        # روان‌سازی خطوط
                            )
        
    last_x, last_y = event.x, event.y

def reset(event):
    global last_x, last_y
    last_x, last_y = None, None

def preprocess_canvas():
    # Getting canvas coordinates on windows
    x = root.winfo_rootx() + canvas.winfo_x()
    y = root.winfo_rooty() + canvas.winfo_y()
    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()

    # Screenshot from canvas
    img = ImageGrab.grab().crop((x, y, x1, y1))

    # Convert to grayscale
    img = img.convert("L")


    # Resize to 28×28
    img = img.resize((28, 28), Image.Resampling.LANCZOS)
    
    

    # Convert to numpy array (value between 0 and 1)
    arr = array(img) 
    arr = arr / 255.0  # Normalize to [0,1]
    arr=arr * 0.98   # Scaling to [0.00,0.98]
    arr=arr + 0.01   # Scaling to [0.01,0.99]

    # Flattening
    arr=arr.reshape(-1)
   
    # predict
    res=predict(arr)

    showwarning("CNN",message=f"predicted value: {res}")    # Show  predicted value
    canvas.delete("all")      # Clear canvas

def on_file_drop(event):
    global file_path

    try:
        files = root.splitlist(event.data)

        if len(files) > 1:
            showerror("Error", "You can only drop one file at a time!")
            return


        allowed_ext = (".png", ".jpg", ".jpeg")
        if not file_path.lower().endswith(allowed_ext):
            showerror("Error", "Only (png, jpg, jpeg) files are supported!")
            file_path = None
            return

        img = Image.open(file_path)
        disp = img.copy()
        disp.thumbnail((280, 280))
        photo = ImageTk.PhotoImage(disp)

        Drop_labls.config(image=photo, text="")
        Drop_labls.image = photo
        Drop_labls.pil_image = img

    except Exception as e:
        showerror("Error", f"Failed to load image:\n{e}")
        file_path = None

def on_browse_file():
    global file_path

    try:
        file = askopenfile(mode='r', filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if not file:
            return

        file_path = file.name

        img = Image.open(file_path)
        disp = img.copy()
        disp.thumbnail((280, 280))
        photo = ImageTk.PhotoImage(disp)

        Drop_labls.config(image=photo, text="")
        Drop_labls.image = photo
        Drop_labls.pil_image = img

    except Exception as e:
        showerror("Error", f"Could not open image:\n{e}")
        file_path = None

def preprocess_file(source=None):
    global file_path

    try:
        pil_img = None
        if source is None:
            pil_img = getattr(Drop_labls, "pil_image", None)
            if pil_img is None:
                showerror("Error", "No image selected. Please drop or browse an image first.")
                return None
        elif isinstance(source, str):
            if not path.exists(source):
                showerror("Error", f"File not found:\n{source}")
                return None
            pil_img = Image.open(source)
        elif isinstance(source, Image.Image):
            pil_img = source
        else:
            showerror("Error", "Unsupported image source.")
            return None


        # Convert to grayscale
        img = pil_img.convert("L")

        # Resize to 28×28
        img = img.resize((28, 28), Image.Resampling.LANCZOS)

        # Convert to numpy array (value between 0 and 1)
        arr = array(img)
        arr = arr / 255.0
        arr = arr * 0.98
        arr = arr + 0.01

        # Flattening
        arr = arr.reshape(-1)

        # predict
        res = predict(arr)

        showinfo("CNN", f"Predicted value: {res}")   # Show Predict Value

        # --- Reset everything after prediction ---
        file_path = None
        Drop_labls.config(image="", text="          Drag and drop\n\t   or\nbrowse file from computer")
        if hasattr(Drop_labls, "image"):
            del Drop_labls.image
        if hasattr(Drop_labls, "pil_image"):
            del Drop_labls.pil_image


    except Exception as e:
        showerror("Error", f"Unexpected error:\n{e}")
        return None

def save_canvas_as_png():
    try:
        # گرفتن مختصات دقیق کانواس روی صفحه
        x = canvas.winfo_rootx()
        y = canvas.winfo_rooty()
        x1 = x + canvas.winfo_width()
        y1 = y + canvas.winfo_height()

        # گرفتن اسکرین‌شات فقط از محدوده کانواس
        img = ImageGrab.grab(bbox=(x, y, x1, y1))

        ext = [("PNG files", "*.png"),("JPG files", "*.jpg"),("JPEG files", "*.jpeg")]
        filename = asksaveasfilename(defaultextension=".png",filetypes=ext)

        if filename != "" :
            img.save(f"{filename}")
                

            showinfo("Success", f"Canvas saved as  {filename}")


    except Exception as e:
        showerror("Error", f"Could not save canvas:\n{e}")

# ================= Root ==================
root = TkinterDnD.Tk()   # تغییر به TkinterDnD.Tk()
root.configure(bg="lightblue")
root.title("Neural network")
root.resizable(False, False)
root.geometry("600x600")
root.iconbitmap("icon.ico")

apply_Dark_Theme_style()  # Apply custom theme


# ================= Notebook =================
tab_control = ttk.Notebook(root)
tab_control.pack(expand=1, fill='both')

######################## Drawing with canvas in notebook##########################
draw_tab_Frame = ttk.Frame(tab_control, width=598, height=504)
tab_control.add(draw_tab_Frame, text="   draw    ")

    # ==== Buttons ====
draw_tab_Processing_Button = ttk.Button(draw_tab_Frame,text="Processing",command=preprocess_canvas)
draw_tab_Processing_Button.place(x=457,y=20,height=55,width=120)

clear_btn = ttk.Button(draw_tab_Frame,text="clear",command=lambda :canvas.delete("all"))
clear_btn.place(x=317, y=20, height=55, width=120)

save_Button=ttk.Button(draw_tab_Frame,text="Save",command=save_canvas_as_png)
save_Button.place(x=177 , y=20, height=55 , width=120)

    # ==== canvas ====
canvas = Canvas(draw_tab_Frame,
                 width=280,
                 height=280,
                 bg="#000000",
                 highlightthickness=2,
                 highlightbackground="#ffffff" )

canvas.place(x=300,y=300,anchor="center")
canvas.bind("<Button-1>", start_paint)     # شروع کشیدن
canvas.bind("<B1-Motion>", paint)          # کشیدن هنگام حرکت
canvas.bind("<ButtonRelease-1>", reset)    # ریست موقعیت وقتی ماوس رها شد


##################### File selection from the system ########################
Choosefile_tab_Frame = ttk.Frame(tab_control, width=598, height=504)
tab_control.add(Choosefile_tab_Frame, text="Choose file")

global file_path
file_path=None
    # ==== Buttons ====

Choosefile_tab_Processing_Button = ttk.Button(Choosefile_tab_Frame, text="Processing", command=preprocess_file)
Choosefile_tab_Processing_Button.place(x=457, y=20, height=55, width=120)

browse_file_Button = ttk.Button(Choosefile_tab_Frame, text="Browse file",command=on_browse_file)
browse_file_Button.place(x=597 // 2, y=643 // 2, anchor="center")

    # ==== Labels ====
Drop_labls = ttk.Label(Choosefile_tab_Frame,
                       text="          Drag and drop\n\t   or\nbrowse file from computer",
                       padding=10 )

Drop_labls.place(x=597 // 2, y=503 // 2, anchor="center")

# Enable Drop on Label
Drop_labls.drop_target_register(DND_FILES)
Drop_labls.dnd_bind('<<Drop>>', on_file_drop)


Attention_icon = Image.open("Attention.png") 
Attention_icon = Attention_icon.resize((24, 24))       
icon = ImageTk.PhotoImage(Attention_icon)

Attention_label = ttk.Label(Choosefile_tab_Frame,
                             image=icon,
                             compound="left",
                             padding=10,
                             wraplength=370,
                             font=("Arial Rounded MT Bold",11),
                             borderwidth=1,
                             text="The selected image should have a white background and the number should be clear.")
Attention_label.image = icon
Attention_label.place(x=10,y=20,height=56)



# ================= Run =================
root.mainloop()
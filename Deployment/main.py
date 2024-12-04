import tkinter as tk
from tkinter import filedialog, ttk, font
from PIL import Image, ImageTk, ImageFont
from ultralytics import YOLO
import os
import webbrowser
import cv2
import math

class RoadScanApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("RoadScan - AI-Driven Road Quality Detection for Accessibility and Safety")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        self.state("zoomed")
        self.iconbitmap("asset/icon.ico")
        self.resizable(False, False)
        self.pages = {}

        self.show_page(MainMenu)

    def show_page(self, page_class):
        """Switches to a new page."""
        page = self.pages.get(page_class)
        if page is None:
            page = page_class(self)
            self.pages[page_class] = page
        page.tkraise()
    
    # Custom Font
    def audiowide(self, a):
        self.pfont1 = ImageFont.truetype("font/Audiowide-Regular.ttf", size=a)
        self.font = font.Font(family=self.pfont1.getname()[0], size=a)
        return self.font
    
    def offside(self, a):
        self.pfont2 = ImageFont.truetype("font/Offside-Regular.ttf", size=a)
        self.font = font.Font(family=self.pfont2.getname()[0], size=a)
        return self.font
    
    # Load Model Function
    def load_model(self):
        self.model_path = "model/best.pt"
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"Model file not found: {self.model_path}")
        self.model = YOLO(self.model_path)
        return self.model


class MainMenu(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")
        self.place(relwidth=1, relheight=1)

        self.widthG = int(self.winfo_screenwidth())
        self.heightG = int(self.winfo_screenheight())

        # Left Frame
        self.left_frame = tk.Frame(self, bg="#09031D", width=self.widthG//2, height=self.heightG)
        self.left_frame.pack(side="left", fill="both", expand=True)

    
        self.image_text_frame = tk.Frame(self.left_frame, bg="#09031D")
        self.image_text_frame.pack(expand=True)

        # Main Logo
        try:
            self.image = Image.open("asset/logo.png") 
            self.image = self.image.resize((int(math.floor(self.widthG*0.390625)), int(math.floor(self.heightG*0.2361111111111111))))
            self.img = ImageTk.PhotoImage(self.image)
            self.img_label = tk.Label(self.image_text_frame, image=self.img, bg="#09031D")
            self.img_label.pack()
        except Exception as e:
            self.img_label = tk.Label(self.image_text_frame, text="Image not found!", fg="#FFFFFF", bg="#09031D", font=("Arial", int(math.floor(self.widthG*0.0104166667)), "bold"))
            self.img_label.pack()

        # Subtitle
        try:
            self.text_label = tk.Label(
                self.image_text_frame,
                text="AI-Driven Road Quality Detection\nfor Accessibility and Safety",
                font=parent.offside(int(math.floor(self.widthG*0.0104166667))),
                fg="#FFFFFF",
                bg="#09031D",
                justify="center",
            )
            self.text_label.pack(pady=int(math.floor(self.heightG*0.0231481481481481)))
        except Exception as e:
            self.text_label = tk.Label(self.left_frame, text="AI-Driven Road Quality Detection\nfor Accessibility and Safety", font=("Arial", int(math.floor(self.widthG*0.0104166667))), fg="#FFFFFF", bg="#1A103F")
            self.text_label.pack(expand=True)

        # Right Frame
        self.right_frame = tk.Frame(self, bg="#667DF6", width=self.widthG//2, height=self.heightG)
        self.right_frame.pack(side="right", fill="both", expand=True)

        # Exit Button
        self.img_image = Image.open("asset/button.png") 
        self.img_image = self.img_image.resize((int(math.floor(self.widthG*0.01953125)), int(math.floor(self.heightG*0.0347222222222222))))
        self.img_image = ImageTk.PhotoImage(self.img_image)
        self.button_exit = tk.Button(self.left_frame, image=self.img_image, compound="left", padx=0, pady=0, background="#C93131", command=parent.destroy)
        self.button_exit.place(relx=0.05, rely=0.05, anchor="nw")

        # Menu Button Frame
        self.button_frame = tk.Frame(self.right_frame, bg="#667DF6")
        self.button_frame.pack(expand=True)  

        # Image Detection Button
        self.image_button_frame = tk.Frame(self.button_frame, bg="#667DF6")
        self.image_button_frame.pack(pady=int(math.floor(self.heightG*0.0231481481481481)))

        try:
            self.image_icon = Image.open("asset/image.png") 
            self.image_icon = self.image_icon.resize((int(math.floor(self.widthG*0.0325520833333333)), int(math.floor(self.heightG*0.0578703703703704))))
            self.image_icon = ImageTk.PhotoImage(self.image_icon)
        except Exception as e:
            self.image_icon = None

        self.button1 = tk.Button(self.image_button_frame, text="Image Detection", font=parent.audiowide(int(math.floor(self.widthG*0.0130208333))), bg="#454545", fg="#FFFFFF", compound="left", image=self.image_icon, relief='flat', padx=int(math.floor(self.widthG*0.0260416666666667)), width=int(math.floor(self.widthG*0.1953125)), height=int(math.floor(self.heightG*0.1041666666666667)), command=lambda p=Menu1Page: parent.show_page(p))
        self.button1.pack(side="left") 

        # Video Detection Button
        self.video_button_frame = tk.Frame(self.button_frame, bg="#667DF6")
        self.video_button_frame.pack(pady=int(math.floor(self.heightG*0.0231481481481481)))

        try:
            self.video_icon = Image.open("asset/cinema.png") 
            self.video_icon = self.video_icon.resize((int(math.floor(self.widthG*0.0325520833333333)), int(math.floor(self.heightG*0.0578703703703704))))
            self.video_icon = ImageTk.PhotoImage(self.video_icon)
        except Exception as e:
            self.video_icon = None

        self.button2 = tk.Button(self.video_button_frame, text="Video Detection", font=parent.audiowide(int(math.floor(self.widthG*0.0130208333))), bg="#454545", fg="#FFFFFF", compound="left", image=self.video_icon, relief='flat', padx=int(math.floor(self.widthG*0.0260416666666667)), width=int(math.floor(self.widthG*0.1953125)), height=int(math.floor(self.heightG*0.1041666666666667)), command=lambda p=Menu2Page: parent.show_page(p))
        self.button2.pack(side="left")

        # About Button
        self.about_button_frame = tk.Frame(self.button_frame, bg="#667DF6")
        self.about_button_frame.pack(pady=int(math.floor(self.heightG*0.0231481481481481)))

        try:
            self.about_icon = Image.open("asset/info.png") 
            self.about_icon = self.about_icon.resize((int(math.floor(self.widthG*0.0325520833333333)), int(math.floor(self.heightG*0.0578703703703704))))
            self.about_icon = ImageTk.PhotoImage(self.about_icon)
        except Exception as e:
            self.about_icon = None

        self.button3 = tk.Button(self.about_button_frame, text="   About Us        ", font=parent.audiowide(int(math.floor(self.widthG*0.0130208333))), bg="#454545", fg="#FFFFFF", compound="left", image=self.about_icon, relief='flat', padx=int(math.floor(self.widthG*0.0260416666666667)), width=int(math.floor(self.widthG*0.1953125)), height=int(math.floor(self.heightG*0.1041666666666667)), command=lambda p=Menu3Page: parent.show_page(p))
        self.button3.pack(side="left")

class Menu1Page(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#09031D")
        self.place(relwidth=1, relheight=1)

        self.running = False
        self.file_path = None
        self.cap = None

        # ================== LOAD YOLO MODEL ===================
        self.model = parent.load_model()

        self.widthG = int(self.winfo_screenwidth())
        self.heightG = int(self.winfo_screenheight())

        self.canvas_width = int(math.floor(self.widthG * 0.35))
        self.canvas_height = int(math.floor(self.heightG * 0.4))

        self.frame_title = tk.Frame(self, bg="#09031D")
        self.frame_title.pack(fill="x", pady=int(math.floor(self.heightG*0.0115740740740741)))

        # Back To Main Menu Button
        self.back_image = Image.open("asset/arrow.png")
        self.back_image = self.back_image.resize((int(math.floor(self.widthG*0.0162760416666667)), int(math.floor(self.heightG*0.0289351851851852))))
        self.back_image = ImageTk.PhotoImage(self.back_image)
        self.back_button = tk.Button(self.frame_title, bg="#D9D9D9", fg="black", image=self.back_image, compound="left",font=parent.audiowide(int(math.floor(self.widthG*0.00651041667))), padx=int(math.floor(self.widthG*0.0032552083333333)), text="Back to Main Menu", command=lambda: parent.show_page(MainMenu))
        self.back_button.pack(side="left", padx=int(math.floor(self.widthG*0.0130208333333333)), pady=int(math.floor(self.heightG*0.005787037037037)))

        # Title
        self.frame_tit = tk.Frame(self, bg="#09031D")
        self.frame_tit.pack(pady=0)
        self.title_label = tk.Label(self.frame_tit, text="IMAGE DETECTION", font=parent.audiowide(int(math.floor(self.widthG*0.0247395833))), fg="white", bg="#09031D")
        self.title_label.pack(padx=int(math.floor(self.widthG*0.0065104166666667)), pady=int(math.floor(self.heightG*0.005787037037037)))

        # Logo
        self.image_path = "asset/logo.png"
        if os.path.exists(self.image_path):
            self.corner_image = Image.open(self.image_path).resize((int(math.floor(self.widthG*0.2083333333333333)), int(math.floor(self.heightG*0.1041666666666667))))
            self.corner_image_tk = ImageTk.PhotoImage(self.corner_image)
            self.label_corner = tk.Label(self.frame_title, image=self.corner_image_tk, bg="#09031D")
            self.label_corner.image = self.corner_image_tk 
            self.label_corner.pack(side="right", padx=int(math.floor(self.widthG*0.0065104166666667)))

        self.main_frame = tk.Frame(self, bg="#09031D")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=int(math.floor(self.widthG*0.0032552083333333)), pady=int(math.floor(self.heightG*0.0231481481481481)))

        self.left = tk.Frame(self.main_frame, bg="#09031D")
        self.left.pack(pady=0, side="left", padx=int(math.floor(self.widthG*0.009765625)))

        self.right = tk.Frame(self.main_frame, bg="#09031D")
        self.right.pack(side=tk.LEFT, fill=tk.Y, pady=0, padx=int(math.floor(self.widthG*0.009765625)))

        # Frame Button
        self.frame_buttons = tk.Frame(self.left, bg="#09031D")
        self.frame_buttons.pack(pady=0)

        # Load Image and Detect Button
        self.img_image = Image.open("asset/img.png")
        self.img_image = self.img_image.resize((int(math.floor(self.widthG*0.01953125)), int(math.floor(self.heightG*0.0347222222222222))))
        self.img_image = ImageTk.PhotoImage(self.img_image)
        self.button_load = tk.Button(self.frame_buttons, bg="#1B00FF", fg="white", image=self.img_image, compound="left", font=parent.audiowide(int(math.floor(self.widthG*0.0078125))), padx=int(math.floor(self.widthG*0.0065104166666667)), text="Load Image and Detect", command=self.start_detection)
        self.button_load.pack(pady=int(math.floor(self.heightG*0.0173611111111111)))

        # Frame Main Content
        self.frame_content = tk.Frame(self.left, bg="#09031D")
        self.frame_content.pack(pady=int(math.floor(self.heightG*0.0115740740740741)))

        # Left Frame
        self.frame_left = tk.Frame(self.frame_content, width=self.canvas_width, height=self.canvas_height, bg="#09031D")
        self.frame_left.grid(row=0, column=0, padx=int(math.floor(self.widthG*0.005859375)), pady=int(math.floor(self.heightG*0.0115740740740741)))

        # Right Frame
        self.frame_right = tk.Frame(self.frame_content, width=self.canvas_width, height=self.canvas_height, bg="#09031D")
        self.frame_right.grid(row=0, column=1, padx=0, pady=int(math.floor(self.heightG*0.0115740740740741)))

        self.canvas_left = tk.Canvas(self.frame_left, width=self.canvas_width, height=self.canvas_height, bg="#09031D")
        self.canvas_left.pack()
        self.canvas_right = tk.Canvas(self.frame_right, width=self.canvas_width, height=self.canvas_height, bg="#09031D")
        self.canvas_right.pack()
        self.canvas_left.create_text(
            self.canvas_width/2, self.canvas_height/2,
            text="Please Insert Image", 
            font=("Arial", int(math.floor(self.widthG*0.0104166667)), "bold"), 
            fill="white"
        )
        self.canvas_right.create_text(
            self.canvas_width/2, self.canvas_height/2,
            text="Please Insert Image", 
            font=("Arial", int(math.floor(self.widthG*0.0104166667)), "bold"),
            fill="white"
        )

        # Original & Detected Image Label
        self.label_left = tk.Label(self.frame_content, text="Original Image", font=parent.audiowide(int(math.floor(self.widthG*0.0091145833))), bg="#D9D9D9", fg="black", padx=int(math.floor(self.widthG*0.0130208333333333)), pady=int(math.floor(self.heightG*0.005787037037037)))
        self.label_left.grid(row=1, column=0, pady=int(math.floor(self.heightG*0.005787037037037)))
        self.label_right = tk.Label(self.frame_content, text="Detected Image", font=parent.audiowide(int(math.floor(self.widthG*0.0091145833))), bg="#D9D9D9", fg="black", padx=int(math.floor(self.widthG*0.0130208333333333)), pady=int(math.floor(self.heightG*0.005787037037037)))
        self.label_right.grid(row=1, column=1, pady=int(math.floor(self.heightG*0.005787037037037)))

        # Result Label
        self.result_title = tk.Label(self.right, text="Result", font=parent.audiowide(int(math.floor(self.widthG*0.0104166667))), bg="#D9D9D9", fg="black", padx=int(math.floor(self.widthG*0.0065104166666667)))
        self.result_title.pack(pady=int(math.floor(self.heightG*0.0289351851851852)))

        # Result Section
        self.result_text = tk.Text(self.right, height=self.canvas_width, width=self.canvas_height, font=("Arial", int(math.ceil(self.widthG*0.0109375))), bg="#D9D9D9", fg="black", wrap=tk.WORD, padx=int(math.floor(self.widthG*0.01953125)), pady=int(math.floor(self.heightG*0.0231481481481481)))
        self.result_text.pack(padx=int(math.floor(self.widthG*0.0065104166666667)), pady=int(math.floor(self.heightG*0.0115740740740741)))
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, "No Object Detected")
        self.result_text.config(state=tk.DISABLED) 

    # Start Detection Fuction
    def start_detection(self):
        self.running = True
        self.file_path = filedialog.askopenfilename(
            title="Pilih File",
            filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")],
        )
        if self.file_path:
            self.cap = cv2.VideoCapture(self.file_path)
            self.input_image = Image.open(self.file_path).resize((self.canvas_width, self.canvas_height))
            self.input_image_tk = ImageTk.PhotoImage(self.input_image)
            self.result_image = Image.open(self.file_path).resize((self.canvas_width, self.canvas_height))
            self.result_image_tk = ImageTk.PhotoImage(self.result_image)

            self.canvas_left.image = self.input_image_tk
            self.canvas_left.create_image(0, 0, anchor=tk.NW, image=self.input_image_tk)
            self.canvas_right.image = self.result_image_tk
            self.canvas_right.create_image(0, 0, anchor=tk.NW, image=self.result_image_tk)
            self.detect_objects()

    # Detect Object Fuction
    def detect_objects(self):
        if not self.cap or not self.cap.isOpened():
            print("Cannot open video")
            return

        class_list = ["Lubang", "Melintang", "Memanjang", "Pinggir", "Retak Buaya", "Sambungan"]
        detection_colors = [(224,20,20), (245,135,10), (18,245,10), (10,92,245), (216,97,232), (255,255,255)]
        frame_wid, frame_hyt = self.canvas_width, self.canvas_height

        def update_frame():
            if not self.running:
                return

            ret, frame = self.cap.read()
            if not ret:
                self.cap.release()
                return

            frame = cv2.resize(frame, (frame_wid, frame_hyt))
            detect_params = self.model.predict(source=[frame], conf=0.25) #================== SETTING CONF ===================
            detected_objects = []

            for box in detect_params[0].boxes:
                clsID = int(box.cls[0])
                conf = box.conf[0]
                bb = box.xyxy[0].numpy()
                cv2.rectangle(
                    frame, (int(bb[0]), int(bb[1])), (int(bb[2]), int(bb[3])), detection_colors[clsID], 3
                )
                cv2.putText(
                    frame,
                    f"{class_list[clsID]} {conf:.2f}",
                    (int(bb[0]), int(bb[1]) - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (255, 255, 255),
                    2,
                )
                detected_objects.append(f"{class_list[clsID]} ({conf:.2f})")

            self.result_text.config(state=tk.NORMAL)
            self.result_text.delete("1.0", tk.END)    
            if detected_objects:
                self.result_text.insert(tk.END, "\n".join(detected_objects))
            else:
                self.result_text.insert(tk.END, "No Object Detected")
            self.result_text.config(state=tk.DISABLED)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = ImageTk.PhotoImage(Image.fromarray(frame_rgb))
            self.canvas_right.create_image(0, 0, anchor=tk.NW, image=img)
            self.canvas_right.image = img

            self.after(10, update_frame)

        update_frame()

class Menu2Page(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#09031D")
        self.place(relwidth=1, relheight=1)

        self.running = False
        self.file_path = None
        self.cap = None

        # ================== LOAD YOLO MODEL ===================
        self.model = parent.load_model()

        self.widthG = int(self.winfo_screenwidth())
        self.heightG = int(self.winfo_screenheight())

        self.frame_title = tk.Frame(self, bg="#09031D")
        self.frame_title.pack(fill="x", pady=int(math.floor(self.heightG*0.0115740740740741)))

        # Back To Main Menu Button
        self.back_image = Image.open("asset/arrow.png") 
        self.back_image = self.back_image.resize((int(math.floor(self.widthG*0.0162760416666667)), int(math.floor(self.heightG*0.0289351851851852))))
        self.back_image = ImageTk.PhotoImage(self.back_image)
        self.back_button = tk.Button(self.frame_title, bg="#D9D9D9", fg="black", image=self.back_image, compound="left",font=parent.audiowide(int(math.floor(self.widthG*0.00651041667))), padx=int(math.floor(self.widthG*0.0032552083333333)), text="Back to Main Menu", command=lambda: parent.show_page(MainMenu))
        self.back_button.pack(side="left", padx=int(math.floor(self.widthG*0.0130208333333333)), pady=int(math.floor(self.heightG*0.005787037037037)))

        # Title
        self.frame_tit = tk.Frame(self, bg="#09031D")
        self.frame_tit.pack(pady=0)
        self.title_label = tk.Label(self.frame_tit, text="VIDEO DETECTION", font=parent.audiowide(int(math.floor(self.widthG*0.0247395833))), fg="white", bg="#09031D")
        self.title_label.pack(padx=int(math.floor(self.widthG*0.0065104166666667)), pady=int(math.floor(self.heightG*0.005787037037037)))

        # Logo
        self.image_path = "asset/logo.png"
        if os.path.exists(self.image_path):
            self.corner_image = Image.open(self.image_path).resize((int(math.floor(self.widthG*0.2083333333333333)), int(math.floor(self.heightG*0.1041666666666667))))
            self.corner_image_tk = ImageTk.PhotoImage(self.corner_image)
            self.label_corner = tk.Label(self.frame_title, image=self.corner_image_tk, bg="#09031D")
            self.label_corner.image = self.corner_image_tk
            self.label_corner.pack(side="right", padx=int(math.floor(self.widthG*0.0065104166666667)))

        # Main Frame
        self.main_frame = tk.Frame(self, bg="#09031D")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=int(math.floor(self.widthG*0.0032552083333333)), pady=int(math.floor(self.heightG*0.0231481481481481)))

        # Left Frame
        self.left_frame = tk.Frame(self.main_frame, bg="#09031D")
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=int(math.floor(self.widthG*0.09765625)))

        # Insert Video Button
        self.img_image = Image.open("asset/img.png") 
        self.img_image = self.img_image.resize((int(math.floor(self.widthG*0.01953125)), int(math.floor(self.heightG*0.0347222222222222))))
        self.img_image = ImageTk.PhotoImage(self.img_image)
        self.button1 = tk.Button(self.left_frame, bg="#1B00FF", fg="white", text="Insert Video", image=self.img_image, font=parent.audiowide(int(math.floor(self.widthG*0.0078125))), padx=int(math.floor(self.widthG*0.0065104166666667)), compound="left", command=self.start_detection)
        self.button1.pack(pady=int(math.floor(self.heightG*0.0115740740740741)))

        self.canvas = tk.Canvas(self.left_frame, width=int(math.floor(self.widthG*0.4557291666666667)), height=int(math.floor(self.heightG*0.462962962962963)), bg="black")
        self.canvas.pack(pady=int(math.floor(self.heightG*0.0115740740740741)))

        self.canvas.create_text(int(math.floor(self.widthG*0.4557291666666667))/2, int(math.floor(self.heightG*0.462962962962963))/2, text="Please Insert Video", font=("Arial", int(math.floor(self.widthG*0.0104166667)), "bold"), fill="white")

        # Control Frame
        self.control_frame = tk.Frame(self.left_frame, bg="#09031D")
        self.control_frame.pack(padx=int(math.floor(self.widthG*0.0032552083333333)))

        # Play Detect Button
        self.play_image = Image.open("asset/play.png") 
        self.play_image = self.play_image.resize((int(math.floor(self.widthG*0.0130208333333333)), int(math.floor(self.heightG*0.0231481481481481))))
        self.play_image = ImageTk.PhotoImage(self.play_image)
        self.play = tk.Button(self.control_frame, image=self.play_image, font=parent.audiowide(int(math.floor(self.widthG*0.0078125))), compound="left", text="Play Detect", command=self.resume_detection, padx=int(math.floor(self.widthG*0.0065104166666667)), pady=int(math.floor(self.heightG*0.0023148148148148)))
        self.play.pack(side=tk.LEFT, padx=int(math.floor(self.widthG*0.0032552083333333)))

        # Pause Detect Button
        self.pause_image = Image.open("asset/pause.png")
        self.pause_image = self.pause_image.resize((int(math.floor(self.widthG*0.0130208333333333)), int(math.floor(self.heightG*0.0231481481481481))))
        self.pause_image = ImageTk.PhotoImage(self.pause_image)
        self.pause = tk.Button(self.control_frame, image=self.pause_image, font=parent.audiowide(int(math.floor(self.widthG*0.0078125))), compound="left", text="Pause Detect", command=self.stop_detection, padx=int(math.floor(self.widthG*0.0065104166666667)), pady=int(math.floor(self.heightG*0.0023148148148148)))
        self.pause.pack(side=tk.LEFT, padx=int(math.floor(self.widthG*0.0032552083333333)))

        # Right Frame
        self.right_frame = tk.Frame(self.main_frame, bg="#09031D")
        self.right_frame.pack(side=tk.LEFT, fill=tk.Y, padx=int(math.floor(self.widthG*0.0065104166666667)))

        # Result Label
        self.result_title = tk.Label(self.right_frame, text="Result", font=parent.audiowide(int(math.floor(self.widthG*0.0104166667))), bg="#D9D9D9", fg="black", padx=int(math.floor(self.widthG*0.0065104166666667)))
        self.result_title.pack(pady=int(math.floor(self.heightG*0.0138888888888889)))

        # Result Section
        self.result_text = tk.Text(self.right_frame, height=int(math.floor(self.heightG*0.0190972222222222)), width=int(math.floor(self.widthG*0.01953125)), font=("Arial", int(math.floor(self.widthG*0.009765625))), bg="#D9D9D9", fg="black", wrap=tk.WORD, padx=int(math.floor(self.widthG*0.01953125)), pady=int(math.floor(self.heightG*0.0231481481481481)))
        # self.result_text = tk.Text(self.right_frame, height=int(math.floor(self.heightG*0.0190972222222222)), width=int(math.floor(self.widthG*0.4557291666666667)), font=("Arial", int(math.floor(self.widthG*0.009765625))), bg="#D9D9D9", fg="black", wrap=tk.WORD, padx=int(math.floor(self.widthG*0.01953125)), pady=int(math.floor(self.heightG*0.0231481481481481)))
        self.result_text.pack(padx=int(math.floor(self.widthG*0.0065104166666667)), pady=int(math.floor(self.heightG*0.0115740740740741)))

        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete("1.0", tk.END)  
        self.result_text.insert(tk.END, "No Object Detected")
        self.result_text.config(state=tk.DISABLED)

    # Start Detection Fuction
    def start_detection(self):
        self.running = True
        self.file_path = filedialog.askopenfilename(
            title="Pilih File",
            filetypes=[("Video Files", "*.mp4;*.avi")],
        )
        if self.file_path:
            self.cap = cv2.VideoCapture(self.file_path)
            self.detect_objects()

    # Stop Detection Fuction
    def stop_detection(self):
        self.running = False

    # Resume Detection Fuction
    def resume_detection(self):
        if not self.running and self.file_path and self.cap:
            self.running = True
            self.detect_objects()

    # Detect Object Fuction
    def detect_objects(self):
        if not self.cap or not self.cap.isOpened():
            print("Cannot open video")
            return

        class_list = ["Lubang", "Melintang", "Memanjang", "Pinggir", "Retak Buaya", "Sambungan"]
        detection_colors = [(224,20,20), (245,135,10), (18,245,10), (10,92,245), (216,97,232), (255,255,255)]
        frame_wid, frame_hyt = int(math.floor(self.widthG*0.4557291666666667)), int(math.floor(self.heightG*0.462962962962963))

        def update_frame():
            if not self.running:
                return

            ret, frame = self.cap.read()
            if not ret:
                print("End of video detection.")
                self.canvas.create_text(
                frame_wid/2, frame_hyt/2,
                text="End of Video Detection", 
                font=("Arial", int(math.floor(self.widthG*0.0104166667)), "bold"), 
                fill="white")
                self.cap.release()
                return

            frame = cv2.resize(frame, (frame_wid, frame_hyt))
            detect_params = self.model.predict(source=[frame], conf=0.25) #================== SETTING CONF ===================
            detected_objects = []

            for box in detect_params[0].boxes:
                clsID = int(box.cls[0])
                conf = box.conf[0]
                bb = box.xyxy[0].numpy()
                cv2.rectangle(
                    frame, (int(bb[0]), int(bb[1])), (int(bb[2]), int(bb[3])), detection_colors[clsID], 3
                )
                cv2.putText(
                    frame,
                    f"{class_list[clsID]} {conf:.2f}",
                    (int(bb[0]), int(bb[1]) - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (255, 255, 255),
                    2,
                )
                detected_objects.append(f"{class_list[clsID]} ({conf:.2f})")

            self.result_text.config(state=tk.NORMAL) 
            self.result_text.delete("1.0", tk.END)   
            if detected_objects:
                self.result_text.insert(tk.END, "\n".join(detected_objects)) 
            else:
                self.result_text.insert(tk.END, "No Object Detected")
            self.result_text.config(state=tk.DISABLED) 
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = ImageTk.PhotoImage(Image.fromarray(frame_rgb))
            self.canvas.create_image(0, 0, anchor=tk.NW, image=img)
            self.canvas.image = img

            self.after(10, update_frame)

        update_frame()

class Menu3Page(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#09031D")
        self.place(relwidth=1, relheight=1)

        self.widthG = int(self.winfo_screenwidth())
        self.heightG = int(self.winfo_screenheight())

        self.frame_title = tk.Frame(self, bg="#09031D")
        self.frame_title.pack(fill="x", pady=int(math.floor(self.heightG*0.0115740740740741)))

        # Back To Main Menu Button
        self.back_image = Image.open("asset/arrow.png") 
        self.back_image = self.back_image.resize((int(math.floor(self.widthG*0.0162760416666667)), int(math.floor(self.heightG*0.0289351851851852))))
        self.back_image = ImageTk.PhotoImage(self.back_image)
        self.back_button = tk.Button(self.frame_title, bg="#D9D9D9", fg="black", image=self.back_image, compound="left", font=parent.audiowide(int(math.floor(self.widthG*0.00651041667))), padx=int(math.floor(self.widthG*0.0032552083333333)), text="Back to Main Menu", command=lambda: parent.show_page(MainMenu))
        self.back_button.pack(side="left", padx=int(math.floor(self.widthG*0.0130208333333333)), pady=int(math.floor(self.heightG*0.005787037037037)))

        # Title
        self.frame_tit = tk.Frame(self, bg="#09031D")
        self.frame_tit.pack(pady=0)
        self.title_label = tk.Label(self.frame_tit, text="ABOUT US", font=parent.audiowide(int(math.floor(self.widthG*0.0247395833))), fg="white", bg="#09031D")
        self.title_label.pack(padx=int(math.floor(self.widthG*0.0065104166666667)), pady=int(math.floor(self.heightG*0.005787037037037)))

        # Logo
        self.image_path = "asset/logo.png" 
        if os.path.exists(self.image_path):
            self.corner_image = Image.open(self.image_path).resize((int(math.floor(self.widthG*0.2083333333333333)), int(math.floor(self.heightG*0.1041666666666667)))) 
            self.corner_image_tk = ImageTk.PhotoImage(self.corner_image)
            self.label_corner = tk.Label(self.frame_title, image=self.corner_image_tk, bg="#09031D")
            self.label_corner.image = self.corner_image_tk
            self.label_corner.pack(side="right", padx=int(math.floor(self.widthG*0.0065104166666667)))

        # Open URL Function
        def open_url():
            self.url = "https://github.com/RoadScanSolutionsTeam/RoadScan" 
            webbrowser.open(self.url)

        # Canvas Frame
        self.canvas_frame = tk.Frame(self)
        self.canvas_frame.pack(pady=int(math.floor(self.heightG*0.04)))

        self.canvas = tk.Canvas(self.canvas_frame, bg="#09031D", width=int(math.floor(self.widthG*0.8)), height=int(math.floor(self.heightG*0.5)))
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar = tk.Scrollbar(self.canvas_frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        # About Section
        self.frame_about = tk.Frame(self.canvas, bg="#09031D", width=int(math.floor(self.widthG*0.8)))
        self.canvas.create_window((0, 0), window=self.frame_about, anchor="nw")

        first_content = """RoadScan adalah platform berbasis teknologi object detection yang memanfaatkan kecerdasan buatan (AI) untuk mendeteksi berbagai kerusakan infrastruktur jalan seperti lubang, retakan, atau deformasi. Solusi ini memberikan kemampuan otomatisasi, akurasi tinggi, dan efisiensi dalam memantau kondisi jalan untuk perencanaan perbaikan yang lebih strategis.

Penggunaan Computer Vision, khususnya Object Detection, terutama untuk mendeteksi dan mengidentifikasi berbagai kerusakan infrastruktur jalan sangat membantu dalam memantau kondisi jalan secara efisien dan akurat. Teknologi yang digunakan adalah YOLOv8s dari Ultralytics. YOLO (You Only Look Once) adalah sistem deteksi objek yang terkenal karena kecepatan dan akurasinya. Versi terbaru, YOLOv8s, membawa peningkatan yang signifikan dari versi sebelumnya.
        """
        second_content = """Automatisasi Inspeksi Jalan
Sistem berbasis AI ini secara otomatis mampu mendeteksi jenis kerusakan jalan dari gambar atau video, menggantikan inspeksi manual yang memakan waktu dan tenaga.

Penghematan Biaya dan Waktu
Implementasi sistem ini menghasilkan respons yang lebih cepat dan efisien terhadap kerusakan jalan sehingga mengurangi biaya perbaikan dan durasi inspeksi manual.

Pemetaan Kerusakan dan Prioritas Perbaikan
Platform ini menghasilkan data untuk memetakan area dengan kerusakan paling parah, sehingga memudahkan penentuan prioritas perbaikan sesuai kebutuhan.

Peningkatan Keselamatan dan Kepuasan Pengguna Jalan
Dengan deteksi dini kerusakan jalan ini menurunkan risiko kecelakaan akibat jalan rusak dan meningkatkan kepercayaan masyarakat terhadap kualitas infrastruktur.
"""
        
        third_content = """RoadScan mendukung pencapaian Sustainable Development Goal (SDG) 11: Kota dan Pemukiman yang Berkelanjutan.

Meningkatkan keselamatan dan mobilitas masyarakat melalui deteksi dini kerusakan jalan.

Mendorong efisiensi dalam perbaikan jalan, sehingga mendukung kota yang lebih tangguh, aman, dan ramah lingkungan.
        """

        self.what = tk.Label(self.frame_about, text="What Is RoadScan", font=parent.audiowide(int(math.floor(self.widthG*0.0130208333))), fg="white", bg="#09031D", wraplength=int(math.floor(self.widthG*0.75)))
        self.what.pack(padx=int(math.floor(self.widthG*0.02)), pady=int(math.floor(self.heightG*0.02)))
        self.whatcont = tk.Label(self.frame_about, text=first_content, font=parent.offside(int(math.floor(self.widthG*0.0091145833))), fg="white", bg="#09031D", wraplength=int(math.floor(self.widthG*0.75)), justify="left")
        self.whatcont.pack(padx=int(math.floor(self.widthG*0.02)))

        self.det = tk.Label(self.frame_about, text="Detailed Features & Benefits", font=parent.audiowide(int(math.floor(self.widthG*0.0130208333))), fg="white", bg="#09031D", wraplength=int(math.floor(self.widthG*0.75)))
        self.det.pack(padx=int(math.floor(self.widthG*0.02)), pady=int(math.floor(self.heightG*0.02)))
        self.detcont = tk.Label(self.frame_about, text=second_content, font=parent.offside(int(math.floor(self.widthG*0.0091145833))), fg="white", bg="#09031D", wraplength=int(math.floor(self.widthG*0.75)), justify="left")
        self.detcont.pack(padx=int(math.floor(self.widthG*0.02)))

        self.det = tk.Label(self.frame_about, text="Sustainability Values", font=parent.audiowide(int(math.floor(self.widthG*0.0130208333))), fg="white", bg="#09031D", wraplength=int(math.floor(self.widthG*0.75)))
        self.det.pack(padx=int(math.floor(self.widthG*0.02)), pady=int(math.floor(self.heightG*0.02)))
        self.detcont = tk.Label(self.frame_about, text=third_content, font=parent.offside(int(math.floor(self.widthG*0.0091145833))), fg="white", bg="#09031D", wraplength=int(math.floor(self.widthG*0.75)), justify="left")
        self.detcont.pack(padx=int(math.floor(self.widthG*0.02)))

        self.det = tk.Label(self.frame_about, text="Get To Know “THE AUTHORS”", font=parent.audiowide(int(math.floor(self.widthG*0.0130208333))), fg="white", bg="#09031D", wraplength=int(math.floor(self.widthG*0.75)))
        self.det.pack(padx=int(math.floor(self.widthG*0.02)), pady=int(math.floor(self.heightG*0.02)))

        # Table
        self.style = ttk.Style()
        self.style.theme_use("default")
        self.style.configure("Treeview", font=parent.offside(int(math.floor(self.widthG*0.0091145833))), rowheight=int(math.floor(self.heightG*0.0347222222222222)), background="#D9D9D9", foreground="black", fieldbackground="#D9D9D9", padding=(0, 0)) 
        self.style.configure("Treeview.Heading", font=parent.audiowide(int(math.floor(self.widthG*0.0091145833))), background="#454545", foreground="white", padding=(0, int(math.floor(self.heightG*0.0231481481481481))))

        self.tree = ttk.Treeview(self.frame_about, columns=("Name", "Email", "Role"), show="headings")
        self.tree.pack(padx=int(math.floor(self.widthG*0.02)), pady=0)

        self.tree.heading("Name", text="Name")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Role", text="Role")

        self.tree.column("Name", width=int(math.floor(self.widthG*0.2604166666666667)), anchor="w", stretch=False) 
        self.tree.column("Email", width=int(math.floor(self.widthG*0.2604166666666667)), anchor="w", stretch=False)
        self.tree.column("Role", width=int(math.floor(self.widthG*0.1953125)), anchor="center", stretch=False)

        def disable_resize(event):
            if self.tree.identify_region(event.x, event.y) == "separator":
                return "break"

        self.tree.bind("<Button-1>", disable_resize)

        data = [
            ("Marsyanda Salsa Nabila", "marsyandasalsa2021@gmail.com", "Team Leader"),
            ("Ilham Khefi Ramadhanu", "ilhamramadhanu25@gmail.com", "Team Member"),
            ("Mochamad Freski Dino Fava", "dinofava12@gmail.com", "Team Member"),
            ("Shafa Anisya Aji Divana", "shafadivana@gmail.com", "Team Member"),
            ("Nisrina Alifa Adzahra", "nisrinalifa@gmail.com", "Team Member"),
            ("Cijo Jidan Riady", "cijo.business@gmail.com", "Team Member"),
            ("Ghea Dwi Apriliana", "gheapriliana96@gmail.com", "Team Member"),
            ("Nicholas Dominic", "nic.dominic@icloud.com", "Supervisor")
        ]

        for row in data:
            self.tree.insert("", tk.END, values=row)

        self.repo = tk.Label(self.frame_about, text='\nOur Repository', font=parent.audiowide(int(math.floor(self.widthG*0.0130208333))), fg="white", bg="#09031D")
        self.repo.pack()

        # Github Button
        self.img_image = Image.open("asset/github.png") 
        self.img_image = self.img_image.resize((int(math.floor(self.widthG*0.0325520833333333)), int(math.floor(self.heightG*0.0578703703703704))))
        self.img_image = ImageTk.PhotoImage(self.img_image)
        self.button_repo = tk.Button(self.frame_about, bg="#D9D9D9", fg="black", image=self.img_image, compound="left", font=parent.audiowide(int(math.floor(self.widthG*0.0130208333))), padx=int(math.floor(self.widthG*0.0130208333333333)), pady=int(math.floor(self.heightG*0.0115740740740741)), text="Github", command=open_url)
        self.button_repo.pack(pady=int(math.floor(self.heightG*0.0173611111111111)))

        self.canvas.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

if __name__ == "__main__":
    app = RoadScanApp()
    app.mainloop()
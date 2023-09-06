import customtkinter as ctk
import tkinter
from PIL import Image, ImageTk
import imageio
import serial
from random import randrange

# # Set up a serial connection
# ser = serial.Serial('COM4', 9600) # Change 'COM4' to the name of the port that your device is connected to

# this function came from: https://stackoverflow.com/a/74162322/14776907
def tksleep(t):
    'emulating time.sleep(seconds)'
    ms = int(t*1000)
    root = tkinter._get_default_root('sleep')
    var = tkinter.IntVar(root)
    root.after(ms, var.set, 1)
    root.wait_variable(var)

def close_doors():
     # Add a label above the video with the text "Do this gesture to open the lock"
    gesture_label = ctk.CTkLabel(root, text="Make sure to close the lock before you go", text_color="blue")
    gesture_label.configure(font=("Comic Sans MS", 40))
    gesture_label.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)
    # Play a local video file named open.mp4 within the Tkinter app
    video_label = ctk.CTkLabel(root, text="")
    video_label.place(relx=0.5, rely=0.55, anchor=ctk.CENTER)
    temp = "RIGHT" # CHANGE TO temp = "" when NOT testing
    while "RIGHT" not in temp:
        video = imageio.get_reader("open.mp4")
        for image in video.iter_data():
            # # Read data from the serial port
            # if ser.in_waiting > 0:
            #     temp = ser.readline().decode('utf-8').strip()
            #     print(temp)
            frame_image = ctk.CTkImage(Image.fromarray(image), size=(450, 450))
            video_label.configure(image=frame_image)
            root.update()
    # Clear the screen
    gesture_label.place_forget()
    video_label.place_forget()
    # Add a label in the center of the screen with the text "Open the doors of knowledge and explore the books that lie within"
    knowledge_label = ctk.CTkLabel(root, text="Thanks for visiting the Tech-Enabled Little Free Library Designed and Made by Raunak Singh")
    knowledge_label.configure(font=("Comic Sans MS", 20))
    knowledge_label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
    tksleep(10)
    knowledge_label.place_forget()


def on_submit2():
    motivation.place_forget()
    submit2.place_forget()
    background_label3.place_forget()

    # Add a label above the video with the text "Do this gesture to open the lock"
    gesture_label = ctk.CTkLabel(root, text="Follow the video to open the lock", text_color="blue")
    gesture_label.configure(font=("Comic Sans MS", 40))
    gesture_label.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)
    # Play a local video file named open.mp4 within the Tkinter app
    video_label = ctk.CTkLabel(root, text="")
    video_label.place(relx=0.5, rely=0.55, anchor=ctk.CENTER)
    temp = "LEFT" # CHANGE TO temp = "" when NOT testing
    while "LEFT" not in temp:
        video = imageio.get_reader("open.mp4")
        for image in video.iter_data():
            # # Read data from the serial port
            # if ser.in_waiting > 0:
            #     temp = ser.readline().decode('utf-8').strip()
            #     print(temp)
            frame_image = ctk.CTkImage(Image.fromarray(image), size=(450, 450))
            video_label.configure(image=frame_image)
            root.update()
    # Clear the screen
    gesture_label.place_forget()
    video_label.place_forget()
    # Add a label in the center of the screen with the text "Open the doors of knowledge and explore the books that lie within"
    knowledge_label = ctk.CTkLabel(root, text="Open the doors of knowledge and explore the books that lie within")
    knowledge_label.configure(font=("Comic Sans MS", 20))
    knowledge_label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
    tksleep(10)
    knowledge_label.place_forget()
    close_doors()

def on_submit():
    if radio_var.get() == 0:
        return
    # Clear the screen
    question.place_forget()
    submit.place_forget()
    background_label.place_forget()
    radiobutton_1.place_forget()
    radiobutton_2.place_forget()
    radiobutton_3.place_forget()
    radiobutton_4.place_forget()

    # Display image1.jpg as background
    background_image = Image.open("image3.jpg")
    background_photo = ctk.CTkImage(light_image=background_image, dark_image=background_image, size=(1000, 600))
    global background_label3
    background_label3 = ctk.CTkLabel(root, text="", image=background_photo)
    background_label3.place(x=0, y=0, relwidth=1, relheight=1)

    global motivation
    motivation = ctk.CTkLabel(root, text="Yay! You are CORRECT!!! 😀🎊🎉", text_color="blue")
    motivation.configure(font=("Comic Sans MS", 40))
    motivation.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

    global submit2
    submit2 = ctk.CTkButton(root, text="Let's Go", command=on_submit2, text_color="black", font=("Comic Sans MS", 30))
    submit2.place(relx=0.5, rely=0.7, anchor=ctk.CENTER)

def on_welcome():

    # Clear the screen
    button.place_forget()
    background2_label.place_forget()
    
    # Display image1.jpg as background
    background_image = Image.open("image1.jpg")
    background_photo = ctk.CTkImage(light_image=background_image, dark_image=background_image, size=(1000, 600))
    global background_label
    background_label = ctk.CTkLabel(root, text="", image=background_photo,)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    myMap = {"Which is your favorite color?": ["Red", "Green", "Blue", "Pink"],
             "Which one is your favorite pet?": ["Dog 🐶", "Cat 😺", "Bird 🐦", "Fish 🐟"],
             "Which one is your favorite subject?": ["Math 🔢", "English ✍️", "Science 🧪", "Art 🎨"],
             "Which one is your favorite shape?": ["Rectangle", "Circle", "Triangle", "Square"],
             "Which one is your favorite fruit?": ["Apple 🍎", "Banana 🍌", "Grapes 🍇", "Orange 🍊"],
             "Which one is your favorite sport?": ["Basketball 🏀", "Baseball ⚾", "Soccer ⚽", "Football 🏈"],
             "Which one is your favorite wild animal?": ["Lion 🦁", "Hippo 🦛", "Elephant 🐘", "Giraffe 🦒"],
             "What is your favorite instrument?": ["Violin 🎻", "Drums 🥁", "Guitar 🎸", "Trumpet 🎺"]}
    
    key = list(myMap.keys())[randrange(len(myMap))]
    # Display a question
    global question
    question = ctk.CTkLabel(root, text=key, text_color="black")
    question.configure(font=("Comic Sans MS", 40))
    question.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)
        
    global radio_var 
    radio_var = tkinter.IntVar(value=0)
    global radiobutton_1, radiobutton_2, radiobutton_3, radiobutton_4
    radiobutton_1 = ctk.CTkRadioButton(root, text=myMap[key][0], variable= radio_var, value=1, text_color="black", font=("Comic Sans MS", 30))
    radiobutton_2 = ctk.CTkRadioButton(root, text=myMap[key][1], variable= radio_var, value=2, text_color="black", font=("Comic Sans MS", 30))
    radiobutton_3 = ctk.CTkRadioButton(root, text=myMap[key][2], variable= radio_var, value=3, text_color="black", font=("Comic Sans MS", 30))
    radiobutton_4 = ctk.CTkRadioButton(root, text=myMap[key][3], variable= radio_var, value=4, text_color="black", font=("Comic Sans MS", 30))

    radiobutton_1.place(relx=0.2, rely=0.5, anchor=ctk.CENTER)
    radiobutton_2.place(relx=0.8, rely=0.5, anchor=ctk.CENTER)
    radiobutton_3.place(relx=0.2, rely=0.7, anchor=ctk.CENTER)
    radiobutton_4.place(relx=0.8, rely=0.7, anchor=ctk.CENTER)

    # Create a "Submit" button
    global submit
    submit = ctk.CTkButton(root, text="Submit", command=on_submit, fg_color="transparent", text_color="black", font=("Comic Sans MS", 30))
    submit.place(relx=0.5, rely=0.9, anchor=ctk.CENTER)

root = ctk.CTk()
root.title("Reading Adventure")

# Set the window size to 1000x600 pixels
root.geometry("1000x600")

def start():
    # Open image2.jpeg and create a CTkImage object
    image = Image.open("image2.jpg")
    ctk_image = ctk.CTkImage(light_image=image, dark_image=image, size=(1000, 550))
    global background2_label
    background2_label = ctk.CTkLabel(root, text="", image=ctk_image)
    background2_label.place(x=0, y=0, relwidth=1, relheight=0.95)

    # Create a button with the welcome message as its text
    global button
    button = ctk.CTkButton(root, text="Welcome, let's start the reading adventure! (Click to begin)", command=on_welcome)
    button.configure(font=("Comic Sans MS", 35))
    button.place(relx=0.5, rely=0.95, anchor=ctk.CENTER)

start()

root.mainloop()

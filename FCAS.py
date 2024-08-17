#FCAS.py
from tkinter import *
from PIL import Image
from PIL import ImageTk
from deepface import DeepFace
import tensorflow as tf
import cv2
import os
import numpy as np
import datetime
import pygame
import xlwings as xw

class Fcas:
    def __init__(self, root):
        self.root = root
        self.workbook = None
        self.root.geometry("1440x900+0+0")
        self.root.title("FACIAL  RECOGNITION  ATTENDANCE  SYSTEM")
        img1 = Image.open(r"C:\Users\Macbook Air\Anti Spoofing\imgs\tr.jpg")
        img1 = img1.resize((1440, 130), Image.BICUBIC)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=1440, height=150)

    #backgroundimage
        bgimg = Image.open(r"C:\Users\Macbook Air\Anti Spoofing\imgs\az.jpg")
        bgimg = bgimg.resize((1440, 720), Image.BICUBIC)
        self.photobgimg = ImageTk.PhotoImage(bgimg)

        bg_img = Label(self.root, image=self.photobgimg)
        bg_img.place(x=0, y=120, width=1440, height=720)

        #title
        heading = Label(bg_img, text="TAKE ATTENDANCE", font=("Exotc350 DmBd BT", 35, "bold"), bg="black", fg="white")
        heading.place(x=-5, y=-5, width=1450, height=70)

        b44 = Button(bg_img, text="START", command=self.face_r, cursor="hand2", font=("calibri", 15, "bold"), bg="darkblue", fg="white")
        b44.place(x=620, y=500, width=180, height=40)

        b55 = Button(bg_img, text="<<<BACK", command=self.end_program, cursor="hand2", font=("calibri", 15, "bold"), bg="darkblue", fg="white")
        b55.place(x=100, y=580, width=180, height=40)

        b66 = Button(bg_img, text="SAVE", command=self.end_program, cursor="hand2", font=("calibri", 15, "bold"), bg="darkblue", fg="white")
        b66.place(x=1120, y=580, width=180, height=40)


    def face_r(self):
        model = 'liveness.model'
        model = tf.keras.models.load_model(model)

        # Get the current date
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")

        # Create the Excel workbook with the current date as the name
        workbook_name = f'att_{current_date}.xlsx'


        try:
            self.workbook = xw.Book(workbook_name)
        except FileNotFoundError:
            self.workbook = xw.Book()
            self.workbook.save(workbook_name)


        sheet_name = datetime.date.today().isoformat()

        try:
            worksheet = self.workbook.sheets(sheet_name)
        except:
            worksheet = self.workbook.sheets.add(sheet_name)
            worksheet.range('A1').value = 'ROLL NO'
            worksheet.range('B1').value = 'NAME'
            worksheet.range('C1').value = 'DATE'
            worksheet.range('D1').value = 'TIME'

        s = 2
        students = []

        cap = cv2.VideoCapture(0)
        # pygame

        pygame.init()

        pg_txt = (39, 112, 50)
        pg_bg = (154, 179, 157)

        font = cv2.FONT_HERSHEY_SIMPLEX
        pygame_font = pygame.font.Font('freesansbold.ttf', 32)
        screen = pygame.display.set_mode((960, 540))
        background = pygame.image.load('bg.jpg')
        background = pygame.transform.rotozoom(background, 0, 0.8)
        screen.blit(background, (0, 0))

        # day today

        t0 = datetime.date.today()
        t0 = t0.day


        running = True

        while running:
            entered = False
            al_entered = False

            moment = datetime.datetime.now()
            hour = moment.hour
            minute = moment.minute
            seconds = moment.second
            day = moment.day
            month = moment.month
            year = moment.year

            date = f"{day}/{month}/{year}"
            time = f"{hour}:{minute}:{seconds}"

            screen.blit(background, (0, 0))

            # check
            if day != t0:
                t0 = day,

                worksheet = self.workbook.sheets.add(date)
                worksheet.range('A1').value = 'ROLL NO'
                worksheet.range('B1').value = 'NAME'
                worksheet.range('C1').value = 'DATE'
                worksheet.range('D1').value = 'TIME'

                students = []
                s = 2
                entered = False
                al_entered = False

            state, frame = cap.read()

            if not state:
                break

            res = DeepFace.find(frame, db_path='./Database/', enforce_detection=False, model_name='VGG-Face')

            if res and len(res) > 0 and 'identity' in res[0]:
                folder_name = res[0]['identity'][0].split('/')[2]  # Get the folder name

                # Split folder name into roll number and name
                if '-' in folder_name:
                    roll_no, name = folder_name.split('-')  # Split roll number and name
                else:
                    # Handle the case where the delimiter is not found
                    roll_no = None
                    name = folder_name

                xmin = int(res[0]['source_x'][0])
                ymin = int(res[0]['source_y'][0])
                w = res[0]['source_w'][0]
                h = res[0]['source_h'][0]
                xmax = int(xmin + w)
                ymax = int(ymin + h)

                # Perform liveness detection
                img = frame[ymin:ymax, xmin:xmax]
                img = cv2.resize(img, (32, 32))
                img = img.astype('float') / 255.0
                img = tf.keras.preprocessing.image.img_to_array(img)
                img = np.expand_dims(img, axis=0)
                liveness = model.predict(img)
                liveness = liveness[0].argmax()

                if liveness == 1:
                    screen.fill((0, 0, 0))

                    cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 255, 0), 1)

                    if roll_no is not None:
                        # Display roll number
                        cv2.putText(frame, f"Roll No: {roll_no}", (xmin, ymin + 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                                    (0, 0, 0), 2)

                    # Display name
                    cv2.putText(frame, f"Name: {name}", (xmin, ymin + 60), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0),2)

                    if roll_no in students:
                        al_entered = True
                    else:
                        worksheet.range(f'A{s}').value = roll_no
                        worksheet.range(f'B{s}').value = name
                        worksheet.range(f'C{s}').value = date
                        worksheet.range(f'D{s}').value = time
                        students.append(roll_no)
                        s += 1
                        entered = True

                    if al_entered:
                        ae_txt = pygame_font.render('Already Entered', True, pg_txt, pg_bg)
                        ae_txtrect = ae_txt.get_rect(center=(960 - 200, (540 // 2) + 40))
                        screen.blit(ae_txt, ae_txtrect)
                    elif entered:
                        e_txt = pygame_font.render('Entered', True, pg_txt, pg_bg)
                        e_txtrect = e_txt.get_rect(center=(960 - 200, (540 // 2) + 40))
                        screen.blit(e_txt, e_txtrect)
            image = pygame.image.frombuffer(frame.tostring(), frame.shape[1::-1], 'BGR')
            image = pygame.transform.rotozoom(image, 0, 0.8)
            screen.blit(image, (20, 80))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        cap.release()
        cv2.destroyAllWindows()



    def end_program(self):
        self.root.destroy()


    def save(self):
        # Specify the directory where you want to save the Excel file
        directory = r"C:\Users\MacBook Air\Anti Spoofing\Attendance"
        # Get the current date
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        # Generate the filename using the current date
        filename = f'att_{current_date}.xlsx'
        # Specify the full path of the file
        save_location = os.path.join(directory, filename)
        # Save the workbook to the specified location
        if hasattr(self, 'workbook') and self.workbook is not None:
            # Save the workbook to the specified location
            self.workbook.save(save_location)
            # Close the workbook
            self.workbook.close()
        else:
            print("Workbook is not initialized.")

    # def load(self):
    #     self.new_window = Tk.Toplevel(self.root)
    #     self.app = LoadingScreen(self.new_window)







if __name__ == "__main__":
    root = Tk()
    obj = Fcas(root)
    root.mainloop()

















































  # if not self.running:
            #     break  # Break the loop if the flag is set to False

        # workbook.save()
        # workbook.close()
        # pygame.quit()

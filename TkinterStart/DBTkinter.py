from tkinter import *
from DBUtil import DBUtil

db_util = DBUtil()
users = db_util.get_all_users('local')

root = Tk()
root.title('Phone Details')
root.resizable(False, False)
root.minsize(640, 480)

user_frame = Frame(root, borderwidth=2)
details_frame = Frame(root, borderwidth=2)

user_frame.grid(row=0, column=0, sticky=SW, )
details_frame.grid(row=0, column=1, columnspan=2, sticky=NSEW)


def display_user(user_name):
    for widget in details_frame.winfo_children():
        widget.destroy()
    details = db_util.get_user_details('local', user_name)
    print('username -> ', user_name)
    if 1 < len(details) < 6:
        Label(details_frame, text="Owner Name").grid(row=0, column=0)
        Label(details_frame, text=details[1]).grid(row=0, column=1, columnspan=2)

        Label(details_frame, text="Phone Brand").grid(row=1, column=0)
        Label(details_frame, text=details[2]).grid(row=1, column=1, columnspan=2)

        Label(details_frame, text="Phone Model").grid(row=2, column=0)
        Label(details_frame, text=details[3]).grid(row=2, column=1, columnspan=2)

        Label(details_frame, text="Comments").grid(row=3, column=0)
        Label(details_frame, text=details[4]).grid(row=3, column=1, columnspan=2)


for user in users:
    label = Label(user_frame, text=user)
    label.pack(fill=X)
    label.bind("<Button-1>", lambda event, data=user: display_user(data))

root.mainloop()

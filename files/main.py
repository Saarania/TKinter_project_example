import tkinter
import tkinter as tk
from tkinter.ttk import *
from animal import Animal
from transport_ability import TransportAbility
import random

window = tk.Tk()
window.geometry('1000x800')
window.title("Epptech inteview alogrythm")

combo_entry = Combobox(window)
lbl_display_animals = tk.Label(window, text="", justify=tkinter.LEFT, anchor="w")

# Constants
number_of_animals = 30
number_of_types = 7

# initializing animals
arr_elements = []
for i in range(number_of_animals):
    r_int = random.randint(0,number_of_types-1)
    r_age = random.randint(1,13)
    if r_int == 0:
        arr_elements.append(Animal(name="duck",age=r_age, transport=(TransportAbility.FLYING, TransportAbility.WALKING, TransportAbility.SWIMMING)))
    elif r_int == 1:
        arr_elements.append(Animal(name="cobra",age=r_age, transport=(TransportAbility.WALKING)))
    elif r_int == 2:
        arr_elements.append(Animal(name="crab",age=r_age, transport=(TransportAbility.WALKING, TransportAbility.SWIMMING)))
    elif r_int == 3:
        arr_elements.append(Animal(name="pidgeon",age=r_age, transport=(TransportAbility.FLYING, TransportAbility.WALKING)))
    elif r_int == 4:
        arr_elements.append(Animal(name="whale",age=r_age, transport=(TransportAbility.SWIMMING)))
    elif r_int == 5:
        arr_elements.append(Animal(name="mosquito",age=r_age , transport=(TransportAbility.FLYING, TransportAbility.WALKING)))
    elif r_int == 6:
        arr_elements.append(Animal(name="bear",age=r_int , transport=(TransportAbility.WALKING)))


def process():
    answer = combo_entry.get()
    selected_transport = 0;
    if answer == "Can swim":
        selected_transport = TransportAbility.SWIMMING
    elif answer == "Can fly":
        selected_transport = TransportAbility.FLYING
    elif answer == "Can walk":
        selected_transport = TransportAbility.WALKING

    txt_result = ""
    # !!! ALGORYTHM PART !!!
    for i in range(number_of_animals):
        try:
            iter(arr_elements[i].transport)
            if selected_transport in arr_elements[i].transport:
                txt_result += arr_elements[i].__str__() + "\n"
        except:
            if arr_elements[i].transport == selected_transport:
                txt_result += arr_elements[i].__str__() + "\n"
                
    lbl_display_animals.config(text=txt_result)

def start_app():

    lbl_intro = tk.Label(window, text="Hello, here is list of animals (items), select a rule for sorting them out.")
    combo_entry['values'] = ("Can swim", "Can fly", "Can walk")
    combo_entry.current(0)
    btn_process = tk.Button(window, text="Process", command=process)

    lbl_intro.grid(sticky=tk.W, column=0,row=0)
    combo_entry.grid(sticky=tk.W, column=0, row=1)
    btn_process.grid(sticky=tk.W, column=1,row=1)

    lbl_blank = tk.Label(window, text="\n")
    lbl_blank.grid(sticky=tk.W, column=0, row=2)

    # Display unsorted array
    str_all_animals = ""
    for i in range(number_of_animals):
        str_all_animals += arr_elements[i].__str__() + "\n"

    # print(f"arr elements len = {len(arr_elements)}")
    # print(f"number of animals = {number_of_animals}")

    lbl_display_animals.config(text=str_all_animals)
    lbl_display_animals.grid(sticky=tk.W, column=0, row=3)

    window.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_app()


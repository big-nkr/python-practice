import tkinter as tk

#function
def multiply():
    number = 0

    try:
        number = int(number_input.get())
        if number == 0:
            raise Exception()
    except:
        output_label.configure(text='ไม่ดีนะแม่ กรอกตัวเลขดี ไม่เอาเลข 0 ด้วยอีดอก \n ออกไปอีสัส !!')
        return

    output = ''
    for i in range(1, 13):
        output += str(number) + ' x ' + str(i)
        output += ' = ' + str(number * i) + '\n'

    output_label.configure(text=output)

#GUI
window = tk.Tk()
window.title('Multiplication Table')
window.minsize(width=400, height=400)

title_label = tk.Label(master=window, text='Times of')
title_label.pack(pady=20)

number_input = tk.Entry(master=window, width=15)
number_input.pack()

show_button = tk.Button(
    master=window, text='Calculate',
    command=multiply, width=15, height=2)
show_button.pack()

output_label = tk.Label(master=window)
output_label.pack(pady = 20)

window.mainloop()

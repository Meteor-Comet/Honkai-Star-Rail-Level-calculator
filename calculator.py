from tkinter import Tk, Label, Entry, Button

def calculate_required_days():
    current_level = int(current_level_entry.get())
    current_exp = int(current_exp_entry.get())
    target_level = int(target_level_entry.get())
    purchase_times = int(purchase_times_entry.get())

    exp_per_level = [0, 450, 500, 550, 610, 670, 720, 780, 840, 900, 960, 1020, 1070, 1130, 1190, 1250, 1310, 1370,
                     1430, 1500, 1600, 1710, 1830, 1950, 2080, 2210, 2350, 2480, 2620, 2750, 2850, 2960, 3080, 3200,
                     3330, 3460, 3600, 3730, 3870, 4000, 4140, 4280, 4430, 4570, 4710, 4860, 5000, 5150, 5300, 5440,
                     5700, 6150, 6630, 7130, 7640, 8170, 8700, 9230, 9780, 10330, 20300, 21780, 23350, 24970, 26630,
                     65070, 68810, 72490, 76120, 79710]
    target_exp = sum(exp_per_level[current_level:target_level])
    remaining_exp = target_exp - current_exp

    natural_recovery_exp = 240 // 10 * 50
    daily_active_exp = {0: 1000, 1: 1150, 2: 1300, 3: 1450, 4: 1600, 5: 1750, 6: 1900}
    if current_level < 65:
        daily_exp = natural_recovery_exp + daily_active_exp.get((current_level - 10) // 10, 0)
    else:
        daily_active_exp = natural_recovery_exp + 1900
    purchase_exp = purchase_times * 300
    up_level_exp = (target_level - current_level - 1) * 300

    required_days = (remaining_exp - up_level_exp) // (daily_exp + purchase_exp)
    if remaining_exp % daily_exp != 0:
        required_days += 1

    result_label.config(text=f"达到目标开拓等级所需的经验为:{remaining_exp}\n达到目标开拓等级所需的时间为: {required_days} 天")

window = Tk()
window.title("开拓等级计算器-by Comet")

current_level_label = Label(window, text="当前开拓等级:")
current_level_label.pack()
current_level_entry = Entry(window)
current_level_entry.pack()

current_exp_label = Label(window, text="当前经验:")
current_exp_label.pack()
current_exp_entry = Entry(window)
current_exp_entry.pack()

target_level_label = Label(window, text="目标开拓等级:")
target_level_label.pack()
target_level_entry = Entry(window)
target_level_entry.pack()

purchase_times_label = Label(window, text="每天购买体力次数:")
purchase_times_label.pack()
purchase_times_entry = Entry(window)
purchase_times_entry.pack()

balance_label = Label(window, text="注:不可跨均衡等级计算,未计算沉浸器与主线/同行任务")
balance_label.pack()

calculate_button = Button(window, text="计算", command=calculate_required_days)
calculate_button.pack()

result_label = Label(window, text="")
result_label.pack()

window.geometry("400x280")
window.mainloop()

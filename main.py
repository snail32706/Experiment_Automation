import numpy as np
import pyautogui
import pygetwindow as gw
# import win32gui
# import pygame
import sys
import time
import os


def Code_Stop():
    '''
    錯誤訊息跳出警報聲，
    使用 "esc" 跳出程式
    '''
    pygame.init()
    pygame.mixer.music.load("error_music.mp3")
    pygame.mixer.music.play()

    start_time = time.time()  # 获取系统的开始时间

    while True:
        current_time = time.time()  # 获取当前时间

        if current_time - start_time > 120:  # 如果运行时间超过 2 分钟（120 秒），则停止循环
            pygame.mixer.music.stop()
            sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.stop()
                    sys.exit()


# --- Shotter --- #



def back_to_Shotter(first=None):
    window = gw.getWindowsWithTitle("SSH-C2B Demo Software (Advanced Mode) v1.0.0.2")[0]
    window.activate()
    # gw.getWindowsWithTitle("SSH-C2B Demo Software (Advanced Mode) v1.0.0.2")[0].activate()
    pyautogui.sleep(0.1)

    if first is not None:
        active_window = gw.getActiveWindow()
        return active_window.left, active_window.top


def Shotter_change_mode(pulse_n):
    # 使用相對位置, 不需要理會視窗放在哪
    # left_located, top_located = back_to_Shotter()
    global left_located, top_located 

    # setting -> load
    pyautogui.moveTo(x=left_located+94, y=top_located+35, duration=0.1)
    pyautogui.click()
    pyautogui.moveTo(x=left_located+94, y=top_located+56, duration=0.1)
    pyautogui.click()
    pyautogui.sleep(0.1)

    # keybord
    pyautogui.typewrite(f"N_{pulse_n}.c2b")
    pyautogui.sleep(1)
    pyautogui.press("enter")
    pyautogui.sleep(0.1)


# --- Labview --- #

Labview_Buttom = {
    "main_Buttom": (32, 130),
    "SET_ZERO": (453, 214),
    "HOME": (542, 214),

    "GOx": (105, 297),
    "Backx": (160, 297),
    "dx_um": (240, 298),
    "GOy": (105, 350),
    "Backy": (160, 350),
    "dy_um": (240, 360),
    "GOz": (105, 404),
    "Backz": (160, 404),
    "dz_um": (240, 422),


    "energy_adjustment": (550, 339),
    "power_step": (550, 390),


    "Read_RTO": (674, 192),
    "Only_test": (757, 191),
    "Auto_mode": (834, 189),

    "delta_x": (692, 264),
    "delta_y": (767, 263),
    "hole_num": (694, 310),

    "auto_power_step": (910, 256),
    "START": (797, 311),
    "rest": (842, 446),

    "row_data": (386, 637),
    "save": (252, 864),
    "file_name": (420, 861),
    "folder_path": (420, 900)
}

def back_to_Labview():

    back_to_Shotter()
    # window = gw.getWindowsWithTitle("0824 - 複製.vi")[0]
    # window.activate()

    pyautogui.moveTo(x=113, y=17, duration=0.3)
    pyautogui.click()
    pyautogui.sleep(1)


def Labview_start_and_save(file_name):
    pyautogui.moveTo(Labview_Buttom["file_name"], duration=0.3)
    pyautogui.doubleClick()
    pyautogui.typewrite(f"{file_name}")
    pyautogui.sleep(0.1)
    pyautogui.moveTo(Labview_Buttom["START"], duration=0.3)
    pyautogui.click()
    pyautogui.moveTo(Labview_Buttom["save"], duration=0.3)
    pyautogui.click()


def Labview_setup(dx, dy, delta_power, folder):
    '''
    設置 dx, dy, Auto dx, dy.
    設置 delta_power
        setting:
        Stage    : dx = 1.5delta_x, dy = delta_x
        Auto mode: delta_x=delta_x, delta_y=0
        energy   : 設置好
        N        : 3
    power_change: 轉軸刻度
    '''
    back_to_Labview()
    pyautogui.moveTo(Labview_Buttom["rest"], duration=0.1)
    pyautogui.click()

    pyautogui.moveTo(Labview_Buttom["main_Buttom"], duration=0.1)
    pyautogui.click()

    pyautogui.moveTo(Labview_Buttom["SET_ZERO"], duration=0.1)
    pyautogui.click()
    pyautogui.moveTo(Labview_Buttom["dx_um"], duration=0.1)
    pyautogui.doubleClick()
    pyautogui.typewrite(f"{1.5*dx}")
    pyautogui.sleep(0.1)
    pyautogui.moveTo(Labview_Buttom["dy_um"], duration=0.1)
    pyautogui.doubleClick()
    pyautogui.typewrite(f"{1*dy}")
    pyautogui.sleep(0.5)

    pyautogui.moveTo(Labview_Buttom["Auto_mode"], duration=0.9)
    pyautogui.click()

    pyautogui.moveTo(Labview_Buttom["delta_x"], duration=0.2)
    pyautogui.doubleClick()
    pyautogui.sleep(0.5)
    pyautogui.typewrite(f"{dx}")
    pyautogui.sleep(0.1)
    pyautogui.moveTo(Labview_Buttom["delta_y"], duration=0.1)
    pyautogui.doubleClick()
    pyautogui.typewrite(f"0")
    pyautogui.sleep(0.1)
    pyautogui.moveTo(Labview_Buttom["hole_num"], duration=0.1)
    pyautogui.doubleClick()
    pyautogui.typewrite(f"3")
    pyautogui.sleep(0.1)

    pyautogui.moveTo(Labview_Buttom["auto_power_step"], duration=0.2)
    pyautogui.doubleClick()
    pyautogui.typewrite(f"0")
    pyautogui.sleep(0.1)

    # 轉軸刻度
    pyautogui.moveTo(Labview_Buttom["power_step"], duration=0.2)
    pyautogui.doubleClick()
    pyautogui.typewrite(f"{delta_power}")
    pyautogui.sleep(0.1)

    # folder 設置
    pyautogui.moveTo(Labview_Buttom["row_data"], duration=0.2)
    pyautogui.click()

    pyautogui.moveTo(Labview_Buttom["folder_path"], duration=0.2)
    pyautogui.click()
    pyautogui.doubleClick()
    pyautogui.typewrite(f"{folder}")
    pyautogui.sleep(2)
    pyautogui.press("enter")
    pyautogui.sleep(0.1)


def Labview_test_energy(delta_power):
    '''
    1. 將 mode 調整成 N=10,
    2. delta_x=0, 在相同的點打洞
    '''
    Shotter_change_mode(10)
    back_to_Labview()

    pyautogui.moveTo(Labview_Buttom["delta_x"], duration=0.1)
    pyautogui.doubleClick()
    pyautogui.sleep(0.5)
    pyautogui.typewrite("0")
    pyautogui.sleep(0.5)

    # 轉軸刻度
    pyautogui.moveTo(Labview_Buttom["power_step"], duration=0.2)
    pyautogui.doubleClick()
    pyautogui.typewrite(f"{delta_power}")
    pyautogui.sleep(0.1)

    global experiment_row_number
    Labview_start_and_save(file_name=f'energy_{experiment_row_number}')


def check_file(folder, file_name):
    '''
    檢查檔案，若沒有問題則 return True
    '''
    file_path = os.path.join(folder, file_name)
    if os.path.isfile(file_path):
        return True
    else:
        return False


def find_file(file_name, wait_total_time, delta_time):
    '''
    while loop to find file.
    等待 wait_total_time 後，delta_time 等待超過 20 次 "break"
     並且播放音樂。
    '''
    global experiment_row_number
    
    pyautogui.sleep(wait_total_time)

    for count_time in range(100):

        if count_time > 20:
            # Code_Stop() # 終止程式
            print("等待太久時間，找不到檔案")
            # Code_Stop()
            break

        elif check_file(folder, f'{file_name}.txt') == True:
            '''
            「file_name」命名規則:
                實驗打洞: f"row_{experiment_row_number}_n{Shotter_number}"
                測量能量: f"energy_{experiment_row_number}"
            '''
            if 'energy' in file_name:
                print(f"Energy check. Correct! \nrow={experiment_row_number}. Start experiment:")

            elif 'n_' in file_name:
                _, pulse_number = file_namesplit('_n')
                print(f"row={experiment_row_number} N={pulse_number}, Success!")
            break 

        pyautogui.sleep(delta_time)
        print(f"waiting {file_name} for {(wait_total_time+count_time*delta_time)/60} min")


def check_energy():
    '''
    檢查檔案中的能量是否正確
    因為有 up_data 存在存，因此沒有準備測試檔案則無法使用。
    '''

    abs_file_path = os.path.join(folder, f'energy_{experiment_row_number}')
    up_data = os.path.join(folder, f'energy_{experiment_row_number-1}')

    rawdat_up = np.loadtxt(up_data, delimiter='\t')
    mean_up, std_up = np.mean(rawdat_up), np.std(rawdat_up)

    rawdat = np.loadtxt(abs_file_path, delimiter='\t')
    mean, std = np.mean(rawdat), np.std(rawdat)

    if (std / mean * 100) > 15:
        # Code_Stop() # 終止程式
        print("energy StD false")
    
    # new 約等於 old * 1.2~1.5
    # new 不能比較小，也不能太大

    elif mean < mean_up*0.8 or mean > mean_up*1.6:
        # Code_Stop() # 終止程式
        print("能量有問題，檢查 HWP 選轉圈數")


def Labview_start_working(dx, delta_power):
    '''
    前置：
    back_to_Labview
    delta_x=更改成與「experiment_one_row」一致
    loop:
    1. 調整 mode
        將 mode 調整成 N = shutter_list[N]。
    2. 移動 1.5delta_x
    3. 開始打洞
        start_and_save
        使用 {Shotter_number} 存擋
    4. 查看檔案是否存在
    '''
    global experiment_row_number
    back_to_Labview()
    pyautogui.moveTo(Labview_Buttom["delta_x"], duration=0.5)
    pyautogui.doubleClick()
    pyautogui.typewrite(f"{dx}")
    pyautogui.sleep(0.1)

    for Shotter_idx, Shotter_number in enumerate(shutter_list):

        file_name = f"row_{experiment_row_number}_n{Shotter_number}"

        # 1 調整 mode
        Shotter_change_mode(Shotter_number)
        pyautogui.sleep(1)

        # 2. 移動 1.5delta_x
        pyautogui.moveTo(Labview_Buttom["GOx"], duration=0.1)
        pyautogui.click()
        pyautogui.sleep(2)

        # 3. start
        Labview_start_and_save(file_name=file_name)
        pyautogui.sleep(1)

        # 4. 查看檔案是否存在
        find_file(file_name=file_name, wait_total_time=30, delta_time=5)



def HOME_GOy_SET_ZERO():
    pyautogui.moveTo(Labview_Buttom["HOME"], duration=0.3)
    pyautogui.click()
    pyautogui.sleep(60)  # wait 90 sencond
    pyautogui.moveTo(Labview_Buttom["GOy"], duration=0.3)
    pyautogui.click()
    pyautogui.sleep(2)
    pyautogui.moveTo(Labview_Buttom["SET_ZERO"], duration=0.3)
    pyautogui.click()
    pyautogui.sleep(0.3)


# ----------------- ----------------- ----------------- #
# ----------------- ----------------- ----------------- #

folder = "C:\\Local Disk D_2192023324\\K.Y. Chen\\20230614\\data"
experiment_row_number = 2
shutter_list = np.array([2, 3, 4, 5, 6, 8, 10, 15, 20, 30, 40, 50, 100, 500])
left_located, top_located = back_to_Shotter(first='yes')

def experiment_one_row(dx, dy):

    global experiment_row_number, folder
    Labview_setup(dx=dx, dy=dy, delta_power=10, folder=folder)

    # for i in range(9):  # 更改 row 數量，預計做 20 個能量

    #     # energy 測試, 找檔案, 查看能量
    #     Labview_test_energy(delta_power=15)
    #     find_file(f"energy_{experiment_row_number}", wait_total_time=25, delta_time=5)
    #     # check_energy(abs_file_path, up_data) # 測試檔案時，註解。
    #     Labview_start_working(dx=dx, delta_power=15)
    #     HOME_GOy_SET_ZERO()

    #     pyautogui.moveTo(Labview_Buttom["energy_adjustment"], duration=0.9) 
    #     pyautogui.click(); pyautogui.sleep(2)
    #     experiment_row_number += 1



if __name__ == '__main__':
    experiment_one_row(dx=40, dy=40)
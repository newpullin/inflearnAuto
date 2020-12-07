import time
import pyautogui

MONITOR_WIDTH = 1920
MONITOR_HEIGHT = 1080

X_POS = 1680
Y_POS = 1034
WIDTH = 220
HEIGHT = 4

while True:
    while True:
        time.sleep(1)
        img1 = pyautogui.screenshot(region=(0, 0, MONITOR_WIDTH, MONITOR_HEIGHT))
        all_white = True
        for y_i in range(HEIGHT):
            for x_i in range(WIDTH):
                if img1.getpixel((X_POS + x_i, Y_POS + y_i)) != (255, 255, 255):
                    all_white = False
                    break
            if not all_white:
                break

        # 만약에
        if all_white:
            print("모두 하얀색")
            break

    # 다음 강의를 재생한다.
    time.sleep(1)
    # 전체 화면을 푼다.
    pyautogui.hotkey('esc')
    time.sleep(1)
    # 다음 강의 버튼을 누른다.
    next_lecture_button = pyautogui.locateCenterOnScreen("./img/next_lecture_button.PNG")

    if next_lecture_button is None:
        # 2차 대책 강구 but 지금은 시간이 없음
        break

    pyautogui.click(next_lecture_button)
    time.sleep(2)

    # 강의자료 인지 확인한다.
    # 일단 스킵

    full_screen_button = pyautogui.locateCenterOnScreen("./img/full_screen_button.PNG")

    pyautogui.click(full_screen_button)
    time.sleep(1)



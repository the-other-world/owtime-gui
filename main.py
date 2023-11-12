import tkinter
import owtimes


# Tkinter 主窗口程序
def create_window(tk: tkinter):
    window: tk.Tk = tk.Tk()  # 主对象
    window.title('异世界时钟')  # 窗口标题
    window.geometry('500x325')  # 窗口大小
    window.resizable(0, 0)  # 窗口大小不可变
    window.iconbitmap('favicon.jpg')  # 图像


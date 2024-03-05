from PIL import ImageGrab
from PIL import ImageFilter
import io
import tkinter as tk
from notion import send_notification
import threading

def get_p(beilv=1.0):  # 屏幕放大倍率
    root = tk.Tk()
    wei = root.winfo_screenwidth()
    hig = root.winfo_screenheight()
    root.destroy()
    return (int(wei * beilv), int(hig * beilv))


def screenshot(k,radius=2):
    mypx = get_p(float(1.5))  # 屏幕放大倍率,我的电脑是125%
    img = ImageGrab.grab(bbox=(0, 0, mypx[0], mypx[1]))
    img = img.filter(ImageFilter.GaussianBlur(radius=radius))
    imgbyte = io.BytesIO()
    img.save(imgbyte, format='JPEG')
    # 创建并启动一个新线程来发送通知，并传递 k 参数
    notification_thread = threading.Thread(target=send_notification, args=(k,))
    notification_thread.start()
    return (imgbyte.getvalue())
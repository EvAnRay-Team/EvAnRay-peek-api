from win10toast import ToastNotifier

def send_notification(username:str):
    # 创建 ToastNotifier 对象
    toast = ToastNotifier()

    # 发送通知
    toast.show_toast(title="某人正在观察你", msg=f"来自用户:{username}", duration=3)

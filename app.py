from flask import Flask, send_file, request
import io
import screenshot

from win10toast import ToastNotifier
toast = ToastNotifier()

app = Flask(__name__)




@app.route('/my/screen', methods=["GET"])
def req():
    r = request.args.get("r")
    k = request.args.get("k")
    if (r == None or r == ''):
        r = 3
    else:
        r = float(r)
    

    # toast.show_toast(title="某人正在观察你", msg=f"来自用户:{k}", duration=1)

    return (send_file(
        io.BytesIO(screenshot.screenshot(k,r)),
        # attachment_filename='arcsig by \'sunset',
        mimetype='image/jpg'
    ), 200)



if __name__ == '__main__':
    app.run("0.0.0.0", 1919, debug=False)

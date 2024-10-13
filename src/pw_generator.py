import pyperclip
import PySimpleGUI as sg
from Password import Password

def pw_generator():
    while True:
        password = Password(toggle_u=True, toggle_n=True, toggle_symbol=True, password_length=16)

        result = password.generate()
        print(result)
        pyperclip.copy(result)
        
        yesno = sg.popup_yes_no(
            "以下のパスワードを作成しクリップボードにコピーしました\n" + \
                f"パスワード: {result}\n気に入りましたか？",
                title="作成しました。")
        if yesno == "Yes":
            break
        
        print("パスワードを再作成しましす。")

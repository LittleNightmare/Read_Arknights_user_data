from json import load
from base64 import b64encode
import requests


def _load_file(user_date_file="arknights user data_login.json", check_list_file="item_table.json"):
    try:
        with open(user_date_file, "r", encoding="utf-8") as f:
            user_data = load(f)
    except:
        print("文件读取出错")

    try:
        with open(check_list_file, "r", encoding="utf-8") as f:
            check_list = load(f)
    except:
        url = "https://raw.github.com/Perfare/ArknightsGameData/master/excel/item_table.json"
        r = requests.get(url)
        with open(check_list_file, "wb") as code:
            code.write(r.content)
        with open(check_list_file, "r", encoding="utf-8") as f:
            check_list = load(f)
    return user_data, check_list


def main(user_data, check_list):
    inventory = user_data["user"]["inventory"]
    ArkPlaner = []
    lolicon = {"inputs": {}, "presets": []}
    for check_list_id in check_list["items"]:
        if check_list_id in inventory:
            content = {"name": check_list["items"][check_list_id]["name"], "need": 0, "have": inventory[check_list_id]}
            ArkPlaner.append(content)
            lolicon["inputs"].setdefault(check_list["items"][check_list_id]["name"],
                                         {"need": "", "have": inventory[check_list_id]})

    with open("ArkPlaner.json", "w", encoding="utf-8") as f:
        f.write(str(ArkPlaner).replace("'", '"'))
    bse64 = b64encode(str(lolicon).replace("'", '"').encode("utf-8"))
    with open("lolicon.txt", "w")as f:
        f.write(str(bse64, 'utf-8'))


if __name__ == "__main__":

    user_data, check_list = _load_file()
    main(user_data, check_list)

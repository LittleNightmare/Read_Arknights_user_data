from json import load
from base64 import b64encode, b64decode
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


def input_needs(ArkPlaner="ArkPlaner.json", lolicon="lolicon.txt"):
    try:
        with open(ArkPlaner, "r", encoding="utf-8") as f:
            list_A = load(f)
    except:
        print("cannot load ArkPlaner for input needs")
    try:
        with open(lolicon, "r", encoding="utf-8") as f:
            list_l = eval(b64decode(f.read()).decode("utf-8").replace("true", "True").replace("false", "False"))
    except:
        print("cannot load lolicon for input needs")
    list_ArkPlaner = {}
    for item in list_A:
        item = dict(item)
        list_ArkPlaner.setdefault(item["name"], item["need"])

    return list_ArkPlaner, list_l

def main(user_data, check_list):
    inventory = user_data["user"]["inventory"]
    ArkPlaner = []
    lolicon = {"inputs": {}, "presets": []}
    try:
        ArkPlaner_old, lolicon_old = input_needs()
        lolicon["presets"] = lolicon_old["presets"]
    except:
        ArkPlaner_old = {}
        lolicon_old = {"inputs": {}, "presets": []}
        print("old file does not exit")

    for check_list_id in check_list["items"]:
        if check_list_id in inventory:
            name = check_list["items"][check_list_id]["name"]
            content = {"name": name,
                       "need": ArkPlaner_old.get(check_list["items"][check_list_id]["name"], 0),
                       "have": inventory[check_list_id]}
            ArkPlaner.append(content)
            try:
                needs = lolicon_old["inputs"][name].get("need", '')
            except:
                needs = ""
            lolicon["inputs"].setdefault(name,
                                         {"need": needs,
                                          "have": inventory[check_list_id]})

    with open("ArkPlaner.json", "w", encoding="utf-8") as f:
        f.write(str(ArkPlaner).replace("'", '"'))
    bse64 = b64encode(str(lolicon).replace("'", '"').replace("True", "true").replace("False", "false").encode("utf-8"))
    with open("lolicon.txt", "w")as f:
        f.write(str(bse64, 'utf-8'))


if __name__ == "__main__":
    user_data, check_list = _load_file()
    main(user_data, check_list)

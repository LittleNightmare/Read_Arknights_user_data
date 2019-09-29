from json import load
from base64 import b64encode
import requests

with open("arknights user data_login.json", encoding="utf-8") as f:
    user_data = load(f)
try:
    with open("item_table.json", encoding="utf-8") as f:
        check_list = load(f)
except:
    url = 'https://raw.githubusercontent.com/Perfare/ArknightsGameData/7c8e2fa1032b1a1b36b57aaccdc1fc29495ab133/excel/item_table.json'
    r = requests.get(url)
    with open("item_table.json", "wb") as code:
        code.write(r.content)
        check_list = load(code)

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

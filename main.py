from sources import say
from sources import cred
from sources import exit

import os
import json

os.system("cls" if os.name == "nt" else "clear")

with open("sources/config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

print("welcome to this free open source terminal, cred for credits and help for command list")

if config.get("user") == "user":
    new_user = input("please write a user name: ")
    config["user"] = new_user

    with open("sources/config.json", "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)

while True:
    cmd = input(f"root/{config['user']}: ")

    if cmd.startswith("say"):
        say.use(cmd)

    elif cmd == "cred":
        cred.use()
    elif cmd == "exit":
        exit.use()
    else:
        print(f"'{cmd}' is not a valid command, write 'help' to get a list of commands")
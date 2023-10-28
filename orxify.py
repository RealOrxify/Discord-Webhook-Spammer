import requests
import json
import argparse

def print_purple(text):
    print("\033[95m" + text + "\033[0m")

def print_green(text):
    print("\033[92m" + text + "\033[0m")

print_purple('''
░█████╗░██████╗░██╗░░██╗██╗███████╗██╗░░░██╗  ░██╗░░░░░░░██╗███████╗██████╗░██╗░░██╗░█████╗░░█████╗░██╗░░██╗
██╔══██╗██╔══██╗╚██╗██╔╝██║██╔════╝╚██╗░██╔╝  ░██║░░██╗░░██║██╔════╝██╔══██╗██║░░██║██╔══██╗██╔══██╗██║░██╔╝
██║░░██║██████╔╝░╚███╔╝░██║█████╗░░░╚████╔╝░  ░╚██╗████╗██╔╝█████╗░░██████╦╝███████║██║░░██║██║░░██║█████═╝░
██║░░██║██╔══██╗░██╔██╗░██║██╔══╝░░░░╚██╔╝░░  ░░████╔═████║░██╔══╝░░██╔══██╗██╔══██║██║░░██║██║░░██║██╔═██╗░
╚█████╔╝██║░░██║██╔╝╚██╗██║██║░░░░░░░░██║░░░  ░░╚██╔╝░╚██╔╝░███████╗██████╦╝██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░  ░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝''')

def send_discord_webhook(webhook_url, channel_id, message):
    payload = {
        "content": message
    }
    headers = {
        "Content-Type": "application/json"
    }

    webhook_url = f"{webhook_url}/channels/{channel_id}"

    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)

    if response.status_code == 204:
        print_green("Message sent successfully!")
    else:
        print_green("Failed to send message. Status code:", response.status_code)

def main():
    parser = argparse.ArgumentParser(description='Send a message to a Discord channel using a webhook')
    parser.add_argument('webhook_url', type=str, help='Discord webhook URL')
    parser.add_argument('channel_id', type=str, help='Discord channel ID')
    parser.add_argument('message', type=str, help='Message to send')

    args = parser.parse_args()
    send_discord_webhook(args.webhook_url, args.channel_id, args.message)

if __name__ == "__main__":
    main()

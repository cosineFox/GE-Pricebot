import discord
import requests
import asyncio
from dotenv import load_dotenv
import os
load_dotenv("token.env")

token = os.getenv("token")  # Replace with your Discord bot token
GOOD_ENTRY_COINGECKO_ID = 'good-entry'  # Replace with the CoinGecko ID for Good Entry

intents = discord.Intents.default()
client = discord.Client(intents=intents)

previous_price = None  # To store the previous price for comparison

def get_good_entry_price():
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={GOOD_ENTRY_COINGECKO_ID}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    print(data)
    return data[GOOD_ENTRY_COINGECKO_ID]['usd']

print(get_good_entry_price)

def calculate_percentage_change(old, new):
    try:
        return ((new - old) / old) * 100
    except ZeroDivisionError:
        return 0

# ... (rest of your bot setup code)

@client.event
async def on_ready():
    global previous_price
    print(f'Logged in as {client.user}')
    while True:
        current_price = get_good_entry_price()
        arrow = "↗" if (previous_price is not None and current_price > previous_price) else "↘"
        percentage_change = calculate_percentage_change(previous_price, current_price) if previous_price is not None else 0

        # Bot username format: $Price (Arrow)
        new_username = f'${current_price:.4f} {arrow}'
        
        # Bot status format: Watching 2.5hr: Percentage%
        time_frame = "2.5hr"  # Change this to "7d" if you want to display the change over 7 days
        status_message = f"{time_frame}: {percentage_change:+.2f}%"
        new_status = discord.Activity(type=discord.ActivityType.watching, name=status_message)

        try:
            await client.user.edit(username=new_username)
            await client.change_presence(activity=new_status)
            print(f'Username and status updated: {new_username} | {status_message}')
        except Exception as e:
            print(f'Error updating username or status: {e}')
        
        previous_price = current_price
        await asyncio.sleep(9000)  # Wait for 2.5 hours (9000 seconds)

# ... (rest of your bot code to run and log in)
client.run(token)

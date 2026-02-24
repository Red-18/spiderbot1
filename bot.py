from pyrogram import Client

TOKEN = "8242770626:AAGz6O7Qf-R0dbgGo0TS2OihxLnwuhX5DKA"

app = Client(
    "spiderbot",
    bot_token=TOKEN
)

@app.on_message()
async def start(client, message):
    if message.text == "/start":
        await message.reply("🕷 Spider Bot Running ✅")

print("Bot Running...")
app.run()

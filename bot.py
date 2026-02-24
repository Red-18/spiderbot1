from pyrogram import Client

TOKEN = "8242770626:AAGK8mjSM0cMTBPSAMUnnII6LfPkMMEuBb4"

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

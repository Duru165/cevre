import discord
from discord.ext import commands
import random
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.command(name="neyi geri dönüşüme atmalıyız")
async def neyi geri dönüşüme atmalıyız(ctx):
    ideas = [
        "Eski plastik şişeleri geri dönüşüme atmalıyız.",
        "Karton/kağıtları geri dönüşüme atmalıyız.",
        "Metalleri  geri dönüşüme atmalıyız.",
        "Ahşapları  geri dönüşüme atmalıyız."
    ]
    await ctx.send(f"İşte neyi  geri dönüşüme atmalıyız: {random.choice(ideas)}")

@bot.command(name="sebepler")
async def neyi sebepler(ctx):
    ideas = [
        "Eski plastik şişeler:su kaynaklarını, denizleri ve toprakları ciddi şekilde kirletir.",
        "Kağıtlar:Kağıt üretiminin çevreye en büyük etkileri arasında kullanılan su miktarı ve bu kullanılmak üzere alınan suların yerine atık su bırakımı bulunmaktadır
        "Kartonlar:.",
        "Metalleri  geri dönüşüme atmalıyız.",
        "Ahşapları  geri dönüşüme atmalıyız."
    ]
    await ctx.send(f"İşte neyi  geri dönüşüme atmalıyız: {random.choice(ideas)}")



bot.run("token")

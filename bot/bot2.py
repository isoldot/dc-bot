import random
import discord
from discord.ext import commands
import tm
import os



intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, Matematik işlem botuyum')


@bot.command(name="soru")
async def soru(ctx):

    sayi1 = random.randint(1, 50)
    sayi2 = random.randint(1, 50)
    islem = random.choice(["+", "*","/","-"])
    
    if islem == "+":
        cevap = sayi1 + sayi2
        soru = f"{sayi1} + {sayi2} = ?"
    elif islem == "/":
        cevap = sayi1 / sayi2
        soru = f"{sayi1} / {sayi2} = ?"
    
    elif islem == "-":
        cevap = sayi1 / sayi2
        soru = f"{sayi1} / {sayi2} = ?"
    else:
        cevap = sayi1 * sayi2
        soru = f"{sayi1} * {sayi2} = ?"

    await ctx.send(f"Soru: {soru}")
    tahmin_mesaji = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
    kullanici_tahmini = tahmin_mesaji.content




    if cevap == int(kullanici_tahmini):
        await ctx.send("cevaplarınız doğru")
    
    else:
        await ctx.send(f"cevabın yanlış doğru cevap {cevap}")


@bot.command()
async def resim_attım(ctx):
    if ctx.message.attachments:
        for dosya in ctx.message.attachments:
            await dosya.save(f"./resim/{dosya.filename}")
            await ctx.send("resmin başarıyla kaydedildi.")
            patates,domates = tm.cr7(f"./resim/{dosya.filename}")
            x =  round(domates * 100,1)
            await ctx.send(f"bu bir {patates},%{x} ihtimalle eminim")
            if patates == "Guvercin":
                await ctx.send("Bulgur ve pirinci bolca tüketen güvercinler oldukça sıcakkanlı canlılardır. Güvercinler aynı zamanda çeşitli sebzeleri de beraberinde tüketmektedir. Lahana, bezelye, karnabahar ve marul gibi yiyecekleri dilimleyerek güvercine verebilirsiniz. Dilerseniz petshoplarda yer alan güvercin yemlerini de tercih edebilirsiniz.")
            elif patates == "Serce":
                await ctx.send("Genellikle meyve, tohum, böcek ve larva gibi besinler tüketirler. Göçmen değildirler. Çekirdek ve ekmek artıkları da yerler.")
            elif patates == "karga":
                await ctx.send("Omnivor bir beslenme şekline sahiptirler, hemen hemen her şeyi yerler. Meyve, sebze, tahıl, kuruyemiş, besin çöpleri, leş, her türlü et çeşidi, böcekler, omurgasızlar, tohum, yavru kuşlar, kuş yumurtaları, yavru hayvanlar (kendinden boyut olarak küçük olan, yavru veya sakat olan canlıları avlayıp yerler)")
            elif patates == "Diger":
                await ctx.send("bu bir kuşmu 3 yaşındaki veled kuş atcan kuş bu kuşmu elin mi tutmuyor kuş çok mu zor kullanıcı hatası kuş at.")

            else:
                await ctx.send("afgan bende s yok banane gel bana bilgisayar alda yapayım paramı var.")

            


    else:
        await ctx.send("resim göndermedin (aferin) resim at o koca beynine bunu sok. resim resim o bişey yazdığın barın yanında artı butonu varya (+) bak bu ona bas resim at. veya alt + f4 e bas o daha iyi en iyisi sen program ekle kaldıra gir o ayarlardaki gir ona discord adlı uygulamayı sil git robloxunu oyna .")



bot.run("TOKEN")
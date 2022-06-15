from msilib.schema import Component
import discord, time
import requests
from bs4 import BeautifulSoup as BS
from discord.ext import commands
from discord_components import DiscordComponents, Button,  ButtonStyle

r = requests.get("https://shazoo.ru/tags/419/games")
r2 = requests.get("https://dtf.ru/tag/meme")
title_o = BS(r.content, "html.parser").select(".leading-normal a")[1].text
content_o = content = BS(r2.content, "html.parser").select(".andropov_image")[1]["data-image-src"]
bot = commands.Bot(command_prefix='!', intents = discord.Intents.all())

@bot.event
async def on_ready():
	print("2")
	global title_o, bot, repair
	channels = bot.get_channel(967744315797405706)
	channels2 = bot.get_channel(914473701284659240)
	print("Logged\n{0.user.name}\n{0.user.id}".format(bot))
	DiscordComponents(bot)
	while True:
		#----------parsing----------
		r = requests.get("https://shazoo.ru/tags/419/games")
		title_s = BS(r.content, "html.parser").select(".leading-normal a")[0].text
		content_s = BS(r.content, "html.parser").select(".break-words")[0].text.replace('    ', '', 1).replace("\n", "")
		url_s = BS(r.content, "html.parser").select(".leading-normal a")[0]["href"]
		image_s = BS(r.content, "html.parser").select(".rounded img")[0]["src"]
		if title_o != title_s:
			emb = discord.Embed(
				title = "**" + title_s + "**",
				url = url_s,
				description = "<@&963356054698225674>\n" + "*" + content_s[:len(content_s)-2] + "*",
				color = discord.Color.green()
			)
			emb.set_image(url = image_s)
			emb.set_footer(text = "Новости Уборной", icon_url = "https://cdn.discordapp.com/icons/899157378975555594/ca12802969c637c5453eb7e15dc01d12.webp?size=96")
			component = [
				Button(style = ButtonStyle.URL, label = "Подробнее", url = url_s),
			]
			title_o = title_s
			print(channels)
			await channels.send(embed = emb, components = component)
		time.sleep(300)


bot.run("TOKEN")

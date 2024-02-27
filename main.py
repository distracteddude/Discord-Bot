import discord
from discord.ext import commands
from datetime import datetime
import requests, json


intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix='=', intents=intents)

@bot.event
async def on_read():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_member_join(member):
    welcome_channel = bot.get_channel(YOUR CHANNEL ID)
    if welcome_channel is not None:
        await welcome_channel.send(f'Welcome to the server! <@{member.id}> \n Type =help_me to view possible commands.')

@bot.event
async def on_member_remove(member):
    leave_channel = bot.get_channel(YOUR CHANNEL ID)
    if leave_channel is not None:
        await leave_channel.send(f'Another one bites the dust, <@{member.id}> left the server.')

@bot.command()
async def time(ctx):
    "Shows the time"
    c = datetime.now()
    current_time = c.strftime('%H:%M')
    await ctx.send(f'Current time is: {current_time}')


@bot.command()
async def date(ctx):
    "Shows the date and time."
    c = datetime.now()
    await ctx.send(f'Current date and time is: {c}')

@bot.command()
async def weather(ctx, city):
    "Shows the weather of any city. (command format: =weather {city name})"

    api_key = "YOUR API KEY"
    
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    city_name = city
    
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    response = requests.get(complete_url)

    x = response.json()


    if x["cod"] != "404":
 
        y = x["main"]
    
        current_temperature = y["temp"]
    
        current_pressure = y["pressure"]
    
        current_humidity = y["humidity"]
    
        z = x["weather"]
    
        weather_description = z[0]["description"]
    
        await ctx.send(f" Temperature (in Celcius unit) = {round(current_temperature - 273.15, 2)}\n atmospheric pressure (in hPa unit) =  {current_pressure} \n humidity (in percentage) =   {current_humidity} \n description =  {weather_description}")

    else:
        await ctx.send(" City Not Found ")


@bot.command()
async def news(ctx, country):
    "Shows the trending news of the country. (command format: =news {country name})"
    
    api_key = 'YOUR API KEY'
    
    base_url = ('https://newsapi.org/v2/top-headlines?')

    country_name = country

    complete_url = (f'{base_url}' + ('country=' + country_name) + '&' + "apiKey=" + api_key)

    response = requests.get(complete_url)
    
    data = response.json()
    y = data["articles"]

    for article in y:

        author_name = article['author']
        title = article['title']
        description = article['description']
        news_url = article['url']

    await ctx.send(f"Author: {author_name} \nTitle: {title}\nDescription: {description}\noriginal url: {news_url}")

@bot.command()
async def apod(ctx):
    "APOD stands for Astronomy Picture Of the Day"

    api_key = "YOUR API KEY"

    url = "https://api.nasa.gov/planetary/apod?api_key=" + api_key

    response = requests.get(url)

    x = response.json()

    title = x['title']
    
    image_link = x['url']

    await ctx.send(f"Title: {title}\n\n{image_link}")



@bot.command
async def age(ctx, name):
    "Predicts the age of the person by their name. (command format: =age {name})"

    base_url = 'https://api.agify.io/'

    full_url = base_url + '?name=' + name 

    response = requests.get(full_url)

    x = response.json()


    # print(response.json())


    await ctx.send(f"Name: {x['name']}\nEstimate age: {x['age']}")



@bot.command()
async def help_me(ctx):
    "Shows the available commands"
    help_text = 'Available commands: \n\n'

    for command in bot.commands:
        help_text += f"{command.name}: {command.help}\n"

    await ctx.send(help_text)


bot.run('YOUR BOT TOKEN')



from discord_webhook import DiscordWebhook, DiscordEmbed
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime, timedelta
import time


def get_weather_message():
    api_key = "b660f3402c54cb9a9c48f89c35249e5c"
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + "Vancouver" + "&units=metric&appid=" + api_key

    response = requests.get(url, auth=HTTPBasicAuth("test", "test"))
    text = response.json()

    current_temp = text['main']['temp']
    weather = text["weather"][0]['description']

    return f"""
    Good afternoon Master!

    Today's weather is {text['weather'][0]['description']}.
    It's {current_temp}°C outside. {"Please don't catch a cold!" if current_temp < 15 else "Enjoy your day today!"}
    """


def execute_webhook(title, text):
    webhook = DiscordWebhook(
        url='https://discord.com/api/webhooks/961374708580888648/nr2K0J8di0AyLwjOwc5FWfbBMAflTcdyn0jv01WN4T-10-XyaQctlG10NoVkhP7BQtnQ')
    embed = DiscordEmbed(title=title, description=text, color='03b2f8')
    # set image
    embed.set_image(url='https://i1.sndcdn.com/artworks-QFkmqGDwkcuZXoEE-P5Dw5g-t500x500.jpg')
    # embed.set_thumbnail(url='https://thicc.mywaifulist.moe/waifus/38792/72ad423ac8014520bbc9e7f4c21528e9790fc40fa6986a498de3b2bbde312bcd_thumb.jpg')
    # set timestamp (default is now)
    embed.set_timestamp()
    # add embed object to webhook
    webhook.add_embed(embed)
    response = webhook.execute()


def main():
    while True:
        message = get_weather_message()
        title = "Weather Info"
        execute_webhook(title, message)
        dt = datetime.now() + timedelta(minutes=60)
        while datetime.now() < dt:
            time.sleep(1)


if __name__ == '__main__':
    main()

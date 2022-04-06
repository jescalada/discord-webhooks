from discord_webhook import DiscordWebhook, DiscordEmbed
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime, timedelta
import time


def get_weather(api_key: str) -> dict:
    """
    Gets the current weather from openweathermap using an API key.

    :param api_key: The API key
    :return: a json containing the data
    """
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + "Vancouver" + "&units=metric&appid=" + api_key
    response = requests.get(url, auth=HTTPBasicAuth("test", "test"))
    json = response.json()
    return json


def generate_weather_message(json: dict) -> str:
    """
    Generates a custom message from a json containing weather data.

    :return: a string with a custom message
    """

    current_temp = json['main']['temp']
    weather = json["weather"][0]['description']

    return f"""
    Good afternoon Master!

    Today's weather is {json['weather'][0]['description']}.
    It's {current_temp}°C outside. {"Please don't catch a cold!" if current_temp < 15 else "Enjoy your day today!"}
    """


def execute_webhook(webhook_url, thumbnail, title, text):
    """
    Sends a message through Discord using a webhook.

    :param webhook_url: the URL of the webhook
    :param thumbnail: the thumbnail for the message
    :param title: the title of the message
    :param text: the content of the message
    """
    webhook = DiscordWebhook(url=webhook_url)
    embed = DiscordEmbed(title=title, description=text, color='03b2f8')

    # set image
    embed.set_thumbnail(url=thumbnail)

    # set timestamp (default is now)
    embed.set_timestamp()

    # add embed object to webhook
    webhook.add_embed(embed)
    response = webhook.execute()


def main():
    """
    Runs a program that sends hourly messages through Discord containing weather info.

    Sends a message every hour with a customized message containing current weather info obtained through an API.
    """
    while True:
        api_key = "b660f3402c54cb9a9c48f89c35249e5c"
        title = "Weather Info"
        webhook_url = 'https://discord.com/api/webhooks/961374708580888648/' \
                      'nr2K0J8di0AyLwjOwc5FWfbBMAflTcdyn0jv01WN4T-10-XyaQctlG10NoVkhP7BQtnQ'
        suguri_thumb = 'https://thicc.mywaifulist.moe/waifus/38792/' \
                       '72ad423ac8014520bbc9e7f4c21528e9790fc40fa6986a498de3b2bbde312bcd_thumb.jpg'
        data = get_weather(api_key)
        message = generate_weather_message(data)
        execute_webhook(webhook_url=webhook_url, thumbnail=suguri_thumb, title=title, text=message)
        dt = datetime.now() + timedelta(minutes=60)
        while datetime.now() < dt:
            time.sleep(1)


if __name__ == '__main__':
    main()

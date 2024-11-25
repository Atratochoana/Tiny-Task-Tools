from dotenv import dotenv_values
from discord_webhook import DiscordWebhook, DiscordEmbed
import json

config = dotenv_values(".env")

webhook = DiscordWebhook(url=config["WEBHOOK"])

embed = DiscordEmbed(title="**Macro Status**", description='- Times run: `0` - Times failed: `0` - Times remaing: `0`', color="03b2f8")


webhook.add_embed(embed)
response = webhook.execute()

print(json.loads(response.content.decode())["webhook_id"])


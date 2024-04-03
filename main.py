from discord import ApplicationContext, Intents
import os
from client import LunaClient
from models.base import Base
from models.guild import Guild
from models.user import User

intents = Intents()
intents.members = True
intents.guilds = True

client = LunaClient(intents=intents)


@client.event
async def on_ready():
    print(f"{client.user.name} has logged in.")


@client.slash_command(guild_ids=[957867801119449109])
async def hello(ctx: ApplicationContext):
    await ctx.respond(f"Hello {ctx.author.name}")


for cog in filter(lambda cog: cog.endswith(".py"), os.listdir("./cogs")):
    client.load_extension(f"cogs.{cog[:-3]}")
    print(f"Loaded cog.{cog[:-3]}")


tables = [Guild.__table__, User.__table__]

Base.metadata.create_all(bind=client.engine, tables=tables)

client.run(client.settings["token"])

import os

import discord
from discord.app import Option
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ['DISCORD_TOKEN']

bot = discord.Bot()

@bot.slash_command(guild_ids=[810813680618831902])
async def hello(ctx):
    """Say hello to the bot"""  # the command description can be supplied as the docstring
    await ctx.send(f"Hello {ctx.author}!")


@bot.slash_command(
    name="hi", description="Wish someone!"
)  # Not passing in guild_ids creates a global slash command (might take an hour to register)
async def global_command(ctx, num: int):  # Takes one integer parameter
    await ctx.send(f"This is a global command, {num}!")


@bot.slash_command(guild_ids=[810813680618831902])
async def joined(
    ctx, member: discord.Member = None
):  # Passing a default value makes the argument optional
    user = member or ctx.author
    await ctx.send(f"{user.name} joined at {discord.utils.format_dt(user.joined_at)}")
    
    
choose = bot.command_group(
    name='choose', description='This is a slash command group!', guild_ids=[...])

@choose.command(name='member')
async def choose_a_user(ctx,
    user: Option(discord.Member, "Choose a member", required=False), #required is True by default
):
    await ctx.send(f"You chose {user}!")

bot.run(TOKEN)
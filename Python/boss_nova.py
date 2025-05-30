"""
Discord bot that plays an audio file (specify path on line 33) in a voice channel when a user enters, and leaves when the channel is empty.

Set the environment variable DISCORD_TOKEN with your bot token with the following command in PowerShell:
[System.Environment]::SetEnvironmentVariable("DISCORD_TOKEN", "your_token_here", "User")

Set the environment variables GUILD_ID and VOICE_CHANNEL_ID variables to your server and voice channel IDs respectively with the following commands in PowerShell:
[System.Environment]::SetEnvironmentVariable("GUILD_ID", "your_server-id_here", "User")
[System.Environment]::SetEnvironmentVariable("VOICE_CHANNEL_ID", "your_voice-channel-id_here", "User")
Restart your shell

Tests:
[System.Environment]::GetEnvironmentVariable("DISCORD_TOKEN", "User")
[System.Environment]::GetEnvironmentVariable("GUILD_ID", "User")
[System.Environment]::GetEnvironmentVariable("VOICE_CHANNEL_ID", "User")

"""

import discord
from discord.ext import commands
import os


TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise ValueError("Please set the DISCORD_TOKEN environment variable with your bot token.")
GUILD_ID = int(os.getenv("GUILD_ID"))
if not GUILD_ID:
    raise ValueError("Please set the GUILD_ID environment variable with your server ID.")
VOICE_CHANNEL_ID = int(os.getenv("VOICE_CHANNEL_ID"))
if not VOICE_CHANNEL_ID:
    raise ValueError("Please set the VOICE_CHANNEL_ID environment variable with your voice channel ID.")
AUDIO_FILE = os.path.abspath(r"D:\Musique\Albums - Mix\Sol_De_Bossa.mp3") # replace with the path to your audio file

intents = discord.Intents.default()
intents.voice_states = True
intents.guilds = True
bot = commands.Bot(command_prefix="!", intents=intents)

def is_channel_empty(channel, bot_id):
    # Returns True if only the bot (or nobody) is in the channel
    for member in channel.members:
        if not member.bot and member.id != bot_id:
            return False
    return True

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} ({bot.user.id})")

@bot.event
async def on_voice_state_update(member, before, after):
    # Only care about the target voice channel
    if before.channel == after.channel:
        return

    guild = bot.get_guild(GUILD_ID)
    voice_channel = guild.get_channel(VOICE_CHANNEL_ID)
    bot_member = guild.get_member(bot.user.id)

    # User joins the target channel
    if after.channel and after.channel.id == VOICE_CHANNEL_ID:
        # If bot is not already in the channel, and the joining member is not the bot
        if not bot_member.voice or bot_member.voice.channel != voice_channel:
            # Only join if there is at least one non-bot user in the channel
            non_bot_members = [m for m in voice_channel.members if not m.bot]
            if non_bot_members:
                voice_client = await voice_channel.connect()
                def play_loop(error=None):
                    if error:
                        print(f"Error during playback: {error}")
                    if voice_client.is_connected():
                        voice_client.play(
                            discord.FFmpegPCMAudio(AUDIO_FILE),
                            after=play_loop
                        )
                play_loop()
                print(f"Bot joined and started playing in {voice_channel.name}")

    # User leaves the target channel
    if before.channel and before.channel.id == VOICE_CHANNEL_ID:
        # If bot is in the channel, check if it's now empty (no non-bot users)
        if bot_member.voice and bot_member.voice.channel == voice_channel:
            non_bot_members = [m for m in voice_channel.members if not m.bot]
            if not non_bot_members:
                if voice_channel.permissions_for(bot_member).move_members:
                    await bot_member.move_to(None) # Move bot out of the channel
                    print("Bot left the voice channel because it became empty.")

    # Bot checks if it is alone in the channel
    if bot_member.voice and bot_member.voice.channel == voice_channel:
        if is_channel_empty(voice_channel, bot.user.id):
            await bot_member.move_to(None)

@bot.event
async def on_error(event, *args, **kwargs):
    print(f"An error occurred in event {event}: {args}, {kwargs}")

bot.run(TOKEN)
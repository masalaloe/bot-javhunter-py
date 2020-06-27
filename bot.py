import discord

from discord.ext import commands as c


bot = c.Bot(command_prefix='.',description='Bot Discord')
TOKEN ='NDc5OTM4Njg3MzYzMzE3Nzcy.XvC7nQ.0STcDJvLsnuEn1LAo1bofNUvz0o'

@bot.event
async def on_ready():
    """http://discordpy.readthedocs.io/en/rewrite/api.html#discord.on_ready"""

    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}')
    print('------')
    print(discord.utils.oauth_url(bot.user.id))

    # Changes our bots Playing Status. type=1(streaming) for a standard game you could remove type and url.
    await bot.change_presence(activity=discord.Streaming(platform='Yutub',game='tes',name=f'ketik {bot.command_prefix}javhunter', type=1, url='https://github.com/masalaloe'))
    print(f'\nSuccessfully logged in and booted...!')
   

### Command oad and Unload Cogs ####   
@bot.command(
    name= 'load',
    aliases= ['l'],
    description= 'load module',
    usage= '<module_name>'
)
async def _load(ctx, extension):
    try:
        bot.load_extension(f'Cogs.{extension}')
        await ctx.send(f'Cogs.{extension} has been loaded.')
    except Exception as e:
        await ctx.send(f'Error : {e}')

@bot.command(
    name= 'unload',
    aliases= ['ul'],
    description= 'Unload module',
    usage= '<module_name>'
)
async def _unload(ctx, extension):
    try:
        bot.unload_extension(f'Cogs.{extension}')
        await ctx.send(f'Cogs.{extension} has been unloaded.')
    except Exception as e:
        await ctx.send(f'Error : {e}')
###############################################

if __name__ == "__main__":
    for filename in os.listdir('./Cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'Cogs.{filename[:-3]}')

bot.run(TOKEN, bot=True, reconnect=True)
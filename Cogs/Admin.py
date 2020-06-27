import discord
import os

from discord.ext import commands as c

class Admin(c.Cog):
    def __init__(self, bot):
        self.bot = bot

    @c.Cog.listener()
    async def on_ready(self):
        print('Cog.Admin is Loaded.')

    @c.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(f'Admin : {error}')
        
    """
        Commands
    """
    @c.command(
        name= 'reload',
        aliases= ['rl'],
        description= 'reload module',
        usage= '<module_name>'
    )
    async def _reload(self, ctx, extension): 
        try:
            self.bot.unload_extension(f'Cogs.{extension}')
            self.bot.load_extension(f'Cogs.{extension}')
            await ctx.send(f'Cogs.{extension} has been reloaded.')
        except Exception as e:
            await ctx.send(f'Error : {e}')

    @c.command(
        name= 'reloadall',
        aliases= ['rla'],
        description= 'Reload all module'
    )
    @c.has_permissions(administrator= True)
    async def _reloadall(self, ctx):
        """Instant reload all extension"""
        try:
            for filename in os.listdir('./Cogs'):
                if filename.endswith('.py'):
                    self.bot.unload_extension(f'Cogs.{filename[:-3]}')
                    self.bot.load_extension(f'Cogs.{filename[:-3]}')
            await ctx.send('All cogs module has been reloaded')
        except Exception as e:
            await ctx.send(f'Eror : {e}')
        
    @c.command(
        name= 'shutdown',
        aliases= ['sh'],
        description= 'Use it wisely'
    )
    @c.has_permissions(administrator= True)
    async def _shutdown(self, ctx):
        """Shutdown the bot"""
        await ctx.send("Aku pergi dulu....")
        await self.bot.logout()


def setup(bot):
    bot.add_cog(Admin(bot))

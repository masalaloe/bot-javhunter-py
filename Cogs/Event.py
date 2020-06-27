import discord

from discord.ext import commands as c

class Event(c.Cog):
    def __init__(self, bot):
        self.bot = bot

    @c.Cog.listener()
    async def on_ready(self):
        print('Cog.Event is Loaded.')

    @c.Cog.listener()
    async def on_member_join(self, member : discord.Member):
        channel = discord.utils.get(member.guild.text_channels, name='raw')
        if channel :
            await channel.send(f'Welcome {member.mention}')
            print(f'{member.name} is joined {member.guild.name}')
        
    @c.Cog.listener()
    async def on_member_remove(self,member : discord.Member):
        channel = discord.utils.get(member.guild.text_channels, name='raw')
        if channel :
            await channel.send(f'See you {member.mention}')
            print(f'{member.name} is leaving {member.guild.name}')

    @c.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(f'Event : {error}')
        ignoredCommand = (c.CommandNotFound, c.UserInputError)

        if isinstance(error, ignoredCommand):
            return
        
        if isinstance(error, c.CheckFailure):
            await ctx.send('You dont have have Permission Role to use this Command!')


def setup(bot):
    bot.add_cog(Event(bot))

import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '.')
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('as the imposter'))
    print('Bot is Ready.')

#Help Command
@client.command()
async def help(ctx):
    author = ctx.message.author
    
    embed = discord.Embed(
        description = 'This is a helper bot, use the commands as you please!',
        colour = discord.Colour.orange()
    )

    embed
    embed.set_author(name="Help")
    embed.add_field(name ='.ping', value='Returns Latency in ms', inline= False)
    embed.add_field(name ='.eightball', value='The Bot will bestow some wisdom', inline= False)
    embed.add_field(name ='.timetable <insert day>', value='Shows the timetable for the current semester', inline= False)
    embed.add_field(name ='.developer', value='Developer Credits', inline= False)
    
    # DM the user the help embed
    await ctx.author.send(author, embed=embed)

    # Send confirmation message in chat
    await ctx.send('You have been DMd the command list!')

# Ping Command
@client.command()
async def ping(ctx):
    await ctx.send(f'Latency = {round(client.latency * 1000)}ms')

# Clear Command
@client.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

# Fortune Command
@client.command()
async def eightball(ctx, *, question):
    responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."]
    await ctx.send(f'Question: {question} \nAnswer : {random.choice(responses)}')

# Sends a copy of the timetable for Semester 1
@client.command()
async def timetable(ctx, arg=None):
    if arg == None:
        await ctx.channel.send("Please enter the day you wish to check with .Timetable <Day>\nOr alternatively use  <Week> to view the entire timetable")
    if arg == 'monday':
        embed = discord.Embed(colour=discord.Colour.red())
        embed.set_author(name="Monday")
        embed.add_field(name="11:00 - 12:00", value="[5108COMP 3D Computer Graphics](https://canvas.ljmu.ac.uk/courses/43947)", inline=True)
        embed.add_field(name="12:00 - 14:00", value="[5108COMP 3D Computer Graphics](https://canvas.ljmu.ac.uk/courses/43947)", inline=False)
        await ctx.channel.send(embed=embed)
    if arg == 'tuesday':
        embed=discord.Embed(colour=discord.Colour.red())
        embed.set_author(name="Tuesday")
        embed.add_field(name="10:30 - 12:30", value="[5107COMP Data Structures and Algorithms for Games](https://canvas.ljmu.ac.uk/courses/51748)", inline=True)
        embed.add_field(name="14:00 - 15:00", value="[5109COMP Digital Games Content Production](https://canvas.ljmu.ac.uk/courses/43948)", inline=False)
        await ctx.channel.send(embed=embed)
    if arg == 'wednesday':
        embed=discord.Embed(colour=discord.Colour.red())
        embed.set_author(name="Wednesday")
        embed.add_field(name="11:00 - 12:00", value="[5108COMP 3D Computer Graphics](https://canvas.ljmu.ac.uk/courses/43947)", inline=True)
        embed.add_field(name="12:00 - 13:00", value="[5108COMP 3D Computer Graphics](https://canvas.ljmu.ac.uk/courses/43947)", inline=False)
        await ctx.channel.send(embed=embed)
    if arg == 'thursday':
        await ctx.channel.send("https://tenor.com/view/sponge-bob-square-pants-patrick-to-do-list-nothing-gif-5517808")
    if arg == 'friday':
        embed=discord.Embed(colour=discord.Colour.red())
        embed.set_author(name="Friday")
        embed.add_field(name="10:00 - 11:00", value="[5107COMP Data Structures and Algorithms for Games](https://canvas.ljmu.ac.uk/courses/51748)", inline=True)
        embed.add_field(name="12:00 - 14:00", value="[5109COMP Digital Games Content Production](https://canvas.ljmu.ac.uk/courses/43948)", inline=False)
        await ctx.channel.send(embed=embed)
    if arg == 'week':
        await ctx.channel.send("https://media.discordapp.net/attachments/760832939369431040/760834373267882035/unknown.png?width=959&height=515")

# DM's User the Dev Credits
@client.command()
async def developer(ctx):
    await ctx.author.send('This bot was developed by Ben Powell (2020)')


client.run('TOKEN REMOVED FOR SECURITY REASONS')
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='.', description='Game bot made by pizza')

print(discord.__version__)

token = "goGen3RaTeYourOwNTokenThisoneWontWOrk"

@bot.event
async def on_ready():
    print('Started the bot without problems')

@bot.command(pass_context=True)
async def staff(ctx):
    msg = ctx.message

    mydict = dict()
    for member in msg.server.members:
        for role in member.roles:
            if role.permissions.manage_roles == True and member.bot == False:

                try:
                    mydict[role.name]["roleMember"].append(member.name + "#" + member.discriminator)
                except:
                    mydict[role.name] = dict(roleMember=[member.name + "#" + member.discriminator],
                                             rankColor=role.colour)

    for roles in mydict:
        rankMem = ""
        for members in mydict[roles]["roleMember"]:
            rankMem += members + "\r\n"

        embed = discord.Embed(color=mydict[roles]["rankColor"])
        embed.add_field(name=roles, value=rankMem[0:len(rankMem) - 2])
        await bot.say(embed=embed)


bot.run(token)

# capture discord_id to validate
@bot.command(pass_context=True)
async def example(ctx):
    get_discord_id = ctx.message.author.id
    user = await bot.get_user_info(get_discord_id)
    print(get_discord_id)

# get username and unique ID from discord user that uses the command
@bot.command(pass_context=True)
async def getinfo(ctx, vote):
        getMemberID = ctx.message.author.id
        getMemberName = ctx.message.author.name

        print (getMemberID)
        print (getMemberName)

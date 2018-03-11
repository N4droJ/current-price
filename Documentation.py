# capture discord_id to validate
@bot.command(pass_context=True)
async def example(ctx):
    get_discord_id = ctx.message.author.id
    user = await bot.get_user_info(get_discord_id)
    print(get_discord_id)

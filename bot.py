import discord

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hola'):
        await message.channel.send('Wena como andamos')

    if message.content.startswith('$moto alert'):
        paf_path = ("./src/moto.png")
        with open(paf_path, 'rb') as image_file:
            await message.channel.send(file=discord.File(image_file))

@client.event
async def on_voice_state_update(member, before, after):
    text_channel = client.get_channel(591403148502106204)

    if before.channel is None and after.channel is not None:
        print(f'{member.name} se unió al canal')
        await text_channel.send(f'{member.name} entro al concejo de sabios')
    # Enviar un mensaje al canal de texto

    elif before.channel is not None and after.channel is None:
        await text_channel.send(f'{member.name} amanerao se fue')


client.run('MTE4NTMwOTUyODMyMTk0OTc0Ng.G94OSs.NSuH87ZvWV8jkpyXLv0nbKXgbN0R88L7VdNEV8')

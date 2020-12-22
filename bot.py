# coding: utf-8
import discord
import bot_id as id
import numpy as np
from parse import parse

client = discord.Client()

@client.event
async def on_message(message):
    if message.author.bot:
        return
    else: #入力に対する反応はここへ(関数は外へ)
        try:

            info = parse('/{}d{}', message.content)

            if info:
                dice_num = int(info[0])
                dice_size = int(info[1])
                m = SimpleDice(dice_num, dice_size)
                await message.channel.send(m)

        except ValueError:
            await message.channel.send('コマンドを見直してね')


#関数はここ

def dice(size):
    num = np.random.randint(1, int(size+1))
    return num

def SimpleDice(num,size):
    result = 0
    list = []
    for i in range(num):
        random = dice(size)
        result = result + random
        list.append(random)
    m = 'dice: ' + str(num) +'d' + str(size) + ' = ' + str(result) + ' ' + str(list)
    return m

client.run(id.token)
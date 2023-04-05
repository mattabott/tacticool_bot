import os
from datetime import datetime
from datetime import datetime

import discord
from discord.ext import commands
from discord.utils import get
from discord.ui import Button, View

from dotenv import load_dotenv

from missions import operators, check_miss, create_custom_sized_pdf

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape
from reportlab.lib.units import mm
from pdf2image import convert_from_path

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

#Posizionamento missioni
@bot.command()
#@commands.has_any_role('DISCORD MOD', 'Dio', 'MANAGEMENT ENG', 'MANAGEMENT ITA')
async def miss(ctx):

    mission_list = []

    await ctx.message.delete()

    mission_names = [
        'Basic Mission', 'Bayonet', 'Breach', 'BSS', 'Cleanup', 'Common Only',
        'Cover', 'Hammer', 'HILDR', 'Knife', 'Locals', 'Logistics',
        'Rare Only', 'Recon', 'Showdown', 'Uncommon Only'
    ]

    def create_mission_button(label):
        return Button(label=label, custom_id=label, style=discord.ButtonStyle.green)
    
    mission_buttons = [create_mission_button(name) for name in mission_names]

    async def mission_callback(interaction):
        mission_list.append(interaction.data["custom_id"])
        await interaction.response.defer()

    for button in mission_buttons:
        button.callback = mission_callback

    confirm = Button(label='confirm', style=discord.ButtonStyle.red)

    async def confirm_callback(interaction):
        pdf_list = []
        date_now = datetime.now()
        data_format = date_now.strftime('%d-%m-%Y')
        pdf_list.append(data_format)
        pdf_list.append('')

        await interaction.response.edit_message(view=None)#content='Missions: \n'

        missioni_migliori = check_miss(operators, mission_list)
        new_dict = {}

        for key, value in missioni_migliori.items():
            if value in new_dict:
                new_dict[value].append(key)
            else:
                new_dict[value] = [key]

        for i, key in enumerate(mission_list):
            if key in new_dict:
               
                pdf_list.append(f'Mission {i + 1} {mission_list[i]} --> {", ".join(new_dict[key])}')
            else:
                
                pdf_list.append(f'Mission {i + 1} {mission_list[i]} -->')

        pdf_list.append('-----------------------')
        pdf_list.append('Operator Repositioning')

        check_dict = {}
        for i in range(len(mission_list)):
            miss_list = []
            op_list = []
            tmp_dict = check_miss(operators, mission_list[i:])

            for key in tmp_dict:
                if key in check_dict:
                    if tmp_dict[key] == check_dict[key]:
                        continue
                    else:
                        miss_list.append(tmp_dict[key])
                        op_list.append(key)
            check_dict = tmp_dict

            # unisco le due liste in un dizionario
            no_miss_dict = dict(zip(op_list, miss_list))

            result = ""
            for value in set(no_miss_dict.values()):
                keys = [k for k, v in no_miss_dict.items() if v == value]
                if len(keys) > 1:
                    result += ", ".join(keys) + " ({})".format(value) + ", "
                else:
                    result += keys[0] + " ({})".format(value) + ", "

            if i == 0:
                continue
            else:
                pdf_list.append(f'After mission {i} --> {result[:-2]}') 

    
        file_name = "missions.pdf"
        #print(pdf_list)
        create_custom_sized_pdf(file_name, pdf_list)
        images = convert_from_path(file_name)
        image_path = 'missions.png'
        images[0].save(image_path, "PNG")

        await ctx.send("Missions:", file=discord.File(image_path))

    confirm.callback = confirm_callback

    view = View()
    for button in mission_buttons:
        view.add_item(button)
    view.add_item(confirm)

    await ctx.send('Choose missions', view=view)

bot.run(TOKEN)
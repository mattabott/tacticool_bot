from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

operators = [
    #comuni
    {'nome_operatore': 'Rookie', 'Basic Mission': 80, 'Bayonet': 35, 'Breach': 55, 'BSS': 50, 'Cleanup': 55, 'Common Only': 120, 'Cover': 55, 'Hammer': 50, 'HILDR': 50, 'Knife': 45, 'Locals': 50, 'Logistics': 55, 'Rare Only': 30, 'Recon': 55, 'Showdown': 55, 'Uncommon Only': 30},
    {'nome_operatore': 'Hawk', 'Basic Mission': 100, 'Bayonet': 40, 'Breach': 70, 'BSS': 60, 'Cleanup': 70, 'Common Only': 150, 'Cover': 70, 'Hammer': 60, 'HILDR': 60, 'Knife': 55, 'Locals': 140, 'Logistics': 70, 'Rare Only': 40, 'Recon': 150, 'Showdown': 70, 'Uncommon Only': 40},
    {'nome_operatore': 'Jason', 'Basic Mission': 100, 'Bayonet': 150, 'Breach': 70, 'BSS': 160, 'Cleanup': 70, 'Common Only': 150, 'Cover': 70, 'Hammer': 60, 'HILDR': 60, 'Knife': 55, 'Locals': 60, 'Logistics': 150, 'Rare Only': 40, 'Recon': 70, 'Showdown': 70, 'Uncommon Only': 40},
    {'nome_operatore': 'Boris', 'Basic Mission': 100, 'Bayonet': 150, 'Breach': 150, 'BSS': 60, 'Cleanup': 70, 'Common Only': 150, 'Cover': 70, 'Hammer': 190, 'HILDR': 60, 'Knife': 55, 'Locals': 60, 'Logistics': 70, 'Rare Only': 40, 'Recon': 70, 'Showdown': 70, 'Uncommon Only': 40},
    {'nome_operatore': 'Thor', 'Basic Mission': 100, 'Bayonet': 150, 'Breach': 70, 'BSS': 60, 'Cleanup': 150, 'Common Only': 150, 'Cover': 70, 'Hammer': 60, 'HILDR': 300, 'Knife': 55, 'Locals': 60, 'Logistics': 70, 'Rare Only': 40, 'Recon': 70, 'Showdown': 70, 'Uncommon Only': 40},
    {'nome_operatore': 'Rick', 'Basic Mission': 100, 'Bayonet': 150, 'Breach': 70, 'BSS': 60, 'Cleanup': 70, 'Common Only': 150, 'Cover': 150, 'Hammer': 190, 'HILDR': 60, 'Knife': 55, 'Locals': 60, 'Logistics': 70, 'Rare Only': 40, 'Recon': 70, 'Showdown': 70, 'Uncommon Only': 40},
    {'nome_operatore': 'Mishka', 'Basic Mission': 100, 'Bayonet': 40, 'Breach': 70, 'BSS': 50, 'Cleanup': 70, 'Common Only': 150, 'Cover': 70, 'Hammer': 190, 'HILDR': 60, 'Knife': 55, 'Locals': 140, 'Logistics': 70, 'Rare Only': 40, 'Recon': 70, 'Showdown': 150, 'Uncommon Only': 40},
    #non comuni
    {'nome_operatore': 'Klaus', 'Basic Mission': 120, 'Bayonet': 155, 'Breach': 85, 'BSS': 70, 'Cleanup': 85, 'Common Only': 50, 'Cover': 85, 'Hammer': 240, 'HILDR': 70, 'Knife': 65, 'Locals': 70, 'Logistics': 85, 'Rare Only': 50, 'Recon': 180, 'Showdown': 85, 'Uncommon Only': 180},
    {'nome_operatore': 'Shi', 'Basic Mission': 120, 'Bayonet': 155, 'Breach': 85, 'BSS': 70, 'Cleanup': 85, 'Common Only': 50, 'Cover': 85, 'Hammer': 70, 'HILDR': 70, 'Knife': 240, 'Locals': 70, 'Logistics': 180, 'Rare Only': 50, 'Recon': 85, 'Showdown': 85, 'Uncommon Only': 180},
    {'nome_operatore': 'Victor', 'Basic Mission': 120, 'Bayonet': 155, 'Breach': 180, 'BSS': 70, 'Cleanup': 85, 'Common Only': 50, 'Cover': 85, 'Hammer': 70, 'HILDR': 70, 'Knife': 240, 'Locals': 70, 'Logistics': 85, 'Rare Only': 50, 'Recon': 85, 'Showdown': 85, 'Uncommon Only': 180},
    {'nome_operatore': 'Spencer', 'Basic Mission': 120, 'Bayonet': 155, 'Breach': 85, 'BSS': 190, 'Cleanup': 180, 'Common Only': 50, 'Cover': 85, 'Hammer': 70, 'HILDR': 70, 'Knife': 65, 'Locals': 70, 'Logistics': 85, 'Rare Only': 50, 'Recon': 85, 'Showdown': 85, 'Uncommon Only': 180},
    {'nome_operatore': 'Travis', 'Basic Mission': 120, 'Bayonet': 155, 'Breach': 85, 'BSS': 70, 'Cleanup': 85, 'Common Only': 50, 'Cover': 180, 'Hammer': 70, 'HILDR': 70, 'Knife': 240, 'Locals': 70, 'Logistics': 85, 'Rare Only': 50, 'Recon': 85, 'Showdown': 85, 'Uncommon Only': 180},
    {'nome_operatore': 'Batya', 'Basic Mission': 120, 'Bayonet': 50, 'Breach': 85, 'BSS': 70, 'Cleanup': 85, 'Common Only': 50, 'Cover': 85, 'Hammer': 240, 'HILDR': 70, 'Knife': 60, 'Locals': 170, 'Logistics': 85, 'Rare Only': 50, 'Recon': 85, 'Showdown': 180, 'Uncommon Only': 180},
    #rari
    {'nome_operatore': 'Varg', 'Basic Mission': 160, 'Bayonet': 65, 'Breach': 155, 'BSS': 80, 'Cleanup': 115, 'Common Only': 65, 'Cover': 115, 'Hammer': 95, 'HILDR': 480, 'Knife': 90, 'Locals': 95, 'Logistics': 115, 'Rare Only': 240, 'Recon': 240, 'Showdown': 115, 'Uncommon Only': 65},
    {'nome_operatore': 'David', 'Basic Mission': 160, 'Bayonet': 210, 'Breach': 115, 'BSS': 255, 'Cleanup': 115, 'Common Only': 65, 'Cover': 115, 'Hammer': 95, 'HILDR': 100, 'Knife': 90, 'Locals': 95, 'Logistics': 240, 'Rare Only': 240, 'Recon': 115, 'Showdown': 115, 'Uncommon Only': 65},
    {'nome_operatore': 'Syndrome', 'Basic Mission': 160, 'Bayonet': 65, 'Breach': 240, 'BSS': 95, 'Cleanup': 115, 'Common Only': 65, 'Cover': 115, 'Hammer': 95, 'HILDR': 100, 'Knife': 90, 'Locals': 225, 'Logistics': 115, 'Rare Only': 240, 'Recon': 115, 'Showdown': 115, 'Uncommon Only': 65},
    {'nome_operatore': 'Joe', 'Basic Mission': 160, 'Bayonet': 65, 'Breach': 115, 'BSS': 95, 'Cleanup': 240, 'Common Only': 65, 'Cover': 115, 'Hammer': 95, 'HILDR': 100, 'Knife': 90, 'Locals': 225, 'Logistics': 115, 'Rare Only': 240, 'Recon': 115, 'Showdown': 115, 'Uncommon Only': 65},
    {'nome_operatore': 'Valera', 'Basic Mission': 160, 'Bayonet': 65, 'Breach': 155, 'BSS': 95, 'Cleanup': 115, 'Common Only': 65, 'Cover': 240, 'Hammer': 95, 'HILDR': 100, 'Knife': 320, 'Locals': 95, 'Logistics': 115, 'Rare Only': 240, 'Recon': 115, 'Showdown': 115, 'Uncommon Only': 65},
    {'nome_operatore': 'Capisce', 'Basic Mission': 160, 'Bayonet': 65, 'Breach': 155, 'BSS': 95, 'Cleanup': 115, 'Common Only': 65, 'Cover': 115, 'Hammer': 95, 'HILDR': 100, 'Knife': 90, 'Locals': 225, 'Logistics': 115, 'Rare Only': 240, 'Recon': 115, 'Showdown': 240, 'Uncommon Only': 65},

    {'nome_operatore': 'Epics', 'Basic Mission': 200, 'Bayonet': 200, 'Breach': 200, 'BSS': 200, 'Cleanup': 200, 'Common Only': 200, 'Cover': 200, 'Hammer': 200, 'HILDR': 200, 'Knife': 200, 'Locals': 200, 'Logistics': 200, 'Rare Only': 200, 'Recon': 200, 'Showdown': 200, 'Uncommon Only': 200},
]

def check_miss(operators, mission_list):
    missioni_migliori = {}
    x = 0

    for operatore in operators:
       
        missione_migliore = None
        punteggio_massimo = float('-inf')

        for missione in mission_list[x:]:
            punteggio = operatore[missione]
           
            if punteggio > punteggio_massimo:
                missione_migliore = missione
                punteggio_massimo = punteggio
            
            elif punteggio == punteggio_massimo:
                if mission_list.index(missione) > mission_list.index(missione_migliore):
                    missione_migliore = missione
                    punteggio_massimo = punteggio

        missioni_migliori[operatore['nome_operatore']] = missione_migliore

    return missioni_migliori

def calculate_text_size(text, font, font_size):
    from reportlab.pdfbase.pdfmetrics import stringWidth, getAscentDescent
    width = stringWidth(text, font, font_size)
    ascent, descent = getAscentDescent(font, font_size)
    height = ascent - descent
    return width, height

def create_custom_sized_pdf(output_filename, text_list, font="Helvetica", font_size=12, margin=2 * mm):
    max_text_width = 0
    total_text_height = 0
    text_sizes = []

    for text in text_list:
        text_width, text_height = calculate_text_size(text, font, font_size)
        text_sizes.append((text_width, text_height))
        max_text_width = max(max_text_width, text_width)
        total_text_height += text_height

    page_width = max_text_width + 2 * margin
    page_height = total_text_height + (len(text_list) + 1) * margin
    custom_size = (page_width, page_height)

    c = canvas.Canvas(output_filename, pagesize=custom_size)
    c.setFont(font, font_size)
    
    y_pos = page_height - margin
    for text, (text_width, text_height) in zip(text_list, text_sizes):
        c.drawString(margin, y_pos - text_height, text)
        y_pos -= text_height + margin

    c.save()

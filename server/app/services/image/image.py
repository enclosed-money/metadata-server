from dotenv import load_dotenv
import json
import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from web3 import Web3


load_dotenv(Path("../../../../.env"))
INFURA_ENDPOINT = os.getenv('INFURA_GOERLI_ENDPOINT')

def get_token_info(token_address: str):
    with open('erc20.json') as r:
        abi = json.loads(r.read())
    w3 = Web3(Web3.HTTPProvider(INFURA_ENDPOINT))
    token = w3.eth.contract(w3.toChecksumAddress(token_address), abi=abi)
    try:
        name = token.functions.name().call()
    except:
        name = 'Unknown'
    try:
        symbol = token.functions.symbol().call()
    except:
        symbol = '?'
    return name, symbol

def generate_image(token_id: int):
    token_address = hex(int(token_id >> 96 & ((1 << 160) - 1)) - (token_id >> 96 & (1 << 160)))
    if token_address != '0x0':
        token_name, token_symbol = get_token_info(token_address)
        token_amount = (token_id & ((1 << 96) - 1)) - (token_id & (1 << 96))
    else:
        token_name = "Ethereum"
        token_symbol = "ETH"
        token_amount = Web3.fromWei((token_id & ((1 << 96) - 1)) - (token_id & (1 << 96)), unit='ether')

    token_symbol_font = ImageFont.truetype("fonts/CourierPrime-Bold.ttf", 30)
    token_amount_font = ImageFont.truetype("fonts/CourierPrime-Regular.ttf", 30)
    token_name_font = ImageFont.truetype("fonts/CourierPrime-Bold.ttf", 10)
    token_address_font = ImageFont.truetype("fonts/CourierPrime-Regular.ttf", 8)

    img = Image.open("base_ticket.png")
    d = ImageDraw.Draw(img)
    d.text((102, 90), token_symbol, align=1, font=token_symbol_font, anchor='ms', fill=(0, 0, 0))
    d.text((200, 90), str(token_amount), align=0, font=token_amount_font, anchor='ls', fill=(0, 0, 0))
    d.text((200, 110), token_name, align=0, font=token_name_font, anchor='ls', fill=(0, 0, 0))
    d.text((200, 120), str(token_address), align=0, font=token_address_font, anchor='ls', fill=(0, 0, 0))

    return img
    #img.show()


#generate_image(10000000000000000)
#generate_image(84304645189062507144825627090669616263424446746814089412702237103736303386634)
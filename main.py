from Utils.productfinder import *
from Utils.spellchecker import *
from Utils.texttrimmer import trim
from Utils.weightdetector import *
from Utils.dbsearcher import *
from Utils.itemspecify import specify_item
nltk.download('punkt')

import pandas as pd

if __name__ == "__main__":
    
    data = pd.read_csv("DB\\db.csv")
    print("Start talking with the bot (type quit to stop)!")
    while True:
        text = input("\nYou: ").lower()
        if text.lower() == "quit":
            break
        elif text:
            orders = trim(text)
            if not orders:
                print("Hello!! This is SOL-BOT, how may I help you? 🙂")
                continue
            for order in orders:
                weight_class = detect_weight(order)
                while not weight_class:
                    print("Sol-bot: How much {} do you want?".format(order))
                    weight_class = detect_weight(input("\nYou: ").lower())
                
                item_indices = searchdb(order.replace(weight_class['text'], "").strip().split(), list(data['keysen']))
                print(item_indices)
                # print("weight: ", weight_class['weight'])
                # print("weight_class: ", weight_class['weight_class'])
                # print("item: ", order.replace(weight_class['text'], "").strip())
                
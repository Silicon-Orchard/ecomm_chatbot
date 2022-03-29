# from google.colab import drive
# drive.mount("/content/gdrive")

# cd /content/gdrive/My Drive/Machine Learning/Chatbot

from random import randint
dataset = []


for i in range(1, 5):
    data = {
        "image": "",
        "cost": 0,
        "stock": 0
    } 

    data["image"] = "images/" + str(i) + ".jpg"
    data["cost"] = randint(10, 200)
    data["stock"] = randint(0, 25)

    dataset.append(data)


print(dataset)

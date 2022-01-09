import discord
import os
import random
import joblib
import numpy as np
import json
import requests

client = discord.Client()

# --------------------------------ANGER----------------------------------------------------


def get_exercise_meditation_anger():
    response = requests.get(
        "https://angermanagementapi.herokuapp.com/api/anagersolution/random")
    json_data = json.loads(response.text)
    quote = "Spit out your anger 😡❤.\nTry these to lighten up your mood" + "\n" + json_data[
        0]['link']
    return (quote)


def get_soothinSongsAnger():
    response = requests.get(
        "https://soothingsongsapi.herokuapp.com/api/songs/random")
    json_data = json.loads(response.text)
    quote = "You seem upset 😟. Loosen up yourself ✨ listen to this relaxing song: " + "\n" + json_data[
        0]['SoothingSongs']
    return (quote)


# --------------------------------SADNESS----------------------------------------------------


def get_soothinSongsSad():
    response = requests.get(
        "https://soothingsongsapi.herokuapp.com/api/songs/random")
    json_data = json.loads(response.text)
    quote = "You seem upset 😟. Don't worry life happens.\nCheer Up!! ✨ And listen to this relaxing song: " + "\n" + json_data[
        0]['SoothingSongs']
    return (quote)


def get_tedtalks():
    response = requests.get(
        "https://tedtalkapi.herokuapp.com/api/tedTalks/random")
    json_data = json.loads(response.text)
    quote = "Everything is going to be okay. \nGive life some time. \nHere, elevate you thought process with some Ted Talks: " + "\n" + json_data[
        0]['tedTalk']
    return (quote)


def get_bookSad():
    response = requests.get(
        "https://booksraahee.herokuapp.com/api/books/random")
    json_data = json.loads(response.text)
    quote = "Let out your feelings. \nTry reading this book: \n\n 📖 '" + json_data[
        0]['bookTitle'] + "' by " + json_data[0][
            'bookAuthors'] + "\n" + json_data[0]['url']
    return (quote)


def get_jokeSad():
    request = requests.get('https://official-joke-api.appspot.com/random_joke')
    json_data = json.loads(
        request.text
    )  #converts response to json #response.text --> from api documentation
    joke = "Don't be sad. Lighten up with this: \n\n\t-" + json_data[
        'setup'] + "\n\t-" + json_data['punchline']
    return joke


# -----------------------------------HAPPINESS-----------------------------------------------------


def get_books():
    response = requests.get(
        "https://booksraahee.herokuapp.com/api/books/random")
    json_data = json.loads(response.text)
    quote = "It is a special day today, because you seem happy. \nOn this occasion, try reading this amazing book: \n\n 📖 '" + json_data[
        0]['bookTitle'] + "' by " + json_data[0][
            'bookAuthors'] + "\n" + json_data[0]['url']
    return (quote)


def get_songs():
    response = requests.get(
        "https://songsapicustom.herokuapp.com/api/songs/random")
    json_data = json.loads(response.text)
    quote = "Relax a bit and listen to: \n\n 🎶 '" + json_data[0][
        'Track Name'] + "' by " + json_data[0]['Artist'] + "\n" + json_data[0][
            'URL']
    return (quote)


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = "Enjoy the mood and get inspired ✨ : \n\n\"" + json_data[0][
        'q'] + "\"\n-" + json_data[0]['a']
    return (quote)


def get_joke():
    request = requests.get('https://official-joke-api.appspot.com/random_joke')
    json_data = json.loads(
        request.text
    )  #converts response to json #response.text --> from api documentation
    joke = "Someone seems happy today (psstt....it's you) \nLaugh out more with this 😂😂: \n\n\t-" + json_data[
        'setup'] + "\n\t-" + json_data['punchline']
    return joke


def get_memes():
    response = requests.get(
        "https://memescustomapi.herokuapp.com/api/memes/random")
    json_data = json.loads(response.text)
    quote = "Enjoy 😎 some more with this meme: " + "\n\n" + json_data[0]['url']
    return (quote)


def get_compliments():
    request = requests.get("https://complimentr.com/api")
    json_data = json.loads(
        request.text
    )  #converts response to json #response.text --> from api documentation
    joke = "Your day will by joyous ✨ because: \n" + json_data[
        'compliment'] + " ❤"
    return joke


#------------------------------------------------------------------------------------------------


def sad():
    list = [
        get_tedtalks(),
        get_soothinSongsSad(),
        get_bookSad(),
        get_jokeSad()
    ]
    response = random.choice(list)
    return response


def joy():
    list = [
        get_compliments(),
        get_joke(),
        get_quote(),
        get_books(),
        get_songs(),
        get_memes()
    ]
    response = random.choice(list)
    return response


def anger():
    list = [get_exercise_meditation_anger(), get_soothinSongsAnger()]
    response = random.choice(list)
    return response


#---------------------------------------------DRIVER FUNCTIONS--------------------------------------

with open('emotion.pkl', 'rb') as file:
    loaded_model = joblib.load(file)


@client.event
async def on_message(message):

    if message.author == client.user:  #should trigger only when it is clients message and not ours
        return

    TheMsg = message.content.lower()

    hello_words = ["hello", "$hello", "hi", "heya", "hola", "hey", "bonjour"]
    for word in hello_words:
        if TheMsg.startswith(word):
            await message.channel.send(
                'Hello! How are you, lovely person \N{smiling face with halo}')

    thank_words = [
        "Thanks", "Thank you", "cute", "pretty", "amazing", "good", "cool",
        "sleeping", "great", "nice", "happiest", "excellent", "thanks", "thnx",
        "thnx"
    ]
    for word in thank_words:
        if TheMsg.startswith(word):
            await message.channel.send(
                "Awww......I am glad that I could help 🤗 \nLet me know if I could help more"
            )

    bye_words = [
        "bye", "goodbye", "see you later", "bbie", "see ya", "see you"
    ]
    for word in bye_words:
        if word in TheMsg:
            await message.channel.send(
                "Cheerio, see you soon!!\nHave a nice day 🤍 \n")

    msg = loaded_model.predict([TheMsg])

    depressed_words = [
        "depression", "depress", "worry", "depressed", "kill myself",
        "cut myself", "I want to die", "hate myself", "end my life",
        "self harm", "i don't want to live", "harm", "die", "kill", "help",
        "Help", "Help me", "help me", "I need help", "Please"
    ]
    depressed = [ele for ele in depressed_words if (ele in TheMsg)]
    if bool(depressed):
        msg = 'depressed'

    if msg in [
            'joy', 'happiness', 'love', 'fun', 'relief', 'enthusiasm',
            'boredom'
    ]:
        print("joy" + msg)
        response = joy()
        await message.channel.send(response)

    elif msg in ['sadness', 'fear', 'empty', 'shame', 'depressed', 'worry']:
        res = [ele for ele in depressed_words if (ele in TheMsg)]
        if bool(res):
            print("depression" + msg)
            i = random.randint(0, 3)

            if i == 0:
                await message.channel.send(
                    "I am so sorry 😧 that \nyou have to go through such a rough patch in life. \nGive life some time.\nAnd remember, \nWe at Raahee 💜 are alwasys open to hear you out. \nVisit us here:\n"
                )
                embedRaahee = discord.Embed(
                    title="Raahee - Your Emotional First Aid",
                    description='https://raahee.in/')
                embedRaaheeApp = discord.Embed(
                    title="Raahee - Your Emotional First Aid",
                    description=
                    'https://play.google.com/store/apps/details?id=app.raahee.app'
                )
                await message.channel.send(embed=embedRaahee)
                await message.channel.send(embed=embedRaaheeApp)

            elif i == 1:
                await message.channel.send(
                    "I am so sorry 😧 that \nyou have to go through such a rough patch in life.\n\nSome organisations that provide free consulation on mental health\n"
                )
                embed1 = discord.Embed(
                    title="Nimhans",
                    description='http://nimhans.ac.in/pssmhs-helpline/')
                embed2 = discord.Embed(title="Sumaitri",
                                       description='http://sumaitri.net/')
                embed3 = discord.Embed(
                    title="Mann Talks",
                    description='https://www.manntalks.org/')
                await message.channel.send(embed=embed1)
                await message.channel.send(embed=embed2)
                await message.channel.send(embed=embed3)
                await message.channel.send("These resources might help 💜")

            elif i == 2:
                await message.channel.send(
                    "I am so sorry 😧 that \nyou have to go through such a rough patch in life.\n\nSome organisations that provide free consulation on mental health.\n Try calling 📞 them might help"
                )
                embed4 = discord.Embed(title="Parivarthan",
                                       description='Call us at +91-7676602602')
                embed5 = discord.Embed(title="Mitram Foundation",
                                       description='Call us at 080-25722573')
                embed6 = discord.Embed(title="Lifeline",
                                       description='Call us at 033-40447437')
                await message.channel.send(embed=embed4)
                await message.channel.send(embed=embed5)
                await message.channel.send(embed=embed6)
                await message.channel.send("These resources might help 💜")

            elif i == 3:
                response = requests.get(
                    "https://depressionmanagementapi.herokuapp.com/api/depression/random"
                )
                json_data = json.loads(response.text)
                quote = "I am so sorry to hear that 😧.\nDon't worry! Time will change 🤍 \nGive yourself time and try this:" + "\n" + json_data[
                    0]['link']
                await message.channel.send(quote)

        else:
            print("sad" + msg)
            response = sad()
            await message.channel.send(response)

    elif msg in ['anger', 'hate', 'disgust']:
        print("anger" + msg)
        response = anger()
        await message.channel.send(response)

    else:
        print("nothing" + msg)

client.run(TOKEN)

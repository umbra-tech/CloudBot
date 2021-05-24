import requests

from cloudbot import hook


markov_model = {}



@hook.command("declare", autohelp=True)
def declare(text, message):
    """[nick] - Outputs Marvok chain based on input's past logs"""
    markov_users = ("echs", "knots", "ngwnn", "nullaffinity", "skeer", "gavisann", "spr1ng", "mobomelter", "umbra", "wabb1t")
    
    if text.lower() in markov_users:
        r = requests.get("https://markovify-api.gavibot.com/response?user={0}".format(text.lower()))
        out = r.content
        out = out.decode()
        message("{0} says: {1}".format(text, out))
        print(out)
    else:
        message("User has not been added yet. THIS SHIT IS A BETA YO")

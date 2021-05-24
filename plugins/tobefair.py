from cloudbot import hook
import re


@hook.command("tobefair", autohelp=False)
def bonk( nick, chan, db, notice):
    """no useful help txt"""
    return "https://c.tenor.com/rwplrVlY2xoAAAAM/letterkenny-to-be-fair.gif"


message = re.compile('t*o* b*e* f*a*i*r*',re.IGNORECASE)


@hook.regex(message)
def wellcool(match, nick, chan, db, notice):
    """no useful help txt"""
    return "https://c.tenor.com/rwplrVlY2xoAAAAM/letterkenny-to-be-fair.gif"
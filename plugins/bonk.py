from cloudbot import hook
import re


@hook.command("bonk", autohelp=False)
def bonk( nick, chan, db, notice):
    """no useful help txt"""
    return "https://usercontent.irccloud-cdn.com/file/tZwoWZ4A/image.png"


message = re.compile('honk',re.IGNORECASE)


@hook.regex(message)
def wellcool(match, nick, chan, db, notice):
    """no useful help txt"""
    return "https://usercontent.irccloud-cdn.com/file/tZwoWZ4A/image.png"
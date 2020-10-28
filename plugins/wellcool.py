from cloudbot import hook
import re


message = re.compile('^.*?\\bwell\\b(\S*\s){0,4}\\bcool\\b.*?$',re.IGNORECASE)


@hook.regex(message)
def wellcool(match, nick, chan, db, notice):
    """no useful help txt"""
    return "https://usercontent.irccloud-cdn.com/file/g8pmTLuo/wellcool.gif"
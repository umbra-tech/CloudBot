from cloudbot import hook
import re


@hook.command("tobefair", autohelp=False)
def tobefair( nick, chan, db, notice):
    """no useful help txt"""
    return "https://usercontent.irccloud-cdn.com/file/SVAKkvZ7/letterkenny-to-be-fair.gif"


message = re.compile('t+o+ b+e+ f+a+i+r+',re.IGNORECASE)


@hook.regex(message)
def tobefair_regex(match, nick, chan, db, notice):
    """no useful help txt"""
    return "https://usercontent.irccloud-cdn.com/file/SVAKkvZ7/letterkenny-to-be-fair.gif"
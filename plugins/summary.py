import dateparser
import logging

from cloudbot import hook


from plugins.chatgpt import chat_gpt

logger = logging.getLogger("cloudbot")

#@hook.command("summary", "tldr", autohelp=False)
#def history(nick, chan, text, event, conn):
#    """[int] - produces summary on [int] number past messages. Max of 100 messages."""
#    depth = 10
#    if text != "":
#        try:
#            depth = int(text)
#        except:
#            return "Error: depth must be an int"
#    prompt = "Please create a summary of the following IRC messages in 150 words or less:"
#    history = []
#
#    for name, timestamp, msg in conn.history[chan]:
#        #history.append(f"{name}: {msg}")
#        history.append(msg)
#
#    history_string = prompt
#    for str in history[0:depth]:
#        history_string += f"{str} "
#
#    tldr = chat_gpt(nick, chan, history_string, event)
#
#    return tldr

@hook.command("summary", "tldr", autohelp=False)
def history(nick, chan, text, event, conn):
    """[int] - produces summary on [int] number past messages. Max of 100 messages."""
    depth = 10
    input_timestamp = ""
    if text != "":
        try:
            if text.isdigit():
                depth = int(text)
            else:
                input_time = text
                input_timestamp = dateparser.parse(input_time,settings={'TIMEZONE':'EST'}).timestamp()

        except Exception as e:
            return f"Error: {e}"
    prompt = "Please create a summary of the following IRC messages in 150 words or less:"
    history = []

    for name, timestamp, msg in reversed(conn.history[chan]):
        #history.append(f"{name}: {msg}")
        if input_timestamp != "" and timestamp > input_timestamp:
            history.append({name: msg})
            #return f"{timestamp}, {input_timestamp},{msg}"
        else:
            history.append({name: msg})

    #reversing the reversing so GPT can better understand the context
    history_string = ""
    for str1 in history[0:depth]:
        history_string = f" {str1} " + history_string
    history_string = prompt + history_string

    tldr = chat_gpt(nick, chan, history_string, event)

    return tldr

@hook.command("tldr_test", autohelp=False)
def history_test(nick, chan, text, event, conn):
    """[int] - produces summary on [int] number past messages. Max of 100 messages."""
    depth = 10
    input_timestamp = ""
    if text != "":
        try:
            if text.isdigit():
                depth = int(text)
            else:
                input_time = text
                input_timestamp = dateparser.parse(input_time,settings={'TIMEZONE':'EST'}).timestamp()

        except Exception as e:
            return f"Error: {e}"
    prompt = "Please create a summary of the following IRC messages in 150 words or less:"
    history = []

    for name, timestamp, msg in reversed(conn.history[chan]):
        #history.append(f"{name}: {msg}")
        if input_timestamp != "" and timestamp > input_timestamp:
            history.append({name: msg})
            #return f"{timestamp}, {input_timestamp},{msg}"
        else:
            history.append({name: msg})

    #reversing the reversing so GPT can better understand the context
    history_string = ""
    for str1 in history[0:depth]:
        history_string = f" {str1} " + history_string
    history_string = prompt + history_string
    logger.info(f"{input_timestamp}: {history_string}")

    #tldr = chat_gpt(nick, chan, history_string, event)

    return "logged to console"

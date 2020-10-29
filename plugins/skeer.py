import markovify
import os

from cloudbot import hook
from cloudbot.util import colors


@hook.command("skeer", autohelp=False)
def skeer(text, message, bot):
    """[nick] - much dongs, very ween, add a user nick as an arguement for slightly different 'output'"""
    # Get raw text as string.
    path = os.path.join(bot.data_dir, "corpus.txt")
    with open(path) as f:
        text = f.read()
    
    # Build the model.
    text_model = markovify.NewlineText(text,state_size=2)
    
    
    
    # Print five randomly-generated sentences
    #for i in range(5):
    #    print(text_model.make_sentence())#
    
    # Print three randomly-generated sentences of no more than 280 characters
    message("Skeer says: {0}".format(text_model.make_short_sentence(140)))
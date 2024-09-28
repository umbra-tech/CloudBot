# This plugin contains the IRC bot functions to create maps and store scores of track times in Liftoff

# The bot commands in this plugin are:
# = liftoff_add_map
# = liftoff_delete_map
# = liftoff_list_maps
# = liftoff_score 
# = liftoff_scores

from datetime import datetime, timedelta
from sqlalchemy import Table, Column, String, Integer, Interval
from sqlalchemy.sql import func, insert, update
from cloudbot.util import database
from cloudbot import hook


maps = Table(
    'liftoff_maps',
    database.metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
)

scores = Table(
    'liftoff_scores',
    database.metadata,
    Column('map_id', Integer),
    Column('username', String),
    Column('time', Interval),
)

@hook.command('liftoff', autohelp=False)
def usage():
    """
    Liftoff plugin usage
    """
    return "Usage: .liftoff_add_map <map_name> | .liftoff_del_map <map_name> | .liftoff_maps | .liftoff_score <map_name> <time> | .liftoff_scores <map_name>"

@hook.command('liftoff_add_map', autohelp=False)
def add_map(nick, text):
    """
    Adds a new map to the database
    """
    if not text:
        return "Usage: liftoff_add_map <map_name>"
    insert(maps).values(name=text).compile().execute()
    return f"Map {text} added"

@hook.command('liftoff_del_map', autohelp=False, permissions=["op"])
def delete_map(text, message):
    """
    Deletes a map from the database
    """
    if not text:
        return "Usage: liftoff_del_map <map_name>"
    delete = maps.delete().where(maps.c.name == text)
    delete.compile().execute()
    return f"Map {text} deleted"

@hook.command('liftoff_maps', autohelp=False)
def list_maps(text, message):
    """
    Lists all maps in the database
    """
    maps_list = maps.select().execute().fetchall()
    return ', '.join([m.name for m in maps_list])

@hook.command('liftoff_score', autohelp=False)
def add_score(nick, text):
    """
    Adds a new score to the database
    """
    if not text:
        return "Usage: .liftoff_score <map_name> <time>"
    map_name, time_str = text.split(' ')
    print(f"map_name: {map_name}, time_str: {time_str}")
    try:
        time = datetime.strptime(time_str, '%M:%S:%f')
    except ValueError:
        return "Invalid time format, use MM:SS:µµµ"
    duration = timedelta(minutes=time.minute, seconds=time.second, microseconds=time.microsecond)
    map = maps.select(maps.c.name == map_name).execute().first()
    if not map:
        return "Map not found"
    insert(scores).values(map_id=map.id, username=nick, time=duration).compile().execute()
    return f"Score added"

@hook.command('liftoff_scores', autohelp=False)
def get_scores(nick, text):
    """
    Lists all scores for a map
    """
    if not text:
        return "Usage: .liftoff_scores <map_name>"
    map_name = text
    map = maps.select(maps.c.name == map_name).execute().first()
    if not map:
        return "Map not found"
    
    scores_list = scores.select(scores.c.map_id == map.id).order_by(scores.c.time.asc()).limit(5).execute()
    out = f"Top 5 times for {map_name}: "
    for s in scores_list:
        out += f"\x02{s.username[:1] + ' ' + s.username[1:]}\x02: {strfdelta(s.time)} • "
    return out

@hook.command('liftoff_del_score', autohelp=False, permissions=["op"])
def delete_score(nick, text):
    """
    Deletes a score from the database
    """
    if not text:
        return "Usage: .liftoff_del_score <map_name> <username> <time>"
    map_name, username, time_str = text.split(' ')
    try:
        time = datetime.strptime(time_str, '%M:%S:%f')
    except ValueError:
        return "Invalid time format, use MM:SS:µµµ"
    duration = timedelta(minutes=time.minute, seconds=time.second, microseconds=time.microsecond)
    map = maps.select(maps.c.name == map_name).execute().first()
    if not map:
        return "Map not found"
    delete = scores.delete().where(scores.c.map_id == map.id).where(scores.c.username == username).where(scores.c.time == duration)
    delete.compile().execute()
    return f"Score deleted"


def strfdelta(tdelta):
    return f"{tdelta.seconds // 60:02}:{tdelta.seconds % 60:02}:{tdelta.microseconds // 1000:03}"
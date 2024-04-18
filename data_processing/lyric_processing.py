"""
This is the pyfile for rule-based pre-processing of the lyrics.
A preliminary cleaning f
(which yielded the "all_song_lyrics_dict_cleaned.json" )

Rules include:
- Modifying the first line -- removing irrelevant text regarding e.g. contributors, lyrics, translations
- Removing text in square brackets -- in lyrics these are often used for section annotations and transitions.
- Removing the last line if it ends with the format of (optional digits)Embed -- a common serial-number-like pattern labelling the lyric at the end
- Standardizing the newline characters and removing consecutive newlines
- When the lyrics are obviously empty, mark them as "Lyrics not available"
- Writing the cleaned lyrics to a file as JSON
"""

import re
import json

def clean_lyrics(lyrics):
    """
    Given a string of lyrics, this function will clean the lyrics according to the rules.
    """
    # Split the lyrics into lines
    lines = lyrics.split('\n')

    # everything before "Contributors" in first line
    if lines:
        lines[0] = re.sub(r'^.*Contributors', '', lines[0])
        lines[0] = re.sub(r'^.*Lyrics', '', lines[0])
        lines[0] = re.sub(r'^.*Translation\w+', '', lines[0])

    # Replace text in square brackets with '\n'
    cleaned_lyrics = '\n'.join(lines)
    cleaned_lyrics = re.sub(r'\[.*?\]', '\n', cleaned_lyrics)

    # Split again after replacing brackets to ensure we're working with the updated lines
    lines = cleaned_lyrics.split('\n')

    # Look at the last line and remove it if it ends with the format of (optional digits)Embed
    if lines and re.match(r'.*\d*Embed$', lines[-1]):
        lines = lines[:-1]

    # Join the lines back into a single string
    cleaned_lyrics = '\n'.join(lines)

    # remove consecutive newlines
    cleaned_lyrics = re.sub(r'\n\n+', '\n\n', cleaned_lyrics)

    return cleaned_lyrics

def rule_based_cleaning(all_song_lyrics_dict, output_file_path = 'all_song_lyrics_dict_cleaned.json'):
    """
    This function takes in a dictionary of song names and semi-cleaned lyrics to
    write to a file as JSON.
    The song with empty lyrics will be marked as "Lyrics not available"

    input:
    all_song_lyrics_dict: a dictionary of song names and semi-cleaned lyrics
    output_file_path: the path to the file to write the cleaned lyrics to
    
    NOTE: it is not suppose to operate on the entire dataset at once,
     if the dataset is too large try batch processing!!
    """


    cleaned_lyrics_dict = {}  # Initialize an empty dictionary to hold the cleaned lyrics

    for song_name, song_lyrics in all_song_lyrics_dict.items():
        if song_lyrics == "Lyrics not available":
            cleaned_lyrics_dict[song_name] = "Lyrics not available"
            continue

        cleaned_lyrics = clean_lyrics(song_lyrics)
        if cleaned_lyrics:
            cleaned_lyrics_dict[song_name] = cleaned_lyrics
        else:
            cleaned_lyrics_dict[song_name] = "Lyrics not available"

    # After all songs have been processed, write the cleaned_lyrics_dict to a file as JSON
    with open(output_file_path, 'w') as f:
        json.dump(cleaned_lyrics_dict, f, indent=4)

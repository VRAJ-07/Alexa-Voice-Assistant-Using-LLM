music = {
    "stealth": "https://youtu.be/U47Tr9BB_wE?si=cOd0zkk9BacqQ49y",
    "animals": "https://youtu.be/IPYTxAHeR_o?si=Cuo3QoZRcBst4OCb",
    "skyfall": "https://youtu.be/DeumyOzKqgI?si=J7SkdbeVcXT7jFWf",
}

def get_music_link(song_name):
    """
    Function to get the music link for the given song name.
    :param song_name: The name of the song (string)
    :return: URL of the song (string) or None if not found
    """
    song_name = song_name.lower().strip()  # Ensure case-insensitive and strip extra spaces
    return music.get(song_name, None)  # Return the URL if found, otherwise None

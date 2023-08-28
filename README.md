# spotify-to-obs

## Description
Takes in spotify playlist and generates a single file with all the songs in that playlist.

## Run Instructions

Prereqs: 
 - Need python installed.
 - Need [spotdl](https://github.com/spotDL/spotify-downloader) installed in system.

1. Clone repo and make playlists directory (required)

```
git clone https://github.com/devhulk/spotify-to-obs.git
cd spotify-to-obs
mkdir playlists
```

2. Install requirements (required)
```
pip install -r requirements.txt
```

3. Run with Spotify playlist link (replace link with your playlist link) 
```
python3 spotify_to_obs.py https://open.spotify.com/playlist/0QHoWDoTGJA0iJZcsNMtYU?si=293d81bb70584f83
```

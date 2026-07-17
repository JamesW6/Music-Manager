# Music Manager
A CLI to download your soundcloud playlists, without going through the troubles of configuring your yt-dlp command and finding your soundcloud playlist link

## Installation
1. Download Source Code and navigate to directory
2. Ensure python is installed
3. If downloading from youtube, ensure firefox is installed
4. run `python -m venv .venv`
5. run `source ./.venv/bin/activate` (for linux, or activate venv however you would on your os)
6. run `./music_mover`


## Youtube Usage
Since youtube is more difficult to scrape than soundcloud, the current system requires a bit of manual work.  
**Current steps**:
1. Run the script
2. Enter youtube account URL
3. If firefox opens and prompts you for cookies, click reject all
4. Choose your playlist to download (newest is first, displaying the names feauture coming soon)
   
## Soundcloud Usage
Soundcloud is much simpler  
**Current steps**:
1. Run the script
2. Enter soundcloud account URL
3. Choose playlist to download

## Disclaimer
This script uses a web scraper, use at your own risk, especially with youtube

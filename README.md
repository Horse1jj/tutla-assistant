# tutla-assistant
Official Tutla Assistant Bot source code

## The Bot
The Tutla Assitant bot has been a project I've worked on for a long time. Today, I decided to share this project.
Tutla Assistant is a Discord Selfbot that has many QOL & Helpful commands, you can see all the commands by running `.help` on any channel.

## Note
This is a selfbot and break Discord's TOS, use it knowing the risks. Secondly, the source code provided is raw and has not been modified for your installation. You willl manually have to change the invite links and so on, you may want to change:
- The Admin Command Roles
- Invite
- Support Links
- Custom Discord server configurations
- Ballsdex pings for myself

## Installation
You require:
- Python 3.8+

  Python Libraries:
- discord.py-self
- wikipedia
- freegpt
- BeautifulSoup
- pillow

**YOU DO NOT NEED DISCORD INSTALLED, IT USES DISCORD's API TO SEND AND GET REQUESTS**

To install this you will first install Python 3.8+ with it in the environment variables. After that you may want to install each of the libraries as follows:
`pip install discord.py-self wikipedia freegpt beautifulsoup4 pillow`

Once successfully installing the libraries you would want to make some changes in the file as it has many advertisements to our Discord and more which have been listed in the notice above.

Then you may proceed to adding the account you want to run the assistant program on. You must get the token of the account and paste it into `assistantdata/token.txt`. You may cofigure premium account in `premium.txt` and banned users in `bans.txt` both in `assistantdata`.
Once the installation is complete you can follow this **optional** method that keepsit 24/6/365:

### 24/7 running
We have also added `run.sh` (for linux) that will restart the file when it crashes (it sometimes crashes). You will need to change `python3.9 err.py` to whatever suits you. That line is the command to run the script with `python3.9` being your python eecutable command and the following file is your code. 

Run `./run.sh` to get it started

# Runiverse game auto
This is a automation attack for Runiverse.world [For education purpose only]

# Requirements
- Installed Python 2.7+ (https://www.python.org/downloads/)

# How to run
1. Install Python if you don't already installed.
2. Clone the repository to a folder on your PC.
3. Open Powershell/Terminal and go to the folder that you extracted from step 2
4. Run this command to install required libraries
```bash
pip install -r requirements.txt
```
5. Copy config.txt.sample to config.txt file
```bash
cp config.txt.sample config.txt
```
6. Copy sample.default to sample folder
```bash
cp sample.default sample
```
7. Captured your Runiverse game screen and crop it just like sample images on each one (skill1.png to skill4.png will be your skill images, script will find skill 4 - 1 respectively to use, if you don't need it just unequip it before running).
8. Start the bot by double click at start.py or use command python start.py (You need to keep open the game screen when running).

** Don't forget to replace your sample folder with the new sample.default

# Configuration
There are default configurations that suit my screen, but you can adjust to suit your screen.
Adjust values inside config.txt file to suit your screen and run bot smoothly.

| Name | Description | Type | Default |
| --- | --- | --- | --- | --- |
| WALK_MAX_DURATION | max duration to walk around  | Second | 2 |

# Remarks
- This bot is created very quickly and might have some glitchs or bugs.
- If you would like to donate me that will be really appreciated. You can send ETH, DAI, USDT, USDC to this crypto currency wallet below:
  0xbf20064C795362e7A87F6d21fe3C57Bd99e4a9A5

# Changelog
## v 0.0.1
+ Inital project

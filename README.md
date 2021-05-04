# Agilis-v1.0 README
Python script to automate the setup of multiplayer custom workshop maps in Rocket League.

# Table of Contents:
* [About Agilis](#About-Agilis)
    * [Functionality](#Functionality)
    * [Requirements](#Requirements)
    * [Quick Start](#Quick-Start)
* [Issues Running Agilis](#Issues-Running-Agilis)
    * [Known Issues](#Known-Issues)
    * [Troubleshooting](#Troubleshooting)
    * [Frequently Asked Questions](#Frequently-Asked-Questions)

# About Agilis

I coded this script in about a week after my first experience trying out custom multiplayer workshop maps in Rocket League. I had a great experience playing the custom maps with my friends but I thought the setup process was a bit overcomplicated and that it can be a barrier for people who want to try it out for the first time but don't know how to get started. I don't have much experience coding projects like this but I'll be happy if it helps at least one person get started with multiplayer custom workshop maps.

## Functionality

Agilis supports both the Epic Games and Steam versions of Rocket League for Windows.
* Every time you run Agilis it adds the required workshop textures to your Rocket League install so that no one gets a content mismatch error.
* Uses https://steamworkshopdownloader.io/ to download and install custom map files for both Epic Games and Steam versions of Rocket League.
* Auto BakkesMod installer with Rocket Plugin setup.
* Auto LogMeIn Hamachi installer.

## Requirements 
* A working Chrome installation.
* The latest verison on Python (Python 3.9.5 is already included in the .zip file)

## Quick Start

Literally the point of me making this script was to make it as easy as possible for everyone to use so let's walk through it:

1. Download the [latest version of Agilis](https://github.com/VerceRL/Agilis-v1.0) by clicking the green "Code" button and clicking "Download ZIP"

   ![Github Code Download](https://github.com/VerceRL/Agilis-v1.0/blob/main/Resources/Github/code.PNG)

2. Right click on the downloaded .zip and select "Extract All..." Leave the default extract location the same, just press "Extract". 

**Note:** Agilis was made with the idea that most people would just leave the extracted Agilis folder in their Downloads. The Agilis folder can be moved elsewhere with the modification of the Target under Launcher Properties but I don't necessarily recommend you do so.
   
   ![Windows Extract All](https://github.com/VerceRL/Agilis-v1.0/blob/main/Resources/Github/extractAll.PNG)
   ![Windows Extract Path](https://github.com/VerceRL/Agilis-v1.0/blob/main/Resources/Github/extractPath.PNG)
   
3. Open the new folder and double-click '_STEP 1 - CLICK "ADD PYTHON TO PATH".exe' This is the installer for the latest version of Python. ***It is very important you click the checkbox "Add Python 3.9 to PATH"*** Then you can click "Install Now" to finish Python setup.

   ![Python Install](https://github.com/VerceRL/Agilis-v1.0/blob/main/Resources/Github/pythonPath.PNG)
   
4. After Python has finished installing double-click '_STEP 2 - RUN.bat' This will install the required Python modules used in Agilis. When that is finished we should get a message letting us know we are ready to use the Launcher! Go ahead and double-click "Launcher" to run Agilis for the first time!
   
5. Agilis will automatically detect if Rocket League is installed in the default location and add the required workshop textures to your version of Rocket League. If you have Rocket League installed in a custom location, Agilis will open a window for you to select where your "rocketleague" folder is located.

**Note:** Folders such as "Binaries", "Engine", "TAGame", etc should not be selected. Select the folder titled "rocketleague"

   ![Directory Locator](https://github.com/VerceRL/Agilis-v1.0/blob/main/Resources/Github/directoryLocator.PNG)
   
7. Agilis will prompt the user for the Steam Workshop URL of the map they want to install. Go ahead and grab that link directly from the Steam Workshop and paste it into Agilis.

   ![Steam Workshop GIF](https://github.com/VerceRL/Agilis-v1.0/blob/main/Resources/Github/workshop.gif)
   
8. Agilis will finish by downloading and installing the requested map and running installers for BakkesMod, Rocket Plugin, and LogMeIn Hamachi if they are not already installed. Want to install another map? Just run the 'Launcher' again! Agilis will see that you already have the required software and go straight to getting your maps setup properply in the right directories.

That is basically it for what Agilis is able to do automatically for you. If you don't know how to use LogMeIn Hamachi or Rocket Plugin, I included some extra steps below so you can connect with your friends.

9. Create an account for LogMeIn Hamachi. After you're done setting up your account make sure the power button on the top left is clicked and then click either "Create a new network" or "Join an existing network" depending on whether you'll be hosting the lobby or joining a friend. Enter a Network ID and Password.

**Note:** LogMeIn Hamachi groups networks per 5 connections but you can add multiple Hamachi networks to have more than 5 players connect to the host at one time.

10. Once everyone has joined the LogMeIn Hamachi network, those who will be joining the host should copy the IPv4 address of the host by clicking on the host's computer's name and clicking on "Copy IPv4 address" it should be a number something like 25.25.25.25
   
**Instructions for the host:** 
* Open Rocket League and press F2 to open BakkesMod.
* Select the "Plugins" tab and select "Rocket Plugin" on the left.
* Set the "Default ip address:" to your IPv4 shown by the power button in LogMeIn Hamachi. Leave the port and password settings alone.
* Press "Open Rocket Plugin GUI" the left side of this window is where you can change certain lobby settings.
* Click the checkbox "Enable custom maps" and select the map for the lobby.
* Press the "Host" button on the bottom left when you are ready to start the lobby.

**Instructions for those joining the host:**
* Open Rocket League and press F2 to open BakkesMod.
* Select the "Plugins" tab and select "Rocket Plugin" on the left.
* Press "Open Rocket Plugin GUI" the right side of this menu is for you.
* After the host has started the game, paste the host's IPv4 address from LogMeIn Hamachi in the "IP Address:" box.
* Leave the port and password settings alone. There is also no need to click the checkbox "Joining a custom map" just leave it empty.

   ![Rocket Plugin GIF](https://github.com/VerceRL/Agilis-v1.0/blob/main/Resources/Github/rocketPlugin.gif)
   
# Issues Running Agilis 
## Known Issues
* If you have both the Steam and the Epic Games verions of Rocket League installed at once on your system Agilis will favor the Steam version.

* Error messages are detailed but don't help the user finish the installation during that instance.

* Plenty of inefficiencies. 

* BakkesMod install isn't the latest version.

* steamworkshopdownloader.io doesn't always play nicely with automation and sometimes requires user to paste URL manually.
  
* Probably so many more.

## Troubleshooting

+ If your "Launcher" shortcut isn't working right-click it, select "Properties" and double-check that the target path is correct. Also check that your Agilis folder is named properly and placed in "Downloads"

+ If Agilis isn't running with administrative privileges make sure you are using the "Launcher"

+ If steamworkshopdownloader.io is not finding your map try pasting the URL manually when Agilis asks you to, if that still doesn't work please double-check your link is correct in another tab.

+ If none of the above works try getting out of Platinum :)

## Frequently Asked Questions

1. **Agilis helped me install all the right software, but how do I add maps?**
   
   To install more maps just run the Launcher again. Agilis will see that you already have the required software and go straight to getting your maps setup properply in the right directories. So when you run Agilis for the first time it is basically a setup script but then after it becomes a tool for quickly installing more custom maps.
   
2. **What's the best way to contact you?**
   
   You can message me on Discord @Verce#5680 I'd be happy to answer questions, help troubleshoot, and hear your suggestions!

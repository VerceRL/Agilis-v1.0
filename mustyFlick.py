import os
import re
import time
import ctypes
import shutil
import zipfile
import pathlib
import pyperclip
import subprocess
from pathlib import Path
from selenium import webdriver
from pywinauto.application import Application
from selenium.webdriver.common.keys import Keys

class bcolors:
    green = '\033[92m'
    yellow = '\033[33m'
    red = '\033[31m'
    reset = '\033[0m'
    cyan = '\033[36m'

os.system('cls')
print(bcolors.cyan+""".................................................
,,,,,,,,,,,,,,.....................,,,,,,,,,,,,,,
,,,,,,,,,,.............................,,,,,,,,,,
,,,,,,,.........        /        .........,,,,,,,
,,,,,.......      //  (((((  //      .......,,,.,                 ___         _ ___
,,,......     ,((/  (((((((((  /((.     ......,,,                /   | ____ _(_) (_)____
,,......   (((((  (((((( ((((((  (((((   ......,,               / /| |/ __ `/ / / / ___/
,.....          ######     ######          .....,              / ___ / /_/ / / / (__  )
.....         ######  /////  ######        ......             /_/  |_\__, /_/_/_/____/
.....       ##       ///////       ##       .....                   /____/
.....                (((((((                .....
.....                 (((((                 .....           Script for Multiplayer Custom
.....                 (((((                ......                  Workshop Maps
,.....                 (((                 .....,
,,......               ###               ......,,              Developed by Verce#5680
,,,......               #               ......,,,
,,,.,......             #            .......,,,.,
,,,,,,,.........                 .........,,,,,,,
,,,,,,,,,,.............................,,,,,,,,,,
,,,,,,,,,,,,,,.....................,,,,,,,,,,,,,,
.................................................
"""+bcolors.reset)

def is_running_as_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def unzip():
    print("["+bcolors.green+"+"+bcolors.reset+"] Unzipping assets...")
    with zipfile.ZipFile('Zipped\\BakkesModSetup.zip', 'r') as zip_ref:
        zip_ref.extractall('Resources\\BakkesModSetup')
    with zipfile.ZipFile('Zipped\\RocketPlugin_0_6_6.zip', 'r') as zip_ref:
        zip_ref.extractall('Resources\\RocketPlugin_0_6_6')
    with zipfile.ZipFile('Zipped\\Workshop-textures.zip', 'r') as zip_ref:
        zip_ref.extractall('Resources\\Workshop-textures')
    if os.path.isfile('Resources\\BakkesModSetup\\BakkesModSetup.exe'):
        if os.path.isfile('Resources\\RocketPlugin_0_6_6\\plugins\\RocketPlugin.dll'):
            if os.path.isfile('Resources\\Workshop-textures\\EditorMeshes.upk'):
                print("["+bcolors.green+"+"+bcolors.reset+"] All assets were successfully unzipped!")
            else:
                print('['+bcolors.red+'!'+bcolors.reset+'] ERROR: Automatic Unzipping Failed - Please manually unzip "Workshop-textures.zip" into the "Resources" folder.')
                exit()
        else:
            print('['+bcolors.red+'!'+bcolors.reset+'] ERROR: Automatic Unzipping Failed - Please manually unzip "RocketPlugin_0_6_6.zip" into the "Resources" folder.')
            exit()
    else:
        print('['+bcolors.red+'!'+bcolors.reset+'] ERROR: Automatic Unzipping Failed - Please manually unzip "BakkesModSetup.zip" into the "Resources" folder.')
        exit()

def workshop_textures_setup():
    global modFolderDir
    global endModFolderPath
    if os.path.isdir('C:\\Program Files (x86)\\Steam\\steamapps\\common\\rocketleague'):
        print("["+bcolors.green+"+"+bcolors.reset+"] The Steam version of Rocket League is installed in it's default directory!")
        targetDir = 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\rocketleague\\TAGame\\CookedPCConsole'
        modFolderDir = 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\rocketleague\\TAGame\\CookedPCConsole\\mods'
        endModFolderPath = "rocketleague\\TAGame\\CookedPCConsole\\mods"
        file_names = os.listdir('Resources\\Workshop-textures')
        checkDir = targetDir+"\\EditorMeshes.upk"

        print("["+bcolors.green+"+"+bcolors.reset+"] Adding Workshop Textures...")
        for file_name in file_names:
            shutil.move(os.path.join('Resources\\Workshop-textures', file_name), os.path.join(targetDir, file_name))
        if os.path.isfile(checkDir):
            print("["+bcolors.green+"+"+bcolors.reset+"] Workshop Textures added successfully!")
            if os.path.isdir(modFolderDir):
                print("["+bcolors.green+"+"+bcolors.reset+"] Mods folder already exists!")
            else:
                print("["+bcolors.green+"+"+bcolors.reset+"] Adding Mods Folder...")
                os.mkdir(modFolderDir)
                if os.path.isdir(modFolderDir):
                    print("["+bcolors.green+"+"+bcolors.reset+"] Mods folder added successfully!")
                else:
                    print('['+bcolors.red+'!'+bcolors.reset+'] ERROR: Automatic Installation Failed - Failed to create "mods" folder within: '+targetDir)
                    exit()
        else:
            print('['+bcolors.red+'!'+bcolors.reset+'] ERROR: Automatic Installation Failed - Failed to copy files from "Resources\Workshop-textures" into: '+targetDir)
            exit()
    elif os.path.isdir('C:\\Program Files\\Epic Games\\rocketleague'):
            print("["+bcolors.green+"+"+bcolors.reset+"] The Epic Games version of Rocket League is installed in it's default directory!")
            targetDir = 'C:\\Program Files\\Epic Games\\rocketleague\\TAGame\\CookedPCConsole'
            modFolderDir = 'C:\\Program Files\\Epic Games\\rocketleague\\TAGame\\CookedPCConsole\\rocketplugin'
            endModFolderPath = "rocketleague\\TAGame\\CookedPCConsole\\rocketplugin"
            file_names = os.listdir('Resources\\Workshop-textures')
            checkDir = targetDir+"\\EditorMeshes.upk"

            print("["+bcolors.green+"+"+bcolors.reset+"] Adding Workshop Textures...")
            for file_name in file_names:
                shutil.move(os.path.join('Resources\\Workshop-textures', file_name), os.path.join(targetDir, file_name))
            if os.path.isfile(checkDir):
                print("["+bcolors.green+"+"+bcolors.reset+"] Workshop Textures added successfully!")
                if os.path.isdir(modFolderDir):
                    print("["+bcolors.green+"+"+bcolors.reset+"] Rocket Plugin folder already exists!")
                else:
                    print("["+bcolors.green+"+"+bcolors.reset+"] Adding Rocket Plugin Folder...")
                    os.mkdir(modFolderDir)
                    if os.path.isdir(modFolderDir):
                        print("["+bcolors.green+"+"+bcolors.reset+"] Rocket Plugin folder added successfully!")
                    else:
                        print('['+bcolors.red+'!'+bcolors.reset+'] ERROR: Automatic Installation Failed - Failed to create "rocketplugin" folder within: '+targetDir)
                        exit()
            else:
                print('['+bcolors.red+'!'+bcolors.reset+'] ERROR: Automatic Installation Failed - Failed to copy files from "Resources\Workshop-textures" into: '+targetDir)
                exit()
    else:
        print("["+bcolors.yellow+"*"+bcolors.reset+'] Rocket League is not installed in the default location! Use the new window to select the location of your "rocketleague" folder.')
        rocketLeagueDirectory = subprocess.check_output("Resources\\directory_locator.py", shell=True)
        decodedDir = rocketLeagueDirectory.decode("utf-8")
        verifyFolder = decodedDir+"/TAGame"
        verifyFolder = verifyFolder.replace("\r\n","")
        if os.path.isdir(verifyFolder):
            targetDir = decodedDir+"/TAGame/CookedPCConsole"
            targetDir = targetDir.replace("\r\n","")
            modFolderDir = decodedDir+"/TAGame/CookedPCConsole/mods"
            modFolderDir = modFolderDir.replace("\r\n","")
            endModFolderPath = "rocketleague\\TAGame\\CookedPCConsole\\mods"
            file_names = os.listdir('Resources\\Workshop-textures')
            checkDir = targetDir+"/EditorMeshes.upk"

            print("["+bcolors.green+"+"+bcolors.reset+"] Adding Workshop Textures...")
            for file_name in file_names:
                shutil.move(os.path.join('Resources\\Workshop-textures', file_name), os.path.join(targetDir, file_name))
            if os.path.isfile(checkDir):
                print("["+bcolors.green+"+"+bcolors.reset+"] Workshop Textures added successfully!")
                if os.path.isdir(modFolderDir):
                    print("["+bcolors.green+"+"+bcolors.reset+"] Mods folder already exists!")
                else:
                    print("["+bcolors.green+"+"+bcolors.reset+"] Adding Mods Folder...")
                    os.mkdir(modFolderDir)
                    if os.path.isdir(modFolderDir):
                        print("["+bcolors.green+"+"+bcolors.reset+"] Mods folder added successfully!")
                    else:
                        print('['+bcolors.red+'!'+bcolors.reset+'] ERROR: Automatic Installation Failed - Failed to create "mods" folder within: '+targetDir)
                        exit()
            else:
                print('['+bcolors.red+'!'+bcolors.reset+'] ERROR: Automatic Installation Failed - Failed to copy files from "Resources\Workshop-textures" into: '+targetDir)
                exit()
        else:
            print('['+bcolors.red+'!'+bcolors.reset+'] ERROR: Automatic Installation Failed - Please select your "rocketleague" folder. Do not select "Binaries", "Engine", "TAGame", etc.')
            exit()

def map_downloader():
    global preInstalledMap
    preInstalledMap = 0
    try:
        input("["+bcolors.yellow+"*"+bcolors.reset+'] Paste Steam Workshop URL here: ')
        url = pyperclip.paste()
        mapID = url.replace("https://steamcommunity.com/sharedfiles/filedetails/?id=","")
        mapID = mapID.replace("&searchtext=","")

        option = webdriver.ChromeOptions()
        option.add_argument("--log-level=3")
        option.add_argument("window-size=800,415")
        option.add_experimental_option('excludeSwitches', ['enable-logging', "enable-automation"])
        option.add_experimental_option('useAutomationExtension', False)
        option.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")

        web = webdriver.Chrome(executable_path='Resources\\chromedriver.exe',options=option)
        web.get('https://steamworkshopdownloader.io/')
        inputBox = web.find_element_by_xpath('//*[@id="downloadUrlLabel"]')
        inputBox.click()
        inputBox.send_keys(Keys.CONTROL, "v")
        time.sleep(3)
        downloadButton = web.find_element_by_xpath('//*[@id="root"]/main/div[3]/div/div/div/div/div[2]/div[2]/span/button')
        downloadButtonText = downloadButton.text
        successfulDownload = "Download"
        downloadComplete = "Downloaded"

        if successfulDownload == downloadButtonText:
            mapName = web.find_element_by_xpath('//*[@id="root"]/main/div[3]/div/div/div/div/div[1]/div[2]/h6/a/strong')
            mapNameText = mapName.text

            mapNameText = re.sub(r'(?<!^)(?=[A-Z])', '_', mapNameText).lower()
            mapNameText = mapNameText.translate ({ord(c): "_" for c in "!@#$%^""&*()[]{};:,./'<>?\|`~-=+"})
            mapNameText = mapNameText.replace(" ","_")
            mapNameText = mapNameText.replace("____","_")
            mapNameText = mapNameText.replace("___","_")
            mapNameText = mapNameText.replace("__","_")
            if mapNameText.endswith('_'):
                mapNameText = mapNameText[:-1]
            if mapNameText.startswith('_'):
                mapNameText = mapNameText[+1:]

            print("["+bcolors.green+"+"+bcolors.reset+"] Successfully found map download!")
            downloadButton.click()
            print("["+bcolors.yellow+"*"+bcolors.reset+'] Waiting for download to finish...')
            while downloadButtonText != downloadComplete:
                time.sleep(1)
                downloadButton = web.find_element_by_xpath('//*[@id="root"]/main/div[3]/div/div/div/div/div[2]/div[2]/span/button')
                downloadButtonText = downloadButton.text
            print("["+bcolors.green+"+"+bcolors.reset+"] Download completed! Extracting files...")
            time.sleep(5)
            web.quit()
            mapZipDir = "C:"+os.getenv('HOMEPATH')+'\\Downloads\\'+mapID+'_'+mapNameText+'.zip'
            mapDestination = "C:"+os.getenv('HOMEPATH')+'\\Downloads\\'+mapID+'_'+mapNameText
            with zipfile.ZipFile(mapZipDir, 'r') as zip_ref:
                zip_ref.extractall(mapDestination)
            if os.path.isdir(mapDestination):
                print("["+bcolors.green+"+"+bcolors.reset+"] Map files extracted successfully! Deleting .zip file...")
                os.remove(mapZipDir)
                if not os.path.isfile(mapZipDir):
                    print("["+bcolors.green+"+"+bcolors.reset+'] Map .zip file deleted sucessfully! Moving map files to "Agilis\Maps"')
                    destination = os.path.join(pathlib.Path(__file__).parent.absolute(), "Maps")
                    newDir = shutil.move(mapDestination, destination)
                    if os.path.isdir(newDir):
                        print("["+bcolors.green+"+"+bcolors.reset+'] Moved to "Agilis\Maps" successfully! Moving .upk file to '+endModFolderPath)
                        for file in os.listdir(newDir):
                            if file.endswith(".udk"):
                                file = Path(os.path.join(newDir, file))
                                file = file.rename(file.with_suffix('.upk'))
                                shutil.move(file, modFolderDir)
                    else:
                        print('['+bcolors.red+'!'+bcolors.reset+'] ERROR: Automatic Installation Failed - Please rename map .udk file to .upk and move to '+modFolderDir)
                        exit()
                else:
                    print('['+bcolors.red+'!'+bcolors.reset+'] ERROR: Automatic Deletion Failed - Please delete map .zip file in your "Downloads" folder.')
                    exit()
            else:
                print('['+bcolors.red+'!'+bcolors.reset+'] ERROR: Automatic Unzipping Failed - Please manually unzip map .zip file in your "Downloads" folder.')
                exit()
        else:
            print("["+bcolors.red+'!'+bcolors.reset+"] ERROR: Map download button not found! Please double check your URL is correct and paste it in the website textbox.")
            input("Press Enter to continue . . .")
            url = pyperclip.paste()
            mapID = url.replace("https://steamcommunity.com/sharedfiles/filedetails/?id=","")
            mapID = mapID.replace("&searchtext=","")
            downloadButton = web.find_element_by_xpath('//*[@id="root"]/main/div[3]/div/div/div/div/div[2]/div[2]/span/button')
            downloadButtonText = downloadButton.text
            successfulDownload = "Download"
            downloadComplete = "Downloaded"
            if successfulDownload == downloadButtonText:
                mapName = web.find_element_by_xpath('//*[@id="root"]/main/div[3]/div/div/div/div/div[1]/div[2]/h6/a/strong')
                mapNameText = mapName.text

                mapNameText = re.sub(r'(?<!^)(?=[A-Z])', '_', mapNameText).lower()
                mapNameText = mapNameText.translate ({ord(c): "_" for c in "!@#$%^""&*()[]{};:,./'<>?\|`~-=+"})
                mapNameText = mapNameText.replace(" ","_")
                mapNameText = mapNameText.replace("____","_")
                mapNameText = mapNameText.replace("___","_")
                mapNameText = mapNameText.replace("__","_")
                if mapNameText.endswith('_'):
                    mapNameText = mapNameText[:-1]
                if mapNameText.startswith('_'):
                    mapNameText = mapNameText[+1:]

                print("["+bcolors.green+"+"+bcolors.reset+"] Successfully found map download!")
                downloadButton.click()
                print("["+bcolors.yellow+"*"+bcolors.reset+'] Waiting for download to finish...')
                while downloadButtonText != downloadComplete:
                    time.sleep(1)
                    downloadButton = web.find_element_by_xpath('//*[@id="root"]/main/div[3]/div/div/div/div/div[2]/div[2]/span/button')
                    downloadButtonText = downloadButton.text
                print("["+bcolors.green+"+"+bcolors.reset+"] Download completed! Extracting files...")
                time.sleep(5)
                web.quit()
                mapZipDir = "C:"+os.getenv('HOMEPATH')+'\\Downloads\\'+mapID+'_'+mapNameText+'.zip'
                mapDestination = "C:"+os.getenv('HOMEPATH')+'\\Downloads\\'+mapID+'_'+mapNameText
                with zipfile.ZipFile(mapZipDir, 'r') as zip_ref:
                    zip_ref.extractall(mapDestination)
                if os.path.isdir(mapDestination):
                    print("["+bcolors.green+"+"+bcolors.reset+"] Map files extracted successfully! Deleting .zip file...")
                    os.remove(mapZipDir)
                    if not os.path.isfile(mapZipDir):
                        print("["+bcolors.green+"+"+bcolors.reset+'] Map .zip file deleted sucessfully! Moving map files to "Agilis\Maps"')
                        destination = os.path.join(pathlib.Path(__file__).parent.absolute(), "Maps")
                        newDir = shutil.move(mapDestination, destination)
                        if os.path.isdir(newDir):
                            print("["+bcolors.green+"+"+bcolors.reset+'] Moved to "Agilis\Maps" successfully! Moving .upk file to '+endModFolderPath)
                            for file in os.listdir(newDir):
                                if file.endswith(".udk"):
                                    file = Path(os.path.join(newDir, file))
                                    file = file.rename(file.with_suffix('.upk'))
                                    shutil.move(file, modFolderDir)
                        else:
                            print('['+bcolors.red+'!'+bcolors.reset+'] ERROR: Automatic Installation Failed - Please rename map .udk file to .upk and move to '+modFolderDir)
                            exit()
                    else:
                        print('['+bcolors.red+'!'+bcolors.reset+'] ERROR: Automatic Deletion Failed - Please delete map .zip file in your "Downloads" folder.')
                        exit()
                else:
                    print('['+bcolors.red+'!'+bcolors.reset+'] ERROR: Automatic Unzipping Failed - Please manually unzip map .zip file in your "Downloads" folder.')
                    exit()
            else:
                print("["+bcolors.red+'!'+bcolors.reset+"] ERROR: Agilis still couldn't find map download button. Please double check your URL is correct. Aborting.")
                exit()

    except shutil.Error:
        try:
            print("["+bcolors.yellow+"*"+bcolors.reset+'] Existing '+mapID+'_'+mapNameText+" folder found! Finishing map installation anyway...")
            destination = os.path.join(pathlib.Path(__file__).parent.absolute(), "Maps")
            newDir = shutil.move(mapDestination, destination)
            if os.path.isdir(newDir):
                print("["+bcolors.green+"+"+bcolors.reset+'] Moved to "Agilis\Maps" successfully! Moving .upk file to '+endModFolderPath)
                for file in os.listdir(newDir):
                    if file.endswith(".udk"):
                        file = Path(os.path.join(newDir, file))
                        file = file.rename(file.with_suffix('.upk'))
                        shutil.move(file, modFolderDir)
            else:
                print('['+bcolors.red+'!'+bcolors.reset+'] ERROR: Automatic Installation Failed - Please rename map .udk file to .upk and move to '+modFolderDir)
                exit()

        except shutil.Error:
            destination = os.path.join(pathlib.Path(__file__).parent.absolute(), "Maps")
            newDir = destination+'\\'+mapID+'_'+mapNameText
            if os.path.isdir(newDir):
                print("["+bcolors.green+"+"+bcolors.reset+'] Moved to "Agilis\Maps" successfully! Moving .upk file to '+endModFolderPath)
                cleanupDir = "C:"+os.getenv('HOMEPATH')+'\\Downloads\\'+mapID+'_'+mapNameText
                if os.path.isdir(cleanupDir):
                    shutil.rmtree(cleanupDir)
                for file in os.listdir(newDir):
                    if file.endswith(".udk"):
                        file = Path(os.path.join(newDir, file))
                        file = file.rename(file.with_suffix('.upk'))
                        shutil.move(file, modFolderDir)
                    preInstalledMap = 1
            else:
                print('['+bcolors.red+'!'+bcolors.reset+'] ERROR: Automatic Installation Failed - Please rename map .udk file to .upk and move to '+modFolderDir)
                exit()

    except Exception:
        try:
            print("["+bcolors.red+'!'+bcolors.reset+"] ERROR: Map download button not found! Please double check your URL is correct and paste it in the website textbox.")
            input("Press Enter to continue . . .")
            url = pyperclip.paste()
            mapID = url.replace("https://steamcommunity.com/sharedfiles/filedetails/?id=","")
            mapID = mapID.replace("&searchtext=","")
            downloadButton = web.find_element_by_xpath('//*[@id="root"]/main/div[3]/div/div/div/div/div[2]/div[2]/span/button')
            downloadButtonText = downloadButton.text
            successfulDownload = "Download"
            downloadComplete = "Downloaded"
            if successfulDownload == downloadButtonText:
                mapName = web.find_element_by_xpath('//*[@id="root"]/main/div[3]/div/div/div/div/div[1]/div[2]/h6/a/strong')
                mapNameText = mapName.text

                mapNameText = re.sub(r'(?<!^)(?=[A-Z])', '_', mapNameText).lower()
                mapNameText = mapNameText.translate ({ord(c): "_" for c in "!@#$%^""&*()[]{};:,./'<>?\|`~-=+"})
                mapNameText = mapNameText.replace(" ","_")
                mapNameText = mapNameText.replace("____","_")
                mapNameText = mapNameText.replace("___","_")
                mapNameText = mapNameText.replace("__","_")
                if mapNameText.endswith('_'):
                    mapNameText = mapNameText[:-1]
                if mapNameText.startswith('_'):
                    mapNameText = mapNameText[+1:]

                print("["+bcolors.green+"+"+bcolors.reset+"] Successfully found map download!")
                downloadButton.click()
                print("["+bcolors.yellow+"*"+bcolors.reset+'] Waiting for download to finish...')
                while downloadButtonText != downloadComplete:
                    time.sleep(1)
                    downloadButton = web.find_element_by_xpath('//*[@id="root"]/main/div[3]/div/div/div/div/div[2]/div[2]/span/button')
                    downloadButtonText = downloadButton.text
                print("["+bcolors.green+"+"+bcolors.reset+"] Download completed! Extracting files...")
                time.sleep(5)
                web.quit()
                mapZipDir = "C:"+os.getenv('HOMEPATH')+'\\Downloads\\'+mapID+'_'+mapNameText+'.zip'
                mapDestination = "C:"+os.getenv('HOMEPATH')+'\\Downloads\\'+mapID+'_'+mapNameText
                with zipfile.ZipFile(mapZipDir, 'r') as zip_ref:
                    zip_ref.extractall(mapDestination)
                if os.path.isdir(mapDestination):
                    print("["+bcolors.green+"+"+bcolors.reset+"] Map files extracted successfully! Deleting .zip file...")
                    os.remove(mapZipDir)
                    if not os.path.isfile(mapZipDir):
                        print("["+bcolors.green+"+"+bcolors.reset+'] Map .zip file deleted sucessfully! Moving map files to "Agilis\Maps"')
                        destination = os.path.join(pathlib.Path(__file__).parent.absolute(), "Maps")
                        newDir = shutil.move(mapDestination, destination)
                        if os.path.isdir(newDir):
                            print("["+bcolors.green+"+"+bcolors.reset+'] Moved to "Agilis\Maps" successfully! Moving .upk file to '+endModFolderPath)
                            for file in os.listdir(newDir):
                                if file.endswith(".udk"):
                                    file = Path(os.path.join(newDir, file))
                                    file = file.rename(file.with_suffix('.upk'))
                                    shutil.move(file, modFolderDir)
                        else:
                            print('['+bcolors.red+'!'+bcolors.reset+'] ERROR: Automatic Installation Failed - Please rename map .udk file to .upk and move to '+modFolderDir)
                            exit()
                    else:
                        print('['+bcolors.red+'!'+bcolors.reset+'] ERROR: Automatic Deletion Failed - Please delete map .zip file in your "Downloads" folder.')
                        exit()
                else:
                    print('['+bcolors.red+'!'+bcolors.reset+'] ERROR: Automatic Unzipping Failed - Please manually unzip map .zip file in your "Downloads" folder.')
                    exit()
            else:
                print("["+bcolors.red+'!'+bcolors.reset+"] ERROR: Agilis still couldn't find map download button. Aborting.")
                exit()

        except shutil.Error:
            try:
                print("["+bcolors.yellow+"*"+bcolors.reset+'] Existing '+mapID+'_'+mapNameText+" folder found! Finishing map installation anyway...")
                destination = os.path.join(pathlib.Path(__file__).parent.absolute(), "Maps")
                newDir = shutil.move(mapDestination, destination)
                if os.path.isdir(newDir):
                    print("["+bcolors.green+"+"+bcolors.reset+'] Moved to "Agilis\Maps" successfully! Moving .upk file to '+endModFolderPath)
                    for file in os.listdir(newDir):
                        if file.endswith(".udk"):
                            file = Path(os.path.join(newDir, file))
                            file = file.rename(file.with_suffix('.upk'))
                            shutil.move(file, modFolderDir)
                else:
                    print('['+bcolors.red+'!'+bcolors.reset+'] ERROR: Automatic Installation Failed - Please rename map .udk file to .upk and move to '+modFolderDir)
                    exit()

            except shutil.Error:
                destination = os.path.join(pathlib.Path(__file__).parent.absolute(), "Maps")
                newDir = destination+'\\'+mapID+'_'+mapNameText
                if os.path.isdir(newDir):
                    print("["+bcolors.green+"+"+bcolors.reset+'] Moved to "Agilis\Maps" successfully! Moving .upk file to '+endModFolderPath)
                    cleanupDir = "C:"+os.getenv('HOMEPATH')+'\\Downloads\\'+mapID+'_'+mapNameText
                    if os.path.isdir(cleanupDir):
                        shutil.rmtree(cleanupDir)
                    for file in os.listdir(newDir):
                        if file.endswith(".udk"):
                            file = Path(os.path.join(newDir, file))
                            file = file.rename(file.with_suffix('.upk'))
                            shutil.move(file, modFolderDir)
                        preInstalledMap = 1
                else:
                    print('['+bcolors.red+'!'+bcolors.reset+'] ERROR: Automatic Installation Failed - Please rename map .udk file to .upk and move to '+modFolderDir)
                    exit()

def bakkesmod_setup():
    bakkesmodDefaultDir = "C:\Program Files\BakkesMod\BakkesMod.exe"
    if os.path.isfile(bakkesmodDefaultDir):
        print("["+bcolors.green+"+"+bcolors.reset+"] BakkesMod is already installed!")
    else:
        print("["+bcolors.green+"+"+bcolors.reset+"] BakkesMod is not installed, running installer...")
        app = Application(backend='uia').start('Resources\\BakkesModSetup\\BakkesModSetup.exe').connect(title='Setup',timeout=15)
        app.Setup.Yes.click()
        app = Application(backend='uia').connect(title='Setup - BakkesMod version 3.0',timeout=20)
        app.SetupBakkesModVersion.Next.click()
        app.SetupBakkesModVersion.NextButton.click()
        app.SetupBakkesModVersion.Install.click()
        app.SetupBakkesModVersion.No.click()
        app.SetupBakkesModVersion.Finish.click()
        if os.path.isfile(bakkesmodDefaultDir):
            print("["+bcolors.green+"+"+bcolors.reset+"] BakkesMod has successfully been installed!")
        else:
            print('['+bcolors.red+'!'+bcolors.reset+'] ERROR: Automatic Installation Failed - Please install manually using the "BakkesModSetup.exe" file found in the "Resources" folder.')
            exit()

def rocket_plugin_setup():
    rocketPluginDir = os.getenv('APPDATA')+"\\bakkesmod\\bakkesmod\\plugins\\RocketPlugin.dll"
    if os.path.isfile(rocketPluginDir):
        print("["+bcolors.green+"+"+bcolors.reset+"] Rocket Plugin is already installed!")
    else:
        print("["+bcolors.green+"+"+bcolors.reset+"] Rocket Plugin is not installed, running installer...")
        os.system('Resources\\rocket_plugin.bat')
        if os.path.isfile(rocketPluginDir):
            print("["+bcolors.green+"+"+bcolors.reset+"] Rocket Plugin has successfully been installed!")
        else:
            print('['+bcolors.red+'!'+bcolors.reset+'] ERROR: Automatic Installation Failed - Please manually copy the "data" and "plugins" folders found in "Resources\RocketPlugin_0_6_6" into your BakkesMod folder.')
            exit()

def hamachi_setup():
    hamachiDefaultDir = "C:\\Program Files (x86)\\LogMeIn Hamachi\\hamachi-2-ui.exe"
    if os.path.isfile(hamachiDefaultDir):
        print("["+bcolors.green+"+"+bcolors.reset+"] LogMeIn Hamachi is already installed!")
    else:
        print("["+bcolors.green+"+"+bcolors.reset+"] LogMeIn Hamachi is not installed, running installer...")
        app = Application(backend='uia').start(r'msiexec.exe /i Resources\hamachi.msi').connect(title='LogMeIn Hamachi Setup',timeout=15)
        app.LogMeInHamachiSetup.Next.click()
        app.LogMeInHamachiSetup.CheckBox.click()
        app.LogMeInHamachiSetup.Next.click()
        app.LogMeInHamachiSetup.Next.click()
        app.LogMeInHamachiSetup.Install.click()
        app.LogMeInHamachiSetup.Finish.wait('enabled', timeout=75)
        app.LogMeInHamachiSetup.Finish.click()
        app.LogMeInHamachiSetup.Finish.wait_not('visible')
        app = Application(backend='uia').connect(title='LogMeIn Hamachi',timeout=30)
        app.LogMeInHamachi.Power.wait('visible')
        app.LogMeInHamachi.Power.click()
        if os.path.isfile(hamachiDefaultDir):
            print("["+bcolors.green+"+"+bcolors.reset+"] LogMeIn Hamachi has successfully been installed!")
        else:
            print('['+bcolors.red+'!'+bcolors.reset+'] ERROR: Automatic Installation Failed - Please install manually using the "hamachi.msi" file found in the "Resources" folder.')
            exit()

def execute():
    if not is_running_as_admin():
        print('['+bcolors.red+'!'+bcolors.reset+'] Agilis is NOT running with administrative privileges! Use the "Launcher" shortcut!')
    else:
        print("["+bcolors.green+"+"+bcolors.reset+"] Agilis is running with administrative privileges!")
        unzip()
        workshop_textures_setup()
        map_downloader()
        bakkesmod_setup()
        rocket_plugin_setup()
        hamachi_setup()
        if preInstalledMap == 1:
            print("["+bcolors.green+"+"+bcolors.reset+"] Agilis finished successfully even though the chosen map was already installed!")
        else:
            print("["+bcolors.green+"+"+bcolors.reset+"] Agilis Finished!")

if __name__ == '__main__':
    execute()

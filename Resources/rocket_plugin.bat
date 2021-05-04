@echo off
cd Resources
xcopy.exe /E /I /Y RocketPlugin_0_6_6\data %appdata%\bakkesmod\bakkesmod\data >NUL
xcopy.exe /E /I /Y RocketPlugin_0_6_6\plugins %appdata%\bakkesmod\bakkesmod\plugins >NUL
import winreg
from datetime import datetime
import time
import ctypes


hkey = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
subKey = winreg.OpenKey(hkey, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize", 0, winreg.KEY_ALL_ACCESS)
subKey2 = winreg.OpenKey(hkey, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_ALL_ACCESS)
winreg.SetValueEx(subKey2, "ThemeChanger", 0, winreg.REG_SZ, r"C:\ThemeChanger\ThemeChanger.exe")

whiteHours = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,18]

class Theme:
    def __init__(self,code,wallpaper):
        self.code = code
        self.wallpaper = wallpaper

    def getCode(self):
        return self.code

    def getWallpaper(self):
        return self.wallpaper

class DarkTheme(Theme):

    def __init__(self):
        Theme.__init__(self,0,r"C:\ThemeChanger\Wallpapers\DarkWallpaper.jpg")

class WhiteTheme(Theme):

    def __init__(self):
        Theme.__init__(self,1,r"C:\ThemeChanger\Wallpapers\WhiteWallpaper.jpg")        


whiteTheme = WhiteTheme()
darkTheme = DarkTheme()

def changeTheme(theme):
    winreg.SetValueEx(subKey, "AppsUseLightTheme", 0, winreg.REG_DWORD, theme.getCode())
    winreg.SetValueEx(subKey, "SystemUsesLightTheme", 0, winreg.REG_DWORD, theme.getCode())
    ctypes.windll.user32.SystemParametersInfoW(0x14, 0, theme.getWallpaper(),0x2)

while True:
    currentTheme = winreg.EnumValue(subKey, 2)
    currentTheme = currentTheme[1]

    hour = datetime.now().hour

    if hour in whiteHours:
        if currentTheme != 1:
            changeTheme(whiteTheme)
    else:
        if currentTheme != 0:
            changeTheme(darkTheme)
    
    time.sleep(5)
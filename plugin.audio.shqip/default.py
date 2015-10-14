#-*- coding: utf-8 -*-
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import urllib,re,string,os,time,threading

#try:
#    from resources.libs import main, settings
#except Exception, e:
#    dialog = xbmcgui.Dialog()
#    ok=dialog.ok('[B][COLOR=FF67cc33]RadioNL Import Error[/COLOR][/B]','Failed To Import Needed Modules',str(e),'Main and Settings module')
#    xbmc.log('RadioNL ERROR - Importing Modules: '+str(e), xbmc.LOGERROR)

#################### Set Environment ######################
ENV = "Dev"  # "Prod" or "Dev"
###########################################################

addon_id = 'plugin.audio.radionl'
selfAddon = xbmcaddon.Addon(id=addon_id)

master_json = "https://raw.githubusercontent.com/mpie/doofree/master/json/master.json"
'''
UpdatePath=os.path.join(main.datapath,'Update')
try: os.makedirs(UpdatePath)
except: pass
CachePath=os.path.join(main.datapath,'Cache')
try: os.makedirs(CachePath)
except: pass
CookiesPath=os.path.join(main.datapath,'Cookies')
try: os.makedirs(CookiesPath)
except: pass
TempPath=os.path.join(main.datapath,'Temp')
try: os.makedirs(TempPath)
except: pass
'''

def getKeyboardInput():
    keyboard = xbmc.Keyboard('')
    keyboard.doModal()
    if (keyboard.isConfirmed()):
        return keyboard.getText()

######## PARAMS and stuff ########
def get_params():
    param=[]
    paramstring=sys.argv[2]
    if len(paramstring)>=2:
        params=sys.argv[2]
        cleanedparams=params.replace('?','')
        if (params[len(params)-1]=='/'):
            params=params[0:len(params)-2]
        pairsofparams=cleanedparams.split('&')
        param={}
        for i in range(len(pairsofparams)):
            splitparams={}
            splitparams=pairsofparams[i].split('=')
            if (len(splitparams))==2:
                param[splitparams[0]]=splitparams[1]
    return param

params=get_params()

url=None
name=None
mode=None
iconimage=None
fanart=None
plot=None
genre=None
title=None
season=None
episode=None
location=None
path=None

try: name=urllib.unquote_plus(params["name"])
except: pass
try: url=urllib.unquote_plus(params["url"])
except: pass
try: mode=int(params["mode"])
except: pass
try:
    iconimage=urllib.unquote_plus(params["iconimage"])
    iconimage = iconimage.replace(' ','%20')
except: pass
try: plot=urllib.unquote_plus(params["plot"])
except: pass
try:
    fanart=urllib.unquote_plus(params["fanart"])
    fanart = fanart.replace(' ','%20')
except: pass
try: genre=urllib.unquote_plus(params["genre"])
except: pass
try: title=urllib.unquote_plus(params["title"])
except: pass
try: episode=int(params["episode"])
except: pass
try: season=int(params["season"])
except: pass
try: location=urllib.unquote_plus(params["location"])
except: pass
try: path=urllib.unquote_plus(params["path"])
except: pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "Thumb: "+str(iconimage)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
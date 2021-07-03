#Weather Forcast
#Icon GNU General Public License v3.0
import tkinter, requests
from tkinter import BOTH, IntVar
from PIL import ImageTk, Image
from io import BytesIO

#Define window
root = tkinter.Tk()
root.title('Weather Forcast')
root.iconbitmap('weather.ico')
root.geometry('400x400')
root.resizable(0,0)

#Define fonts and colors
sky_color = "#76c3ef"
grass_color = "#aad207"
output_color = "#dcf0fb"
input_color = "#ecf2ae"
large_font = ('SimSun', 14)
small_font = ('SimSun', 10)

#Define functions
def search():
    """Use open weather api to look up current weather conditions given a city and country"""
    
    global response
    #Example response return.
    '''{"coord":{"lon":-73.97,"lat":42.6},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],
    "base":"stations","main":{"temp":73.4,"feels_like":73.9,"temp_min":72,"temp_max":75,"pressure":1000,"humidity":77},
    "wind":{"speed":9.06,"deg":258},"clouds":{"all":76},"dt":1594551984,"sys":{"type":3,"id":19530,"country":"US","sunrise":1594546166,
    "sunset":1594600397},"timezone":-14400,"id":5106841,"name":"Albany","cod":200}'''

    #Get API response
    url = "https://community-open-weather-map.p.rapidapi.com/weather"
    
    #Search by the appropriate query, either city name or zip
    if search_method.get() == 1:
        querystring = {"q": city_entry.get(), "units":"imperial"}
    elif search_method.get() == 2:
        querystring = {"zip":city_entry.get(), "units":"imperial"}

    #Post your own api key!!!
    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "c42126af80msh78e27579e963d14p1d5209jsnb5d3ce6de98d"
        }

    #6da92ea5e09090fa9c8a08e08eb30284
    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.json()

    get_weather()
    get_icon()


def get_weather():
    """Grab information from API response and update labels"""
    #Gather the data to be used from response
    city_name = response['name']
    city_lat = str(response['coord']['lat'])
    city_lon = str(response['coord']['lon'])

    main_weather = response['weather'][0]['main']
    description = response['weather'][0]['description']

    temp = str(response['main']['temp'])
    feels_like = str(response['main']['feels_like'])
    temp_min = str(response['main']['temp_min'])
    temp_max = str(response['main']['temp_max'])
    humidity = str(response['main']['humidity'])

    #Update output lables
    city_info_label.config(text=city_name + "(" + city_lat + ", " + city_lon + ")", font=large_font, bg=output_color)
    weather_label.config( text="Weather: " + main_weather + ", " + description, font=small_font, bg=output_color)
    temp_label.config(text='Temperature: ' + temp + " F", font=small_font, bg=output_color)
    feels_label.config(text='Feels Like: ' + feels_like + " F", font=small_font, bg=output_color)
    temp_min_label.config(text='Min Temperature: ' + temp_min + " F", font=small_font, bg=output_color)
    temp_max_label.config(text='Max Temperature: ' + temp_max + " F", font=small_font, bg=output_color)
    humidity_label.config(text='Humidity: ' + humidity, font=small_font, bg=output_color)


def get_icon():
    """Get the approrpiate weather icon from API response"""
    #Get and display weather icon
    #To prevent garbage collection of photo, make global
    global img
    global response

    #Get the icon id from API response.  
    icon_id = response['weather'][0]['icon']

    #Check OWM documentation for how icon_id corresponds to url.
    url = 'http://openweathermap.org/img/wn/{icon}.png'.format(icon=icon_id)

    #Make a request at the url to dl icon; stream=True automatically dl
    response = requests.get(url, stream=True)

    #Turn into form tkinter can use
    img_data = response.content
    img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))

    #Update label
    photo_label.config(image=img)


#Define GUI Layout
#Create frames
sky_frame = tkinter.Frame(root, bg=sky_color, height=250)
grass_frame = tkinter.Frame(root, bg=grass_color)
sky_frame.pack(fill=BOTH, expand=True)
grass_frame.pack(fill=BOTH, expand=True)

output_frame = tkinter.LabelFrame(sky_frame, bg=output_color, width=325, height=225)
input_frame = tkinter.LabelFrame(grass_frame, bg=input_color, width=325)
output_frame.pack(pady=30)
#Call pack_propagate(0) to keep frame size regardless of what is inside on output_frame
output_frame.pack_propagate(0)
input_frame.pack(pady=15)

#Output frame layout
#Create labels for output frame weather data
city_info_label = tkinter.Label(output_frame, bg=output_color)
weather_label = tkinter.Label(output_frame, bg=output_color)
temp_label = tkinter.Label(output_frame, bg=output_color)
feels_label = tkinter.Label(output_frame, bg=output_color)
temp_min_label = tkinter.Label(output_frame, bg=output_color)
temp_max_label = tkinter.Label(output_frame, bg=output_color)
humidity_label = tkinter.Label(output_frame, bg=output_color)
photo_label = tkinter.Label(output_frame, bg=output_color)

city_info_label.pack(pady=8)    
weather_label.pack()
temp_label.pack()
feels_label.pack()
temp_min_label.pack()
temp_max_label.pack()
humidity_label.pack()
photo_label.pack(pady=8)

#Input frame layout
#Create input frame buttons and entry
city_entry = tkinter.Entry(input_frame, width=20, font=large_font)
submit_button = tkinter.Button(input_frame, text="Submit", font=large_font, bg=input_color, command=search)
search_method = IntVar()
search_method.set(1)
search_city = tkinter.Radiobutton(input_frame, text="Search by city name", variable=search_method, value=1, font=small_font, bg=input_color)
search_zip = tkinter.Radiobutton(input_frame, text="Search by zipcode", variable=search_method, value=2, font=small_font, bg=input_color)

city_entry.grid(row=0, column=0, padx=10, pady=(10,0))
submit_button.grid(row=0, column=1, padx=10, pady=(10,0))
search_city.grid(row=1, column=0, pady=2)
search_zip.grid(row=1, column=1, padx=5, pady=2)

#Run the root window's main loop
root.mainloop()

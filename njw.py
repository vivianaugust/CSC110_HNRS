from urllib.request import urlopen
import datetime
import json
from graphics_file import graphics
import re

url2 = """https://tinyurl.com/pytinymoon"""
response2 = urlopen(url2)
moon_data = json.loads(response2.read())


def change_url():
    global data
    city = input('Type your nearest National Weather Service City: ').capitalize()
    state = input('Which state is it in? (if it\'s outside of the united states, type the country): ').capitalize()
    code = 'TWC'
    x = 32
    y = -110
    f = open('codes - Sheet1.csv', 'r')
    places = []
    for line in f:
        place_1 = line.strip('\n').split(' ')
        for v in place_1:
            place = re.split(',', v)
        for value in place:
            places.append(value)
    if city not in places or state not in places:
        city = input('\nYour city or state is not a valid national weather service city. Please try again.\n'
                     'For a list of accepted cities, visit '
                     'https://en.wikipedia.org/wiki/List_of_National_Weather_Service_Weather_Forecast_Offices.\n\n'
                     'New City: ').capitalize()
        state = input('New State: ').capitalize()
    for line in f:
        ln = line.strip('\n').split(',')
        if city in ln and state in ln:
            code = ln[-1]
    f.close()
    f_2 = open('4letter - Sheet1.csv', 'r')
    f_3 = open('nws - Sheet1.csv', 'r')
    for line in f_2:
        lr = line.strip('\n').split(',')
        if code in lr:
            code = lr[-1]
        if lr[-1] not in f_3:
            f_4 = open('second - Sheet1.csv', 'r')
            for lin in f_4:
                li = lin.strip('\n').split(',')
                for v in li:
                    if city in v:
                        x = li[-2]
                        y = li[-1]
        else:
            for lines in f_3:
                tl = lines.strip('\n').split(',')
                if code in tl:
                    x = tl[-2]
                    y = tl[-1]
    url = "https://api.weather.gov/points/" + str(x) + ',' + str(y)
    response = urlopen(url)
    source = json.loads(response.read())
    new_url = source["properties"]["forecastHourly"]
    try:
        next = urlopen(new_url)
    except:
        print('The forecast for', city, 'is currently unavailable. Please try again later. If this error continues,'
                                        ' please contact support at sdb.support@noaa.gov.')
        quit()
    else:
        data = json.loads(next.read())
        return data


class Weather:
    """
    This class defines two functions.
    1) draw_forecast(): Takes the daily high and low temps, and a short summary and outputs a text based visualization.
    2) graph(): Using all objects and both data sets, displays images and text in a graphics interface w/Tkinter.

    The other function (__init__()) defines 6 objects.
    1) day_of_week: a list of the days of the week from today + 6 days in string format, len(day_of_week) = 7
    2) daily_high: a list of integers of the high temperatures for each day of the week, len(daily_high) = 7
    3) daily_low: a list of integers of the low temperatures for each day of the week, len(daily_low) = 7
    4) short_summary: a list of the short forecasts for each day of the week in string format, len(short_summary) = 7
    5) fast_wind: a list of the fast wind speeds for each day of the week, len(fast_wind) = 7
    6) slow_wind: a list of the slow wind speeds for each day of the week, len(slow_wind) = 7
    """

    def __init__(self, day_of_week, daily_high, daily_low, short_summary, fast_wind, slow_wind):
        self.day_of_week = day_of_week
        self.daily_high = daily_high
        self.daily_low = daily_low
        self.short_summary = short_summary
        self.fast_wind = fast_wind
        self.slow_wind = slow_wind

    def graph(self):
        """
        Using all objects and both data sets, displays images and text in a graphics interface w/Tkinter.
        :return N/A: gui.draw() displays the graphics written in this function
        """
        all_images = ['lll.png', 'lll2.png', 'lll3.png', 'lll4.png', 'lll5.png', 'lll6.png', 'iii.png', 'iii2.png',
                      'iii3.png', 'iii4.png', 'iii5.png', 'iii6.png', 'love.png', 'love2.png', 'love3.png',
                      'love4.png',
                      'love5.png', 'love6.png', 'snow.png', 'snow2.png', 'snow3.png', 'snow4.png', 'snow5.png',
                      'snow6.png', 'rain.png', 'rain2.png', 'rain3.png', 'rain4.png', 'rain5.png', 'rain6.png',
                      'smile.png', 'smile2.png', 'smile3.png', 'smile4.png', 'smile5.png', 'smile6.png',
                      'inkpx-word-art.png', 'inkpx-word-art2.png', 'inkpx-word-art3.png', 'inkpx-word-art4.png',
                      'inkpx-word-art5.png', 'inkpx-word-art6.png']
        # scales stores the downsizing integers for each image of the days of the week.
        scales = []
        # images stores all the files associated with each image for the day of the week.
        images = {}
        # printing is a list containing the chosen file for each image in images.
        printing = []
        # create the canvas to add graphics to
        gui = graphics('Weather')
        w = gui.primary.winfo_screenwidth()
        h = gui.primary.winfo_screenheight()
        difference = int((w * (3 / 1440)) - 3)
        locations = [(h / 2) - 265, (h / 2) - 265 + 90, (h / 2) - 265 + 2 * 90, (h / 2) - 265 + 3 * 90, (h / 2) - 265
                     + 4 * 90, (h / 2) - 265 + 5 * 90]
        if data["properties"]["periods"][1]["isDaytime"]:
            gui.image(0, 0, 1, 3 - difference, "sky.png")
        else:
            gui.image(0, 0, 1, 3 - difference, "night.png")
        # create the logo for pink sky
        gui.image((w / 2) - 155, 0, 1, 2, "pngegg.png")
        gui.image((w / 2) - 25, 50, 1, 30, "moon.png")
        gui.image((w / 2) - 105, 100, 1, 5, "l.png")
        # A = '<KeyPress>'
        # gui.set_keyboard_action((gui.text((w / 2) + 275, 100, A, 'black', 17)).A)
        # two rectangles to organize the information for the current weekday and the upcoming weekdays.
        gui.rectangle((w / 2) + 49, (h / 2) - 265, 515, 545, 'lavender blush')
        gui.rectangle((w / 2) - 564, (h / 2) - 265, 515, 545, 'lavender blush')
        # loops through the list of short summaries for the next 6 days, and appends the images and scales lists.
        i = 0
        while i < len(self.short_summary):
            if self.short_summary[i] == "Showers And Thunderstorms" or \
                    self.short_summary[i] == "Slight Chance Showers And Thunderstorms" or \
                    self.short_summary[i] == "Chance Showers And Thunderstorms":
                image = [all_images[0], all_images[1], all_images[2], all_images[3], all_images[4], all_images[5]]
                if image not in list(images.values()):
                    images.update({image[0]: image})
                else:
                    images.update({'repeat' + str(i): image[0]})
                scale = 7
                scales.append(scale)
            elif self.short_summary[i] == "Sunny":
                image = [all_images[6], all_images[7], all_images[8], all_images[9], all_images[10], all_images[11]]
                if image not in list(images.values()):
                    images.update({image[0]: image})
                else:
                    images.update({'repeat' + str(i): image[0]})
                scale = 29
                scales.append(scale)
            elif self.short_summary[i] == "Partly Cloudy" or self.short_summary[i] == "Mostly Sunny" \
                    or self.short_summary[i] == "Partly Sunny":
                image = [all_images[12], all_images[13], all_images[14], all_images[15], all_images[16],
                         all_images[17]]
                if image not in list(images.values()):
                    images.update({image[0]: image})
                else:
                    images.update({'repeat' + str(i): image[0]})
                scale = 32
                scales.append(scale)
            elif self.short_summary[i] == "Snow Showers Likely":
                image = [all_images[18], all_images[19], all_images[20], all_images[21], all_images[22],
                         all_images[23]]
                if image not in list(images.values()):
                    images.update({image[0]: image})
                else:
                    images.update({'repeat' + str(i): image[0]})
                scale = 3
                scales.append(scale)
            elif self.short_summary[i] == "Rain Showers" or self.short_summary[i] == "Chance Rain Showers" \
                    or self.short_summary[i] == "Rain Showers Likely" or \
                    self.short_summary[i] == "Slight Chance Rain Showers":
                image = [all_images[24], all_images[25], all_images[26], all_images[27], all_images[28],
                         all_images[29]]
                if image not in list(images.values()):
                    images.update({image[0]: image})
                else:
                    images.update({'repeat' + str(i): image[0]})
                scale = 27
                scales.append(scale)
            elif self.short_summary[i] == "Mostly Cloudy":
                image = [all_images[30], all_images[31], all_images[32], all_images[33], all_images[34],
                         all_images[35]]
                if image not in list(images.values()):
                    images.update({image[0]: image})
                else:
                    images.update({'repeat' + str(i): image[0]})
                scale = 8
                scales.append(scale)
            # if the short summary does not exist within the if statements above, the image is of a cute bird.
            else:
                image = [all_images[36], all_images[37], all_images[38], all_images[39], all_images[40],
                         all_images[41]]
                if image not in list(images.values()):
                    images.update({image[0]: image})
                else:
                    images.update({'repeat' + str(i): image[0]})
                scale = 30
                scales.append(scale)
            i += 1
            # starting at j = 0, print the upcoming day of the week, high, low, and short summary in increments of y=90.
            j = 0
            while j < len(locations):
                gui.text((w / 2) + 49 + 101, locations[j], self.day_of_week[j + 1].capitalize(), 'medium violet red'
                         , 20)
                gui.text((w / 2) + 49 + 101, locations[j] + 35, 'High: ' + str(self.daily_high[j + 1]) + '.....'
                         + self.short_summary[j + 1], 'dark orchid', 17)
                gui.text((w / 2) + 49 + 101, locations[j] + 60, 'Low: ' + str(self.daily_low[j + 1]), 'dark orchid',
                         17)
                j += 1
        # this loop checks if there are any repeated images by setting previous_image to image1 and appending
        # a specific file in images for that day of the week to printing
        # if the current image is equal to the previous image.
        copy = images.copy()
        for key, value in copy.items():
            if key[:6] != 'repeat':
                im = value.pop(0)
                printing.append(im)
            else:
                im = copy[value].pop(0)
                printing.append(im)
        j = 1
        while j < len(locations) + 1:
            if printing[j][1:4] in 'inkpx-word-art.png':
                gui.image((w / 2) + 49 - 22, locations[j - 1], 1, scales[j], printing[j])
            else:
                gui.image((w / 2) + 49, locations[j - 1], 1, scales[j], printing[j])
            j += 1
        # the next set of lines pulls from moon_data, and checks the moonphase value. Depending on the value,
        # a different image is associated with moon, and a different scale as well.
        # *I still need to check the scales for each moon*
        # there are also cute little quotes for some of the phases of the moon displayed in text.
        moon = ''
        moon_scale = 1
        if moon_data["days"][0]["moonphase"] == 0:
            moon = 'new_moon.png'
            moon_scale = 2
        if 0 < moon_data["days"][0]["moonphase"] < 0.25:
            moon = 'waxing_crescent.png'
            moon_scale = 3
        if moon_data["days"][0]["moonphase"] == 0.25:
            moon = 'first_quarter.png'
            moon_scale = 3
        if 0.25 < moon_data["days"][0]["moonphase"] < 0.5:
            moon = 'waxing_gibbous.png'
            moon_scale = 2
        if moon_data["days"][0]["moonphase"] == 0.5:
            moon = 'full_moon.png'
        if 0.5 < moon_data["days"][0]["moonphase"] < 0.75:
            moon = 'waning_gibbous.png'
            moon_scale = 3
        if moon_data["days"][0]["moonphase"] == 0.75:
            moon = 'last_quarter.png'
            moon_scale = 3
        if 0.75 < moon_data["days"][0]["moonphase"] < 1:
            moon = 'waning_crescent.png'
            moon_scale = 4
        if 0.75 < moon_data["days"][0]["moonphase"] == 1:
            moon = 'moon.png'
            moon_scale = 4
        # Display the selected moon and moon scale.
        gui.image((w / 2) - 565, (h / 2) - 265, 1, moon_scale, moon)
        # Make the image bigger for the current day of the week by subtracting 10 from the scale if possible.
        keys = list(images.keys())
        if scales[0] > 11:
            gui.image((w / 2) - 200, (h / 2) + 145, 1, scales[0] - 10, images[keys[0]][0])
        else:
            gui.image((w / 2) - 200, (h / 2) + 145, 1, scales[0], images[keys[0]][0])
        # Display the current day of the week, high and low temp, and fast and slow wind speed.
        for i in range(6):
            gui.text((w / 2) - 565, (h / 2) - 55, self.day_of_week[0].capitalize(), 'medium violet red', 30)
            gui.text((w / 2) - 565, (h / 2) + 5,
                     'High: ' + str(self.daily_high[0]) + '........' + self.short_summary[0],
                     'dark orchid', 17)
            gui.text((w / 2) - 565, (h / 2) + 40, 'Low: ' + str(self.daily_low[0]), 'dark orchid', 17)
            gui.text((w / 2) - 564, (h / 2) + 95, 'High Wind Speed: ' + str(self.fast_wind[0]) + ' mph', 'dark orchid',
                     17)
            gui.text((w / 2) - 564, (h / 2) + 125, 'Low Wind Speed: ' + str(self.slow_wind[0]) + ' mph', 'dark orchid',
                     17)
            # Pulling from the moondata, we display text showing the time of the sunrise and sunset for the current day.
            if int(moon_data['days'][0]['sunrise'][0:2]) > 12:
                sunrise = str(int(moon_data['days'][0]['sunrise'][0:2]) - 12) + str(moon_data['days'][0]['sunrise'][2:])
                gui.text((w / 2) - 564, (h / 2) + 185, 'Sunrise: ' + sunrise + ' AM', 'dark orchid', 17)
            else:
                sunrise = str(moon_data['days'][0]['sunrise'])
                gui.text((w / 2) - 564, (h / 2) + 185, 'Sunrise: ' + sunrise + ' AM', 'dark orchid', 17)
            if int(moon_data['days'][0]['sunset'][0:2]) > 12:
                sunset = str(0) + str(int(moon_data['days'][0]['sunset'][0:2]) - 12) + str(
                    moon_data['days'][0]['sunset'][2:])
                gui.text((w / 2) - 564, (h / 2) + 215, 'Sunset: ' + ' ' + sunset + ' PM', 'dark orchid', 17)
            else:
                sunset = str(moon_data['days'][0]['sunset'])
                gui.text((w / 2) - 564, (h / 2) + 215, 'Sunset: ' + ' ' + sunset + ' PM', 'dark orchid', 17)
        # This method displays all the graphics planned above.
        gui.draw()


def main():
    """
    Three functions are written in this function in order to create the lists to define the objects in class Weather:
    1) high_low(): Loops through the 24 hours in a day, 12 periods and returns the high and low temperatures in a list.
        -param s: starting point and ending point
        -param e: ending point
        -return [high, low]: a list of length 2 containing the high and low temperatures for that day of the week.
    2) wind_speed(): Loops through the 24 hours in a day, 12 periods and finds the fast and slow wind speeds in a list.
        -param s: starting point and ending point
        -param e: ending point
        -return [fast, slow]: list of length 2 containing the fast and low wind speeds for that day of the week.
    3) summaries_list(): Loops through the 24 hours in a day, 12 periods and finds the mode of the short summaries.
        -param s: starting point and ending point
        -param e: ending point
        -return most_common_summary: a string of the most commonly referenced short forecast for that day.

    The function also loops through all the periods and detects when there is a new day, containing all the days of the
    week in a list (days_of_week).

    :return N/A: calls the weather class and its functions with new values for each object created as lists by main().
    """
    go = graphics('Weather')
    w = go.primary.winfo_screenwidth()
    h = go.primary.winfo_screenheight()
    difference = int((w * (3 / 1440)) - 3)
    # choosing the background image based on if isDaytime in first period of data is true or false.
    go.image(0, 0, 1, 3 - difference, "sky.png")
    go.rectangle(0, (h / 2) + 365, w, 35, 'yellow')
    go.text((w / 2) - 570, (h / 2) + 370, 'When you\'ve found your nearest National Weather Service city '
                                          'on the map, ex out of the tab, and type it into the terminal.', 'black', 17)
    # gui.rectangle((w / 2) - 609, (h / 2) - 320, 1206, 630-730, 'light slate blue')
    go.rectangle(0, (h / 2) - 265, w, 630, 'snow')
    go.image(0, (h / 2) - 265, 1, 1, 'cwa.png')
    go.text((w / 2) + 250, (h / 2) - 265, 'Welcome to Pink Sky!', 'medium violet red', 27)
    go.text(825, (h / 2) - 265, '\n\n\n'
                                'My name is Vivian Welch; I am the creator of this program.\n'
                                'My dream is to code the graphics for the National Weather\n'
                                'Service, providing fun and reliable sources of your daily weather.\n'
                                '\n'
                                'Pink Sky pulls data from the Weather Service, visualizing some of\n'
                                'the most accurate weather data in the country. There are\n'
                                '131 National Weather Service locations, including offices in\n'
                                'Alaska, Hawai\'i, Puerto Rico, and Guam.\n'
                                '\n'
                                'When choosing your local National Weather Service office, it\'s\n'
                                'important to recognize that some offices cover regions that\n'
                                'span multiple states.\n'
                                '\n'
                                'I\'m from New Jersey, but my forecasts come from the Philadelphia\n'
                                'weather station.\n'
                                '\n'
                                'For more information about National Weather Service locations,\n'
                                'visit https://www.weather.gov/srh/nwsoffices#.\n',
            'black', 17)
    # create the logo for pink sky
    go.image((w / 2) - 155, 0, 1, 2, "pngegg.png")
    go.image((w / 2) - 25, 50, 1, 30, "moon.png")
    go.image((w / 2) - 105, 100, 1, 5, "l.png")
    # A = '<KeyPress>'
    # gui.set_keyboard_action((gui.text((w / 2) + 275, 100, A, 'black', 17)).A)
    go.image(0, (h / 2) - 340, 1, 30, 'inkpx-word-art.png')
    go.image((w / 2) + 110, (h / 2) - 265, 1, 8, 'smile.png')
    go.image(w - 107, (h / 2) - 265, 1, 8, 'smile2.png')
    go.draw()
    change_url()

    def high_low(s, e):
        """
        Loops through the 24 hours in a day, 12 periods and returns the high and low temperatures in a list.
        :param s: starting point and ending point
        :param e: ending point
        :return [high, low]: a list of length 2 containing the high and low temperatures for that day of the week.
        """
        # Set high and low temperatures to check.
        low = data["properties"]["periods"][s + 1]["temperature"]
        high = data["properties"]["periods"][s]["temperature"]
        i = s
        # If we are starting at the first period, set the high temperature to the temperature for the first period.
        if s == 1:
            high = data["properties"]["periods"][1]["temperature"]
        # Until the given period to end at, check if the current temperature is greater than high or less than low.
        while i <= e:
            if data["properties"]["periods"][i]["temperature"] <= low:
                low = data["properties"]["periods"][i]["temperature"]
            elif data["properties"]["periods"][i]["temperature"] >= high:
                high = data["properties"]["periods"][i]["temperature"]
            i += 1
        # In a list return the high and low values.
        return [high, low]

    def wind_speed(s, e):
        """
        Loops through the 24 hours in a day, 12 periods and finds the fast and slow wind speeds in a list.
        :param s: starting point and ending point
        :param e: ending point
        :return [fast, slow]: list of length 2 containing the fast and low wind speeds for that day of the week.
        """
        # Set the slow and fast values to check.
        slow = int(data["properties"]["periods"][s + 1]["windSpeed"][0:2])
        fast = int(data["properties"]["periods"][s]["windSpeed"][0:2])
        i = s
        # If we are starting at the first period, set the fast wind speed to the wind speed for the first period.
        if s == 1:
            fast = int(data["properties"]["periods"][1]["windSpeed"][0:2])
        # Until the given period to end at, check if the current wind speed is greater than fast or less than slow.
        while i <= e:
            if int(data["properties"]["periods"][i]["windSpeed"][0:2]) <= slow:
                slow = int(data["properties"]["periods"][i]["windSpeed"][0:2])
            elif int(data["properties"]["periods"][i]["windSpeed"][0:2]) >= fast:
                fast = int(data["properties"]["periods"][i]["windSpeed"][0:2])
            i += 1
        # Return fast and slow in a list.
        return [fast, slow]

    def summaries_list(s, e):
        """
        Loops through the 24 hours in a day, 12 periods and finds the mode of the short summaries for that day.
        :param s: starting point and ending point
        :param e: ending point
        :return most_common_summary: a string of the most commonly referenced short forecast for that day.
        """
        i = s
        list_of_summaries = []
        mode = {}
        while i <= e:
            list_of_summaries.append(data["properties"]["periods"][i]["shortForecast"])
            i += 1
        # Find the mode of the summaries.
        for a in list_of_summaries:
            if a not in mode:
                mode[a] = 1
            else:
                mode[a] += 1
        most_common_summary = [b for b, l in mode.items() if l == max(mode.values())]
        return most_common_summary

    all_periods = data["properties"]["periods"]  # list with all periods
    previous_weekday = datetime.datetime(int(data["properties"]["periods"][1]["startTime"][:4]),
                                         int(data["properties"]["periods"][1]["startTime"][5:7]),
                                         int(data["properties"]["periods"][1]["startTime"][8:10])).strftime('%A')
    # Create list with finalized days to visualize.
    days_of_week = []
    indices = [1]
    # For each item in the list of periods
    for p in all_periods:
        # Grab that item.
        current_weekday = datetime.datetime(int(p["startTime"][:4]), int(p["startTime"][5:7]),
                                            int(p["startTime"][8:10])).strftime('%A')
        # Is it a different day?
        if current_weekday != previous_weekday:
            days_of_week.append(previous_weekday)
            previous_weekday = current_weekday
            indices.append(p['number'])
    # If the list of the days of the week is too short, add the day in the last period.
    if len(days_of_week) == 6:
        days_of_week.append(datetime.datetime(int(data["properties"]["periods"][-1]["startTime"][:4]),
                                              int(data["properties"]["periods"][-1]["startTime"][5:7]),
                                              int(data["properties"]["periods"][-1]["startTime"][8:10])).strftime(
            '%A'))
    # Compile lists of values for each day of the week.
    daily_high = [high_low(indices[0], indices[1])[0], high_low(indices[1], indices[2])[0],
                  high_low(indices[2], indices[3])[0], high_low(indices[3], indices[4])[0],
                  high_low(indices[4], indices[5])[0], high_low(indices[5], indices[6])[0],
                  high_low(indices[6], 155)[0]]
    daily_lows = [high_low(indices[0], indices[1])[1], high_low(indices[1], indices[2])[1],
                  high_low(indices[2], indices[3])[1], high_low(indices[3], indices[4])[1],
                  high_low(indices[4], indices[5])[1], high_low(indices[5], indices[6])[1],
                  high_low(indices[6], 155)[1]]
    fast_winds = [wind_speed(indices[0], indices[1])[0], wind_speed(indices[1], indices[2])[0],
                  wind_speed(indices[2], indices[3])[0], wind_speed(indices[3], indices[4])[0],
                  wind_speed(indices[4], indices[5])[0], wind_speed(indices[5], indices[6])[0],
                  wind_speed(indices[6], 155)[0]]
    slow_winds = [wind_speed(indices[0], indices[1])[1], wind_speed(indices[1], indices[2])[1],
                  wind_speed(indices[2], indices[3])[1], wind_speed(indices[3], indices[4])[1],
                  wind_speed(indices[4], indices[5])[1], wind_speed(indices[5], indices[6])[1],
                  wind_speed(indices[6], 155)[1]]
    short_summaries = [summaries_list(indices[0], indices[1])[0], summaries_list(indices[1], indices[2])[0],
                       summaries_list(indices[2], indices[3])[0], summaries_list(indices[3], indices[4])[0],
                       summaries_list(indices[4], indices[5])[0], summaries_list(indices[5], indices[6])[0],
                       summaries_list(indices[6], 155)[0]]
    # Call the class Weather, with the created lists for each object
    go = Weather(days_of_week, daily_high, daily_lows, short_summaries, fast_winds, slow_winds)
    # Call the text based visualization function and the graphics function.
    go.graph()


main()

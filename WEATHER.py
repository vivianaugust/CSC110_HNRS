from urllib.request import urlopen
import datetime
import json
from graphics_file import graphics

url = "https://api.weather.gov/gridpoints/TWC/90,49/forecast/hourly"
url2 = """https://tinyurl.com/pytinymoon"""
response = urlopen(url)
response2 = urlopen(url2)
data = json.loads(response.read())
moon_data = json.loads(response2.read())


def draw_forecast(day_of_week, daily_high, daily_low, short_summary):
    """
    Takes the daily high and low temps, and a short summary and outputs a text based visual
    :param day_of_week: 10-day week
    :param daily_high: list of 10 integers high
    :param daily_low: list of 10 integers low
    :param short_summary: list of  10 string descriptors
    :return string: ascii art in a string from short_summary and high and low temperatures displayed
    """
    i = 0
    print('Your forecast for the next 6 days :)\n_____________________________________\n')
    while i < len(day_of_week):
        print(day_of_week[i])
        print('High:', daily_high[i])
        print('Low:', daily_low[i])
        if short_summary[i] == "Showers And Thunderstorms":
            print(short_summary[i])
            print(r"""
         _, .--.
        (  / (  '-.
       .-=-.    ) -.
       /   (  .' .   \.
       \ ( ' ,_) ) \_/
        (_ , /\  ,_/
          '--\ `\--`
             _\ _\.
             `\ \.
              _\_\.
              `\.\.
                \.
            -.'.`\.'.-
            Be Careful!""")
        elif short_summary[i] == "Sunny":
            print(r"""

                        .   |
                            |
              \    *        |     *    .  /
                \        *  |  .        /
             .    \     ___---___     /    .  
                    \.--         --./     
         ~-_    *  ./               \.   *   _-~
            ~-_   /    ^         ^    \   _-~     *
       *       ~-/    ___       ___    \-~        
         .      |    (_O_)     (_O_)    |      .
             * |                         | *     
    -----------|                         |-----------
      .        |    <               >    |        .    
            *   |    \             /    | *
               _-\    `.         .'    /-_    *
         .  _-~ . \     `-.___.-'     /   ~-_     
         _-~       `\               /'*      ~-_  
        ~           /`--___   ___--'\           ~
               *  /        ---     .  \        .
                /     *     |           \.
              /             |   *         \.
                         .  |        .
                            |
                            |
            Get outside and enjoy that sunshine!""")
        elif short_summary[i] == "Partly Cloudy" or short_summary[i] == "Mostly Sunny" \
                or short_summary[i] == "Partly Sunny":
            print(short_summary[i])
            print(r"""                 .
                  |					
         .               /		     /	
          \       I     /		   /		
                      /           /
            \  ,     /           /
             \    (`  ).       /            _
     -  --==   \  (     ).=-- /          .+(`  )`.
                 (       '`./         :(   .    )
            .+(`(      .   )     .--  `.  (    ) )
           ((    (..__.:'-'   .=(   )   ` _`  ) )
    `.     `(       ) )       (   .  )     (   )  ._
      )      ` __.:'   )     (   (   ))     `-'.:(`  )
    )  )  ( )       --'       `- __.'         :(      ))
    .-'  (_.'          .')                    `(    )  ))
                      (_  )                     ` __.:'

    --..,___.--,--'`,---..-.--+--.,,-,,..._.--..-._.-a:f--.

            Shade and sun, what could be better!""")
        elif short_summary[i] == "Snow Showers Likely":
            print(r"""
                                ()
                                /\
                               //\\
                              <<  >>
                          ()   \\//   ()
                ()._____   /\   \\   /\   _____.()
                   \.--.\ //\\ //\\ //\\ /.--./
                    \\__\\/__\//__\//__\\/__//
                     '--/\\--//\--//\--/\\--'
                        \\\\///\\//\\\////
                    ()-= >>\\< <\\> >\\<< =-()
                        ////\\\//\\///\\\\
                     .--\\/--\//--\//--\//--.
                    //""/\\""//\""//\""//\""\\
                   /'--'/ \\// \\// \\// \'--'\
                 ()`'''`   '\/   //   \/   `'""`().
                          '()   //\.\.   ()
                              '<<  >>
                                \\//
                                 \/
                                 ()
                Do you wanna to build a snowman?""")
        elif short_summary[i] == "Rain Showers" or short_summary[i] == "Chance Rain Showers" \
                or short_summary[i] == "Rain Showers Likely":
            print(short_summary[i])
            print(r"""
         |       |        |       | |
     ' |   |   |     '  |      '      
                  |           |     | 
     '     |  _,..--I--..,_ |         
       / _.-`` _,-`   `-,_ ``-._ \   .
         `-,_,_,.,_   _,.,_._,-`      
    |  | '   '     `Y` __ '     '     
      '|        ,-. I /  \       |  | 
     |    |    /   )I \  /     '   |  
    '  '      /   / I_.""._           
    |  |    ,l  .'..`      `.   ' |  |
     |     / | /   \        l         
          /, '"  .  \      ||   |   | 
     |  ' ||      |"|      ||   |     
    '     ||      | |      ||       | 
    |     \|      | '.____,'/  |  |   
       |   |      |  |    |F   '    | 
     | '   |      |  | |\ |     ' |   
           |      |  | || |      |    
    |  |   |      |  | || |    |    | 
           |      |  | || |      |    
     ' |   '.____,'  \_||_/   |    |  
             |/\|    [_][_]      |    
    ''''''''''''''''''''''''''''''''''
    Today's a great day for a cozy movie :)""")
        elif short_summary[i] == "Mostly Cloudy":
            print(short_summary[i])
            print(r"""
                                _                                  
                  (`  ).                   _           
                 (     ).              .:(`  )`.       
                _(       '`.          :(   .    )      
            .=(`(      .   )     .--  `.  (    ) )      
           ((    (..__.:'-'   .+(   )   ` _`  ) )                 
    `.     `(       ) )       (   .  )     (   )  ._   
      )      ` __.:'   )     (   (   ))     `-'.-(`  ) 
    )  )  ( )       --'       `- __.'         :(      )) 
    .-'  (_.'          .')                    `(    )  ))
                      (_  )                     ` __.:'          

    --..,___.--,--'`,---..-.--+--.,,-,,..._.--..-._.-.:.--.
    'I've got sunshine, on a cloudy day,' The Temptations.""")
        else:
            print(short_summary[i])
        print('__________________________________________')
        i += 1
    print('Ascii art from https://www.asciiart.eu/nature/clouds')


def high_low(start, end):
    """
    loops through the 24 hours in a day, 12 periods and finds the max temp
    :param start: starting point and ending point
    :param end: ending point
    :return daily_high: max temp int
    """
    low = data["properties"]["periods"][start + 1]["temperature"]
    high = data["properties"]["periods"][start]["temperature"]
    i = start
    if start == 1:
        high = data["properties"]["periods"][1]["temperature"]
    while i <= end:
        if data["properties"]["periods"][i]["temperature"] <= low:
            low = data["properties"]["periods"][i]["temperature"]
        elif data["properties"]["periods"][i]["temperature"] >= high:
            high = data["properties"]["periods"][i]["temperature"]
        i += 1
    return [high, low]


def wind_speed(start, end):
    """
    loops through the 24 hours in a day, 12 periods and finds the max temp
    :param start: starting point and ending point
    :param end: ending point
    :return daily_high: max temp int
    """
    slow = int(data["properties"]["periods"][start + 1]["windSpeed"][0:2])
    fast = int(data["properties"]["periods"][start]["windSpeed"][0:2])
    i = start
    if start == 1:
        fast = int(data["properties"]["periods"][1]["windSpeed"][0:2])
    while i <= end:
        if int(data["properties"]["periods"][i]["windSpeed"][0:2]) <= slow:
            slow = int(data["properties"]["periods"][i]["windSpeed"][0:2])
        elif int(data["properties"]["periods"][i]["windSpeed"][0:2]) >= fast:
            fast = int(data["properties"]["periods"][i]["windSpeed"][0:2])
        i += 1
    return [fast, slow]


def summaries_list(start, end):
    """
    loops through the 24 hours in a day, 12 periods and finds the max temp
    :param start: starting point and ending point
    :param end: ending point
    :return daily_high: max temp int
    """
    i = start
    list_of_summaries = []
    mode = {}
    while i <= end:
        list_of_summaries.append(data["properties"]["periods"][i]["shortForecast"])
        i += 1
    # find the mode of the summaries
    for a in list_of_summaries:
        if not a in mode:
            mode[a] = 1
        else:
            mode[a] += 1
    most_common_summary = [b for b, l in mode.items() if l == max(mode.values())]
    return most_common_summary


def main():
    all_periods = data["properties"]["periods"]  # list with all periods
    previous_weekday = datetime.datetime(int(data["properties"]["periods"][1]["startTime"][:4]),
                                         int(data["properties"]["periods"][1]["startTime"][5:7]),
                                         int(data["properties"]["periods"][1]["startTime"][8:10])).strftime('%A')
    # create list with finalized days to visualize
    days_of_week = []
    indices = [1]
    # for each item in the list of periods
    for p in all_periods:
        # grab that item
        current_weekday = datetime.datetime(int(p["startTime"][:4]), int(p["startTime"][5:7]),
                                            int(p["startTime"][8:10])).strftime('%A')
        # is it a different day?
        if current_weekday != previous_weekday:
            days_of_week.append(previous_weekday)
            previous_weekday = current_weekday
            indices.append(p['number'])
    if len(days_of_week) == 6:
        days_of_week.append(datetime.datetime(int(data["properties"]["periods"][-1]["startTime"][:4]),
                                              int(data["properties"]["periods"][-1]["startTime"][5:7]),
                                              int(data["properties"]["periods"][-1]["startTime"][8:10])).strftime('%A'))
    daily_highs = [high_low(indices[0], indices[1])[0], high_low(indices[1], indices[2])[0],
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

    def graph(day_of_week, daily_high, daily_low, short_summary):
        """

        :return:
        """
        all_images = ['lll.png', 'lll2.png', 'lll3.png', 'lll4.png', 'lll5.png', 'lll6.png', 'iii.png', 'iii2.png',
                      'iii3.png', 'iii4.png', 'iii5.png', 'iii6.png', 'love.png', 'love2.png', 'love3.png', 'love4.png',
                      'love5.png', 'love6.png', 'snow.png', 'snow2.png', 'snow3.png', 'snow4.png', 'snow5.png',
                      'snow6.png', 'rain.png', 'rain2.png', 'rain3.png', 'rain4.png', 'rain5.png', 'rain6.png',
                      'smile.png', 'smile2.png', 'smile3.png', 'smile4.png', 'smile5.png', 'smile6.png',
                      'inkpx-word-art.png', 'inkpx-word-art2.png', 'inkpx-word-art3.png', 'inkpx-word-art4.png',
                      'inkpx-word-art5.png', 'inkpx-word-art6.png']
        scales = []
        images = {}
        printing = []
        locations = [215, 305, 395, 485, 575, 665]
        gui = graphics(1480, 790, 'Weather')
        if data["properties"]["periods"][1]["isDaytime"] == True:
            gui.image(0, 0, 1, 3, "night.png")
        else:
            gui.image(0, 0, 1, 3, "sky.png")
        gui.rectangle(769, 215, 515, 545, 'lavender blush')
        gui.rectangle(164, 215, 515, 545, 'lavender blush')
        gui.image(565, 0, 1, 2, "pngegg.png")
        gui.image(695, 50, 1, 30, "moon.png")
        gui.image(615, 100, 1, 5, "l.png")
        i = 0
        while i < len(short_summary):
            if short_summary[i] == "Showers And Thunderstorms":
                image = [all_images[0], all_images[1], all_images[2], all_images[3], all_images[4], all_images[5]]
                images.update({'image' + str(i): image})
                scale = 1
                scales.append(scale)
            elif short_summary[i] == "Sunny":
                image = [all_images[6], all_images[7], all_images[8], all_images[9], all_images[10], all_images[11]]
                images.update({'image' + str(i): image})
                scale = 9
                scales.append(scale)
            elif short_summary[i] == "Partly Cloudy" or short_summary[i] == "Mostly Sunny" \
                    or short_summary[i] == "Partly Sunny":
                image = [all_images[12], all_images[13], all_images[14], all_images[15], all_images[16], all_images[17]]
                images.update({'image' + str(i): image})
                scale = 32
                scales.append(scale)
            elif short_summary[i] == "Snow Showers Likely":
                image = [all_images[18], all_images[19], all_images[20], all_images[21], all_images[22], all_images[23]]
                images.update({'image' + str(i): image})
                scale = 3
                scales.append(scale)
            elif short_summary[i] == "Rain Showers" or short_summary[i] == "Chance Rain Showers" \
                    or short_summary[i] == "Rain Showers Likely" or short_summary[i] == "Slight Chance Rain Showers":
                image = [all_images[24], all_images[25], all_images[26], all_images[27], all_images[28], all_images[29]]
                images.update({'image' + str(i): image})
                scale = 27
                scales.append(scale)
            elif short_summary[i] == "Mostly Cloudy":
                image = [all_images[30], all_images[31], all_images[32], all_images[33], all_images[34], all_images[35]]
                images.update({'image' + str(i): image})
                scale = 8
                scales.append(scale)
            else:
                image = [all_images[36], all_images[37], all_images[38], all_images[39], all_images[40], all_images[41]]
                images.update({'image' + str(i): image})
                scale = 3
                scales.append(scale)
            if i > 0:
                gui.text(1000, 150 + (i * 90), short_summary[i], 'dark orchid', 17)
                gui.text(870, 125 + (i * 90), day_of_week[i].capitalize(), 'medium violet red', 20)
                gui.text(870, 150 + (i * 90), 'High: ' + str(daily_high[i]) + '........', 'dark orchid', 17)
                gui.text(870, 175 + (i * 90), 'Low: ' + str(daily_low[i]), 'dark orchid', 17)
            i += 1
        previous_image = images['image1']
        j = 0
        while j < len(locations):
            current_image = images['image' + str(j + 1)]
            if current_image == previous_image:
                printing.append(current_image[j])
                previous_image = current_image
            else:
                printing.append(current_image[j])
            gui.image(769, locations[j], 1, scales[j + 1], printing[j])
            j += 1
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
            moon_scale = 2
        if 0.25 < moon_data["days"][0]["moonphase"] < 0.5:
            moon = 'waxing_gibbous.png'
            moon_scale = 1
        if moon_data["days"][0]["moonphase"] == 0.5:
            moon = 'full_moon.png'
        if 0.5 < moon_data["days"][0]["moonphase"] < 0.75:
            moon = 'waning_gibbous.png'
            moon_scale = 1
        if moon_data["days"][0]["moonphase"] == 0.75:
            moon = 'last_quarter.png'
            moon_scale = 1
        if 0.75 < moon_data["days"][0]["moonphase"] < 1:
            moon = 'waning_crescent.png'
            moon_scale = 4
            gui.text(310, 215, """A Waning Crescent Moon is
    the perfect time to rest and regenerate.
    It's a period of self-care; 
    to find inner peace and reconnect with yourself,
    surrendering all that has happened
    that is out of our control, 
    before the lunar cycle begins again.""",
                     'medium violet red', 13)
        if 0.75 < moon_data["days"][0]["moonphase"] == 1:
            moon = 'moon.png'
            moon_scale = 1
        gui.image(164, 215, 1, moon_scale, moon)
        gui.text(294, 425, short_summary[0], 'dark orchid', 17)
        if scales[0] > 11:
            gui.image(530, 375, 1, scales[0] - 10, images['image0'][5])
        else:
            gui.image(550, 395, 1, scales[0], images['image0'][5])
        gui.text(164, 395, day_of_week[0].capitalize(), 'medium violet red', 20)
        gui.text(164, 425, 'High: ' + str(daily_high[0]) + '........', 'dark orchid', 17)
        gui.text(164, 445, 'Low: ' + str(daily_low[0]), 'dark orchid', 17)
        gui.draw()
        print(printing)
        print(short_summaries)
        print(images)
        print(scales)
        print(indices)
        print(fast_winds)
        print(slow_winds)

    print(days_of_week)

    graph(days_of_week, daily_highs, daily_lows, short_summaries)
    draw_forecast(days_of_week, daily_highs, daily_lows, short_summaries)


main()

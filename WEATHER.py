from urllib.request import urlopen
import datetime
import json

url = "https://api.weather.gov/gridpoints/TWC/90,49/forecast/hourly"
response = urlopen(url)
data = json.loads(response.read())


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
    print('Your forecast for the next 10 days :)\n_____________________________________\n')
    while i < len(day_of_week):
        print(day_of_week[i])
        print('High:', daily_high[i])
        print('Low:', daily_low[i])
        if short_summary[i] == "showers and thunderstorms":
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


def high_low(init_period):
    """
    loops through the 24 hours in a day, 12 periods and finds the max temp
    :param init_period: starting point
    :return daily_high: max temp int
    """
    i = init_period
    final = init_period + 11
    temps = []
    while i <= final:
        temps.append(data["properties"]["periods"][i]["temperature"])
        i += 1
    low = temps[0]
    high = temps[1]
    i = init_period
    while i <= final:
        spot = i - init_period
        if temps[spot] <= low:
            low = temps[spot]
        else:
            high = temps[spot]
        i += 1
    return [high, low]


def main():
    all_periods = data["properties"]["periods"] # list with all periods
    
    previous_weekday = int(data["properties"]["periods"][0]["startTime"][:4]),
                                      int(data["properties"]["periods"][0]["startTime"][5:7]),
                                      int(data["properties"]["periods"][0]["startTime"][8:10])).strftime('%A')
    
    # create list with finalized days to visualize
    selected_periods = []
    # for each item in the list of periods
    for p in all_periods:
        # grab that item
        current_weekday = datetime.datetime(int(p["startTime"][:4]),
                                      int(p["startTime"][5:7]),
                                      int(p["startTime"][8:10])).strftime('%A')
        # is it a different day?
        if current_weekday != previous_weekday:
            # save 
            selected_periods.append(previous_weekday)
            previous_weekday = current_weekday
        
        
    
    days_of_week = [datetime.datetime(int(data["properties"]["periods"][0]["startTime"][:4]),
                                      int(data["properties"]["periods"][0]["startTime"][5:7]),
                                      int(data["properties"]["periods"][0]["startTime"][8:10])).strftime('%A'),
                    datetime.datetime(int(data["properties"]["periods"][12]["startTime"][:4]),
                                      int(data["properties"]["periods"][12]["startTime"][5:7]),
                                      int(data["properties"]["periods"][12]["startTime"][8:10])).strftime('%A'),
                    datetime.datetime(int(data["properties"]["periods"][36]["startTime"][:4]),
                                      int(data["properties"]["periods"][36]["startTime"][5:7]),
                                      int(data["properties"]["periods"][36]["startTime"][8:10])).strftime('%A'),
                    datetime.datetime(int(data["properties"]["periods"][36]["startTime"][:4]),
                                      int(data["properties"]["periods"][36]["startTime"][5:7]),
                                      int(data["properties"]["periods"][36]["startTime"][8:10])).strftime('%A'),
                    datetime.datetime(int(data["properties"]["periods"][48]["startTime"][:4]),
                                      int(data["properties"]["periods"][48]["startTime"][5:7]),
                                      int(data["properties"]["periods"][48]["startTime"][8:10])).strftime('%A'),
                    datetime.datetime(int(data["properties"]["periods"][60]["startTime"][:4]),
                                      int(data["properties"]["periods"][60]["startTime"][5:7]),
                                      int(data["properties"]["periods"][60]["startTime"][8:10])).strftime('%A'),
                    datetime.datetime(int(data["properties"]["periods"][72]["startTime"][:4]),
                                      int(data["properties"]["periods"][72]["startTime"][5:7]),
                                      int(data["properties"]["periods"][72]["startTime"][8:10])).strftime('%A'),
                    datetime.datetime(int(data["properties"]["periods"][84]["startTime"][:3]),
                                      int(data["properties"]["periods"][84]["startTime"][5:7]),
                                      int(data["properties"]["periods"][84]["startTime"][8:10])).strftime('%A'),
                    datetime.datetime(int(data["properties"]["periods"][96]["startTime"][:4]),
                                      int(data["properties"]["periods"][96]["startTime"][5:7]),
                                      int(data["properties"]["periods"][96]["startTime"][8:10])).strftime('%A'),
                    datetime.datetime(int(data["properties"]["periods"][108]["startTime"][:4]),
                                      int(data["properties"]["periods"][108]["startTime"][5:7]),
                                      int(data["properties"]["periods"][108]["startTime"][8:10])).strftime('%A')]
    daily_highs = [int(high_low(0)[0]), int(high_low(12)[0]), int(high_low(24)[0]), int(high_low(36)[0]),
                   int(high_low(48)[0]), int(high_low(60)[0]), int(high_low(72)[0]), int(high_low(84)[0]),
                   int(high_low(96)[0]), int(high_low(108)[0])]
    daily_lows = [int(high_low(0)[1]), int(high_low(12)[1]), int(high_low(24)[1]), int(high_low(36)[1]),
                  int(high_low(48)[1]), int(high_low(60)[1]), int(high_low(72)[1]),
                  int(high_low(84)[1]), int(high_low(96)[1]), int(high_low(108)[1])]
    short_summaries = [data["properties"]["periods"][0]["shortForecast"],
                       data["properties"]["periods"][12]["shortForecast"],
                       data["properties"]["periods"][24]["shortForecast"],
                       data["properties"]["periods"][36]["shortForecast"],
                       data["properties"]["periods"][48]["shortForecast"],
                       data["properties"]["periods"][60]["shortForecast"],
                       data["properties"]["periods"][72]["shortForecast"],
                       data["properties"]["periods"][84]["shortForecast"],
                       data["properties"]["periods"][96]["shortForecast"],
                       data["properties"]["periods"][108]["shortForecast"]]
    draw_forecast(days_of_week, daily_highs, daily_lows, short_summaries)


print(datetime.datetime(int(data["properties"]["periods"][24]["startTime"][:4]),
                        int(data["properties"]["periods"][24]["startTime"][5:7]),
                        int(data["properties"]["periods"][24]["startTime"][8:10])).strftime('%A'))


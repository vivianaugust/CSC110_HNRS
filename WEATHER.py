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
        if short_summary[i] == 'showers and thunderstorms':
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
        if short_summary[i] == 'sunny':
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
        if short_summary[i] == 'partly cloudy':
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
        if short_summary[i] == 'windy':
            print(r"""
                                                     ___    ,'''''''.
                                        ,'''   '''''      `.
                                       ,'        _.         `._
                                      ,'       ,'              `''''.
                                     ,'    .-""`.    ,-'            `.
                                    ,'    (        ,'                :
                                  ,'     ,'           __,            `.
                            ,'''''     .' ;-.    ,  ,'  \             `''''.
                          ,'           `-(   `._(_,'     )_                `.
                         ,'         ,---. \ @ ;   \ @ _,'                   `.
                    ,-""'         ,'      ,--'-    `;'                       `.
                   ,'            ,'      (      `. ,'                          `.
                   ;            ,'        \    _,','                            `.
                  ,'            ;          `--'  ,'                              `.
                 ,'             ;          __    (                    ,           `.
                 ;              `____...  `      `.                  ,'           ,'
                 ;    ...----'''' )  _.-  .      `.                ,'    ,'    ,'
    _....----''' '.        _..--'_.-:.-' .'        `.             ,''.   ,' `--'
                  `' .-'`-.:..___...--' `-._      ,-''   `-'
            _.--'       _.-'    .'   .' .'               `'''''
      __.-''        _.-'     .-'   .'  /
     '          _.-' .-'  .-'        .'
            _.-'  .-'  .-' .'  .'   /
        _.-'      .-'   .-'  .'   .'
    _.-'       .-'    .'   .'    /
           _.-'    .-'   .'    .'
        .-'            .'''
        Hold on to your hats!""")
        if short_summary[i] == "raining":
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
        if short_summary[i] == "cloudy":
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
        print('__________________________________________')
        i += 1
    print('Ascii art from https://www.asciiart.eu/nature/clouds')


def main():
    day_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday',
                   'Monday', 'Tuesday', 'Wednesday']
    daily_high = [51, 54, 65, 72, 73, 61, 62, 58, 65, 70]
    daily_low = [40, 38, 52, 57, 55, 48, 32, 32, 42, 47]
    short_summary = ["showers and thunderstorms", 'sunny', 'cloudy', 'partly cloudy', 'raining',
                     'sunny', 'windy', 'cloudy', 'showers and thunderstorms', 'partly cloudy']
    draw_forecast(day_of_week, daily_high, daily_low, short_summary)

    
main()

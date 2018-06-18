import curses
import screen_setup as ss
import sys

screen, red, yellow_background, blue, default, yellow_text, cyan_dots = ss.curses_setup()

def print_hotdog():

    while(True):
        try:
            screen.clear()
            y = 20
            x = 20

            screen.addstr(y,x+19,       ',,,,,,,,,,,,'                                          ,curses.color_pair(yellow_text))
            screen.addstr(y+1, x+15,    '..,,,,,,,,,,,,,,,......'                               ,curses.color_pair(yellow_text))
            screen.addstr(y+2, x+13,    '.........,,,,,,,*******,,,,,,,,...'                    ,curses.color_pair(yellow_text))
            screen.addstr(y+2, x+11,    '.,,,,,,...'                                            ,curses.color_pair(red))
            screen.addstr(y+3, x+32,    '.....,,,************,,,,,...'                          ,curses.color_pair(yellow_text))
            screen.addstr(y+3, x+9,     '.*/(((((((((//*,,..... '                               ,curses.color_pair(red))
            screen.addstr(y+4, x+37,    '.......,,,**********,,,,...'                           ,curses.color_pair(yellow_text))
            screen.addstr(y+4, x+8,     '.,**//((((((((((((((((//**,,.'                         ,curses.color_pair(red))
            screen.addstr(y+5, x+8,     '.....,,**///((((((((((((((###(((/*,,.'                 ,curses.color_pair(red))
            screen.addstr(y+5, x+45,    '.....,,*********,,,...'                                ,curses.color_pair(yellow_text))
            screen.addstr(y+6, x+53,    '..,,**///**,,,..'                                      ,curses.color_pair(yellow_text))
            screen.addstr(y+6, x+8,     '.,,,,.......,,***///(((((((((((((#(((((//*,,.'         ,curses.color_pair(red))
            screen.addstr(y+7, x+12,    '****,,,.........,,**//((((((((((((((#####(//*,,,*'     ,curses.color_pair(red))
            screen.addstr(y+7, x+10,    '.,'                                                    ,curses.color_pair(yellow_text))
            screen.addstr(y+7, x+61,    '*//**,,..'                                             ,curses.color_pair(yellow_text))
            screen.addstr(y+8, x+63,    '***,,,.'                                               ,curses.color_pair(yellow_text))
            screen.addstr(y+8, x+15,    '*********,,,,......,,***///((((((((##########(/*'      ,curses.color_pair(red))
            screen.addstr(y+8, x+11,    '..,,'                                                  ,curses.color_pair(yellow_text))
            screen.addstr(y+9, x+19,    '***/////******,,,,,....,,**//((((###########(/*,..'    ,curses.color_pair(red))
            screen.addstr(y+9, x+66,    ',..'                                                   ,curses.color_pair(yellow_text))
            screen.addstr(y+9, x+13,    '...,,*'                                                ,curses.color_pair(yellow_text))
            screen.addstr(y+10, x+66,   '.'                                                     ,curses.color_pair(yellow_text))
            screen.addstr(y+10, x+26,   '*****//////****,,,,,,,,***//((######(((*'              ,curses.color_pair(red))
            screen.addstr(y+10, x+16,   '.....,,***'                                            ,curses.color_pair(yellow_text))
            screen.addstr(y+11, x+34,   '****///////*****,,***/(((#####(/.'                     ,curses.color_pair(red))
            screen.addstr(y+11, x+21,   '....,,,,,,****.'                                       ,curses.color_pair(yellow_text))
            screen.addstr(y+12, x+39,   '***///////////////(((####(*.'                          ,curses.color_pair(red))
            screen.addstr(y+12, x+26,   '.....,,,,,***'                                         ,curses.color_pair(yellow_text))
            screen.addstr(y+13, x+45,   '****///(((//(((###(*.'                                 ,curses.color_pair(red))
            screen.addstr(y+13, x+66,   '.'                                                     ,curses.color_pair(yellow_text))
            screen.addstr(y+13, x+32,   '....,,,,*****'                                         ,curses.color_pair(yellow_text))
            screen.addstr(y+14, x+36,   '........,,,***,***//'                                  ,curses.color_pair(yellow_text))
            screen.addstr(y+14, x+54,   '///*****,'                                             ,curses.color_pair(red))
            screen.addstr(y+14, x+63,   ',.'                                                    ,curses.color_pair(yellow_text))
            screen.addstr(y+15, x+39,   '.....,,,,,,,****/***,,,,,.'                            ,curses.color_pair(yellow_text))
            screen.addstr(y+16, x+44,   '....,,,,,********,.'                                   ,curses.color_pair(yellow_text))

            '''
            screen.addstr(y, x,         '               ..,,,,,,,,,,,,,,,......')
            screen.addstr(y+1, x,       '             .........,,,,,,,*******,,,,,,,,...')
            screen.addstr(y+2, x,       '           .,,,,,,...   ......,,,,,**********,,,,,,,...')
            screen.addstr(y+3, x,       '         .*/(((((((((//*,,..... .....,,,************,,,,,...')
            screen.addstr(y+4, x,       '        .,**//((((((((((((((((//**,,........,,,**********,,,,...')
            screen.addstr(y+5, x,       '        .....,,**///((((((((((((((###(((/*,,......,,*********,,,...')
            screen.addstr(y+6, x,       '        .,,,,.......,,***///(((((((((((((#(((((//*,,...,,**///**,,,..')
            screen.addstr(y+7, x,       '          .,****,,,.........,,**//((((((((((((((#####(//*,,,**//**,,..')
            screen.addstr(y+8, x,       '           ..,,*********,,,,......,,***///((((((((##########(/****,,,.')
            screen.addstr(y+9, x,       '             ...,,****/////******,,,,,....,,**//((((###########(/*,..')
            screen.addstr(y+10, x,      '                .....,,********//////****,,,,,,,,***//((######(((*.')
            screen.addstr(y+11, x,      '                     ....,,,,,,*******///////*****,,***/(((#####(/.')
            screen.addstr(y+12, x,      '                          .....,,,,,******///////////////(((####(*.')
            screen.addstr(y+13, x,      '                                ....,,,,*********///(((//(((###(*..')
            screen.addstr(y+14, x,      '                                  ........,,,***,***/////*****,,.')
            screen.addstr(y+15, x,      '                                       .....,,,,,,,****/***,,,,,.')
            screen.addstr(y+16, x,      '                                            ....,,,,,********,.')
            '''
            screen.refresh()
        except KeyboardInterrupt:
            curses.endwin()
            sys.exit()

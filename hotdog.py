import curses
import screen_setup as ss
import sys

screen, red, yellow_background, blue, default, yellow_text, cyan_dots = ss.curses_setup()

def print_hotdog(screen):
    while(True):
        try:
            screen.clear()
            y = 10
            x = 10
            '''
            screen.addstr(y-1,x,        '                   ...,,,....'                                             ,curses.color_pair(yellow_text))
            screen.addstr(y, x,         '               ..,,,,,,,,,,,,,,,......'                                    ,curses.color_pair(yellow_text))
            screen.addstr(y+1, x,       '             .........,,,,,,,*******,,,,,,,,...'                           ,curses.color_pair(yellow_text))
            screen.addstr(y+1, x,       '           .,,,,,,...'                                                     ,curses.color_pair(red))
            screen.addstr(y+2, x,       '                                .....,,,************,,,,,...'              ,curses.color_pair(yellow_text))
            screen.addstr(y+2, x,       '         .*/(((((((((//*,,.....'                                           ,curses.color_pair(red))
            screen.addstr(y+3, x,       '                                     .......,,,**********,,,,...'          ,curses.color_pair(yellow_text))
            screen.addstr(y+3, x,       '        .,**//((((((((((((((((//**,,.'                                     ,curses.color_pair(red))
            screen.addstr(y+4, x,       '        .....,,**///((((((((((((((###(((/*,,......,,*********,,,...')
            screen.addstr(y+5, x,       '        .,,,,.......,,***///(((((((((((((#(((((//*,,...,,**///**,,,..')
            screen.addstr(y+6, x,       '        .,,,,.......,,***///(((((((((((((#(((((//*,,...,,**///**,,,..')
            screen.addstr(y+7, x,       '          .,****,,,.........,,**//((((((((((((((#####(//*,,,**//**,,..')
            screen.addstr(y+8, x,       '           ..,,*********,,,,......,,***///((((((((##########(/****,,,.')
            screen.addstr(y+9, x,       '             ...,,****/////******,,,,,....,,**//((((###########(/*,..')
            screen.addstr(y+10, x,      '                .....,,********//////****,,,,,,,,***//((######(((*.')
            screen.addstr(y+11, x,      '                     ....,,,,,,*******///////*****,,***/(((#####(/.')
            screen.addstr(y+12, x,      '                          .....,,,,,******///////////////(((####(*.')
            screen.addstr(y+13, x,      '                                ....,,,,*********///(((//(((###(*..')
            screen.addstr(y+14, x,      '                                  ........,,,***,***//'                    ,curses.color_pair(yellow_text))
            screen.addstr(y+14, x+54,                                                            '///*****,'        ,curses.color_pair(red))
            screen.addstr(y+14, x+63,                                                                     ',.'      ,curses.color_pair(yellow_text))
            screen.addstr(y+15, x,      '                                       .....,,,,,,,****/***,,,,,.'         ,curses.color_pair(yellow_text))
            screen.addstr(y+16, x,      '                                            ....,,,,,********,.'           ,curses.color_pair(yellow_text))
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

            screen.refresh()
        except KeyboardInterrupt:
            curses.endwin()
            sys.exit()

curses.wrapper(print_hotdog)

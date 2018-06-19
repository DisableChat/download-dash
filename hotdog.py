import curses
import screen_setup as ss
import sys
import os
import time
import subprocess
import distro_obj as dis
from subprocess import DEVNULL, STDOUT, run, Popen

screen, red, yellow_background, blue, default, yellow_text, cyan_dots = ss.curses_setup()
window_height, window_width = ss.window_res(screen)



def odds_screen():
    with open(os.devnull, 'wb') as devnull:
        subprocess.Popen(['aplay', dis.file_directory + 'quickmath.wav'], stdout=devnull, stderr=subprocess.STDOUT)
    # Odds Function
    while True:
        try:
            middle_height, middle_width = ss.window_res(screen)
            screen.addstr(1,middle_width - 13, "*PRESS SPACE TO START RACE*")
            screen.addstr(5,middle_width - 8, "Odds Display Page")
            screen.border()
            key = screen.getkey()
            if(key == ' '):
                break
                drums.terminate()
            screen.clear()
            screen.refresh()
            time.sleep(.1)

        except KeyboardInterrupt:
            curses.endwin()
            sys.exit("Keyboard, Interrupt Quitting...")

def print_hotdog():
    with open(os.devnull, 'wb') as devnull:
        subprocess.Popen(['aplay', dis.file_directory + 'countdown.wav'], stdout=devnull, stderr=subprocess.STDOUT)
    try:
        for k in range(3,0,-1):
            count = 0
            while(count != 12):
                middle_height, middle_width = ss.window_res(screen)
                screen.clear()
                screen.border()
                screen.addstr(middle_height - 4, middle_width - 22 ,
                    '(>0.0)>   -_-_COUNTDOWN HYPE_-_-   <(0.0<)', curses.color_pair(yellow_background))
                screen.addch(middle_height-2, middle_width - 1, str(k) , curses.color_pair(yellow_background))

                screen.addstr(middle_height,middle_width-40+19,       ',,,,,,,,,,,,'                                          ,curses.color_pair(yellow_text))
                screen.addstr(middle_height+1, middle_width-40+15,    '..,,,,,,,,,,,,,,,......'                               ,curses.color_pair(yellow_text))
                screen.addstr(middle_height+2, middle_width-40+13,    '.........,,,,,,,*******,,,,,,,,...'                    ,curses.color_pair(yellow_text))
                screen.addstr(middle_height+2, middle_width-40+11,    '.,,,,,,...'                                            ,curses.color_pair(red))
                screen.addstr(middle_height+3, middle_width-40+32,    '.....,,,************,,,,,...'                          ,curses.color_pair(yellow_text))
                screen.addstr(middle_height+3, middle_width-40+9,     '.*/(((((((((//*,,..... '                               ,curses.color_pair(red))
                screen.addstr(middle_height+4, middle_width-40+37,    '.......,,,**********,,,,...'                           ,curses.color_pair(yellow_text))
                screen.addstr(middle_height+4, middle_width-40+8,     '.,**//((((((((((((((((//**,,.'                         ,curses.color_pair(red))
                screen.addstr(middle_height+5, middle_width-40+8,     '.....,,**///((((((((((((((###(((/*,,.'                 ,curses.color_pair(red))
                screen.addstr(middle_height+5, middle_width-40+45,    '.....,,*********,,,...'                                ,curses.color_pair(yellow_text))
                screen.addstr(middle_height+6, middle_width-40+53,    '..,,**///**,,,..'                                      ,curses.color_pair(yellow_text))
                screen.addstr(middle_height+6, middle_width-40+8,     '.,,,,.......,,***///(((((((((((((#(((((//*,,.'         ,curses.color_pair(red))
                screen.addstr(middle_height+7, middle_width-40+12,    '****,,,.........,,**//((((((((((((((#####(//*,,,*'     ,curses.color_pair(red))
                screen.addstr(middle_height+7, middle_width-40+10,    '.,'                                                    ,curses.color_pair(yellow_text))
                screen.addstr(middle_height+7, middle_width-40+61,    '*//**,,..'                                             ,curses.color_pair(yellow_text))
                screen.addstr(middle_height+8, middle_width-40+63,    '***,,,.'                                               ,curses.color_pair(yellow_text))
                screen.addstr(middle_height+8, middle_width-40+15,    '*********,,,,......,,***///((((((((##########(/*'      ,curses.color_pair(red))
                screen.addstr(middle_height+8, middle_width-40+11,    '..,,'                                                  ,curses.color_pair(yellow_text))
                screen.addstr(middle_height+9, middle_width-40+19,    '***/////******,,,,,....,,**//((((###########(/*,..'    ,curses.color_pair(red))
                screen.addstr(middle_height+9, middle_width-40+66,    ',..'                                                   ,curses.color_pair(yellow_text))
                screen.addstr(middle_height+9, middle_width-40+13,    '...,,*'                                                ,curses.color_pair(yellow_text))
                screen.addstr(middle_height+10, middle_width-40+66,   '.'                                                     ,curses.color_pair(yellow_text))
                screen.addstr(middle_height+10, middle_width-40+26,   '*****//////****,,,,,,,,***//((######(((*'              ,curses.color_pair(red))
                screen.addstr(middle_height+10, middle_width-40+16,   '.....,,***'                                            ,curses.color_pair(yellow_text))
                screen.addstr(middle_height+11, middle_width-40+34,   '****///////*****,,***/(((#####(/.'                     ,curses.color_pair(red))
                screen.addstr(middle_height+11, middle_width-40+21,   '....,,,,,,****.'                                       ,curses.color_pair(yellow_text))
                screen.addstr(middle_height+12, middle_width-40+39,   '***///////////////(((####(*.'                          ,curses.color_pair(red))
                screen.addstr(middle_height+12, middle_width-40+26,   '.....,,,,,***'                                         ,curses.color_pair(yellow_text))
                screen.addstr(middle_height+13, middle_width-40+45,   '****///(((//(((###(*.'                                 ,curses.color_pair(red))
                screen.addstr(middle_height+13, middle_width-40+66,   '.'                                                     ,curses.color_pair(yellow_text))
                screen.addstr(middle_height+13, middle_width-40+32,   '....,,,,*****'                                         ,curses.color_pair(yellow_text))
                screen.addstr(middle_height+14, middle_width-40+36,   '........,,,***,***//'                                  ,curses.color_pair(yellow_text))
                screen.addstr(middle_height+14, middle_width-40+54,   '///*****,'                                             ,curses.color_pair(red))
                screen.addstr(middle_height+14, middle_width-40+63,   ',.'                                                    ,curses.color_pair(yellow_text))
                screen.addstr(middle_height+15, middle_width-40+39,   '.....,,,,,,,****/***,,,,,.'                            ,curses.color_pair(yellow_text))
                screen.addstr(middle_height+16, middle_width-40+44,   '....,,,,,********,.'                                   ,curses.color_pair(yellow_text))

                screen.refresh()
                time.sleep(.1)
                count += 1

        count1 = 0
        while(count1 != 12):
            middle_height, middle_width = ss.window_res(screen)
            screen.clear()
            screen.border()
            screen.addstr(middle_height - 4, middle_width - 22 ,
                '(>0.0)>   -_-_COUNTDOWN HYPE_-_-   <(0.0<)', curses.color_pair(yellow_background))
            screen.addstr(middle_height -2, middle_width - 2, 'GO!', curses.color_pair(yellow_background))

            screen.addstr(middle_height,middle_width-40+19,       ',,,,,,,,,,,,'                                          ,curses.color_pair(yellow_text))
            screen.addstr(middle_height+1, middle_width-40+15,    '..,,,,,,,,,,,,,,,......'                               ,curses.color_pair(yellow_text))
            screen.addstr(middle_height+2, middle_width-40+13,    '.........,,,,,,,*******,,,,,,,,...'                    ,curses.color_pair(yellow_text))
            screen.addstr(middle_height+2, middle_width-40+11,    '.,,,,,,...'                                            ,curses.color_pair(red))
            screen.addstr(middle_height+3, middle_width-40+32,    '.....,,,************,,,,,...'                          ,curses.color_pair(yellow_text))
            screen.addstr(middle_height+3, middle_width-40+9,     '.*/(((((((((//*,,..... '                               ,curses.color_pair(red))
            screen.addstr(middle_height+4, middle_width-40+37,    '.......,,,**********,,,,...'                           ,curses.color_pair(yellow_text))
            screen.addstr(middle_height+4, middle_width-40+8,     '.,**//((((((((((((((((//**,,.'                         ,curses.color_pair(red))
            screen.addstr(middle_height+5, middle_width-40+8,     '.....,,**///((((((((((((((###(((/*,,.'                 ,curses.color_pair(red))
            screen.addstr(middle_height+5, middle_width-40+45,    '.....,,*********,,,...'                                ,curses.color_pair(yellow_text))
            screen.addstr(middle_height+6, middle_width-40+53,    '..,,**///**,,,..'                                      ,curses.color_pair(yellow_text))
            screen.addstr(middle_height+6, middle_width-40+8,     '.,,,,.......,,***///(((((((((((((#(((((//*,,.'         ,curses.color_pair(red))
            screen.addstr(middle_height+7, middle_width-40+12,    '****,,,.........,,**//((((((((((((((#####(//*,,,*'     ,curses.color_pair(red))
            screen.addstr(middle_height+7, middle_width-40+10,    '.,'                                                    ,curses.color_pair(yellow_text))
            screen.addstr(middle_height+7, middle_width-40+61,    '*//**,,..'                                             ,curses.color_pair(yellow_text))
            screen.addstr(middle_height+8, middle_width-40+63,    '***,,,.'                                               ,curses.color_pair(yellow_text))
            screen.addstr(middle_height+8, middle_width-40+15,    '*********,,,,......,,***///((((((((##########(/*'      ,curses.color_pair(red))
            screen.addstr(middle_height+8, middle_width-40+11,    '..,,'                                                  ,curses.color_pair(yellow_text))
            screen.addstr(middle_height+9, middle_width-40+19,    '***/////******,,,,,....,,**//((((###########(/*,..'    ,curses.color_pair(red))
            screen.addstr(middle_height+9, middle_width-40+66,    ',..'                                                   ,curses.color_pair(yellow_text))
            screen.addstr(middle_height+9, middle_width-40+13,    '...,,*'                                                ,curses.color_pair(yellow_text))
            screen.addstr(middle_height+10, middle_width-40+66,   '.'                                                     ,curses.color_pair(yellow_text))
            screen.addstr(middle_height+10, middle_width-40+26,   '*****//////****,,,,,,,,***//((######(((*'              ,curses.color_pair(red))
            screen.addstr(middle_height+10, middle_width-40+16,   '.....,,***'                                            ,curses.color_pair(yellow_text))
            screen.addstr(middle_height+11, middle_width-40+34,   '****///////*****,,***/(((#####(/.'                     ,curses.color_pair(red))
            screen.addstr(middle_height+11, middle_width-40+21,   '....,,,,,,****.'                                       ,curses.color_pair(yellow_text))
            screen.addstr(middle_height+12, middle_width-40+39,   '***///////////////(((####(*.'                          ,curses.color_pair(red))
            screen.addstr(middle_height+12, middle_width-40+26,   '.....,,,,,***'                                         ,curses.color_pair(yellow_text))
            screen.addstr(middle_height+13, middle_width-40+45,   '****///(((//(((###(*.'                                 ,curses.color_pair(red))
            screen.addstr(middle_height+13, middle_width-40+66,   '.'                                                     ,curses.color_pair(yellow_text))
            screen.addstr(middle_height+13, middle_width-40+32,   '....,,,,*****'                                         ,curses.color_pair(yellow_text))
            screen.addstr(middle_height+14, middle_width-40+36,   '........,,,***,***//'                                  ,curses.color_pair(yellow_text))
            screen.addstr(middle_height+14, middle_width-40+54,   '///*****,'                                             ,curses.color_pair(red))
            screen.addstr(middle_height+14, middle_width-40+63,   ',.'                                                    ,curses.color_pair(yellow_text))
            screen.addstr(middle_height+15, middle_width-40+39,   '.....,,,,,,,****/***,,,,,.'                            ,curses.color_pair(yellow_text))
            screen.addstr(middle_height+16, middle_width-40+44,   '....,,,,,********,.'                                   ,curses.color_pair(yellow_text))
            screen.refresh()
            time.sleep(.1)
            count1 += 1
        screen.clear()

    except KeyboardInterrupt:
        curses.endwin()
        sys.exit("Keyboard Interrupt, Quitting...")


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

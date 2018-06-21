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

    # Audio File for welcome screen "smash themed sound effects"
    with open(os.devnull, 'wb') as devnull:
        subprocess.Popen(['aplay', dis.file_directory + 'smash.wav'], stdout=devnull, stderr=subprocess.STDOUT)

    # Printing PLayer info
    while True:
        try:
            middle_height, middle_width = ss.window_res(screen)
            screen.addstr(5,middle_width - 10, "*press space to start*")
            screen.addstr(3,middle_width - 8, "Odds Display Page", curses.A_UNDERLINE)
            screen.border()

            # Y componet offset for players X ussed in percent_print array
            y_offset    = 5
            j           = 4
            x           = 0

            for p in dis.players_array:

                # Displaying the OS being downloaded for player
                screen.addstr(y_offset+4, 13,  "Player"+str(x+1)+" |::| OS:", curses.A_BOLD)
                screen.addstr(y_offset+4, 26, str(dis.url_array_random_os[x]), curses.color_pair(cyan_dots))

                screen.addstr(y_offset+8, 10, "-"*(window_width*2-20))


                # Displaying File Name
                screen.addstr(y_offset+4, 40, "| File: ", curses.A_BOLD)
                screen.addstr(y_offset+4, 41, str(dis.five_files[x]),curses.color_pair(default))

                # Displaying URL
                screen.addstr(y_offset+6, 13, 'URL:')
                screen.addstr(y_offset+6, 19, str(dis.random_url_array[x]))

                # Displaying Latency
                screen.addch(y_offset+4, 89, '|',curses.A_BOLD)
                screen.addstr(y_offset+4, 90, 'Latency: ' + p.latency,curses.A_STANDOUT)
                #screen.addstr(y_offset+6, 13, 'ADDRESS: ' + str(p.server), curses.A_BOLD)

                # Offesting the next racer in y-direction and updating x for player percent_print array
                y_offset    += 6
                x           += 1

            # Space to continue to next screen
            key = screen.getkey()
            if(key == ' '):
                with open(os.devnull, 'wb') as devnull:
                    subprocess.Popen(['aplay', dis.file_directory + 'smash-effect.wav'], stdout=devnull, stderr=subprocess.STDOUT)
                    time.sleep(1.5)
                break


            screen.clear()
            screen.refresh()
            time.sleep(.1)

        except KeyboardInterrupt:
            curses.endwin()
            sys.exit("Keyboard, Interrupt Quitting...")

# Print screen pre stats page

def print_pre_intro():

    try:
        middle_height, middle_width = ss.window_res(screen)
        screen.border()

        # Y componet offset for players X ussed in percent_print array
        y_offset    = 11
        j           = 4
        x           = 0

        screen.addstr(middle_height-8,middle_width-35, " __    __     _                            _____        _____ _           ", curses.A_BOLD)
        screen.addstr(middle_height-7,middle_width-35, "/ / /\ \ \___| | ___ ___  _ __ ___   ___  /__   \___   /__   \ |__   ___  ", curses.A_BOLD)
        screen.addstr(middle_height-6,middle_width-35, "\ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \   / /\/ _ \    / /\/ '_ \ / _ \\", curses.A_BOLD)
        screen.addstr(middle_height-5,middle_width-35, " \  /\  /  __/ | (_| (_) | | | | | |  __/  / / | (_) |  / /  | | | |  __/ ", curses.A_BOLD)
        screen.addstr(middle_height-4,middle_width-35, "  \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \/   \___/   \/   |_| |_|\___| ", curses.A_BOLD)

        screen.addstr(middle_height-3,middle_width-45,"             _        ___                 ___                    _                 _            ",curses.A_BOLD)
        screen.addstr(middle_height-2,middle_width-45,"  /\  /\___ | |_     /   \___   __ _     /   \_____      ___ __ | | ___   __ _  __| | ___ _ __  ",curses.A_BOLD)
        screen.addstr(middle_height-1,middle_width-45," / /_/ / _ \| __|   / /\ / _ \ / _` |   / /\ / _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__| ",curses.A_BOLD)
        screen.addstr(middle_height,middle_width-45,  "/ __  / (_) | |_   / /_// (_) | (_| |  / /_// (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |    ",curses.A_BOLD)
        screen.addstr(middle_height+1,middle_width-45,"\/ /_/ \___/ \__| /___,' \___/ \__, | /___,' \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|    ",curses.A_BOLD)
        screen.addstr(middle_height+2,middle_width-45,"                               |___/                                                            ", curses.A_BOLD)

        # Audio File for welcome screen
        with open(os.devnull, 'wb') as devnull:
            subprocess.Popen(['aplay', dis.file_directory + 'welcome.wav'], stdout=devnull, stderr=subprocess.STDOUT)

        screen.refresh()

    except KeyboardInterrupt:
        curses.endwin()
        sys.exit("Keyboard, Interrupt Quitting...")

    screen.clear()
    k = 0
    for p in dis.players_array:
        p.server, directories = p.parse_server_info(str(dis.random_url_array[k]))
        p.determine_latancy()
        k += 1
    time.sleep(1)

# Print Hot dog litterally just prints the ascii hotdog dawggg
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

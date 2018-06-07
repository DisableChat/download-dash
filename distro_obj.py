
# Directory info
distro_list_dir     = '/home/wes/Source/download-dash/distros.txt'
file_directory      = '/home/wes/Source/download-dash/mirrorlists/'

# Text file names
arch            = 'arch.txt'
centos          = 'centos.txt'
debian          = 'debian.txt'
dragonflybsd    = 'dragonflybsd.txt'
fedora          = 'fedora.txt'
gentoo          = 'gentoo.txt'
mageia          = 'mageia.txt'
mint            = 'mint.txt'
nethbsd         = 'netbsd.txt'
openbsd         = 'openbsd.txt'
sabayon         = 'sabayon.txt'
slackware       = 'slackware.txt'
ubuntu          = 'ubuntu.txt'


##
# Distro takes the txt files and creates an array of the object Distro
# which contains the distro, location, path, filenames and address.
##
class Distro:

    # Array to hold distro obj's
    distro_lib_array = ''

    # Distro object vars
    distro           = ''
    path             = ''
    address          = ''
    filenames        = ''

    def open_file(self, file_directory, file):

        with open(file_directory + file, 'r') as fp:
            array = fp.readlines()
            for lines in range(len(array)):
                print(array[lines].strip('\n'))



test = Distro()
test.open_file(file_directory, fedora)

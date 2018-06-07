# Directory info
distro_list_dir     = '/home/wes/Source/download-dash/distros.txt'
file_directory      = '/home/wes/Source/download-dash/'

# Text file names
arch            = 'mirrorlists/arch.txt'
centos          = 'mirrorlists/centos.txt'
debian          = 'mirrorlists/debian.txt'
dragonflybsd    = 'mirrorlists/dragonflybsd.txt'
fedora          = 'mirrorlists/fedora.txt'
gentoo          = 'mirrorlists/gentoo.txt'
mageia          = 'mirrorlists/mageia.txt'
mint            = 'mirrorlists/mint.txt'
nethbsd         = 'mirrorlists/netbsd.txt'
openbsd         = 'mirrorlists/openbsd.txt'
sabayon         = 'mirrorlists/sabayon.txt'
slackware       = 'mirrorlists/slackware.txt'
ubuntu          = 'mirrorlists/ubuntu.txt'

# Array to hold distro obj's
distro_lib_array = []

##
# Distro takes the txt files and creates an array of the object Distro
# which contains the distro, location, path, filenames and address.
##
class Distro:

    # Distro object vars
    distro          = ''
    path            = ''
    address         = []
    filenames       = ''

    distro_loc      = []

    # Opens the txt file containing the distro addresses and then
    def create_address_array(self, file_directory, file):

        with open(file_directory + file, 'r') as fp:
            self.address = fp.readlines()
            for lines in range(len(self.address)):
                self.address[lines] = self.address[lines].strip('\n')


    def get_distro_spacing(self, distro_list_dir):

        counter = 0

        with open(distro_list_dir, 'r') as fp:
            array = fp.readlines()
            for line in range(len(array)):
                if(array[line].find(':') != -1):
                    self.distro_loc.append(line)
                    counter += 1

            for line in range(len(self.distro_loc)):
                print(self.distro_loc[line])

            print ("Number of Distros: ", counter)




test = Distro()
test.create_address_array(file_directory, fedora)
print(test.address[1] + 'hi')
test.get_distro_spacing(distro_list_dir)

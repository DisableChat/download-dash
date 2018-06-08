# Directory info
distro_list_dir     = '/home/wes/Source/download-dash/distros.txt'
file_directory      = '/home/wes/Source/download-dash/'

# Text file names
arch            = 'mirrorlists/arch.txt'
centos          = 'mirrorlists/centos.txt'
debian_dvd      = 'mirrorlists/debian.txt'
debian_cd       = 'mirrorlists/debian.txt'
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

    continue_flag   = True

    # Distro object vars
    distro          = ''
    path            = ''
    address         = []
    filenames       = ''

    # array of the locations of where the distros start (ie. arch = distro_loc[0])
    distro_loc      = []

    # Opens the txt file containing the distro addresses and then
    def create_address_array(self, file_directory, file):

        with open(file_directory + file, 'r') as fp:
            self.address = fp.readlines()
            for lines in range(len(self.address)):
                self.address[lines] = self.address[lines].strip('\n')

    # Determine the spacing between distros so we can use them for conditons later on
    def get_distro_spacing(self, distro_list_dir):

        counter = 0

        # Determing spacing and then appending them to the distro__loc array
        with open(distro_list_dir, 'r') as fp:

            array = fp.readlines()
            for line in range(len(array)):
                if(array[line].find(':') != -1):
                    self.distro_loc.append(line)
                    counter += 1

            # Append here becasue in parse_distro_txt we need to have a condition to check against
            self.distro_loc.append(999)


    # Parses distros text file
    def parse_distro_txt(self, distro_list_dir):

        # Distro_num represents distro number in distros txt so arch = 1
        distro_num = 1
        counter = 0


        with open(distro_list_dir, 'r') as fp:

            # Creating an array of the lines of the text file
            array = fp.readlines()

            # Loop while flag = True and distro num < len of the # of distros
            while(self.continue_flag and distro_num < len(self.distro_loc)):

                # Loop through text file
                for line in range(len(array)):

                    # Self.distro_loc[pos] = distro - 1 (so pos 0 = arch)
                    if(line < self.distro_loc[distro_num] and (line + 1) > self.distro_loc[distro_num - 1]):

                        # Located in file as a indicator
                        if(array[line].find('END:') != -1):
                            return

                        # Stripping the words and \n from the lines of in the text file
                        if(array[line].find(':') != -1):
                            print(array[line].strip('\n'))
                            array[line+1] = (array[line+1].strip('location '))
                            print(array[line+1].strip('= ' + '\n'))
                            array[line+2] = (array[line+2].strip('path +'))
                            print(array[line+2].strip('= '+ '\n'))

                            # First directory but need to strip the filename from that line of txt
                            array[line+3] = (array[line+3].strip('filenames '))
                            print(array[line+3].strip('+= ' + '\n'))
                            counter = line + 4

                            # Finding the rest of the directories
                            while(array[counter + 1].find(':') == -1):
                                print(array[counter].strip())
                                counter += 1

                            # Setting flag to false to get out of while loop so we can move to next distro
                            self.continue_flag = False

                # Reseting flag and incrementing distro we will be on next
                self.reset_flag()
                distro_num += 1

    # Flag reset function
    def reset_flag(self):
        self.continue_flag = True

#-----------------------------------------------------TEST--------------------------------------------------#

test = Distro()
test.create_address_array(file_directory, fedora)
print(test.address[1] + 'hi')
test.get_distro_spacing(distro_list_dir)
test.parse_distro_txt(distro_list_dir)

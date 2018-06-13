import random

random.seed()

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

os_array = [arch,centos,debian_dvd,debian_cd,dragonflybsd,fedora,gentoo,mageia,mint,nethbsd,openbsd,sabayon,slackware,ubuntu]

# Array to hold distro obj's
distro_lib_array = []

# Array of random url's
random_url_array = []

# Final array of url's with no repeats from same os
url_array           = []
url_array_os        = []

# Used by runtime, to know which os has been chosen for random url
url_array_random_os = []
file_array_tmp      = []
five_files          = []

##
# Distro takes the txt files and creates an array of the object Distro
# which contains the distro, location, path, filenames and address.
##
class Distro:

    # array of the locations of where the distros start (ie. arch = distro_loc[0])
    distro_loc      = []
    distro_ver      = 0


    # Each objects inital variables when instantiated
    def __init__(self):
        self.distro         = ''
        self.location       = ''
        self. path          = ''
        self.filenames      = []
        self.address        = []

        self.random_url     = ''

    # Opens the txt file containing the distro addresses and then
    def create_address_array(self, file_directory, file):
        with open(file_directory + file, 'r') as fp:
            self.address = fp.readlines()
            for lines in range(len(self.address)):
                self.address[lines] = self.address[lines].strip('\n')

            # TODO Print helpers
            #for i in range(len(self.address)):
            #    print(self.address[i])

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
    def parse_distro_txt(self, distro_list_dir, distro_ver):

        # Distro_num represents distro number in distros txt so arch = 1
        distro_num = distro_ver
        counter = 0
        i = 1

        with open(distro_list_dir, 'r') as fp:

            # Creating an array of the lines of the text file
            array = fp.readlines()

            # TODO Helper function
            #print('Distro Number In Array',distro_num)

            # Loop through text file
            for line in range(len(array)):

                # Self.distro_loc[pos] = distro - 1 (so pos 0 = arch)
                if(line < self.distro_loc[distro_num] and (line + 1) > self.distro_loc[distro_num - 1]):

                    # Located in file as a indicator
                    if(array[line].find('END:') != -1):
                        return

                    # Stripping the words and \n from the lines of in the text file
                    if(array[line].find(':') != -1):
                        self.distro = (array[line].strip(':' + '\n'))
                    #    print(self.distro) # TODO Print helper

                        # Setting Obj's location
                        array[line+1] = (array[line+1].strip('location '))
                        self.location = (array[line+1].strip('= ' + '\n'))
                    #    print(self.location) # TODO Print helper

                        # Setting Obj's path
                        array[line+2] = (array[line+2].strip('path +'))
                        self.path = (array[line+2].strip('= ' + '\n'))
                    #    print(self.path) # TODO Print helper

                        # First directory but need to strip the filename from that line of txt
                        array[line+3] = (array[line+3].strip('filenames '))
                        self.filenames.append(array[line+3].strip('+= ' + '\n'))
                        counter = line + 4

                        # Finding the rest of the directories and appending them to array
                        while(array[counter + 1].find(':') == -1):
                            self.filenames.append(array[counter].strip())
                            i += 1
                            counter += 1

            # TODO print helper
            #for k in range(len(self.filenames)):
            #    print(self.filenames[k])

    # Randomly chooses file name and address and connects them with the distro's location
    # and path to create a randomly generated url from library
    def glue_url(self, num):
        section_one = random.choice(distro_lib_array[num].address)
        section_two =   distro_lib_array[num].path
        section_three = str(random.choice(distro_lib_array[num].filenames))
        self.random_url = section_one + section_two + section_three
        random_url = section_one + section_two + section_three
        file_array_tmp.append(section_three)
        return random_url

    # Get txt file addresses for os and put them in corrosponding objects address array
    def get_address(self):
        # We do len(self.distro_loc )- 1 because END: is considered 1 of the os's
        for i in range(1, len(self.distro_loc)- 1, 1):
            distro_lib_array[i].create_address_array(file_directory, os_array[i-1])

#-----------------------------------------------------Creation----------------------------------------------------#

test = Distro()
test.get_distro_spacing(distro_list_dir)
for i in range(len(test.distro_loc)):
    distro_lib_array.append(Distro())

# Going through and parsing
i = 0
for d in distro_lib_array:
    d.parse_distro_txt(distro_list_dir, i)
    i += 1

# filling addresses into the corresponding obj
distro_lib_array[1].get_address()

# creating random url for each obj in array
for j in range(1,len(distro_lib_array)-1, 1):

    distro_lib_array[j].glue_url(j)
    random_url_array.append(distro_lib_array[j].random_url)
    # TODO printer helper to show if the url you downloaded is typo due to txt docu
    #print(distro_lib_array[j].random_url)
    url_array_os.append(distro_lib_array[j].distro)


# Choose racers finally chooses the racers from distro where there are no repeats on os and each is unique
def choose_racers():

    size = len(random_url_array)
    tmp_array = []

    for k in range(0, len(test.distro_loc)-2, 1):
        tmp_array.append(distro_lib_array[k+1].distro)

    while(size > 9):

        index = random.randrange(size)

        url_array.append(random_url_array[index])
        url_array_random_os.append(tmp_array[index])
        five_files.append(file_array_tmp[index])
        #element3 = file_array_tmp[index]
        #print (element3)
        random_url_array[index] = random_url_array[size - 1]
        tmp_array[index] = tmp_array[size - 1]
        file_array_tmp[index] = file_array_tmp[size - 1]
        size -= 1
    #TODO Printer Helper used to show if URL downloaded is typo or bug NOTE ask creator for clarification
        #print(element)
        #print(element2)
    #for i in range(5):
    #    print(url_array[i])
    #    print(five_files[i])
    #    print(url_array_random_os[i])
    return url_array, url_array_os

#choose_racers()

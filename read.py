# read.py
import distro_http_obj as dho
class Distro:

    # Directory info
    file_directory      = '/home/wes/Source/download-dash/mirrorlists/'
    file_name           = 'sabayon.txt'
    distro_list_dir     = '/home/wes/Source/download-dash/distros.txt'


    # Distro array vars
    distro_counter      = 1
    distro_array        = [distro_counter]
    distro_seperation   = [distro_counter]

    # Creates a distro_array func
    def create_distro_array(self):
        with open(self.distro_list_dir, 'r') as fp:
            array = fp.readlines()
            for line in range(len(array)):
                if(array[line].find(':') != -1):
                    print(array[line].strip('\n'))
                    print(line)
                    self.distro_seperation.append(line)
                    self.distro_counter += 1

            print ("\nNumber of Distros: ", self.distro_counter)
            for i in range(len(self.distro_seperation) - 1):
                print("Line Number: ", self.distro_seperation[i + 1])


test = Distro()
distro_obj = dho.Distro_HTTP()
test.create_distro_array()

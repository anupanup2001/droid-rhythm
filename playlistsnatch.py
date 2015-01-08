import xml.etree.ElementTree as ET
import subprocess
#fileName = '/home/fornix/.local/share/rhythmbox/playlists.xml'
filename = 'playlists.xml'

class PlaylistSnatch:
    """This class will snatch playlist files from rhythmbox"""
    
    def __init__(self, fileName):
        self.tree = ET.parse(fileName)
        self.root = self.tree.getroot()

    def getPlaylistNames(self):
        names = []
        for playlist in self.root:
            names.append(playlist.attrib['name'])
        return names
        
    def getFileNamesFromPlaylist(self, nPlaylistIndex):
        files = []
        l_playlistElem = self.root[nPlaylistIndex]
        for item in l_playlistElem:
            files.append(item.text)
        return files

if __name__ == "__main__":
    x = PlaylistSnatch(filename)
    print (x.__doc__)
    names = x.getPlaylistNames()
    while True:
        i = 1
        for playlist in names:
            print i, ". ", playlist
            i = i + 1
        l_nSelection = raw_input("Your Selection. q to quit -->")
        if l_nSelection == 'q':
            break
        files = x.getFileNamesFromPlaylist(int(l_nSelection) - 1)
        
        #Print all file names
        for l_fileName in files:
            subprocess.call(["echo", l_fileName[7:]])
        subprocess.call(["pause"])

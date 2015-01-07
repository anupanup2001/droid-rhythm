import xml.etree.ElementTree as ET
class PlaylistSnatch:
    """This clas will snatch playlist files from rhythmbox"""
    
    def __init__(self, fileName):
        self.tree = ET.parse(fileName)
        self.root = self.tree.getroot()

    def getPlaylistNames(self):
        names = []
        for playlist in self.root:
            names.append(playlist.attrib['name'])
        return names

if __name__ == "__main__":
    x = PlaylistSnatch('/home/fornix/.local/share/rhythmbox/playlists.xml')
    print (x.__doc__)
    print x.getPlaylistNames()

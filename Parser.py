from decouple import config
import urllib.request

class Parser:
    def __init__(self):
        self.ads = []
        file = open('url_list.txt', 'r')
        lines = file.readlines()
        file.close()
        for line in lines:
            url = line.replace('\n', '')
            if url:
                self.ads.append(url)

        self.url = config('WEB_URL')

    # Add URL to the list of URLs
    def addAdd(self, adURL):
        self.ads.append(adURL)
        file = open('url_list.txt', 'a')
        file.write("{}\n".format(adURL))
        file.close

    def parse(self):
        # Establish a connection with the website
        connection = urllib.request.urlopen(self.url)
        # Read the page into bytes
        bytes = connection.read()
        # Decode the bytes into a string
        html = bytes.decode('utf8')
        # Close the connection with the website
        connection.close()
        # Split new lines into array elements
        html = html.split('\n')

        # Declare an empty array for new ads
        newAds = []

        for line in html:
            # Check if the line contains the class which tells us the line also contains the ad url
            if 'class="prodajalec_o"' in line:
                # Parse the ad URL
                parsedURL = line.split('href=')[1].split('"')[1].split('/')[2]

                # Check if the parsed URL is not amongst the already parsed ads
                if parsedURL not in self.ads:
                    self.addAdd(parsedURL)

    def getURLs(self):
        return self.ads

    def validateIDs(self):
        uniqueIDs = []
        notUniqueIDs = []
        for ad in self.ads:
            id = ad.split('_')[1]
            if id not in uniqueIDs:
                uniqueIDs.append(id)
            elif id not in notUniqueIDs:
                notUniqueIDs.append(id)
        return notUniqueIDs
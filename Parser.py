from Mailer import Mailer
import urllib.request

mailer = Mailer()

class Parser:
    # Load data from enviromental variables, set the parse URL and load all the parsed URLs
    def __init__(self, parseURL):
        print('Initializing parser')
        self.ads = []
        file = open('url_list.txt', 'r')
        lines = file.readlines()
        file.close()
        for line in lines:
            url = line.strip('\n')
            if url:
                self.ads.append(url)

        self.url = parseURL
        self.adType =  self.url.split('/')[3]
        print('Parser successfully initialized!')

    # Add URL to the list of URLs
    def addAd(self, adURL):
        print('Adding ad for {}'.format(adURL))
        self.ads.append(adURL)
        file = open('url_list.txt', 'a')
        file.write("{}\n".format(adURL))
        file.close

    # Parse the site based on the URL on the class instance
    def parse(self):
        # Establish a connection with the website
        print('Establishing connection with the server...')
        connection = urllib.request.urlopen(self.url)

        # Read the page into bytes
        print('Connection established, getting data...')
        bytes = connection.read()

        # Close the connection with the website
        connection.close()

        # Decode the bytes into a string
        print('Data recieved, decoding...')
        html = bytes.decode('utf8')

        # Split new lines into array elements
        print('Data decoded, parsing...')
        html = html.split('\n')

        # Declare an empty array for new ads
        newAds = []

        # Loop through all of the lines of the HTML of the webpage
        for line in html:
            # Check if the line contains the class which tells us the line also contains the ad url
            if 'class="prodajalec_o"' in line:
                # Parse the ad URL
                parsedURL = line.split('href=')[1].split('"')[1].split('/')[2]

                # Check if the parsed URL is not amongst the already parsed ads
                if parsedURL not in self.ads:
                    self.addAd(parsedURL)
                    newAds.append('https://www.nepremicnine.net/{}/{}'.format(self.adType, parsedURL))
        
        # Check if there was any new ads found
        if len(newAds) > 0:
            print('Found {} new ads, sending email...'.format(len(newAds)))
            self.sendEmailWithAds(newAds)
        else:
            print('No new ads found!')
    
    # Send an email containing all the new ads
    def sendEmailWithAds(self, ads):
        # Build the email message
        message = "Novi oglasi za iskalnik - {}\n".format(self.url)
        for ad in ads:
            message = "{}{}/\n".format(message, ad)

        # Send the email
        mailer.sendEmail(message, 'Novi oglasi')

    # Get all of the parsed URLs
    def getURLs(self):
        return self.ads

    # Validate the ad IDs to search for for duplicate ads
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
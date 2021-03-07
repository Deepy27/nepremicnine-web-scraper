from Parser import Parser
from Logger import Logger
from decouple import config
import traceback
import time

# Load the URLs to be parsed from the enviromental variables
# @TODO - add checks for correct information
parseURLs = config('WEB_URLS').split(',')
parsers = []

# Loop through all of the parse URLs
for parseURL in parseURLs:
    # Generate a parser and add it to the parsers array
    parsers.append(Parser(parseURL))

# @TODO - make some better logic than this
while True:
    # Try to parse all of the URLs, if anything went wrong, log it
    try:
        # Loop through all of the parsers
        for parser in parsers:
            # Parse the URL
            parser.parse()
    except Exception as e:
        # Log the error
        Logger.log(traceback.format_exc())

    # @TODO - implement some better logic here as well, maybe load the delay from .env?
    time.sleep(1)
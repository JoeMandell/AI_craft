from bs4 import BeautifulSoup
import requests
import re

response3 = requests.get("https://www.grabcraft.com/js/RenderObject/myRenderObject_2442.js")
soup3 = BeautifulSoup(response3.content, 'html.parser')

coordinates_list = []

# Regular expression pattern to match x, y, z values
pattern = r'"x":(\d+),"y":"(\d+)","z":"(\d+)"'

# Find all matches in the text_data
matches = re.findall(pattern, str(soup3))

# Extract and store x, y, z values in the coordinates_list
for match in matches:
    x = int(match[0])
    y = int(match[1])
    z = int(match[2])
    coordinates_list.append([x, y, z])

print(coordinates_list)

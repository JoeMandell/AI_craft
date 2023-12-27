from bs4 import BeautifulSoup
import requests
import re
import csv



names = []
descriptions = []
xyzlist = []
value_tags_list = []
value_block_count_list = []
materials_list = []
coordlist = []


number = 1
url = "https://www.grabcraft.com/minecraft/buildings/sort/name2/pg/"

for k in range(3):
    response = requests.get(url + str(number))
    soup = BeautifulSoup(response.content, 'html.parser')
    building_elements = soup.find_all('div', class_='text-info')
    
    #Gets the building name and the number of blocks it uses
    for building in building_elements:
        #info for name
        title_element = building.find('h3', class_='name').find('a')
        link = str(title_element.get('href'))
        #info for description

        print(str(link))
        response2 = requests.get("https://www.grabcraft.com" + link)
        soup2 = BeautifulSoup(response2.content, 'html.parser')

        title = soup2.find('h1', id='content-title').text
        print(title)
        names.append(title)
        

        description = soup2.find('div', class_='description').text
        print(description)
        descriptions.append(description)

        xyzlisttemp = []
        value_dimension_x = soup2.find('td', class_='value dimension-x').text
        print(value_dimension_x)
        xyzlisttemp.append(value_dimension_x)

        value_dimension_y = soup2.find('td', class_='value dimension-y').text
        print(value_dimension_y)
        xyzlisttemp.append(value_dimension_y)

        value_dimension_z = soup2.find('td', class_='value dimension-z').text
        print(value_dimension_z)
        xyzlisttemp.append(value_dimension_z)
        xyzlist.append(xyzlisttemp[0] +","+ xyzlisttemp[1] +","+ xyzlisttemp[2] )

        
        value_tags = soup2.find('td', class_='value tags').text
        print(value_tags)
        value_tags_list.append(value_tags)

        value_block_count = soup2.find('td', class_='value block_count').text
        print(value_block_count)
        value_block_count_list.append(value_block_count)

        templist = []
        materials = soup2.find('table', id='materials_list').find_all('td', 'name')
        for i in materials[:3]:
            print(i.text.strip())
            
            templist.append(i.text.strip())
        materials_list.append(templist[0] +","+ templist[1] +","+ templist[2] )
        




        

        ThreeD_link = re.search(r'RenderObject/([^/]+)\.js', str(soup2))
        ThreeD_link = ThreeD_link.group(1)
        response3 = requests.get("https://www.grabcraft.com/js/RenderObject/" + ThreeD_link + ".js")
        print("https://www.grabcraft.com/js/RenderObject/" + ThreeD_link + ".js")
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
        coordlist.append(coordinates_list)

    number += 1



print(len(names))
print(len(descriptions))
print(len(xyzlist))
print(len(value_tags_list))
print(len(value_block_count_list))
print(len(materials_list))


# Organize data into rows
rows = zip(names, xyzlist, value_tags_list, value_block_count_list, materials_list,coordlist)

# Define the CSV file name
csv_file = 'data.csv'

# Write data to CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    # Write header if needed
    writer.writerow(['names', 'xyzlist', 'value_tags_list', 'value_block_count_list', 'materials_list','coordinate list'])  # Replace with your column headers
    # Write rows from the lists
    writer.writerows(rows)

print(f"CSV file '{csv_file}' has been created with the data from the lists.")



def scraper(url):
    response = requests.get(url + str(number))
    soup = BeautifulSoup(response.content, 'html.parser')
    building_elements = soup.find_all('div', class_='text-info')
    
    #Gets the building name and the number of blocks it uses
    for building in building_elements:
        #info for name
        title_element = building.find('h3', class_='name').find('a')
        link = str(title_element.get('href'))
        #info for description

        print(str(link))
        response2 = requests.get("https://www.grabcraft.com" + link)
        soup2 = BeautifulSoup(response2.content, 'html.parser')

        title = soup2.find('h1', id='content-title').text
        print(title)
        names.append(title)
        

        description = soup2.find('div', class_='description').text
        print(description)
        descriptions.append(description)

        xyzlisttemp = []
        value_dimension_x = soup2.find('td', class_='value dimension-x').text
        print(value_dimension_x)
        xyzlisttemp.append(value_dimension_x)

        value_dimension_y = soup2.find('td', class_='value dimension-y').text
        print(value_dimension_y)
        xyzlisttemp.append(value_dimension_y)

        value_dimension_z = soup2.find('td', class_='value dimension-z').text
        print(value_dimension_z)
        xyzlisttemp.append(value_dimension_z)
        xyzlist.append(xyzlisttemp[0] +","+ xyzlisttemp[1] +","+ xyzlisttemp[2] )

        
        value_tags = soup2.find('td', class_='value tags').text
        print(value_tags)
        value_tags_list.append(value_tags)

        value_block_count = soup2.find('td', class_='value block_count').text
        print(value_block_count)
        value_block_count_list.append(value_block_count)

        templist = []
        materials = soup2.find('table', id='materials_list').find_all('td', 'name')
        for i in materials[:3]:
            print(i.text.strip())
            
            templist.append(i.text.strip())
        materials_list.append(templist[0] +","+ templist[1] +","+ templist[2] )
        

        ThreeD_link = re.search(r'RenderObject/([^/]+)\.js', str(soup2))
        ThreeD_link = ThreeD_link.group(1)
        response3 = requests.get("https://www.grabcraft.com/js/RenderObject/" + ThreeD_link + ".js")
        print("https://www.grabcraft.com/js/RenderObject/" + ThreeD_link + ".js")
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


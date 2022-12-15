import csv
from xml.etree.ElementTree import Element, SubElement, ElementTree

html = Element('html')


head = SubElement(html,'head')
body = SubElement(html,'body')


table = SubElement(body,'table')

table.set("border","1")
headers = SubElement(table, "tr")
title_header = SubElement(headers, "th")
title_header.text = "Title"

url_header = SubElement(headers, "th")
url_header.text = "URL"

with open('feminism_results.csv') as csvfile:

	reader = csv.reader(csvfile)
	next(reader)

	for row in reader:


		# <tr>
		# 	<td>title</td>
		# 	<td>note</td>
		# </tr>


		tr = SubElement(table,'tr')


		name_td = SubElement(tr,'td')
		sol_name = f"{row[2]}"
		name_td.text = sol_name

		link_td = SubElement(tr,'td')
		if len(row) > 6:
			sol_url = row[6]
			link_td.text = sol_url



ElementTree(html).write('test.html')

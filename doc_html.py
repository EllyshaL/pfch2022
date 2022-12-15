import csv
from xml.etree.ElementTree import Element, SubElement, ElementTree

html = Element('html')


head = SubElement(html,'head')
body = SubElement(html,'body')


table = SubElement(body,'table')

table.set("border","1")

with open('feminism_results.csv') as csvfile:

	reader = csv.reader(csvfile)

	for row in reader:


		# <tr>
		# 	<td>title</td>
		# 	<td>note</td>
		# </tr>


		tr = SubElement(table,'tr')


		name_td = SubElement(tr,'td')

		if row[3] == "":
			sol_name = f"{row[2]}, {"resources"}"
		else:
			sol_name = f"{row[2]}, {"resources"}, (URL:{row[1]})"


		name_td.text = sol_name


		note_td = SubElement(tr,'td')


		ref_td = SubElement(tr,'td')


		print(sol_name)

ElementTree(html).write('test.html')

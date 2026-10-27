import xml.dom.minidom as minidom

print("Task_4")
with open(r"C:\Users\Lena\Desktop\Программирование на Питон\LW2\currency.xml") as xml_file:
    xml_data = xml_file.read()
    dom = minidom.parseString(xml_data)
    dom.normalize()
    nodes = dom.getElementsByTagName('Valute')
    value_list = []

    for node in nodes:
        for child in node.childNodes:
            if child.nodeType == 1:
                if child.tagName == 'Value':
                    value_list.append(float(child.firstChild.data.replace(',','.')))
    if len(value_list) > 0:
        print("The average Value indicator:", sum(value_list)/len(value_list))
    
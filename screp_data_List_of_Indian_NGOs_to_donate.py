link='https://www.giveindia.org/certified-indian-ngos'
def List_of_Indian_NGOs_to_donate(url): 
	from bs4 import BeautifulSoup
	import pprint
	import requests
	page = requests.get(url)
	soup = BeautifulSoup(page.text,"html.parser")
	man_class=soup.find('table',class_='jsx-697282504 certified-ngo-table')
	list1=[]
	for i in man_class.findAll('tr',class_='jsx-697282504'):
		list_2=[]
		for td in i.findAll('td',class_='jsx-697282504'):
			# print(td.text)
			list_2.append(td.text)
		list1.append(list_2)
	# print(list1)
	list_2=[]
	var=1
	while var < len(list1):
		a=list1[var]
		dict_1={'name':a[0],'work':a[1],'state':a[2]}
		list_2.append(dict_1)

		var+=1

	new_list=[]
	for i in list_2:
		a=i['state']
		if a not in new_list:
			new_list.append(a)
	state_dict={}
	for j in new_list:
		state_list=[]
		for k in list_2:
			if k['state'] == j:
				state_list.append(k)
		# print(state_list)
		# print(j)
		state_dict[j]=state_list
	pprint.pprint(state_dict)


List_of_Indian_NGOs_to_donate(link)
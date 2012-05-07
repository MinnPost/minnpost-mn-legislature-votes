import sunlight

def get_vote(bill):
	bill_data = sunlight.openstates.bill_detail('MN','2011-2012',bill)
	
	affirmative_ids = []
	
	for legislator in bill_data['votes'][-1]['yes_votes']:
		affirmative_ids.append(legislator['leg_id'])
	
	negative_ids = []
	
	for legislator in bill_data['votes'][-1]['no_votes']:
		negative_ids.append(legislator['leg_id'])
		
	all_votes = []
	
	for leg in affirmative_ids:
		legislator = sunlight.openstates.legislator_detail(leg)
		
		name = legislator['full_name']
		party = legislator['party']
		district = legislator['roles'][0]['district']
		vote = 'yes'
		
		all_votes.append([name,party,district,vote])
		
	for leg in negative_ids:
		legislator = sunlight.openstates.legislator_detail(leg)
		
		name = legislator['full_name']
		party = legislator['party']
		district = legislator['roles'][0]['district']
		vote = 'no'
		
		all_votes.append([name,party,district,vote])
		
	return all_votes

def write_table(bill):
	f = open('votetable.html', 'a')
	votes = get_vote(bill)
	f.write("<table>\n")
	for leg in votes:
		f.write("<tr>")
		for info in leg:
			f.write("<td>"+info+"</td>")
		f.write("</tr>\n")
	f.write("</table>")
	f.close()
	
write_table('HF 1974')

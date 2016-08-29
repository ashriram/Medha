#!/usr/bin/env ruby
require 'csv'
require 'json'
require 'date'
FILE = ARGV[0]
START_DATE = ARGV[1]
END_DATE = ARGV[2]

EduFile = File.new("ParsedEducation.txt", "w+")
CompanyFile = File.new("ParsedCompanies.txt", "w+")


counter = 0
print "Finding employees with start dates after " + ARGV[1] + "\n"
file = File.read(ARGV[0])
data_hash = JSON.parse(file)
for i in data_hash
	print "\n" + counter.to_s + "." + i['name'] + "\n"  
	counter=counter + 1 
	print "-----------Education----------------\n"
	if i['education'] != []
		edu = i['education']
		print edu.last['name'] + "," + edu.last['description'] + "," + edu.last['period'] + "\n" 
	end
  	print "---------- Past Companies-----------\n"
	for j in i['past_companies']
		unless j['end_date'].nil? 
			# This means that the start date was before that year and the end date was either that year or later
			if Date.parse(j['start_date']) <= Date.parse(ARGV[1]) && Date.parse(j['end_date']) >= Date.parse(ARGV[1])
				print j['company'] + "," + j['start_date'] + "," + j['end_date']
				print "\n"
			end
			# This means that the start date was before that year and the end date was either that year or later
			if Date.parse(j['start_date']) >= Date.parse(ARGV[1]) 
				print j['company'] + "," + j['start_date'] + "," + j['end_date']
				print "\n"
			end
		end		
	end
	print "-----------Current Companies-------\n"
	for j in i['current_companies']
		unless j['end_date'].nil? 
			# This means that the start date was before that year and the end date was either that year or later
			if Date.parse(j['start_date']) <= Date.parse(ARGV[1]) && Date.parse(j['end_date']) >= Date.parse(ARGV[1])
				print j['company'] + "," + j['start_date'] + "," + j['end_date']
				print "\n"
			end
			# This means that the start date was before that year and the end date was either that year or later
			if Date.parse(j['start_date']) >= Date.parse(ARGV[1]) 
				print j['company'] + "," + j['start_date'] + "," + j['end_date']
				print "\n"
			end
		end
	end  
end 

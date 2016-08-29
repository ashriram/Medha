#!/usr/bin/env ruby
require 'csv'
require 'json'

counter = 0
txtfile = File.new("LinkedIn.txt", "w+")
jsonfile = File.new("LinkedIn.json", "w+")
require_relative '../lib/linkedin-scraper'
File.open("Names.txt", "r+") do |file|
  while line = file.gets
  	profile = Linkedin::Profile.new(line)
	txtfile.puts counter.to_s + "." + profile.name
	txtfile.puts JSON.pretty_generate JSON.parse(profile.to_json)
	txtfile.puts "\n\n"
	X = profile.to_json
	jsonfile.puts X
#puts "\n\n"
#puts JSON.parse(X)
	jsonfile.puts ",\n"
	counter=counter+1
  end
end
puts "Parsed" + counter.to_s
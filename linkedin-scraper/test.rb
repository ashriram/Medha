require 'rubygems'
require 'mechanize'
require 'cgi'
require 'net/http'
Dir["#{File.expand_path(File.dirname(__FILE__))}/linkedin-scraper/*.rb"].each { |file| require file }

profile = Linkedin::Profile.get_profile("http://www.linkedin.com/in/jeffweiner08")

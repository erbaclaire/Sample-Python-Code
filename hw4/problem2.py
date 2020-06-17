'''
Homework 4 - Problem 2:
In this problem, we're going to continue exploring open data from the City of
Chicago, except this time we're going to take advantage of object-oriented
programming to build the foundation for a hypothetical "Chicago Public Schools
application". We have provided you with a CSV file with data on each public school
in Chicago including its name, location, address, what grades are taught, and what
network it is part of. You are asked to write three classes that will allow a user to
easily interact with this data.

See HW4 PDF for specifications
'''

# Checked work with Matt Pozsgai
import csv
import webbrowser
from math import sqrt, asin, cos, sin, radians, degrees

class School:

    def __init__(self, data):
        self.id = data['School_ID']
        self.name = data['Short_Name']
        self.network = data['Network']
        self.address = data['Address']
        self.zip = data['Zip']
        self.phone = data['Phone']
        self.grades = data['Grades'].split(',')
        self.location = Coordinate.fromdegrees(float(data['Lat']), float(data['Long']))

    def open_website(self):
        webbrowser.open_new_tab("https://schoolinfo.cps.edu/schoolprofile/SchoolDetails.aspx?SchoolId={}".format(self.id))

    def distance(self, coord):
        return self.location.distance(coord)

    def full_address(self):
        return ("{}\nChicago, IL {}".format(self.address, self.zip))

    def __repr__(self):
        return "School({})".format(self.name)


class Coordinate:

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    @classmethod # cite: https://www.geeksforgeeks.org/class-method-vs-static-method-python/
    def fromdegrees(cls, latitude, longitude):
        return cls(radians(latitude), radians(longitude))

    def distance(self, coord):
        return (2*3961*asin(sqrt(sin((self.latitude-coord.latitude)/2)**2 + cos(self.latitude)*cos(coord.latitude)*(sin((self.longitude-coord.longitude)/2)**2))))
    
    def as_degrees(self):
        return (degrees(self.latitude), degrees(self.longitude))

    def show_map(self):
        webbrowser.open_new_tab("http://maps.google.com/maps?q={},{}".format(self.as_degrees()[0],self.as_degrees()[1]))

    def __repr__(self):
        return "Coordinate{}".format(self.as_degrees())


class CPS:

    def __init__(self, filename):
        with open(filename, newline='') as f:
            reader = csv.DictReader(f)
            self.schools = []
            for row in reader:
                self.schools.append(School(row))
        
    def nearby_schools(self, coord, radius = 1.0):
        return [school for school in self.schools if school.distance(coord) < radius]

    def get_schools_by_grade(self, *grades):
        return [school for school in self.schools if len(set(map(lambda x: x.strip(), school.grades)) & set(grades)) == len(set(grades))]

    def get_schools_by_network(self, network):
        return [school for school in self.schools if school.network == network]

'''
if __name__ == '__main__':
    cps = CPS('schools.csv')

    print(cps.schools[:5])

    print([s for s in cps.schools if s.name.startswith('OR')])

    ace_tech = cps.schools[1]    
    print(ace_tech.name)
    print(ace_tech.id)
    print(ace_tech.network)
    print(ace_tech.address)
    print(ace_tech.zip)
    print(ace_tech.full_address())
    print(ace_tech.phone)
    print(ace_tech.grades)
    print(ace_tech.location)
    print(ace_tech.location.as_degrees())
    print(ace_tech.distance(cps.schools[77].location))
    
    the_bean = Coordinate.fromdegrees(41.8821512, -87.6246838)
    print(cps.nearby_schools(the_bean, radius=0.5)) 
    print(cps.get_schools_by_grade('PK', '12'))
    print(cps.get_schools_by_network('Contract'))

    cics_ip = cps.schools[11]
    cics_ip.open_website()
    ace_tech.location.show_map()
'''

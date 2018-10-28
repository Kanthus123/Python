#It presents a way to access the elements of an object without exposing the underlying presentation.

#An old radio set will be a good example of iterator, where user could start at some channel and then use next or previous buttons to go through the respective channels.
#Or take an example of MP3 player or a TV set where you could press the next and previous buttons to go through the consecutive channels or
#in other words they all provide an interface to iterate through the respective channels, songs or radio stations.

class RadioStation:

    def __init__(self, frequency):
        self.frequency = frequency

    def get_frequency(self):
        return self.frequency

class StationList:


    def __init__(self):
        self.stations = []
        self.counter = 0

    def add_station(self, station):
        self.stations.append(station)

    def remove_station(self, to_remove):
        to_remove_frequency = to_remove.get_frequency()
        self.stations = [s for s in self.stations if s.get_frequency() != to_remove_frequency]

    def count(self):
        return len(self.stations)

    def current(self):
        return self.stations[self.counter]

    def key(self):
        return self.counter

    def next(self):
        self.counter += 1

    def rewind(self):
        self.counter = 0

if __name__ == '__main__':

    stations_list = StationList()
    station_list.add_station(RadioStation(89))
    station_list.add_station(RadioStation(101))
    station_list.add_station(RadioStation(102))
    station_list.add_station(RadioStation(103.2))

    for i in range(station_list.count(), 0, -1):
        print(station_list.current().get_frequency())
        station_list.next()

    station_list.remove_station(RadioStation(89))
    station_list.rewind()

    for i in range(station_list.count(), 0, -1):
        print(station_list.current().get_frequency())
        station_list.next()

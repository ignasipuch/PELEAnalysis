# Python imports
import sys


class TimeStructure:

    name = ""
    name_to_search_in_log_file = ""
    time_position_in_log_file = 0

    def __init__(self):
        self._total_time = 0
        self._occurrences = 0
        self._lowest_time = sys.float_info.max
        self._highest_time = sys.float_info.min

    def print_report(self):
        print(self)

    def __str__(self):
        return "PELE " + self.name + " time: \n" + \
               "---Average time: " + str(self.calculate_average()) + "\n" + \
               "---Highest time: " + str(self.highest_time) + "\n" + \
               "---Lowest time: " + str(self.lowest_time) + "\n"

    # Properties
    @property
    def total_time(self):
        return self._total_time

    @property
    def occurrences(self):
        return self._occurrences

    @property
    def lowest_time(self):
        return self._lowest_time

    @property
    def highest_time(self):
        return self._highest_time

    # Setters
    @total_time.setter
    def total_time(self, time):
        self._total_time = time

    @occurrences.setter
    def occurrences(self, number_of_occurrences):
        self._occurrences = number_of_occurrences

    @lowest_time.setter
    def lowest_time(self, time):
        self._lowest_time = time

    @highest_time.setter
    def highest_time(self, time):
        self._highest_time = time

    # Methods
    def increment_total_time(self, time):
        self.total_time += time

    def increment_occurrences(self, number_of_occurrences):
        self.occurrences += number_of_occurrences

    def calculate_average(self):
        return self.total_time / self.occurrences

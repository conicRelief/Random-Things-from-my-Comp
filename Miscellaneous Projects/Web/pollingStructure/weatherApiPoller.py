import requests
import time
import calendar
import thread
import math
import heapq
import json

class weatherPollingClass:

    def __initiate_polling(self,pollingIntervalInSeconds,iter):
        print "Polling", pollingIntervalInSeconds
        tableSize = int(self.max_table_size)

        while True:
            time.sleep(pollingIntervalInSeconds)
            # Interesting Idea here.
            # we need to reward hits and penalize timeouts of faults.
            # input: timeout-interval. There is likely a sweet spot that reduces the running moving average.
            # output:

            # print("Im polling!", self.resource)
            ## Every interval look at the most recently polled
            # print self.max_table_size
            ## In this section we update the n-most recently requested times.
            # things_to_poll = [self.maxHeap.pop() for x in xrange(tableSize)]


    def make_a_request(self,city):
        self.resource = self.resource + 1
        print self.prepend, "Handling Request from" ,  city,'| assigning request key:', self.resource

        # The following is O(N). With fancy hash-maps we can get closer to O(nLog(n)). Implementation is an exercise left
        # to patient programmers. The purpose of this code is exploitation of request statistics
        #  and the utilization of a "reference-of-locality"-like polling policy for a 3rd party API integration.
        # In this setting request cost is not measured in time, but in monetary setback (since every request we make costs us)

        response = None
        newHeap = []
        currentTime = calendar.timegm(time.gmtime())
        timeInterval = 10
        while True:
            if len(self.maxHeap) is 0:
                break
            obj = heapq.heappop(self.maxHeap)
            if currentTime - obj[0] > timeInterval:
                print "Time Break"
                break
            if 'name' in obj[1]:
                if obj[1]['name'] == city:
                    response = obj[1]
            heapq.heappush(newHeap, obj)
        self.maxHeap = newHeap
        if response is None:
            self.faults = self.faults + 1
            print self.prepend, self.longno
            response = self.getWeatherByCity(city)
            heapq.heappush(self.maxHeap ,( calendar.timegm(time.gmtime()), response))
            print self.prepend, "Request [ key:", self.resource, "] was handled"
            return  response
        else:
            self.hits = self.hits + 1

            print self.prepend, self.longyes
            print "Fault Percentage:", float(self.faults)/float(self.faults + self.hits)
            print self.prepend, "Request [ key:", self.resource, "] was handled"
            return response





        #
        # if self.maxHeap.count(self) > self.max_table_size:
        #     a = [self.maxHeap.pop() for x in xrange(int(self.max_table_size))]
        #     b = []
        #     for x in a:
        #         print ">>>>>", x
        #
        # self.maxHeap.push(time.time(),(self.getWeatherByCity(city)))
        # if self.hashMap.has_key(city):
        #     self.hits = self.hits + 1
        #     return self.hashMap[city]
        # else:
        #    self.faults = self.faults + 1
        #    a = self.getWeatherByCity(city)
        #    print a
        print self.prepend, "Request [ key:", self.resource, "] was handled"
        #print self.resource, "::Current Value"

    def __init__(self, pollingIntervalInSeconds=5.0,  max_requests_an_hour = 2000.0, soft = True):
        # =============================Constants========================================
        self.prepend = "API>>>>>"
        self.longyes = "                                        | HIT  | ----- |"
        self.longno  = "                                        | ---- | FAULT |"
        self.app_id = "2de143494c0b295cca9337e1e96b00e"
        self.service_URL = "http://api.openweathermap.org/data/2.5/"
        requestsAMinute = 60/pollingIntervalInSeconds

        # =============================Variables========================================
        self.polling_interval_in_seconds = pollingIntervalInSeconds
        self.hits = 0;
        self.faults = 0;
        self.maxHeap = []
        self.resource = 0
        self.requestsMade = 0

        self.max_table_size = math.ceil(max_requests_an_hour/60/requestsAMinute)
        print "WeatherApi polling class is created with a tableSizeOf",self.max_table_size,"cached entries"
        print "Cached entries will be updated every", pollingIntervalInSeconds ,"seconds"

        # I insert a while loop here that polls at regular intervals.
        # while True:
        #     time.sleep(pollingIntervalInSeconds)
        print "!!!!!!!!!!!!!!!!!", pollingIntervalInSeconds
        thread.start_new_thread( self.__initiate_polling,(pollingIntervalInSeconds,0))
        print "!!!!!!!!!!!!!!!!!"


    def getWeatherByCity(self, cityName):
        print "=========================================================================================Fetching:" ,city
        r = requests.get(self.service_URL + "weather", params={"q":cityName,"appid":"44db6a862fba0b067b1930da0d769e98"})
        resp = r.json()
        self.requestsMade = self.requestsMade +  1
        # print resp['name']
        return resp
    def ambiguos_poll(self):
        # Ok so here is the weird part. I need to capture ambiguity of a users request when receiving a location.
        # Paris and Paris, Tx are not the same.
        # A weird user with even weirder queries might completely mess up caching our messages by not being precise
        #  enough in their wording
        #  My polling mechanism needs to know how to deal with this.

        # Here This Is something I know about the backend...
        # To some extent the backend is able to understand this ambiguity, deliberate on whether or not it is ambiguous,
        # then pass back an ultimatum in the form of some response text with GPS coordinates

        # So. To understand how the underlying weatherAPI Handles ambiguity. I will be using GPS coordinates
        # of the response to consolidate all weirdly formatted queries into one reference.

        # If "Jackson" and "Jackson,CA" returns the same GPS, They belong to the same set.
        # if "Paris" and "Paris,Tx" return different GPS then they belong to two different sets.
        # Chances are, if there is widespread use of this library, then assumming an uneven distribution of users
        # reference locality is going to win and keep "Paris" (France) cached.

        #  I maintain two hash-maps. One maps a set of strings to GPS coordinate.
        pass
    def regular_poll(self):


        pass

# ======================================================== CORE LOGIC STARTS HERE =============================================================
# Roll Unfair Dice
import cityDice
import random

poller = weatherPollingClass()
print "Poller Instantiated without any obvious thread-related issues"

# cityDice.unfairDice() is an unfair die. It builds a discrete pmf that reflects internet usage trends accros several major european cities.
# more information on this module can be found in cityDice.py
dice = cityDice.unfairDice()

# This block simulates requests to certain cities using weather api.
start_time = calendar.timegm(time.gmtime())
while True:
    interv = random.random() * 4
    time.sleep(interv * 0.1)
    current_time = calendar.timegm(time.gmtime())
    #  getRandomCity() polls our pmf and returns a random city. The frequency of each returned value is directly related to our
    #  PMF
    city = dice.getRandomCity()
    # print("Someone is requesting weather information for ", city)
    poller.make_a_request(city)
    if current_time - start_time > 20:
        break
print poller.faults + poller.hits, ":: Requests Made"
print poller.faults, ":: Faults  Made"
print poller.hits, ":: Hits Made Made"
print "Reduced cost to ::", float((float(poller.faults)/float((poller.faults + poller.hits)))*100.0) ,"% of original"


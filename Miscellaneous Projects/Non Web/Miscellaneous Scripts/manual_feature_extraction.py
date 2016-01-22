__author__ = 'otto'

"""
This code is in charge of extracting sales related features from sales CSV. The process will extract the following features:
Gaussian Parameters for cash, credit, exemptions, prepaid, and combined sales. Where a gaussian parameter is defined as
covariance

"""

from copy import copy
import numpy as np
import matplotlib.pyplot as plt
import datetime
from scipy import signal


def interpolate_data(data, min = None, max = None):
    if min == None:
        min = min(data[:,0])
    if max == None:
        max = max(data[:,0])

    #takes max value, takes min value
def loadfromFile(source):
    return open(source, "r")

def uglyTokenDigestor(token):
    token = token.replace("\"", "").split("-")
    minitoken = token[2].replace('\"', "").replace('T', ":").replace('Z', "").split(":")
    a = datetime.datetime(int(token[0]), int(token[1]), int(minitoken[0]), int(minitoken[1]), int(minitoken[2]),
                          int(float(minitoken[3])))
    return (a.strftime("%s"))

def trim_trailing_zeros(data):
    pass

def trim_leading_zeros(data):
    pass

# Oh my god. Im going nowhere with this project fast. Perhaps I should focus on the simpler features first. I would be willinng to bet that immediat
def dissectData(data):
    cash = []
    credit = []
    prepaid = []
    exemption = []
    for line in data:
        tokens = line.split(",")
        if tokens[8] == "\"cash\"":
            cash.append((int(uglyTokenDigestor(tokens[2])), int(tokens[4])))
        elif tokens[8] == "\"credit\"":
            credit.append((int(uglyTokenDigestor(tokens[2])), int(tokens[4])))
        elif tokens[8] == "\"exempt\"":
            exemption.append((int(uglyTokenDigestor(tokens[2])), int(tokens[4])))
        elif tokens[8] == "\"prepaid\"":
            prepaid.append((int(uglyTokenDigestor(tokens[2])), int(tokens[4])))
    data.close()
    return cash, credit, prepaid, exemption


def segmentLists(data, time=24 * 60 * 60):
    timeSegments = []
    previous = data[0]
    current_frame = 0
    for i, x in enumerate(data):
        if x[0] - previous[0] > time:
            timeSegments.append(data[current_frame:i])
            current_frame = i
        previous = x
    timeSegments.append(data[current_frame:])
    return timeSegments




def windowSum(data, window=5):
    arrayOfWindowValues = []
    tempValue = 0
    volume = 0
    tempTimeCuttoff = data[0][0] + window
    for x in data:
        if x[0] < tempTimeCuttoff:
            tempValue = tempValue + x[1]
            volume = volume + 1
        else:
            arrayOfWindowValues.append((tempTimeCuttoff, copy(tempValue), copy(volume)))
            tempValue = 0
            volume = 0
            tempTimeCuttoff = tempTimeCuttoff + window

    return arrayOfWindowValues
def movingStandarDeviation(data, window):
    mstd = []
    for index,value in enumerate(data):
        if index>window:
            stdArray = []
            for x in range(window):
                stdArray.append(data[index-x][1])
            stdArray = np.array(stdArray)
            if len(data[1,:]) == 2:
                mstd.append((value[0],copy(np.std(stdArray))))
            elif len(data[1,:]) == 3:
                mstd.append((value[0],copy(np.std(stdArray)),value[2]))
    return np.array(mstd)

def movingAverage(data, window):
    ma = []
    for index,value in enumerate(data):
        if index > window:
            sum = 0
            for x in range(window):
                sum = sum + data[index-x][1]

            if len(data[1,:]) == 2:
                ma.append((value[0],int(float(copy(sum))/window)))
            elif len(data[1,:]) == 3:
                ma.append((value[0],int(float(copy(sum))/window), value[2]))
    return np.array(ma)

def maximum_profit_window(list_of_data):
    current_max = list_of_data[0]
    for series in list_of_data:
        a = np.sum(series, axis=0)
        if a[1] > np.sum(current_max, axis=0)[1]:
            current_max = series
    return current_max

def extrapolate_peak(data, frame = 10):
    # find the peak of a moving average. return peak time, return peak value
    pass
def extrapolate_slope(data, peak):
    # using peak information. slop is extrapolated.
    pass

def price_to_volume(data):
    array = []
    for index, value in enumerate(data[:,0]):
        if(data[index][2] == 0):
            array.append((value, 0))
        else:
            array.append((value, int(float(data[index][1])/data[index][2])))
    return np.array(array)

def extraplate_peaks(data):
    peakind = signal.find_peaks_cwt(data, np.arange(1,10))
    return peakind
"""
==============================
MAIN CODING LOGIC STARTS HERE
==============================
"""

data = loadfromFile("event_csv/two_events.csv")
cash, credit, prepaid, exempt = dissectData(data)


segmented_cash      = segmentLists(cash)
segmented_credit    = segmentLists(credit)
segmented_prepaid   = segmentLists(prepaid)
segmented_exempt    = segmentLists(exempt)

final = np.array(segmented_cash)[0]
for x in np.array(segmented_cash[:1]):
    final = np.concatenate((final,x))
final = np.array(windowSum(final, window=60))

final = movingAverage(final, window = 5)
# plt.plot(final[:,0], final[:,1])

"""
Since information right now is not being introduced to this system at even rates(courtesy of wierd csv format being
read instead of database) The max cash function will attempt to find the most apppropriate time-frame by which the data
is introduced.  Max cash will be removed once data is loaded properly.
"""

max_cash    = maximum_profit_window(np.array(segmented_cash))
max_credit  = maximum_profit_window(np.array(segmented_credit))
max_prepaid = maximum_profit_window(np.array(segmented_prepaid))
max_exempt  = maximum_profit_window(np.array(segmented_exempt))


credit_per_minute   = np.array(windowSum(max_cash,      window=60))
cash_per_minute     = np.array(windowSum(max_credit,    window=60))
prepaid_per_minute  = np.array(windowSum(max_prepaid,   window=60))
exempt_per_minute   = np.array(windowSum(max_exempt,    window= 60))

cash_per_minute     = movingAverage(cash_per_minute,    10)
credit_per_minute   = movingAverage(credit_per_minute,  10)
prepaid_per_minute  = movingAverage(prepaid_per_minute, 10)

cash_volatility_per_minute      = movingStandarDeviation(cash_per_minute, 5)
credit_volatility_per_minute    = movingStandarDeviation(credit_per_minute, 5)
prepaid_volatility_per_minute   = movingStandarDeviation(exempt_per_minute, 5)
"""
Creating a very simple pyplot to display our data.
"""


cash_income_to_volume_ratio = price_to_volume(cash_per_minute)
cash_income_to_volume_ratio = movingAverage(cash_income_to_volume_ratio, 5)

credit_income_to_volume_ratio = price_to_volume(credit_per_minute)
credit_income_to_volume_ratio = movingAverage(credit_income_to_volume_ratio, 5)
#
prepaid_income_to_volume_ratio = price_to_volume(prepaid_per_minute)
prepaid_income_to_volume_ratio = movingAverage(prepaid_income_to_volume_ratio, 5)
#
def display_income_to_volume_ratio():
    plt.plot(   cash_income_to_volume_ratio[:,0], cash_income_to_volume_ratio[:,1])
    plt.plot(   credit_income_to_volume_ratio[:,0], credit_income_to_volume_ratio[:,1])
    plt.plot(   prepaid_income_to_volume_ratio[:,0], prepaid_income_to_volume_ratio[:,1])


def display_income_volatilities():
    plt.plot(   cash_volatility_per_minute[:,0],        cash_income_to_volume_ratio[:,1])
    plt.plot(   credit_volatility_per_minute[:,0],      credit_volatility_per_minute[:,1])
    plt.plot(   prepaid_income_to_volume_ratio[:,0],    prepaid_income_to_volume_ratio[:,1])

def displat_income_per_minute():
    plt.plot(   cash_per_minute     [:,0],      cash_per_minute [:,1])
    plt.plot(   cash_per_minute     [:,0],      cash_per_minute [:,2])
    plt.plot(   credit_per_minute   [:,0],    credit_per_minute [:,1])
    plt.plot(   prepaid_per_minute  [:,0],   prepaid_per_minute [:,1])


# display_income_to_volume_ratio()
# display_income_volatilities()
sigma_max_cash = np.std(np.array(max_cash)[:,0])
mu_max_cash = np.mean(np.array(max_cash)[:,0])

sigma_cash   =   np.std(cash_per_minute[:,1])
mu_cash      =   np.mean(cash_per_minute[:,1])

print "====="
print sigma_max_cash
print mu_max_cash
print "====="





def dumbSearch(peaks, data, index = 1, mx = True):
    array_to_be_returned = []
    candidate_peaks = []
    if mx == True:
        max = candidate_peaks
        for x in peaks:
            candidate_peaks.append(max(peaks))
    else:
        candidate_peaks = peaks
    for i, x in enumerate(data[:,index]):
        if x  in peaks:
            array_to_be_returned.append(data[:,0][i])
    return  array_to_be_returned

cash_per_minute_peaks       = extraplate_peaks(cash_per_minute      [:,1])
credit_per_minute_peaks     = extraplate_peaks(credit_per_minute    [:,1])
prepaid_per_minute_peaks    = extraplate_peaks(prepaid_per_minute   [:,1])
exempt_per_minute_peaks     = extraplate_peaks(exempt_per_minute    [:,1])


print

# plt.plot(a)


# plt.plot(exempt_per_minute[:,0], exempt_per_minute[:,1])
# ax.plot(cash_per_minute[[1,0]])

#
# fig, ax = plt.subplots()
# ax.plot(cash_per_minute[[1,0]])
# plt.show()
#


# numpyA = np.array(segmented_cash[0])
# numpyB = np.array(segmented_credit[1])
#
#
# aFirst = windowSum(numpyA, window= 120)
#
# print np.fliplr(aFirst)
# fig, ax = plt.subplots()
# ax.plot(aFirst)
plt.show()



# print len(x) , x
# def process(n):
#     import time, socket
#     time.sleep(n)
#     host = socket.gethostname()
#     return (host, n)
#
# if __name__ == '__main__':
#     import dispy, random
#     cluster =  dispy.JobCluster(process)
#     jobs = []
#     for i in range(10):
#         job = cluster.submit(random.randint(5,20))
#         job.id = jobs.append(job)
#     for job in jobs:
#         host, n= job()
#         print('%s executed job %s at %s with %s' % (host, job.id, job.start_time, n))
#
#     cluster.stats()
#


#
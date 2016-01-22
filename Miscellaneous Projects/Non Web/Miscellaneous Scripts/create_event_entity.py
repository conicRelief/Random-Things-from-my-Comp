
# This file talks to our database and extrapolates necessary information about events.
# hopefully, this way we will be able to access features with better structures.

import numpy as np
import psycopg2 as psql
import statistics as stat
import json
import sys
import numpy
import time
import homemade_haversine
import matplotlib.pyplot as plt






#### Tier 1: Global Features.
global_event_parkings = [] # an empty list of event parkings in general.



#### Tier 2: Event specific Features.



### Tier 3: External or Worldy features. This may be weather, CPI, Time of day. Wether there is work the next day.



### Other modifiers.


DEBUG_FEATURE_EXTRACTION = False
DEBUG_EVENT_NO = 1



def findEventParking(the_event,             conn = None,cur = None):
    command = "SELECT * FROM event_parkings WHERE " + "event_id = \'" + the_event + "\';"
    cur.execute(command)
    return cur.fetchall()

def getEventLocation(landmark_ID, cur):
    command = "SELECT * FROM landmarks WHERE id = \'" + landmark_ID + "\';"
    cur.execute(command)
    response = cur.fetchall()
    location = response[0][9]
    return location['lat'], location['lon']

def getLot(lot_id, cur):
    command = "SELECT * FROM lots WHERE id = \'" +lot_id +"\';"
    cur.execute(command)
    response = cur.fetchall()
    return response
def filter_prime_order(order,curr):
    created_at  = order[13]
    money_made_on_order = order[5]
    command = "SELECT * FROM prime_orders WHERE order_id =\'" + order[0] + "\';"
    curr.execute(command)
    ref = cur.fetchall()
    # print ref[0][3]
    fet = []
    if len(ref) == 0:
        fet = ""
    else:
        fet = ref[0][3]
    return {'created_at':created_at,"money_made": money_made_on_order , 'payment_type':fet}

def getInfoAboutEvent(the_event,cur):

    event_name = the_event[1]
    event_id = the_event[0]
    landmark_id = the_event[2]
    time_start, time_end =  the_event[3],the_event[4]
    print "~~~Event~~~ ::", event_name , "::::: ", event_id
    event_lat, event_lon = getEventLocation(landmark_id, cur)
    event_parkings =  findEventParking(event_id ,cur = cur)
    event_parking_tuples = []
    for i, x in enumerate(event_parkings):
        the_lot = getLot(x[1], cur)
        current_location = the_lot[0][4]
        print "|PROCESSING EVENT PARKING [", i ,"] |   ",
        distance_to_parking_location = homemade_haversine.haversine(event_lat, event_lon, current_location['lat'], current_location['lon'])
        orders = get_relevant_orders(the_lot[0][0],event_id,cur)
        complete_order_information = []
        for o in orders:
            filtered = filter_prime_order(o, cur)
            filtered['time_from_start'] = int((time_start - filtered['created_at']).seconds)
            complete_order_information.append(filtered)
        event_parking_tuples.append({'event_parking':x,'distance_to_event':distance_to_parking_location,'order_information':complete_order_information})
        print "Done"
    entity_object = { 'event_id':event_id,'time_start':time_start,'time_end':time_end,'event_name': event_name,'event_parking_tuples': event_parking_tuples}


    return  entity_object
def get_relevant_orders(lot_id, event_id, curr):
    command = "SELECT * FROM orders WHERE lot_ids[1]=\'" + lot_id + "\' AND event_ids[1]=\'" + event_id + "\';"
    curr.execute(command)
    lot_info = curr.fetchall()
    return lot_info

def runningMeanFast(x, N):
    return np.convolve(x, np.ones((N,))/N, mode='valid')


def windowSum(data, window =5):
    time_sorted_data = sorted(data, key=lambda tup: tup[0])
    return_value = []
    temp_sum_of_quantities = 0
    temp_volume_of_tuples = 0
    try:
        temp_cutoff_time = time_sorted_data[0][0]
        for time, quantity in time_sorted_data:
            if time < temp_cutoff_time:
                temp_sum_of_quantities = temp_sum_of_quantities + quantity
                temp_volume_of_tuples = temp_volume_of_tuples + 1
            else:
                return_value.append((time,temp_sum_of_quantities,temp_volume_of_tuples))
                temp_sum_of_quantities = quantity
                temp_volume_of_tuples = 1
                temp_cutoff_time = temp_cutoff_time + window
    except:
        print "tsd", time_sorted_data
    return return_value


def process_event(x):
    entity_object = getInfoAboutEvent(x,cur)
    # (event_id, event_name,distance_to_parking_location, event_parking_tuples)
    #(Event Information)
    event_name = entity_object['event_name']
    event_parkings = entity_object['event_parking_tuples']
    print "\n | MANUALLY EXTRACTING FEATURES  FOR :::" , event_name, ":::|"

    #Build this list to capture event
    event_parking_feature_vectors = []

    for i , x in enumerate(event_parkings):
        print "|||EVENT PARKING   ", i
        print "     |Distance to event", x['distance_to_event']
        consider = {'cash':None,'credit':None,'prepaid':None,'prepaid':None }

        cash      = filter(lambda x: x['payment_type'] == 'cash',       x['order_information'])
        credit    = filter(lambda x: x['payment_type'] == 'credit',     x['order_information'])
        prepaid   = filter(lambda x: x['payment_type'] == 'prepaid',    x['order_information'])
        exemption = filter(lambda x: x['payment_type'] == 'exemption',  x['order_information'])
        total     = x['order_information']



        cash_money           = map(lambda x: (time.mktime(x['created_at'].timetuple()),x['money_made']), cash)
        credit_money         = map(lambda x: (time.mktime(x['created_at'].timetuple()),x['money_made']), credit)
        prepaid_money        = map(lambda x: (time.mktime(x['created_at'].timetuple()),x['money_made']), prepaid)
        exemption_money      = map(lambda x: (time.mktime(x['created_at'].timetuple()),x['money_made']), exemption)
        total_money      = map(lambda x: (time.mktime(x['created_at'].timetuple()),x['money_made']), total)

        if len(cash) != 0:
            cash_money_and_volume_per_minute = windowSum(cash_money, window= 60)
            mean_volume_of_cash         = sum(map(lambda x : x['money_made'], cash))/len(cash)
            mean_arribal_time_of_cash   = sum(map(lambda x: x['time_from_start'], cash))/len(cash)
            filterered_volume_of_cash = filter(lambda y: y != 0 ,map(lambda x: x[2], cash_money_and_volume_per_minute))
            mean_volume_of_cash_orders  = float(sum(filterered_volume_of_cash))/float((len(filterered_volume_of_cash)+1))
            print "     ==Cash Flow Profile+"
            print "     |Mean Ammount of money speant", mean_volume_of_cash
            print "     |Mean Arrival Time", mean_arribal_time_of_cash/60
            print "     |Mean Volume of Orders", mean_volume_of_cash_orders


        if len(credit) != 0:
            credit_money_and_volume_per_minute = windowSum(cash_money, window= 60)
            mean_volume_of_credit         = sum(map(lambda x : x['money_made'], credit))/len(credit)
            mean_arribal_time_of_credit   = sum(map(lambda x: x['time_from_start'], credit))/len(credit)
            filterered_volume_of_credit = filter(lambda y: y != 0 ,map(lambda x: x[2], credit_money_and_volume_per_minute))
            mean_volume_of_credit_orders  = float(sum(filterered_volume_of_credit)/(len(filterered_volume_of_credit)+1))
            print "     ==Credit Flow Profile+"
            print "     |Mean Volume", mean_volume_of_credit
            print "     |Mean Arrival Time", mean_arribal_time_of_credit/60
            print "     |Mean Volume of Orders", mean_volume_of_credit_orders

        if len(prepaid) != 0:
            prepaid_money_and_volume_per_minute = windowSum(prepaid_money, window= 60)
            mean_volume_of_prepaid         = sum(map(lambda x : x['money_made'], prepaid))/len(prepaid)
            mean_arribal_time_of_prepaid   = sum(map(lambda x: x['time_from_start'], prepaid))/len(prepaid)
            filterered_volume_of_prepaid = filter(lambda y: y != 0 ,map(lambda x: x[2], prepaid_money_and_volume_per_minute))
            mean_volume_of_prepaid_orders  = float(sum(filterered_volume_of_prepaid)/(len(filterered_volume_of_prepaid)+1))
            print "     ==Prepaid Flow Profile+"
            print "     |Mean Volume", mean_volume_of_prepaid
            print "     |Mean Arrival Time", mean_arribal_time_of_prepaid/60
            print "     |Mean Volume of Orders", mean_volume_of_prepaid_orders


        # credit_money_and_volume_per_minute = windowSum(credit_money, window= 60)
        # prepaid_money_and_volume_per_minute = windowSum(prepaid_money, window= 60)
        # exemtion_money_and_volume_per_minute = windowSum(exemption_money, window= 60)
        # total_money_and_volume_per_minute = windowSum(total_money, window= 60)


        # if len(cash_money_and_volume_per_minute) == 0:
        #     pass
        # else:
        #     global_event_parkings.append((x['distance_to_event'], sum(map(lambda x: x[1], cash_money_and_volume_per_minute))/len(cash_money_and_volume_per_minute)))



"""
Main programming logic starts here here.
Basically this portion of the progam processes input in a format that is usefull to our
feature engineering portion of our software.
"""

print "Connecting to database..."
conn = psql.connect("dbname='parkhub' user='otto' host='localhost'")
print "Connected to database!!!"
cur = conn.cursor()
cur.execute("SELECT * FROM events")
rows = cur.fetchall()


if DEBUG_FEATURE_EXTRACTION is True:
    process_event(rows[DEBUG_EVENT_NO])
else:
    for x in rows[1:]:
        process_event(x)
# except:
#     print "create_event_entity.py was not able to connect to the database"

#
#
# distance_sorted_data =np.array(sorted(global_event_parkings, key=lambda tup: tup[0]))
# for i,val in enumerate(distance_sorted_data):
#     if val[0] > 3:
#         distance_sorted_data[i][0] = 0
# plt.scatter(   distance_sorted_data[:,0], distance_sorted_data[:,1], marker = 'o')
# plt.show()

from icalendar import Calendar, Event
from datetime import datetime
from pytz import UTC # timezone
import csv

contact_file = "contacts.csv"
ics_export_file = "birthday.ics"
alert_begin = 8
alert_end = 10

cal = Calendar()
cal.add("prodid", "Birthday-Calendar")
cal.add("version", "1.0")

def openContacts():
    with open(contact_file, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if(row["Birthday"] != ""):
                print(row["Name"],row["Birthday"])
                year = row["Birthday"][0:4]
                month =row["Birthday"][5:7]
                day = row["Birthday"][8:9]
                # sometimes google saves the birthday of your 
                # contacts like this
                #  --.01-01
                # this is why we change the undifined value to 2000
                format_time = row["Birthday"].replace("--", "-").replace(" ","2000")
                format_time = format_time.split("-")
                format_time_list = []
                for i in format_time:
                    format_time_list.append(i)
                # Callback
                writeICS(format_time_list,row)
            
def writeICS(format_time_list,row):
    f_year = int(format_time_list[0])
    f_month = int(format_time_list[1])
    f_day = int(format_time_list[2])

    # Event Docs:
    # https://www.kanzaki.com/docs/ical/
    event = Event()
    event.add("rrule", {"freq": "yearly"} )
    event.add("summary", row["Name"])
    event.add("dtstart", datetime(f_year,f_month,f_day,alert_begin,0,0,tzinfo=UTC))
    event.add("dtend", datetime(f_year,f_month,f_day,alert_end,0,0,tzinfo=UTC))
    event.add("dtstamp", datetime.now())
    # unique ID
    event["uid"] = str(datetime(f_year,f_month,f_day,alert_begin,0,0,tzinfo=UTC))+row["Name"]
    event.add("priority", 5)
    cal.add_component(event)

    f = open(ics_export_file, "wb")
    f.write(cal.to_ical())
    f.close()
openContacts()

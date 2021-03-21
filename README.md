# Birthday Calendar From Contacts
<img src="https://github.com/Domepo/BirthdayCalendarFromContacts/blob/main/example/happy_birthday.gif" alt="https://pixabay.com/de/photos/portrait-kind-h%C3%A4nde-verstecken-317041/" width="192" height="144"><br>
This is a simple tool to convert your contacts.csv to an ical file <br>
##### Why?
Google dont give you an Birthday alert when you synchronize Google-Calender and Google-Contacts. <br>
In most cases your forced to download apps which notify you<br>

## Installation
```pip
pip3 install icalendar
```
## Quickstart
- [Export the contacts.csv ](https://support.google.com/contacts/answer/7199294?co=GENIE.Platform=Desktop&hl=en#:~:text=Export%20contacts&text=Go%20to%20Google%20Contacts.&text=click%20More%20actions-,Export.,save%20your%20file,%20click%20Export.) file from your phone
- put the file into your working folder
- run main.py
- import the birthday.ics file to your prefered calendar

#### Example contacts.csv file:
| Name            | Additional Name | Birthday   | Initials |
|-----------------|-----------------|------------|----------|
| Albert Einstein | Smartboy        | 1879-03-14 | AE       |
| Elon Musk       | Tesla CEO       | 1971-06-28 | EM       |
| Nat Friedman    | Github          | 1977-08-06 | NF       |

#### Example birthday.ics file:
```ics
BEGIN:VCALENDAR
VERSION:1.0
PRODID:Birthday-Calendar
BEGIN:VEVENT
SUMMARY:Albert Einstein
DTSTART;VALUE=DATE-TIME:18790314T080000Z
DTEND;VALUE=DATE-TIME:18790314T100000Z
DTSTAMP;VALUE=DATE-TIME:20210321T212250Z
UID:1879-03-14 08:00:00+00:00Albert Einstein
RRULE:FREQ=YEARLY
PRIORITY:5
END:VEVENT
BEGIN:VEVENT
SUMMARY:Elon Musk
DTSTART;VALUE=DATE-TIME:19710628T080000Z
DTEND;VALUE=DATE-TIME:19710628T100000Z
DTSTAMP;VALUE=DATE-TIME:20210321T212250Z
UID:1971-06-28 08:00:00+00:00Elon Musk
RRULE:FREQ=YEARLY
PRIORITY:5
END:VEVENT
BEGIN:VEVENT
SUMMARY:Nat Friedman
DTSTART;VALUE=DATE-TIME:19770806T080000Z
DTEND;VALUE=DATE-TIME:19770806T100000Z
DTSTAMP;VALUE=DATE-TIME:20210321T212250Z
UID:1977-08-06 08:00:00+00:00Nat Friedman
RRULE:FREQ=YEARLY
PRIORITY:5
END:VEVENT
END:VCALENDAR
```
#### Inside Google Calendar:
<img src="https://github.com/Domepo/BirthdayCalendarFromContacts/blob/main/example/Screenshot.png" alt="https://pixabay.com/de/photos/portrait-kind-h%C3%A4nde-verstecken-317041/" width="435" height="313"><br>


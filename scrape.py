import scrapetube
import dateparser 
import datetime as dt

convertDays = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}


calendarDays = {
    "Monday" : [],
    "Tuesday": [],
    "Wednesday": [],
    "Thursday": [],
    "Friday": [],
    "Saturday": [],
    "Sunday": []
}

haveMore = input("\nHave more channels? Type anything to continue.\n")
channelUsername = input("\nYour channel name:\n")
series = input("\nThe channel series name:\n")

while len(haveMore) != 0:
    channels = scrapetube.get_channel(channel_username=channelUsername, limit=10, sort_by="newest", content_type="videos")
    for channel in channels:
        currentTitle = channel['title']['runs'][0]['text']
        if series.lower() in currentTitle.lower():
            # print(channel["title"]['accessibility'])
            currentDateAgo = channel['publishedTimeText']['simpleText']
            currentDate = dateparser.parse(currentDateAgo).strftime("%Y-%m-%d")
            currYear, currMonth, currDay = currentDate.split("-") 
            currDayOfTheWeekInt = dt.datetime(year=int(currYear),month=int(currMonth),day=int(currDay)).weekday()
            currDayOfTheWeek = convertDays[currDayOfTheWeekInt]
            print(currentTitle + " - "+ currentDateAgo + " - " + currentDate + " - " + currDayOfTheWeek)

            if channelUsername not in calendarDays[currDayOfTheWeek]:
                calendarDays[currDayOfTheWeek].append(channelUsername)
        
    haveMore = input("\nHave more channels? Type anything to continue.\n")
    channelUsername = input("\nYour channel name:\n")
    series = input("\nThe channel series name:\n")

print(calendarDays)



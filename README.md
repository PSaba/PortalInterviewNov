# PortalInterviewNov

I chose dictionary with key as date, since events can only clash if they occur on the same day
 value is array with name, start time, and end time as they need to be kept in certain order
that way same day items are together
I went through each date, going through all the events in the date and comparing the times
if any of the start and end times clashed, that is, one events doesn't end before the start of the other event or starts in the middle of the event, then add to list
if both events checked is the same event, not added
if more time, would have sorted according to starting time and checked if ending time is before other event's starting time

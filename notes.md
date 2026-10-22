pull main data > pull class data > append to csv > send discord
eventually move to session instead, simplifies auth for the whole program

For classes:
some info:
for real class ppl count use limit - available, indicator is simply a 0-5 scale rating of availablity.
for time make it iso8601 like xHxxM; WARNING! treat '-' signs inside the notation as -xM for example. As in PT1H-5M is 1H -5M = 55M
Supposedly LocalTime 

pull data, add a column with how many people the latest pull recorded -> either put it up to the software that'll be managing the data to subtract the 2 or do it manually.

apparently it does store the old records after all, but like max day old i think. so basically go by StartTime and then subtract each record by what classes it wouldve been affected by (only the ones with status unavailable and statusreason class already ended, for differerent maybe throw a new 'error' in some log to let me know). 

<!-- Going by hour does have its problems though, I'll have to account for the situation where I pull the data and one class will be avialbe and some other will not -->
I think nevermind cause then on the next iteration it'll just subtract the values again.


gym_id, poll_date, raw_ppl_count, fixed ppl_count, classes_ppl(limit-available), which_classes
might do it in sql now, not sure



---

in get_gym_data or the gym normalize function 


---
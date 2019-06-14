```# 1) old events which might not have the new question types 
# 2) Negative scores tests 
# 3) Zero state (no submissions for programming questions)
# 4) Tests with no candidates taken test

# 1) Old events which might not have new question types 

import datetime
t = datetime.datetime(2017,4,1)
events = Event.objects.filter(timestamp__lte=t, published=True)
events.count()
published_event_ids = list(events.values_list('id', flat=True))

dpr_event_ids = DiagramProblemsReport.objects.filter(event_id__in=published_event_ids).values_list('event_id', flat=True)
unique_dpr_event_ids = list(set(dpr_event_ids))
event_without_dpr = set(published_event_ids) - set(unique_dpr_event_ids)

# 2) Submission with negative scores
events = Event.objects.filter(submission__score__lt=0, published=True)[:1000]
event_ids = Event.objects.filter(submission__score__lt=0, published=True).values_list('id', flat=True)[:1000]
unique_event_ids = list(set(event_ids))

# 3) Zero state, no submission for prog questions
qs = ProgProblemReport.objects.filter(attempted=False).order_by('-timestamp')[:100]
participation_ids = qs.values_list('participation_id', flat=True)
for p_id in participation_ids:
    p = Participation.objects.get(id=p_id)
    user_email = User.objects.get(id=p.user_id).email
    event_slug = Event.objects.get(id=p.event_id).slug
    print (event_slug, user_email)

#4) Tests where no candidate has taken test

qs = Event.objects.filter(published=True).annotate(c=Count('participation')).filter(c=0)
events = qs[:100]


# Writing the output data to csv

filename = '/tmp/events_with_zero_participation.csv'
import csv
with open(filename, 'w') as _f:
    writer = csv.writer(_f)
    for event in events:
        data = [event.slug]
        writer.writerow(data)```
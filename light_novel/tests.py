# from django.test import TestCase
import pandas as pd
from light_novel.models import Character, Move, Chapter, Timeline

# p = pd.read_csv('F:\\lightnovel\\Characters.csv')
# for i in range(len(p['Name'])):
#     c = Character()
#     c.name = p['Name'][i]
#     c.main_side = 'side'
#     c.element = p['Element'][i]
#     c.gender = p['Sex'][i]
#     c.appearance = p['Role'][i]
#     c.save()
with open('F:\\lightnovel\\timeline.txt', 'r') as f:
    for line in f:
        print(line)
#             t = Timeline()
#             d = line[:11] + '00:00'
#             e = line[13:]
#             t.event = e
#             t.date_time = d
#             t.save()

# Create your tests here.
# m = pd.read_csv('F:\lightnovel\moves.csv')
#
#
# for i in range(len(m['Name'])):
#     c = Move()
#     c.name = m['Name'][i]
#     c.description = m['Description'][i]
#     c.owner = Character.objects.filter(name=m['Owner'][i])[0]
#     print(c.name, c.owner)
#     c.save()

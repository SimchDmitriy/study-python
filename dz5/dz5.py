import json
import csv

purchase_log_path = '/Users/dmitrijsmirnov/Desktop/Учеба/2 курс/Python и аналитика/study-python/dz5/purchase_log.txt'
visit_log_path = '/Users/dmitrijsmirnov/Desktop/Учеба/2 курс/Python и аналитика/study-python/dz5/visit_log__1_.csv'
funnel_output_path = '/Users/dmitrijsmirnov/Desktop/Учеба/2 курс/Python и аналитика/study-python/dz5/funnel.csv'

purchases = {}

with open(purchase_log_path, mode='r', encoding='utf-8') as purchase_file:
    for line in purchase_file:
        row = json.loads(line.strip())
        user_id = row['user_id']
        category = row['category']
        purchases[user_id] = category

with open(visit_log_path, mode='r', encoding='utf-8') as visit_file, \
     open(funnel_output_path, mode='w', encoding='utf-8', newline='') as funnel_file:
    
    reader = csv.DictReader(visit_file)
    writer = csv.writer(funnel_file)
    
    writer.writerow(['user_id', 'source', 'category'])
    
    for row in reader:
        user_id = row['user_id']
        source = row['source']
        
        if user_id in purchases:
            writer.writerow([user_id, source, purchases[user_id]])
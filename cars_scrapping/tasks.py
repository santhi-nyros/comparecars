from celery.task.schedules import crontab
from celery.decorators import periodic_task
#from cars_scrapping import scrapers
from celery.utils.log import get_task_logger
from datetime import datetime
from cars_scrapping.views import *
from celery.decorators import task

logger = get_task_logger(__name__)



from datetime import timedelta

@task(name='task.cars_scrapping')
def carwale():
	print "hai"
	restore=scrapping_csv()
	print "restoring database data"
	keyword=keywords()
	print "keywords update"






# @task(name='task.cars_scrapping')
# def carwale():

# 	carwale_updating=carwale_update()
# 	print "updating records of carwale website completed"

# 	carwale_deleting=carwale_delete()
# 	print "deleted records in database which are not available in carwale website"

# 	carwale_is_there=carwale_active()
# 	print "carwale is_there field set to 0 after completion of deleting records"

# 	cartrade_updating=cartrade_update()
# 	print "updating records of cartrade website completed"

# 	cartrade_deleting=cartrade_delete()
# 	print "deleted records in database which are not available in cartrade website"

# 	cartrade_is_there=cartrade_active()
# 	print "cartrade is_there field set to 0 after completion of deleting records"

	

	





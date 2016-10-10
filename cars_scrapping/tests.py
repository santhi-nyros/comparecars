
from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from compare_cars.models import *
from selenium import webdriver
import time
from django.http import HttpResponse
import unittest


# Create your tests here.
class SimpleTest(TestCase):
	def test_basic_addition(self):
		"""
		Tests that 1 + 1 always equals 2.
		"""
		print"test"
		self.failUnlessEqual(1 + 1, 2)

class CartradeTest(TestCase):
	def test_cartrade(self):
		master_data_store = Car_Master_Data.objects.create(
			website_name= "cartrade",
			city_id="Hyderabad", 
			city_name="Hyderabad",
			make_id ="hvmodelsMaruti-Suzuki",
			make_name = "Maruti Suzuki",
			model_id = "mod_800",
			model_name = "800").save()

		master_data_retrive = Car_Master_Data.objects.all()
		for master in master_data_retrive:
			driver = webdriver.Firefox()
			# print master.city_name
			print master.city_id
			print master.make_id
			print master.model_id
			driver.get('http://www.cartrade.com/buy-used-cars')
			try:
				close_popup = driver.find_element_by_css_selector('div#selectcityfilm a.closebtn')
				time.sleep(1)
				close_popup.click()
			except:
				pass

			try:  
				select_city = driver.find_element_by_css_selector('div.leftbar select#sortcity  option[value^="%s"]'%master.city_id)
				select_city.click()
				time.sleep(1)
				print master.city_name
			except:
				pass

			try:
				select_make = driver.find_element_by_css_selector('li#%s div.spclass span.rcircle'%master.make_id)
				select_make.click()
				time.sleep(1)
				print master.make_name
			except:
				pass

			try:
				model_select =driver.find_element_by_css_selector('ul#mklist.features li#hvmodelsMaruti-Suzuki.hvchild.open ul#chmodelsMaruti-Suzuki li label input#%s'%master.model_id)
				model_select.click()
				time.sleep(1)
				print master.model_name
			except:
				pass

			car_data_list_total_div = [element for element in driver.find_elements_by_css_selector('div#searchFilters div.btmMrg.carlistblk div.widgetBox1 ')]
			for data in car_data_list_total_div:
				try:
					title = data.find_element_by_css_selector('div.titleblk div.pull-left.carlistcont div.h2heading').text
					print title
				except:
					title = "Default Title"
					print title

				try:
					href = data.find_element_by_css_selector('div.titleblk div.pull-left.carlistcont div.h2heading a').get_attribute("href")
					print href
				except:
					href = "http://www.chevrolet.co.in/trailblazer-powerful-suv.html?cmp=4456906_9138324_1673028_124445889_296988365_0"

				try:
					price=data.find_element_by_css_selector('div.titleblk div.pull-left.carlistcont div.price div.pull-left strong.pull-left').text
					price_car=price.replace(",","")
					print price_car

				except:
					price_car = "3,50,000"
					
				# scrollDown(driver, 1)
				time.sleep(3)
				try:
					image = data.find_element_by_css_selector('div.carimgblk a img').get_attribute("src")
					print image
				except:
					image = "http://imagecdn5.cartrade.com/img/300x225/lis/Maruti-Suzuki_A-Star_491097_20983_1_1435575807451.jpg"
					print image    
				try:     
					year = title.split("(")[1].split(")")[0]
					print year
				except:
					print "ddd"
				time.sleep(1)
			CarDetails(website_name="www.carwale.com",
							city=master.city_name,
							car_make=master.make_name,
							car_model=master.model_name,
							price=price_car,
							model_year=year,
							car_title=title,
							car_href=href,
							car_image =image
							).save()
			print"try"
				
				# return HttpResponse("carwale data stored into the database successfully")
			details = CarDetails.objects.all()
			self.assertEqual(details.count(), 1)


		# details = CarDetails.objects.all()
		# self.assertEqual(details.count(), 1)



'''
Run test case by using follwoing commands

python manage.py test

python manage.py test scrapcars.tests.CartradeTest.test_cartrade
                   

'''

class CarwaleTest(TestCase):
	def test_carwale(self):
		master_data_store =Car_Master_Data(website_name="www.carwale.com",
						city_id=2,
						city_name="Bangalore",
						make_id=8,
						make_name="Hyundai",
						model_id=8.307,
						model_name="verna").save()
		master_data_retrive = Car_Master_Data.objects.all()

		for master in master_data_retrive:
			driver = webdriver.Firefox()
			driver.get("http://www.carwale.com/used/cars-for-sale/")
			# print master.city_name
			print master.city_id
			print master.make_id
			print master.model_id
			try:
				city = driver.find_element_by_css_selector("select#drpCity.form-control option[value='%s']"%master.city_id)
				city.click()
				print master.city_name
				time.sleep(2)
			except:
				pass

			try:
				make = driver.find_element_by_css_selector("ul#makesList.ul-makes li.us-sprite.makeLi[carfilterid='%s']"%master.make_id) 
				make.click()
				print master.make_name
				time.sleep(10)
			except:
				pass

			try:
				model = driver.find_element_by_css_selector('ul#makesList.ul-makes li.us-sprite.makeLi div.list-points-models ul.rootUl li.us-sprite.rootLi[carfilterid="%s"]'%master.model_id)
				model.click()
				print master.model_name
				time.sleep(2)
			except:
				pass

			# driver = scrollDown(driver, 2)

			car_data_list = [element for element in driver.find_elements_by_css_selector('div.stock-list ul#listing1.ko-listing li.listing-adv.listingContent.padding-top10.padding-bottom10.cur-pointer div.stock-detail')]        
			print "*********"*12
			# print city_name
			time.sleep(2)
			for data in car_data_list:
				amount = data.find_element_by_css_selector('div.leftfloat.table-div.margin-left20 span.rupee-lac.slprice.font20').text
				print amount
				if(amount.endswith("lakhs")):
					split_lakhs=amount.split("lakhs")
					float_value=float(split_lakhs[0])
					print float_value
					muilt_value=100000
					total=float_value*muilt_value
					print total
					price=int(total)
					print price
				else:
					price=amount.replace(",","")
					print price
				title= data.find_element_by_css_selector('div.leftfloat.table-div.margin-left20 h2.listingTitle.font18 a').text
				print title

				href = data.find_element_by_css_selector('div.leftfloat.table-div.margin-left20 h2.listingTitle.font18 a').get_attribute("href")
				print href
				time.sleep(5)

				# driver = scrollDown(driver, 2)
				print"scroll"

				image = data.find_element_by_css_selector('div.leftfloat.thumb-div div.thumb-area div.img-placer a.slideShow img').get_attribute("src")
				print image

				year = data.find_element_by_css_selector('div.leftfloat.table-div.margin-left20 a.text-grey p.listingItemKms.font14.text-light-grey.margin-top5 span:nth-of-type(7)').text
				print year

				time.sleep(2)
				print"*******"
				
			CarDetails(website_name="www.carwale.com",
							city=master.city_name,
							car_make=master.make_name,
							car_model=master.model_name,
							price=price,
							model_year=year,
							car_title=title,
							car_href=href,
							car_image =image
							).save()
			print"try"
				
				# return HttpResponse("carwale data stored into the database successfully")
			details = CarDetails.objects.all()
			self.assertEqual(details.count(), 1)




class CarwaleTest_update(TestCase):
	def test_carwale_update(self):
		master_data_store =Car_Master_Data(website_name="www.carwale.com",
						city_id=2,
						city_name="Bangalore",
						make_id=8,
						make_name="Hyundai",
						model_id=8.307,
						model_name="verna").save()
		master_data_retrive = Car_Master_Data.objects.all()

		for master in master_data_retrive:
			driver = webdriver.Firefox()
			driver.get("http://www.carwale.com/used/cars-for-sale/")
			print master.city_id
			print master.make_id
			print master.model_id
		
			try:
				city = driver.find_element_by_css_selector('select#drpCity.form-control option[value="%s"]'%master.city_id)
				city.click()
				print master.city_name
				time.sleep(2)
			except:
				pass

			try:
				make = driver.find_element_by_css_selector("ul#makesList.ul-makes li.us-sprite.makeLi[carfilterid='%s']"%master.make_id) 
				make.click()
				print master.make_name
				time.sleep(10)
			except:
				pass

			try:
				model = driver.find_element_by_css_selector('ul#makesList.ul-makes li.us-sprite.makeLi div.list-points-models ul.rootUl li.us-sprite.rootLi[carfilterid="%s"]'%master.model_id)
				model.click()
				print master.model_name
				time.sleep(2)
			except:
				pass

			# driver = scrollDown(driver, 2)
			car_data_list = [element for element in driver.find_elements_by_css_selector('div.stock-list ul#listing1.ko-listing li.listing-adv.listingContent.padding-top10.padding-bottom10.cur-pointer div.stock-detail')]        
			print "*********"*12
			print master.city_name
			time.sleep(2)
			for data in car_data_list:
				amount = data.find_element_by_css_selector('div.leftfloat.table-div.margin-left20 span.rupee-lac.slprice.font20').text
				print amount
				if(amount.endswith("lakhs")):
					split_lakhs=amount.split("lakhs")
					float_value=float(split_lakhs[0])
					print float_value
					muilt_value=100000
					total=float_value*muilt_value
					print total
					price=int(total)
					print price
				else:
					price=amount.replace(",","")
					print price
				title= data.find_element_by_css_selector('div.leftfloat.table-div.margin-left20 h2.listingTitle.font18 a').text
				print title

				href = data.find_element_by_css_selector('div.leftfloat.table-div.margin-left20 h2.listingTitle.font18 a').get_attribute("href")
				print href
				time.sleep(5)

				# driver = scrollDown(driver, 2)
				print"scroll"

				image = data.find_element_by_css_selector('div.leftfloat.thumb-div div.thumb-area div.img-placer a.slideShow img').get_attribute("src")
				print image

				year = data.find_element_by_css_selector('div.leftfloat.table-div.margin-left20 a.text-grey p.listingItemKms.font14.text-light-grey.margin-top5 span:nth-of-type(7)').text
				print year

				time.sleep(2)
				print"*******"
				cars_detail = CarDetails.objects.all()
				for detail in cars_detail:
					href_detail=detail.car_href
					save_detail=CarDetails(website_name="www.carwale.com",
									city=master.city_name,
									car_make=master.make_name,
									car_model=master.model_name,
									price=price,
									model_year=year,
									car_title=title,
									car_href=href,
									car_image =image,
									is_there=1,
									)
					if(href!=href_detail):
						print "not equal"
						try:
							save_detail.save()
							print"saved"
						except:
							pass
					else:
						print "already existed"
						CarDetails.objects.filter(car_href=href).update(website_name="www.carwale.com",
									city=master.city_name,
									car_make=master.make_name,
									car_model=master.model_name,
									price=price,
									model_year=year,
									car_title=title,
									car_href=href,
									car_image =image,
									is_there=1,
									)
			details = CarDetails.objects.all()
			self.assertNotEqual(details.count(), 1)


class CarwaleTest_delete(TestCase):					
	def carwale_delete_test(self):
		cars_detail = CarDetails.objects.filter(is_there=0,website_name="www.carwale.com").delete()
		print "deleted"
		

class CarwaleTest_active(TestCase):
	def carwale_active_test(self):
		CarDetails.objects.filter(website_name="www.carwale.com").update(is_there=0)
		print "is_there chaged to 0"
	

class CartradeTest_update(TestCase):
	def test_cartrade_update(self):
		master_data_store = Car_Master_Data.objects.create(
			website_name= "cartrade",
			city_id="Hyderabad", 
			city_name="Hyderabad",
			make_id ="hvmodelsMaruti-Suzuki",
			make_name = "Maruti Suzuki",
			model_id = "mod_800",
			model_name = "800").save()

		master_data_retrive = Car_Master_Data.objects.all()
		for master in master_data_retrive:
			driver = webdriver.Firefox()
			# print master.city_name
			print master.city_id
			print master.make_id
			print master.model_id
			driver.get('http://www.cartrade.com/buy-used-cars')
			try:
				close_popup = driver.find_element_by_css_selector('div#selectcityfilm a.closebtn')
				time.sleep(1)
				close_popup.click()
			except:
				pass

			try:
				close_popup = driver.find_element_by_css_selector('div#selectcityfilm a.closebtn')
				time.sleep(1)
				close_popup.click()
			except:
				pass

			try:
				select_city = driver.find_element_by_css_selector('div.leftbar select#sortcity  option[value^="%s"]'%master.city_id)
				select_city.click()
				time.sleep(1)
			except:
				pass

			try:
				select_model = driver.find_element_by_css_selector('li#%s div.spclass span.rcircle'%master.make_id)
				select_model.click()
				time.sleep(1)
			except:
				pass

			try:
				model_select =driver.find_element_by_css_selector('ul#mklist.features li#hvmodelsMaruti-Suzuki.hvchild.open ul#chmodelsMaruti-Suzuki li label input#%s'%master.model_id)
				model_select.click()
				time.sleep(1)
			except:
				pass

			car_data_list_total_div = [element for element in driver.find_elements_by_css_selector('div#searchFilters div.btmMrg.carlistblk div.widgetBox1 ')]
			for data in car_data_list_total_div:
				try:
					title = data.find_element_by_css_selector('div.titleblk div.pull-left.carlistcont div.h2heading').text
					print title
				except:
					title = "Default Title"
					print title

				try:
					href = data.find_element_by_css_selector('div.titleblk div.pull-left.carlistcont div.h2heading a').get_attribute("href")
					print href
				except:
					href = "http://www.chevrolet.co.in/trailblazer-powerful-suv.html?cmp=4456906_9138324_1673028_124445889_296988365_0"

				try:
					price=data.find_element_by_css_selector('div.titleblk div.pull-left.carlistcont div.price div.pull-left strong.pull-left').text
					price_car=price.replace(",","")
					print "Amount"
					print price_car

				except:
					price_car = "3,50,000"
					
				# scrollDown(driver, 1)
				time.sleep(3)
				try:
					image = data.find_element_by_css_selector('div.carimgblk a img').get_attribute("src")
					print image
				except:
					image = "http://imagecdn5.cartrade.com/img/300x225/lis/Maruti-Suzuki_A-Star_491097_20983_1_1435575807451.jpg"
					print image         
				year = title.split("(")[1].split(")")[0]
				print year
				time.sleep(1)
				cars_detail = CarDetails.objects.filter(website_name="www.cartrade.com")
				for detail in cars_detail:
					href_detail=detail.car_href
					save_detail=CarDetails(
					website_name="www.cartrade.com",
					city=master.city_id,
					car_make=master.make_name,
					car_model= master.model_name,
					price = price_car,
					model_year=year,
					car_title =title,
					car_href = href,
					car_image =image,
					is_there=1,
					)
					if(href!=href_detail):
						print "not equal"
						try:
							save_detail.save()
							print"saved"
						except:
							pass
					else:
						print "already existed"
						CarDetails.objects.filter(car_href=href).update(website_name="www.cartrade.com",
					city=master.city_id,
					car_make=master.make_name,
					car_model= master.model_name,
					price = price_car,
					model_year=year,
					car_title =title,
					car_href = href,
					car_image =image,
					is_there=1,
					)
			details = CarDetails.objects.all()
			self.assertNotEqual(details.count(), 1)


class CartradeTest_delete(TestCase):
	def cartrade_delete_test(self):
		cars_detail = CarDetails.objects.filter(is_there=0,website_name="www.cartrade.com").delete()
		print "deleted"
		
class CartradeTest_active(TestCase):
	def cartrade_active(self):
		CarDetails.objects.filter(website_name="www.cartrade.com").update(is_there=0)
		print "is_there chaged to 0"
	


class Cars_test(unittest.TestCase):
	def test_cars_test(self):
		driver = webdriver.Firefox()
		driver.get('http://10.90.90.193:8080/#/Delhi')
		city = driver.find_element_by_css_selector('div#main-content.container ng-view div.row.ng-scope div.selectFilter div.filter select.City-Filter.ng-pristine.ng-valid option[value^="2"]')
		city.click()
		print"ddd"
		make = driver.find_element_by_css_selector('h3#acc_title.ng-binding')
		make.click()
		print "make"

		model = driver.find_element_by_css_selector('h3#acc_title.ng-binding')
		model.click()
		print "model"


if __name__ == "__main__":
	unittest.main()





# class Cars(TestCase):
# 	def test_cars(self):
# 		driver = webdriver.Firefox()
# 		driver.get('http://10.90.90.193:8080/#/Delhi')
# 		city = driver.find_element_by_css_selector('div#main-content.container ng-view div.row.ng-scope div.selectFilter div.filter select.City-Filter.ng-pristine.ng-valid option[value^="2"]')
# 		city.click()
# 		print"ddd"
# 		make = driver.find_element_by_css_selector('h3#acc_title.ng-binding')
# 		make.click()
# 		print "make"

# 		model = driver.find_element_by_css_selector('h3#acc_title.ng-binding')
# 		model.click()
# 		print "model"

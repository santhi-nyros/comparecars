from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from django.http import HttpResponse
from django.conf import settings
import csv
from compare_cars.models import Car_Master_Data,CarDetails
from django.shortcuts import redirect

def masterdata_carwale(request):

    city_id = ['105','2','12','3000','176','198','128','10','224','244']
    cities=['Hyderabad', 'Bangalore' , 'Pune', 'Mumbai','Chennai' ,'Kolkata', 'Ahmedabad', 'Delhi','Noida','Chandigarh']
    city_name = dict(zip(city_id,cities))

    make_id = ['10','8','20','16','17','7','5','2','9','15']
    makes=['Maruti Suzuki','Hyundai','Volkswagen','Tata','Toyota','Honda','Ford','Chevrolet','Mahindra','Skoda']
    makes_name = dict(zip(make_id,makes))

    Maruti_models_id = ['10.24','10.41','10.35','10.288','10.332']
    Maruti_models_name=['800','A-Star','Alto','Swift','Zen']
    Maruti = dict(zip(Maruti_models_id,Maruti_models_name))

    Hyundai_models_id=['8.307','8.31','8.113','8.261','8.278']
    Hyundai_models_name=['Verna','Accent','Elantra','Santro','Sonata']
    Hyundai = dict(zip(Hyundai_models_id,Hyundai_models_name))

    Volkswagen_models_id=['20.304','20.227','20.177','20.224']
    Volkswagen_models_name=['Vento','Polo','Jetta,Passat']
    Volkswagen = dict(zip(Volkswagen_models_id,Volkswagen_models_name))

    Tata_models_id=['16.169','16.169','16.257','16.213','16.193']
    Tata_models_name = ["Indica","Indigo","Safari","Nano","Manza"]
    Tata = dict(zip(Tata_models_id,Tata_models_name))

    Toyota_models_id=['17.172','17.135','17.88','17.353','17.58']
    Toyota_models_name = ['Innova','Fortuner','Corolla','Corolla Altis','Camry']
    Toyota = dict(zip(Toyota_models_id,Toyota_models_name))

    Honda_models_id=['7.32','7.36','7.74','7.75','7.98']
    Honda_models_name=['Accord','Amaze','City','Civic','CR-V']
    Honda = dict(zip(Honda_models_id,Honda_models_name))

    Ford_models_id=['5.111','5.114','5.128','5.166','5.141']
    Ford_models_name=['Ecosport','Endeavour','Fiesta','Ikon','Fusion']
    Ford = dict(zip(Ford_models_id,Ford_models_name))

    Chevrolet_models_id=['2.46','2.299','2.60','2.115','2.279']
    Chevrolet_models_name=['Aveo','Aveo U-Va','Captiva','Enjoy','Spark']
    Chevrolet = dict(zip(Chevrolet_models_id,Chevrolet_models_name))

    Mahindra_models_id=['9.53','9.174','9.266','9.236','9.328']
    Mahindra_models_name=['Bolero','Jeep','Scorpio','Quanto','Xylo']
    Mahindra = dict(zip(Mahindra_models_id,Mahindra_models_name))

    Skoda_models_id=['15.126','15.184','15.215','15.287','15.241']
    Skoda_models_name=['Fabia','Laura','Octavia','Superb','Rapid']
    Skoda = dict(zip(Skoda_models_id,Skoda_models_name))

    for key,values in city_name.items():
        city_id=key
        city_name=values
        print city_name
        for key,values in makes_name.items():
            make_id=key
            make_name=values
            print make_name
            if make_name == "Maruti Suzuki":
                for key,values in Maruti.items():
                    data=Car_Master_Data(website_name="www.carwale.com",city_id=city_id,city_name=city_name,make_id=make_id,make_name=make_name,model_id=key,model_name=values).save()
            elif make_name == "Hyundai":
                for key,values in Hyundai.items():
                    data=Car_Master_Data(website_name="www.carwale.com",city_id=city_id,city_name=city_name,make_id=make_id,make_name=make_name,model_id=key,model_name=values).save()
            elif make_name == "Volkswagen":
                for key,values in Volkswagen.items():
                    data=Car_Master_Data(website_name="www.carwale.com",city_id=city_id,city_name=city_name,make_id=make_id,make_name=make_name,model_id=key,model_name=values).save()
            elif make_name == "Tata":
                for key,values in Tata.items():
                    data=Car_Master_Data(website_name="www.carwale.com",city_id=city_id,city_name=city_name,make_id=make_id,make_name=make_name,model_id=key,model_name=values).save()
            elif make_name == "Toyota":
                for key,values in Toyota.items():
                    data=Car_Master_Data(website_name="www.carwale.com",city_id=city_id,city_name=city_name,make_id=make_id,make_name=make_name,model_id=key,model_name=values).save()
            elif make_name == "Honda":
                for key,values in Honda.items():
                    data=Car_Master_Data(website_name="www.carwale.com",city_id=city_id,city_name=city_name,make_id=make_id,make_name=make_name,model_id=key,model_name=values).save()
            elif make_name == "Ford":
                for key,values in Ford.items():
                    data=Car_Master_Data(website_name="www.carwale.com",city_id=city_id,city_name=city_name,make_id=make_id,make_name=make_name,model_id=key,model_name=values).save()
            elif make_name == "Chevrolet":
                for key,values in Chevrolet.items():
                    data=Car_Master_Data(website_name="www.carwale.com",city_id=city_id,city_name=city_name,make_id=make_id,make_name=make_name,model_id=key,model_name=values).save()
            elif make_name == "Mahindra":
                for key,values in Mahindra.items():
                    data=Car_Master_Data(website_name="www.carwale.com",city_id=city_id,city_name=city_name,make_id=make_id,make_name=make_name,model_id=key,model_name=values).save()
            elif make_name == "Skoda":
                for key,values in Skoda.items():
                    data=Car_Master_Data(website_name="www.carwale.com",city_id=city_id,city_name=city_name,make_id=make_id,make_name=make_name,model_id=key,model_name=values).save()

    return HttpResponse("master data of carwale stored into the database successfully")

def masterdata_cartrade(request):
    time.sleep(10)
    city_list =['Hyderabad', 'Bangalore' , 'Pune', 'Mumbai','Chennai' ,'Kolkata', 'Ahmedabad', 'New Delhi','Noida','chandigarh']
    
    make_name= ['Maruthi suziki', ]   

    make_list = ["hvmodelsMaruti-Suzuki","hvmodelsHyundai","hvmodelsVolkswagen","hvmodelsTata",
                 "hvmodelsToyota","hvmodelsHonda","hvmodelsFord","hvmodelsChevrolet","hvmodelsMahindra",
                    "hvmodelsSkoda"]

    model_maruthi_list = ["mod_800","mod_A-Star","mod_Alto","mod_Swift","mod_Zen"]

    model_hyundai_list = ["mod_Verna","mod_Accent","mod_Elantra","mod_Santro","mod_Sonata"]
    
    model_volks_list = ["mod_Vento","mod_Beetle","mod_Passat","mod_Polo","mod_Jetta"]

    model_tata_list = ["mod_Safari","mod_Indigo","mod_Nano","mod_Manza","mod_Indica"]

    model_tayota_list = ["mod_Innova","mod_Fortuner","mod_Corolla","mod_Altis","mod_Camry"]

    model_honda_list = ["mod_Accord","mod_Amaze","mod_Civic","mod_City","mod_CR-V"]  

    model_ford_list = ["mod_Fusion","mod_EcoSport","mod_Endeavour","mod_Ikon","mod_Fiesta"]  

    model_chevro_list = ["mod_Aveo","mod_Aveo-Old","mod_Aveo-U-VA","mod_Captiva","mod_Enjoy"]

    model_mahindra_list = ["mod_Scorpio","mod_Bolero","mod_Xylo","mod_Jeep","mod_Quanto"]  

    model_skoda_list = ["mod_Fabia","mod_Laura","mod_Superb","mod_Octavia","mod_Rapid"]  

    for city in city_list:
        print city
        for make in make_list:
            print make
            makename = make.split("hvmodels")[1]
            if  make == "hvmodelsMaruti-Suzuki":
                for model in model_maruthi_list:
                    modelname= model.split('mod_')[1]
                    data=Car_Master_Data(website_name="www.cartrade.com",city_id=city,city_name=city,make_id=make,make_name=makename,model_id=model,model_name=modelname).save()
            elif  make == "hvmodelsHyundai":
                for model in model_hyundai_list:
                    modelname= model.split('mod_')[1]
                    data=Car_Master_Data(website_name="www.cartrade.com",city_id=city,city_name=city,make_id=make,make_name=makename,model_id=model,model_name=modelname).save()
            elif  make == "hvmodelsVolkswagen":
                for model in model_volks_list:
                    modelname= model.split('mod_')[1]
                    data=Car_Master_Data(website_name="www.cartrade.com",city_id=city,city_name=city,make_id=make,make_name=makename,model_id=model,model_name=modelname).save()
            elif  make == "hvmodelsTata":
                for model in model_tata_list:
                    modelname= model.split('mod_')[1]
                    data=Car_Master_Data(website_name="www.cartrade.com",city_id=city,city_name=city,make_id=make,make_name=makename,model_id=model,model_name=modelname).save()
            elif  make == "hvmodelsToyota":
                for model in model_tayota_list:
                    modelname= model.split('mod_')[1]
                    data=Car_Master_Data(website_name="www.cartrade.com",city_id=city,city_name=city,make_id=make,make_name=makename,model_id=model,model_name=modelname).save()
            elif  make == "hvmodelsHonda":
                for model in model_honda_list:
                    modelname= model.split('mod_')[1]
                    data=Car_Master_Data(website_name="www.cartrade.com",city_id=city,city_name=city,make_id=make,make_name=makename,model_id=model,model_name=modelname).save()
            elif  make == "hvmodelsFord":
                for model in model_ford_list:
                    modelname= model.split('mod_')[1]
                    data=Car_Master_Data(website_name="www.cartrade.com",city_id=city,city_name=city,make_id=make,make_name=makename,model_id=model,model_name=modelname).save()
            elif  make == "hvmodelsChevrolet":
                for model in model_chevro_list:
                    modelname= model.split('mod_')[1]
                    data=Car_Master_Data(website_name="www.cartrade.com",city_id=city,city_name=city,make_id=make,make_name=makename,model_id=model,model_name=modelname).save()
            elif  make == "hvmodelsMahindra":
                for model in model_mahindra_list:
                    modelname= model.split('mod_')[1]
                    data=Car_Master_Data(website_name="www.cartrade.com",city_id=city,city_name=city,make_id=make,make_name=makename,model_id=model,model_name=modelname).save()
            elif  make == "hvmodelsSkoda":
                for model in model_skoda_list:
                    modelname= model.split('mod_')[1]
                    data=Car_Master_Data(website_name="www.cartrade.com",city_id=city,city_name=city,make_id=make,make_name=makename,model_id=model,model_name=modelname).save()

    return HttpResponse("successfully created master data for cartrade website")


def scrollDown(driver, numberOfScrollDowns):
    body = driver.find_element_by_tag_name("body")
    while numberOfScrollDowns >=0:
        body.send_keys(Keys.PAGE_DOWN)
        numberOfScrollDowns -= 1
    return driver



def carwale_scrap(request):
    driver = webdriver.Firefox()
    all_cars = Car_Master_Data.objects.filter(website_name="www.carwale.com")
    for car in all_cars:
        driver.get("http://www.carwale.com/used/cars-for-sale/")
        print driver.title
        time.sleep(2)
        car_city = car.city_id
        car_make = car.make_id
        car_model = car.model_id
        city_name=car.city_name
        make_name=car.make_name
        model_name=car.model_name

        try:
            city = driver.find_element_by_css_selector('select#drpCity.form-control option[value="%s"]'%car_city)
            city.click()
            print city_name
            time.sleep(2)
        except:
            pass

        try:
            make = driver.find_element_by_css_selector("ul#makesList.ul-makes li.us-sprite.makeLi[carfilterid='%s']"%car_make) 
            make.click()
            print make_name
            time.sleep(10)
        except:
            pass

        try:
            model = driver.find_element_by_css_selector('ul#makesList.ul-makes li.us-sprite.makeLi div.list-points-models ul.rootUl li.us-sprite.rootLi[carfilterid="%s"]'%car_model)
            model.click()
            print model_name
            time.sleep(2)
        except:
            pass

        driver = scrollDown(driver, 2)

        car_data_list = [element for element in driver.find_elements_by_css_selector('div.stock-list ul#listing1.ko-listing li.listing-adv.listingContent.padding-top10.padding-bottom10.cur-pointer div.stock-detail')]        
        print "*********"*12
        print city_name
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

            driver = scrollDown(driver, 2)
            print"scroll"

            image = data.find_element_by_css_selector('div.leftfloat.thumb-div div.thumb-area div.img-placer a.slideShow img').get_attribute("src")
            print image

            year = data.find_element_by_css_selector('div.leftfloat.table-div.margin-left20 a.text-grey p.listingItemKms.font14.text-light-grey.margin-top5 span:nth-of-type(7)').text
            print year

            time.sleep(2)
            print"*******"
            try:
                
                CarDetails(website_name="www.carwale.com",
                        city=city_name,
                        car_make=make_name,
                        car_model=model_name,
                        price=price,
                        model_year=year,
                        car_title=title,
                        car_href=href,
                        car_image =image
                        ).save()
                print"try"
            except:
                print"exception"
                pass 
                
    return HttpResponse("carwale data stored into the database successfully")

# from pyvirtualdisplay import Display
def cartrade_scrap(request):
    # display = Display(visible=0, size=(1024, 768))
    # display.start()
    driver = webdriver.Firefox()
    
    master_data = Car_Master_Data.objects.filter(website_name="www.cartrade.com")
    for master in master_data:
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
                
            scrollDown(driver, 1)
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
            try:
                CarDetails(
                website_name="www.cartrade.com",
                city=master.city_id,
                car_make=master.make_name,
                car_model= master.model_name,
                price = price_car,
                model_year=year,
                car_title =title,
                car_href = href,
                car_image =image,
                ).save()
                print "saved"
            except:
                print "exception"
                pass

    # driver.close()
    # display.stop()

    return HttpResponse("successfully scrapped cartrade")



def carwale_update():
    driver = webdriver.Firefox()
    all_cars = Car_Master_Data.objects.filter(website_name="www.carwale.com")
    for car in all_cars:
        driver.get("http://www.carwale.com/used/cars-for-sale/")
        print driver.title
        time.sleep(2)
        car_city = car.city_id
        car_make = car.make_id
        car_model = car.model_id
        city_name=car.city_name
        make_name=car.make_name
        model_name=car.model_name
        try:
            city = driver.find_element_by_css_selector('select#drpCity.form-control option[value="%s"]'%car_city)
            city.click()
            print city_name
            time.sleep(2)
        except:
            pass

        try:
            make = driver.find_element_by_css_selector("ul#makesList.ul-makes li.us-sprite.makeLi[carfilterid='%s']"%car_make) 
            make.click()
            print make_name
            time.sleep(10)
        except:
            pass

        try:
            model = driver.find_element_by_css_selector('ul#makesList.ul-makes li.us-sprite.makeLi div.list-points-models ul.rootUl li.us-sprite.rootLi[carfilterid="%s"]'%car_model)
            model.click()
            print model_name
            time.sleep(2)
        except:
            pass

        driver = scrollDown(driver, 2)
        car_data_list = [element for element in driver.find_elements_by_css_selector('div.stock-list ul#listing1.ko-listing li.listing-adv.listingContent.padding-top10.padding-bottom10.cur-pointer div.stock-detail')]        
        print "*********"*12
        print city_name
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

            driver = scrollDown(driver, 2)
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
                                city=city_name,
                                car_make=make_name,
                                car_model=model_name,
                                price=price,
                                model_year=year,
                                car_title=title,
                                car_href=href,
                                car_image =image,
                                is_verified=True,
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
                                city=city_name,
                                car_make=make_name,
                                car_model=model_name,
                                price=price,
                                model_year=year,
                                car_title=title,
                                car_href=href,
                                car_image =image,
                                is_verified=True,
                                )
    return HttpResponse("updated")

def carwale_delete():
    cars_detail = CarDetails.objects.filter(is_verified=False,website_name="www.carwale.com").delete()
    print "deleted"
    return HttpResponse("deleted")
def carwale_active():
    CarDetails.objects.filter(website_name="www.carwale.com").update(is_verified=False)
    print "is_verified chaged to 0"
    return HttpResponse("is_verified to set 0")


def cartrade_update():
    driver = webdriver.Firefox()
    master_data = Car_Master_Data.objects.filter(website_name="www.cartrade.com")
    for master in master_data:
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
                
            scrollDown(driver, 1)
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
                is_verified=True,
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
                is_verified=True,
                )
    return HttpResponse("updated")

def cartrade_delete():
    cars_detail = CarDetails.objects.filter(is_verified=False,website_name="www.cartrade.com").delete()
    print cars_detail
    print "deleted"
    return HttpResponse("deleted")

def cartrade_active():
    CarDetails.objects.filter(website_name="www.cartrade.com").update(is_verified=False)
    print "is_verified chaged to 0"
    return HttpResponse("is_verified to set 0")


from django.shortcuts import render_to_response
from django.template import RequestContext


def search(request):
    print "ddd"
    
    searchtxt = request.GET.get('q', '')
    print searchtxt
    context_object_name = 'city_list'
    details = []
    cities=['Hyderabad', 'Bangalore' , 'Pune', 'Mumbai','Chennai' ,'Kolkata', 'Ahmedabad', 'Delhi','Noida','Chandigarh']
    for city in cities:
        if(city==searchtxt):
            # print city
            details=CarDetails.objects.filter(city=city)
            print details
            print type(details)
            return render_to_response('search.html', {'city_list':details}, context_instance=RequestContext(request))
    
    return render(request, 'search_details.html')


def store_scrapdata(request):
    print '***************'
    print settings.PROJECT_ROOT
    path = '%s/compare_cars_cardetails_24th.csv'%(settings.PROJECT_ROOT)
    print path
    with open(path,'rb') as f:
        data=[tuple(line) for line in csv.reader(f)]
        for store in data:
            print store[1]
            print store[2]
            print store[3]
            print store[4]
            print store[5]
            print store[6]
            print store[7]
            print store[8]
            print store[9]
            print '**********'
            print store[10]
            print store[11]
            store_scrapping = CarDetails(website_name=store[1],city=store[2],car_make=store[3],
                car_model=store[4],price=store[5],model_year=store[6],
                car_title=store[7],car_href=store[8],car_image=store[9],is_verified=False,
                )
            try:
                store_scrapping.save()
            except :
                print("exception")
                pass

    return HttpResponse("data hasbeen stored into DB")

def keyword_update(request):
    ''' elastic search'''
    data = CarDetails.objects.all()

    key = ""

    for d in data:
        city = str(d.city)
        year = str(d.model_year)
        make = str(d.car_make)
        model = str(d.car_model)

        key = city + year + make + model 

        CarDetails.objects.filter(city=city,model_year=d.model_year,car_make=make,car_model=model).update(keywords=key)

        print "$$$$$$$$"
        print key

    return HttpResponse("keyword_update")

from .forms import SearchingForm

def searching(request):
    # Searching(city = "Kolkata",car_make="Tata",
    #     car_model="Alto",price = 30000,model_year=2014,
    #     keywords="KolkataTataalto300002014").save()
    if request.method == 'POST':
        form = SearchingForm(request.POST)
        search_word = request.POST.get("search_word")
        #filterargs = { 'car_make': 'search_word', 'car_model': 'search_word', 'car_model': 'search_word'}

        if form.is_valid():
            #x = CarDetails.objects.filter(**filterargs)
            # print x
            # print type(x)

            data = CarDetails.objects.filter(keywords__icontains=search_word)

            for i in data:
                print i
                print i.city

            # if x:
            #     print "city based"
            #     hi = x.filter(car_make=search_word)
            #     print "&&&&"
            #     print hi


            # else:
            #     print "error"


                # car_make__contains=search_word,,car_model__icontains=search_word,
                # model_year__contains=search_word)
            # print '***********'
            # print search
            # for ser in x:
                # print '******'
                # print ser.city
                #print ser.
            return HttpResponse("this is searching demo")
            
    else:
        form =SearchingForm()
    return render_to_response('demo.html', {'form':form},
        context_instance=RequestContext(request))  

def image_update(request):
    # image = data.find_element_by_css_selector('div.leftfloat.thumb-div div.thumb-area div.img-placer a.slideShow img').get_attribute("src")
    # print image
    some = CarDetails.objects.all()
    print some 
    for ss in some :
        print ss.car_image
        image = ss.car_image
        print image
        print type(image)



        # if image.endswith("gif"):
        #     image="http://www.yourlexusdealer.com/yld/pub-share/img/default_car.jpg"

        #     img = CarDetails.objects.filter(car_image=image).update()
        #     print img
        # else:
        #     print "error"
    return HttpResponse("hai")

    # update compare_cars_cardetails set car_image=replace(car_image,'http://img.aeplcdn.com/grey.gif',"http://www.yourlexusdealer.com/yld/pub-share/img/default_car.jpg")

def records_count(request):

    total  = CarDetails.objects.all().count()

    return HttpResponse("Total records are %s"%(total))


def scrapping_csv():
    return store_scrapdata(request)
    

def keywords():
    return keyword_update(request)
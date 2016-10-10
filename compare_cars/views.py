from .models import Car_Master_Data,CarDetails
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import serializers
from .serializers import CompareCarSerializer,MaterCarSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response







# master data views

class Get_allMakes(generics.ListCreateAPIView):
    """
    List all boards, or create a new board.
    """
    # queryset_results = CarMakeDetails.objects.order_by().values('makes').distinct()
    print "car_make"
    queryset = CarDetails.objects.order_by("price")
    # queryset = CarDetails.objects.all().order_by("price")
    # print queryset
    serializer_class = CompareCarSerializer






# scrapped  data views
@api_view(['GET'])
def Get_allMakesDetails(request,car_make):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        models= CarDetails.objects.filter(car_make=car_make)
        #print models
    except models.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CompareCarSerializer(models,many=True)
        lookup_field = 'car_make'
        return Response(serializer.data)

# class Get_allMakesDetails(views.APIView):
#     queryset = CarMakeDetails.objects.filter(makes='Tata')
#     serializer_class = CompareCarSerializer

@api_view(['GET'])
def Get_allModelDetails(request,car_make,car_model):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        print "models"
        makes_set = CarDetails.objects.order_by("price").filter(car_make=car_make)
        models_set = makes_set.filter(car_model=car_model)
        # for model in models_set:
        #     print '*********************'
        #     print model.car_image
    except:
        # return Response(status=status.HTTP_404_NOT_FOUND)
        print "error"

    if request.method == 'GET':
        serializer = CompareCarSerializer(models_set,many=True)
        lookup_field = 'car_make'
        s_data = serializer.data
        for s in s_data:
            print s["car_image"]
        # print "-----------------------------------------------"
        # print serializer.data
        # print "-----------------------------------------------"
        return Response(serializer.data)


@api_view(['GET'])
def Get_DataFromCity(request,city):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        print "cities"
        city_search =city.title()
        city_data = CarDetails.objects.order_by("price").filter(city=city_search)
        # city_data = CarDetails.objects.order_by("price").filter(city=city)
        print city_data
    except city_data.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CompareCarSerializer(city_data,many=True)
        lookup_field = 'car_make'
        print "-----------------------------------------------"
        print serializer.data
        print "-----------------------------------------------"
        return Response(serializer.data)


@api_view(['GET'])
def Get_AllDataFromCity(request,city,car_make,car_model):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        print "cities"
        city_search =city.title()
        makes = CarDetails.objects.order_by("price").filter(city=city_search)
        models = makes.filter(car_make=car_make)
        models_set = models.filter(car_model=car_model)
        
    except models_set.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CompareCarSerializer(models_set,many=True)
        lookup_field = 'car_make'
        print "-----------------------------------------------"
        print serializer.data
        print "-----------------------------------------------"
        return Response(serializer.data)




@api_view(['GET'])
def elastic(request,text):
    print "hai"
    information=[]
    try:
        print "try"
        cities=['Hyderabad', 'Bangalore' , 'Pune', 'Mumbai','Chennai' ,'Kolkata', 'Ahmedabad', 'Delhi','Noida','Chandigarh']
        makes=['Maruti Suzuki','Hyundai','Volkswagen','Tata','Toyota','Honda','Ford','Chevrolet','Mahindra','Skoda']
        models=['800','A-Star','Alto','Swift','Zen','Verna','Accent','Elantra','Santro','Sonata',
                'Vento','Polo','Jetta','Passat',"Indica","Indigo","Safari","Nano","Manza",
                'Innova','Fortuner','Corolla','Corolla Altis','Camry','Accord','Amaze','City','Civic','CR-V','Ecosport','Endeavour','Fiesta','Ikon','Fusion',
                'Aveo','Aveo U-Va','Captiva','Enjoy','Spark','Bolero','Jeep','Scorpio','Quanto','Xylo',
                'Fabia','Laura','Octavia','Superb','Rapid']
        import re
        search=text.title()
        print "###########"
        print text
        print len(search)
        l=re.split(',',search)
        length=len(l)
        print length
        result1=[]
        result2=[]
        result3=[]
        result4=[]
        if(length==1):
            s1=[]
            d=l[0].isdigit()
            if(d==True):
                digit_length=len(str(l[0]))
                print "ddd"
                print "************"
                if(digit_length==4):
                    s1=l[0]
                    print s1
                    print"!!!"
                elif(digit_length==3):
                    for model in models:
                        if(model==l[0]):
                            s1=model
                            print s1

            else:
                for city in cities:
                    if(city==l[0]):
                        s1=city
                        print s1
                    else:
                        print "not city"
                for make in makes:
                    if(make==l[0]):
                        s1=make
                        print s1
                    else:
                        print "not make"
                for model in models:
                    if(model==l[0]):
                        s1=model
                        print s1
                    else:
                        print"not model"


            list1 = CarDetails.objects.filter(keywords__icontains = s1)
            print list1
            for i in list1:
                i.car_href
                result1.append(i.car_href)
            information=CarDetails.objects.filter(car_href__in=result1)
            serializer_class = CompareCarSerializer
            for info in information:
                print info.city
                print info.car_make
                print info.car_model
                print info.car_href
                print info.car_image
                print info.model_year


        elif(length==2):
            print l[0]
            print l[1]
            sort=sorted(l)
            print sort
            print sort[0]
            print sort[1]
            digit1=sort[0].isdigit()
            digit2=sort[1].isdigit()
            digit_length1=len(str(sort[0]))
            digit_length2=len(str(sort[1]))
            s1=[]
            s2=[]
            if(digit1==True and digit2==True):
                print "hai"
                if(digit_length1==4 and digit_length2==3):
                    print"two"
                    s1=sort[0]
                    s2=sort[1]
            elif(digit1==True or digit2==True):
                print"digit"
                digit_length=len(str(sort[0]))
                if(digit_length==4 or digit_length==3):
                    s2=sort[0]
                    print "ddd"
                    for city in cities:
                        if(city==sort[1]):
                            s1=city
                            print s1
                        else:
                            print "not city"
                    for make in makes:
                        if(make==sort[1]):
                            s1=make
                            print s1
                        else:
                            print "not make"
                    for model in models:
                        if(model==sort[1]):
                            s1=model
                            print s1
            else:
                for city in cities:
                    if(city==l[0]):
                        s1=city
                        print s1
                    elif(city==l[1]):
                        s2=city
                    else:
                        print "not city"
                for make in makes:
                    if(make==l[0]):
                        s1=make
                        print s1
                    elif(make==l[1]):
                        s2=make
                    else:
                        print "not make"
                for model in models:
                    if(model==l[0]):
                        s1=model
                        print s1
                    elif(model==l[1]):
                        s2=model
                    else:
                        print"not model"

            list1 = CarDetails.objects.filter(keywords__icontains = s1)
            # print list1
            for i in list1:
                i.car_href
                result1.append(i.car_href)
            list2 = CarDetails.objects.filter(keywords__icontains = s2)
            for j in list2:
                result2.append(j.car_href)
            common_data = list(set(result1).intersection(result2))
            information=CarDetails.objects.filter(car_href__in=common_data)
            for info in information:
                print info.city
                print info.car_make
                print info.car_model
                print info.car_href
                print info.car_image
                print info.model_year


        elif(length==3):
            print l[0]
            print l[1]
            print l[2]
            sort=sorted(l)
            print sort[0]
            print sort[1]
            print sort[2]
            s1=[]
            s2=[]
            s3=[]
            digit1=sort[0].isdigit()
            digit2=sort[1].isdigit()
            digit3=sort[2].isdigit()
            if(digit1==True and digit2==True and digit3==False):
                digit_length1=len(str(sort[0]))
                digit_length2=len(str(sort[1]))
                print sort
                if(digit_length1==4 and digit_length2==3):
                    print "EEEGFHGUIJU"
                    s1=sort[0]
                    s2=sort[1]
                # s3=sort[2]
                    for city in cities:
                        if(city==sort[2]):
                            s3=city
                            print s3
                    for make in makes:
                        if(make==sort[2]):
                            s3=make
                            print s3
                    for model in models:
                            if(model==sort[2]):
                                s3=model
                                print s3

            elif(digit1==True or digit2==True or digit3==True):
                print"digit"

                digit_length=len(str(sort[0]))
                if(digit_length==4 or digit_length==3):
                    for city in cities:
                        if(city==sort[1]):
                            s1=city
                            print s1
                        elif(city==sort[2]):
                            s1=city
                            print s1
                        else:
                            print "not city"
                    for make in makes:
                        if(make==sort[1]):
                            s2=make
                            print s2
                        elif(make==sort[2]):
                            s2=make
                        else:
                            print "not make"
                    for model in models:
                        if(model==sort[1]):
                            s3=model
                            print s3
                        elif(model==sort[2]):
                            s3=model
                            print s3
                    s=[s1,s2,s3]
                    remove_empty=filter(lambda x: len(x) > 0, s)
                    print"#########"
                    s1=sort[0]
                    s2=remove_empty[0]
                    s3=remove_empty[1]
                    print s1
                    print s2
                    print s3
                    print"#########"

            else:
                for city in cities:
                    if(city==l[0]):
                        s1=city
                        print s1
                    elif(city==l[1]):
                        s1=city
                        print s1
                    elif(city==l[2]):
                        s1=city
                    else:
                        print "not city"
                for make in makes:
                    if(make==l[0]):
                        s2=make
                        print s2
                    elif(make==l[1]):
                        s2=make
                    elif(make==l[2]):
                        s2=make
                    else:
                        print "not make"
                for model in models:
                    if(model==l[0]):
                        s3=model
                        print s3
                    elif(model==l[1]):
                        s3=model
                        print s3
                    elif(model==l[2]):
                        s3=model
                        print s3
            list1 = CarDetails.objects.filter(keywords__icontains = s1)
            for i in list1:
                i.car_href
                result1.append(i.car_href)
            list2 = CarDetails.objects.filter(keywords__icontains = s2)
            for j in list2:
                result2.append(j.car_href)
            list3=CarDetails.objects.filter(keywords__icontains=s3)
            for k in list3:
                result3.append(k.car_href)
            common_data = list(set(result1).intersection(result2,result3))
            information=CarDetails.objects.filter(car_href__in=common_data)
            for info in information:
                print info.city
                print info.car_make
                print info.car_model
                print info.car_href
                print info.car_image
                print info.model_year

        elif(length==4):
            print l[0]
            print l[1]
            print l[2]
            print l[3]
            digit1=l[0].isdigit()
            digit2=l[1].isdigit()
            digit3=l[2].isdigit()
            digit4=l[3].isdigit()
            if(digit1==True or digit2==True or digit3==True or digit4==True):
                print"digit"
                sort=sorted(l)
                print sort[0]
                print sort[1]
                print sort[2]
                print sort[3]
                s1=[]
                s2=[]
                s3=[]
                s4=[]
                digit_length=len(str(sort[0]))
                if(digit_length==4):
                    for city in cities:
                        if(city==sort[1]):
                            s1=city
                            print s1
                        elif(city==sort[2]):
                            s1=city
                            print s1
                        elif(city==sort[3]):
                            s1=city
                        else:
                            print "not city"
                    for make in makes:
                        if(make==sort[1]):
                            s2=make
                            print s2
                        elif(make==sort[2]):
                            s2=make
                        elif(make==sort[3]):
                            s2=make
                        else:
                            print "not make"
                    for model in models:
                        if(model==sort[1]):
                            s3=model
                            print s3
                        elif(model==sort[2]):
                            s3=model
                            print s3
                        elif(model==sort[3]):
                            s3=model            
                    list1 = CarDetails.objects.filter(keywords__icontains = sort[0])
                    for i in list1:
                        i.car_href
                        result1.append(i.car_href)
                    list2 = CarDetails.objects.filter(keywords__icontains = s1)
                    for j in list2:
                        result2.append(j.car_href)
                    list3=CarDetails.objects.filter(keywords__icontains=s2)
                    for k in list3:
                        result3.append(k.car_href)
                    list4=CarDetails.objects.filter(keywords__icontains=s3)
                    for p in list4:
                        result4.append(p.car_href)
                    total_list=[list1,list2,list3,list4]
                    for t in total_list:
                        print t
                    information = list(set(total_list[0]).intersection(*total_list[1:]))
                    print"$$$$$$$$$$"
                    print information
                    for info in information:
                        print info.city
                        print info.car_make
                        print info.car_model
                        print info.car_href
                        print info.car_image
                        print info.model_year
    except:
        print"your enterd wrong"

    if request.method == 'GET':
        serializer = CompareCarSerializer(information,many=True)
        # lookup_field = 'car_make'
        print "-----------------------------------------------"
        # print serializer.data
        print "-----------------------------------------------"
        return Response(serializer.data)


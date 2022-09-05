
# line1 =[[1, "Helwan"], [2, "Ain Helwan"], [3, "Helwan University"], [4, "Wadi Hof"], [5, "Helwan Gardens"], [6, "Masara"], [7, "Tora Cement"], [8, "Kotsika"], [9, "Tora al-Balad"], [10, "Maadi Barracks"], [11, "Maadi"], [12 , "Hadayek al-Maadi"], [13, "Dar al-Salaam"], [14, "Al-Zahra"], [15, "Mar Gerges"], [16, "The Good King"], [17, "Sayida Zainab"] [18, "Saad Zagloul"], [19, "Anwar Sadat"], [20, "Jamal Abdel Nasser"], [21, "Ahmed Orabi"], [22, "The Martyrs"], [23, " Ghamra"], [24, "Al-Demerdash"], [25, "Manshiyat al-Sadr"], [26, "The Dome Bridge"], [27, "Hammam al-Quba"], [28, "Saray al-Qubba"], [29 , "The Gardens of Olives"], [30, "Helmiyet al-Zaytoun"], [31, "Al-Matareya"], [32, "Ain Shams"], [33, "Izbat al-Nakhl"], [34, "The Meadow"], [35, "The New Prairie"]]
# line2=[[36,"Munib"],[37,"Sakiat Makki"],[38,"Umm al-Masrya"],[39,"Giza"],[40,"Faisal"],[41,"University Cairo"],[42,"Al-Research"],[43,"Dokki"],[44,"Opera"],[19,"Anwar El-Sadat"],[45,"Mohamed Naguib"],[46," The Threshold"],[22,"Martyrs"],[47,"Masara"],[48,"Rawd al-Faraj"],[49,"Santa Teresa"],[50,"Al-Khalfawi"],[51," Parasols"],[52, "Faculty of Agriculture"],[53, "Shubra El-Kheima"]]
# line3=[[54,"Adly Mansour"],[55,"Hykestep"],[56,"Omar Ibn al-Khattab"],[57,"Quba"],[58,"Hisham Barakat"],[59, "Al-Nuzha"], [60, "The Sun Club"], [61, "Alf Maskan"], [62, "Heliopolis"], [63, "Aaron"], [64, "Al-Ahram"], [65, "Girls College"], [66,"Stadium"], [67, "Fairground"], [68 ,"Abbasiya"], [69, "Abdo Pasha"], [70, "Army"], [71 ,"Bab al-Sha aria"],[47,"Ataba"],[20, "Gamal Abdel Nasser"],[72, "Maspero"],[73,"Safaa Hijazi"],[74,"Kit Kat"] ]

# list = []
# for i in range(0,20):
#     list.append(line1[i][1])
#     print(list)
    
from operator import indexOf

def get_station_index(line,station):
    for i in range (0,len(line)):
        if line[i]['name']== station:
            return i
        
line1=[{"id":1,"name":"Helwan","tabadol":"f"},{"id":2,"name":"Ain Helwan","tabadol":"f"},{"id":3,"name":"Helwan University","tabadol":"f"},{"id":4,"name":"Wadi Hof","tabadol":"f"},{"id":5,"name":"Hadayek Helwan","tabadol":"f"},{"id":6,"name":"Masara","tabadol":"f"},{"id":7,"name":"Tora El-Asmant","tabadol":"f"},{"id":8,"name":"Kozzika","tabadol":"f"},{"id":9,"name":"Tora El-Balad","tabadol":"f"},{"id":10,"name":"Sakanat El-Maadi","tabadol":"f"},{"id":11,"name":"Maadi","tabadol":"f"},{"id":12,"name":"Hadayek El-Maadi","tabadol":"f"},{"id":13,"name":"Dar El-Salam","tabadol":"f"},{"id":14,"name":"El-Zahraa","tabadol":"f"},{"id":15,"name":"Mar Girgis","tabadol":"f"},{"id":16,"name":"El-Malek El-Saleh","tabadol":"f"},{"id":17,"name":"Al-Sayeda Zeinab","tabadol":"f"},{"id":18,"name":"Saad Zaghloul","tabadol":"f"},{"id":19,"name":"Sadat","tabadol":"t","line":2},{"id":20,"name":"Nasser","tabadol":"t","line":3},{"id":21,"name":"Orabi","tabadol":"f"},{"id":22,"name":"Al-Shohadaa","tabadol":"t","line":2},{"id":23,"name":"Ghamra","tabadol":"f"},{"id":24,"name":"El-Demerdash","tabadol":"f"},{"id":25,"name":"Manshiet El-Sadr","tabadol":"f"},{"id":26,"name":"Kobri El-Qobba","tabadol":"f"},{"id":27,"name":"Hammamat El-Qobba","tabadol":"f"},{"id":28,"name":"Saray El-Qobba","tabadol":"f"},{"id":29,"name":"Hadayeq El-Zaitoun","tabadol":"f"},{"id":30,"name":"Helmeyet El-Zaitoun","tabadol":"f"},{"id":31,"name":"El-Matareyya","tabadol":"f"},{"id":32,"name":"Ain Shams","tabadol":"f"},{"id":33,"name":"Ezbet El-Nakhl","tabadol":"f"},{"id":34,"name":"El-Marg","tabadol":"f"},{"id":35,"name":"New El-Marg","tabadol":"f"},]
line2=[{"id":36,"name":"Munib","tabadol":"f"},{"id":37,"name":"Sakiat Makki","tabadol":"f"},{"id":38,"name":"Umm al-Masrya","tabadol":"f"},{"id":39,"name":"Giza","tabadol":"f"},{"id":40,"name":"Faisal","tabadol":"f"},{"id":41,"name":"Cairo University","tabadol":"f"},{"id":42,"name":"El Bohoth","tabadol":"f"},{"id":43,"name":"Dokki","tabadol":"f"},{"id":44,"name":"Opera","tabadol":"f"},{"id":19,"name":"Sadat","tabadol":"t","line":1},{"id":45,"name":"Mohamed Naguib","tabadol":"f"},{"id":46,"name":"Attaba","tabadol":"t","line":3},{"id":22,"name":"Al-Shohadaa","tabadol":"t","line":'1'},{"id":47,"name":"Masarra","tabadol":"f"},{"id":48,"name":"Road El-Farag","tabadol":"f"},{"id":49,"name":"St. Teresa","tabadol":"f"},{"id":50,"name":"Khalafawy","tabadol":"f"},{"id":51,"name":"Mezallat","tabadol":"f"},{"id":52,"name":"Kolleyyet El-Zeraa","tabadol":"f"},{"id":53,"name":"Shubra El-Kheima","tabadol":"f"}]
line3=[{"id":54,"name":"Adly Mansour","tabadol":"f"},{"id":55,"name":"El Haykestep","tabadol":"f"},{"id":56,"name":"Omar Ibn El-Khattab","tabadol":"f"},{"id":57,"name":"Qobaa","tabadol":"f"},{"id":58,"name":"Hesham Barakat","tabadol":"f"},{"id":59,"name":"El-Nozha","tabadol":"f"},{"id":60,"name":"Nadi El-Shams","tabadol":"f"},{"id":61,"name":"Alf Maskan","tabadol":"f"},{"id":62,"name":"Heliopolis Square","tabadol":"f"},{"id":63,"name":"Haroun","tabadol":"f"},{"id":64,"name":"Al-Ahram","tabadol":"f"},{"id":65,"name":"Koleyet El-Banat","tabadol":"f"},{"id":66,"name":"Stadium","tabadol":"f"},{"id":67,"name":"Fair Zone","tabadol":"f"},{"id":68,"name":"Abbassia","tabadol":"f"},{"id":69,"name":"Abdou Pasha","tabadol":"f"},{"id":70,"name":"El Geish","tabadol":"f"},{"id":71,"name":"Bab El Shaaria","tabadol":"f"},{"id":47,"name":"Attaba","tabadol":"t","line":2},{"id":20,"name":"Nasser","tabadol":"t","line":1},{"id":72,"name":"Maspero","tabadol":"f"},{"id":73,"name":"Zamalek","tabadol":"f"},{"id":74,"name":"Kit Kat","tabadol":"f"}]
line1_and_line2=[{"id":19,"name":"Sadat","line1_index":get_station_index(line1,'Sadat'),"line2_index":get_station_index(line2,'Sadat')},{"id":22,"name":"Al-Shohadaa","line1_index":get_station_index(line1,'Al-Shohadaa'),"line2_index":get_station_index(line2,'Al-Shohadaa')}]
line2_and_line3=[{"id":46,"name":"Attaba","line2_index":get_station_index(line2,'Attaba'),"line3_index":get_station_index(line3,'Attaba')}]
line1_and_line3=[{"id":20,"name":"Nasser","line1_index":get_station_index(line1,'Nasser'),"line3_index":get_station_index(line3,'Nasser')}]
##########################check stations number ########################
def check_line_number(station):
    metro_line1=0
    metro_line2=0
    metro_line3=0
       
    for i in range(0,len(line1)):
        if station ==line1[i]['name']:
            metro_line1=1
    
    for i in range(0,len(line2)):
        if station ==line2[i]['name']:
            metro_line2=1
            
    for i in range(0,len(line3)):
        if station ==line3[i]['name']:
            metro_line3=1
    
    return{"line1":metro_line1,"line2":metro_line2,"line3":metro_line3}

##########################check if stations in the same line ########################
def same_line_stations(source,destination):
    source_line=check_line_number(source)
    destination_line=check_line_number(destination)
    if source_line['line1']==destination_line['line1'] and source_line['line1']==1:
        return "line1"
    elif source_line['line2']==destination_line['line2'] and source_line['line2']==1:
        return "line2"
    elif source_line['line3']==destination_line['line3'] and source_line['line3']==1:
        return "line3"
    else :
        return "none"
    
    
##########################check  stations line 2 ######################## 
def my_one_station_line(station):
    for key, value in check_line_number(station).items():
            if value == 1:
             return key
########################## get station index ########################
def get_station_index(line,station):
    for i in range (0,len(line)):
        if line[i]['name']== station:
            return i
##########################check tiket money########################
def check_money(mylist):
    if len(mylist)<=9 :
        return 5
    elif len(mylist)>9 and len(mylist)<=15:
        return 10
    else:
        return 15
##########################get main route########################
def main_route(source,destination):
    same_line=same_line_stations(source,destination) 
    if same_line!='none':
        resolult=[]
        
    ##################line1#######################3
        if same_line=='line1':
            station1=get_station_index(line1,source)
            station2=get_station_index(line1,destination)
            
            if station1 < station2:
             for i in range(station1,station2+1):
                 resolult.append(line1[i]['name'])
            else:
             for i in range(station1,station2-1,-1):
                    resolult.append(line1[i]['name'])               
            # resolult=station2-station1

        elif same_line=='line2':
            station1=get_station_index(line2,source)
            station2=get_station_index(line2,destination)
           
            if station1 < station2:
             for i in range(station1,station2+1):
                 resolult.append(line2[i]['name'])
            else:
             for i in range(station1,station2-1,-1):
                    resolult.append(line2[i]['name'])               
            # resolult=station2-station1
        elif same_line=='line3':
            station1=get_station_index(line3,source)
            station2=get_station_index(line3,destination)
            
            if station1 < station2:
             for i in range(station1,station2+1):
                 resolult.append(line3[i]['name']) 
            else:
             for i in range(station1,station2-1,-1):
                    resolult.append(line3[i]['name'])    
        return {"stations":resolult,"number of stations":len(resolult),"line":same_line,"money":str(check_money(resolult))+" Eg"}          
            # resolult=station2-station1                  
    else:
        station1=my_one_station_line(source)
        station2=my_one_station_line(destination)
        
                             ##############working with line 1 and line 2 #####################################3
        if (station1 == 'line1' and station2 =='line2') or (station1 == 'line2' and station2 =='line1'):
             if station1=='line2':
                source,destination = destination,source
             len1= abs(line1_and_line2[0]['line1_index']-get_station_index(line1,source))+abs(line1_and_line2[0]['line2_index']-get_station_index(line2,destination))
             len2= abs(line1_and_line2[1]['line1_index']-get_station_index(line1,source))+abs(line1_and_line2[1]['line2_index']-get_station_index(line2,destination))
             len3=abs(line1_and_line3[0]['line1_index']-get_station_index(line1,source))+abs(line1_and_line3[0]['line3_index']-line2_and_line3[0]['line3_index'])+abs(line2_and_line3[0]['line2_index']-get_station_index(line2,destination))
             
             print (len1)
             print (len2)
             print (len3)
             route=[]
             if 1:

                 if len1<len2 or len1==len2:
                    if get_station_index(line1,source)<line1_and_line2[0]['line1_index']:
                       for i in range(get_station_index(line1,source),line1_and_line2[0]['line1_index']+1):
                          route.append(line1[i]['name'])
                       if get_station_index(line2,destination)<line1_and_line2[0]['line2_index']:
                           for i in range(line1_and_line2[0]['line2_index']-1,get_station_index(line2,destination)-1,-1):
                              route.append(line2[i]['name'])
                       else:
                           for i in range(line1_and_line2[0]['line2_index']+1,get_station_index(line2,destination)+1):
                                  route.append(line2[i]['name'])
                           
                           
                    else:
                        for i in range(get_station_index(line1,source),line1_and_line2[0]['line1_index']-1,-1):
                            route.append(line1[i]['name'])
                        if get_station_index(line2,destination)<line1_and_line2[0]['line2_index']:
                           for i in range(line1_and_line2[0]['line2_index'],get_station_index(line2,destination)-1,-1):
                              route.append(line2[i]['name'])
                        else:
                               for i in range(line1_and_line2[0]['line2_index']+1,get_station_index(line2,destination)+1):
                                  route.append(line2[i]['name'])
                        
                 elif len2<len1 and len2<len3:
                     ##############################second line is smalllller#####################################
                    if get_station_index(line1,source)<line1_and_line2[1]['line1_index']:
                           for i in range(get_station_index(line1,source),line1_and_line2[1]['line1_index']+1):
                             route.append(line1[i]['name'])
                           if get_station_index(line2,destination)<line1_and_line2[1]['line2_index']:
                            for i in range(get_station_index(line2,destination),line1_and_line2[1]['line2_index']+1):
                              route.append(line2[i]['name'])
                           else:
                              for i in range(line1_and_line2[1]['line2_index']+1,get_station_index(line2,destination)+1):
                                  route.append(line2[i]['name'])
                           
                              
                    else:
                        for i in range(get_station_index(line1,source),line1_and_line2[1]['line1_index']-1,-1):
                            route.append(line1[i]['name'])
                        if get_station_index(line2,destination)<line1_and_line2[1]['line2_index']:
                           for i in range(line1_and_line2[1]['line2_index']-1,get_station_index(line2,destination)-1,-1):
                              route.append(line2[i]['name'])
                        else:
                               for i in range(line1_and_line2[1]['line2_index']+1,get_station_index(line2,destination)+1):
                                  route.append(line2[i]['name'])
                        print(route)    
                 if station1=='line2':
                    route2=[]
                    for i in range(len(route)-1,-1,-1):
                         route2.append(route[i])
                    route=route2

                
            #  else:
            #      if len3<len2 and len3<len1:
            #          if get_station_index(line1,source)<line1_and_line3[0]['line1_index']:
            #                 for i in range(get_station_index(line1,source),line1_and_line3[0]['line1_index']+1):
            #                   route.append(line1[i]['name'])
            #                 if line1_and_line3[0]["line3_index"]<line2_and_line3[0]['line3_index']:
            #                    for i in range(line1_and_line3[0]["line3_index"],line2_and_line3[0]['line3_index']):
            #                      route.append(line3[i]['name'])
            #                      route.append('ahmed')
            #                 else:
            #                     for i in range (line2_and_line3[0]['line3_index'], line1_and_line3[0]["line3_index"]-1,-1):
            #                         route.append(line3[i]['name'])
            #                         route.append('ahmed')
                                    
            #                 if get_station_index(line2,destination)<line2_and_line3[0]['line2_index']:
            #                    for i in range(line2_and_line3[0]['line2_index']-1,get_station_index(line2,destination)-1,-1):
            #                     route.append(line2[i]['name'])
            #                     route.append('ahmed')
            #                 else:
            #                    for i in range(line2_and_line3[0]['line2_index']+1,get_station_index(line2,destination)+1):
            #                         route.append(line2[i]['name'])
            #                         route.append('ahmed')
                              
                     
                    ##############working with line 2 and line 3 #####################################3
        elif (station1 == 'line2' and station2 =='line3') or (station1 == 'line3' and station2 =='line2'):
               if station1=='line3':
                    source,destination = destination,source
               len1= abs(line2_and_line3[0]['line2_index']-get_station_index(line2,source))+abs(line2_and_line3[0]['line3_index']-get_station_index(line3,destination))
               len2= abs(line1_and_line2[0]['line2_index']-get_station_index(line2,source))+abs(line1_and_line2[0]['line1_index']-line1_and_line3[0]['line1_index'])+abs(line1_and_line3[0]['line3_index']-get_station_index(line3,destination))
               len3= abs(line1_and_line2[1]['line2_index']-get_station_index(line2,source))+abs(line1_and_line2[1]['line1_index']-line1_and_line3[0]['line1_index'])+abs(line1_and_line3[0]['line3_index']-get_station_index(line3,destination))
               print(len1)
               print(len2)
               print(len3)
               route=[]
               if get_station_index(line2,source)<line2_and_line3[0]['line2_index']:
                       for i in range(get_station_index(line2,source),line2_and_line3[0]['line2_index']+1):
                          route.append(line2[i]['name'])
                       if get_station_index(line3,destination)<line1_and_line3[0]['line3_index']:
                           for i in range(line1_and_line3[0]['line3_index']-2,get_station_index(line3,destination)-1,-1):
                              route.append(line3[i]['name'])
                       else:
                           for i in range(line2_and_line3[0]['line2_index']+1,get_station_index(line3,destination)+1):
                                  route.append(line3[i]['name'])
                           
                         
               else:
                        for i in range(get_station_index(line2,source),line2_and_line3[0]['line2_index']-1,-1):
                            route.append(line2[i]['name'])
                        if get_station_index(line3,destination)<line2_and_line3[0]['line3_index']:
                           for i in range(line2_and_line3[0]['line3_index'],get_station_index(line3,destination)-1,-1):
                              route.append(line3[i]['name'])
                        else:
                               for i in range(line2_and_line3[0]['line3_index']+1,get_station_index(line3,destination)+1):
                                  route.append(line3[i]['name'])
                        
                         
               if station1=='line3':
                    route2=[]
                    for i in range(len(route)-1,-1,-1):
                         route2.append(route[i])
                    route=route2
                     ##############working with line 3 and line 1 #####################################3
        elif (station1 == 'line1' and station2 =='line3') or (station1 == 'line3' and station2 =='line1'):
            
               if station1=='line3':
                    source,destination = destination,source
               len1= abs(line1_and_line3[0]['line1_index']-get_station_index(line1,source))+abs(line1_and_line3[0]['line3_index']-get_station_index(line3,destination))
               len2=abs(line1_and_line2[0]['line1_index']-get_station_index(line1,source))+abs(line1_and_line2[0]['line2_index']-line2_and_line3[0]['line2_index'])+abs(line2_and_line3[0]['line2_index']-get_station_index(line3,destination))
               len3=abs(line1_and_line2[1]['line1_index']-get_station_index(line1,source))+abs(line1_and_line2[1]['line2_index']-line2_and_line3[0]['line2_index'])+abs(line2_and_line3[0]['line2_index']-get_station_index(line3,destination))
               print(len1)
               print(len2)
               print(len3)
               route=[]      
               if get_station_index(line1,source)<line1_and_line3[0]['line1_index']:
                       for i in range(get_station_index(line1,source),line1_and_line3[0]['line1_index']+1):
                          route.append(line1[i]['name'])
                       if get_station_index(line3,destination)<line1_and_line3[0]['line3_index']:
                           for i in range(line1_and_line3[0]['line3_index']-1,get_station_index(line3,destination)-1,-1):
                              route.append(line3[i]['name'])
                       else:
                           for i in range(line1_and_line3[0]['line1_index']+1,get_station_index(line3,destination)+1):
                                  route.append(line3[i]['name'])
                           
                         
               else:
                        for i in range(get_station_index(line1,source),line1_and_line3[0]['line1_index']-1,-1):
                            route.append(line1[i]['name'])
                        if get_station_index(line3,destination)<line1_and_line3[0]['line3_index']:
                           for i in range(line1_and_line3[0]['line3_index'],get_station_index(line3,destination)-1,-1):
                              route.append(line3[i]['name'])
                        else:
                               for i in range(line1_and_line3[0]['line3_index']+1,get_station_index(line3,destination)+1):
                                  route.append(line3[i]['name'])
                        
                         
               if station1=='line3':
                    route2=[]
                    for i in range(len(route)-1,-1,-1):
                         route2.append(route[i])
                    route=route2
            
        # print(station1)
        # print(station2)
        return {"stations":route,"number of stations":len(route),"money":str(check_money(route))+" Eg"} 

value=main_route('Omar Ibn El-Khattab','Helwan')
print(value) 

        
        
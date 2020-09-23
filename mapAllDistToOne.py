import pandas as pd

dict = {}

dict['name'] = ["mapping"]

#list1 = ["bishnupur/Q938190",
#"chandel/Q2301769",
#"churachandpur/Q2577281",
#"imphal_east/Q1916666",
#"imphal_west/Q1822188",
#"senapati/Q2301706",
#"tamenglong/Q2301717",
#"thoubal/Q2086198",
#"ukhrul/Q735101",
#"kangpokpi/Q28419386",
#"tengnoupal/Q28419388",
#"pherzawl/Q28173809",
#"noney/Q28419389",
#"kamjong/Q28419390",
#"jiribam/Q28419387",
#"kakching/Q28173825"]
#dict['manipur'] = list1

#list2 = ["south_sikkim_district/Q1805051",
#"west_sikkim_district/Q611357",
#"east_sikkim_district/Q1772832",
#"north_sikkim_district/Q1784149"]
#dict['sikkim'] = list2

list3 = ["mumbai_city/Q2341660",
"mumbai_suburban/Q2085374",
"konkan_division/Q6268840,mumbai"]   #This is for removal purpose
dict['mumbai'] = list3

list4 =  ["central_delhi/Q107941",
"east_delhi/Q107960",
"north_east_delhi/Q429329",
"north_delhi/Q693367",
"north_west_delhi/Q766125",
"west_delhi/Q549807",
"new_delhi/Q987",
"shahdara/Q83486",
"south_east_delhi/Q25553535",
"south_west_delhi/Q2379189",
"south_delhi/Q2061938"]
#"noklak/Q48731903"     #This is for removal purpose
dict['delhi'] = list4

list5 = ["north_goa/Q108234",
"south_goa/Q108244"]
dict['goa'] = list5

list6 = ["adilabad/Q15211",
"bhadradri_kothagudem/Q28169767",
"hyderabad/Q15340",
"jagtial/Q28169780",
"jangaon/Q28170170",
"jayashankar_bhupalapally/Q28169775",
"jogulamba_gadwal/Q27897618",
"kamareddy/Q27956125",
"karimnagar/Q15373",
"khammam/Q15371",
"komram_bheem/Q28170184",
"mahabubabad/Q28169761",
"mahabubnagar/Q15380",
"mancherial_district/Q28169747",
"medak/Q15386",
"medchal\u2013malkajgiri/Q27614841",
"nagarkurnool/Q28169773",
"nalgonda/Q15384",
"nirmal/Q28169750",
"nizamabad/Q15391",
"peddapalli/Q27614797",
"rajanna_sircilla/Q28172781",
"rangareddy/Q15388",
"sangareddy/Q28169753",
"siddipet/Q28169756",
"suryapet/Q28169770",
"vikarabad/Q28170173",
"wanaparthy/Q28172504",
"warangal_rural/Q28169759",
"warangal_urban/Q213077",
"mulugu/Q61746006",
"narayanpur/Q2322000",
"yadadri_bhuvanagiri/Q28169764"]

dict['telangana'] = list6

list7 = [
"baksa/Q2360266",
"barpeta/Q41249",
"bongaigaon/Q42197",
"cachar/Q42209",
"charaideo/Q24039029",
"chirang/Q2574898",
"darrang/Q42461",
"dhemaji/Q42473",
"dhubri/Q42485",
"dibrugarh/Q42479",
"dima_hasao_district/Q42774",
"goalpara/Q42522",
"golaghat/Q42517",
"hailakandi/Q42505",
"hojai/Q24699407",
"jorhat/Q42611",
"kamrup/Q2247441",
"kamrup_metropolitan/Q2464674",
"east_karbi_anglong/Q42558",
"karimganj/Q42542",
"kokrajhar/Q42618",
"lakhimpur/Q42743",
"majuli/Q28110729",
"nagaon/Q42686",
"nalbari/Q42779",
"sivasagar/Q42768",
"sonitpur/Q42765",
"south_salmara-mankachar/Q24907599",
"tinsukia/Q42756",
"udalguri/Q321998",
"west_karbi_anglong/Q24949218",
"bishwanath/Q28110722,assam",
"marigaon/Q42737,assam"
]

dict['assam'] = list7

listtofile = []

for i in dict.items():
    l = i[1]
    for j in l:
        tmp = []
        tmp.append(j)
        tmp.append(i[0])
        listtofile.append(tmp)

out = pd.DataFrame(listtofile)
out.to_csv('mapAllDictToOne.csv',index=False,header=False)
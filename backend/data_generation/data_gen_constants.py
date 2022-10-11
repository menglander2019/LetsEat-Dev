header = ['name', 'current_day', '+', '-', 'restrictions', 'occasion', 'num_people', 'meal', 'price_range', 'cuisine', 'Classy', 'Loud', 'Groups', 'Kids','Garage',
        'Street', 'WiFi','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','TV','Outdoor',
        'Dancing','Working','Smoking','Bike','Casual','Moderate','Breakfast','Lunch','Dinner','Dessert',
        'Brunch','Late','Trendy', 'Divey','Bar', 'ATTEND?']
        
data = [['Bob', 'italian,mexican', 'indian,american', 'vegan', 'italian'],
        ['Chuck', 'chinese,american', 'mexican,vietnamese', '', 'mexican']]

restrictions = ['vegan', 'vegetarian', 'gluten-free', 'kosher', 'pescatarian']

occasions = ['friends', 'date', 'family', 'work', 'solo']

days = ['M', 'T', 'W', 'R', 'F', 'SA', 'SU']

meals = ['breakfast', 'lunch', 'dinner', 'dessert']

price_ranges = ['$', '$$', '$$$', '$$$$']

num_rows = 500
num_pot_positives = 5
num_pot_negatives = 5

restriction_pct = 0.17

scraped_column_ct = 31

num_pot_people = 10

# list of all cuisine options on yelp (may need to be adjusted for what the API returns)
cuisines = """afghani
african
senegalese
southafrican
newamerican
tradamerican
arabian
argentine
armenian
asianfusion
australian
austrian
bangladeshi
bbq
basque
belgian
brasseries
brazilian
breakfast_brunch
pancakes
british
buffets
bulgarian
burgers
burmese
cafes
themedcafes
cafeteria
cajun
cambodian
caribbean
dominican
haitian
puertorican
trinidadian
catalan
cheesesteaks
chickenshop
chicken_wings
chinese
cantonese
dimsum
hainan
shanghainese
szechuan
comfortfood
creperies
cuban
czech
delis
diners
dinnertheater
eritrean
ethiopian
hotdogs
filipino
fishnchips
fondue
food_court
foodstands
french
mauritius
reunion
gamemeat
gastropubs
georgian
german
gluten_free
greek
guamanian
halal
hawaiian
himalayan
honduran
hkcafe
hotdog
hotpot
hungarian
iberian
indpak
indonesian
irish
italian
calabrian
sardinian
sicilian
tuscan
japanese
conveyorsushi
izakaya
japacurry
ramen
teppanyaki
kebab
korean
kosher
laotian
latin
colombian
salvadoran
venezuelan
raw_food
malaysian
mediterranean
falafel
mexican
tacos
mideastern
egyptian
lebanese
modern_european
mongolian
moroccan
newmexican
nicaraguan
noodles
pakistani
panasian
persian
peruvian
pizza
polish
polynesian
popuprestaurants
portuguese
poutineries
russian
salad
sandwiches
scandinavian
scottish
seafood
singaporean
slovakian
somali
soulfood
soup
southern
spanish
srilankan
steak
supperclubs
sushi
syrian
taiwanese
tapas
tapasmallplates
tex-mex
thai
turkish
ukrainian
uzbek
vegan
vegetarian
vietnamese
waffles
wraps"""
# cuisines = """Afghan (afghani)
# African (african)
# Senegalese (senegalese)
# South African (southafrican)
# American (New) (newamerican)
# American (Traditional) (tradamerican)
# Arabic (arabian)
# Argentine (argentine)
# Armenian (armenian)
# Asian Fusion (asianfusion)
# Australian (australian)
# Austrian (austrian)
# Bangladeshi (bangladeshi)
# Barbeque (bbq)
# Basque (basque)
# Belgian (belgian)
# Brasseries (brasseries)
# Brazilian (brazilian)
# Breakfast & Brunch (breakfast_brunch)
# Pancakes (pancakes)
# British (british)
# Buffets (buffets)
# Bulgarian (bulgarian)
# Burgers (burgers)
# Burmese (burmese)
# Cafes (cafes)
# Themed Cafes (themedcafes)
# Cafeteria (cafeteria)
# Cajun/Creole (cajun)
# Cambodian (cambodian)
# Caribbean (caribbean)
# Dominican (dominican)
# Haitian (haitian)
# Puerto Rican (puertorican)
# Trinidadian (trinidadian)
# Catalan (catalan)
# Cheesesteaks (cheesesteaks)
# Chicken Shop (chickenshop)
# Chicken Wings (chicken_wings)
# Chinese (chinese)
# Cantonese (cantonese)
# Dim Sum (dimsum)
# Hainan (hainan)
# Shanghainese (shanghainese)
# Szechuan (szechuan)
# Comfort Food (comfortfood)
# Creperies (creperies)
# Cuban (cuban)
# Czech (czech)
# Delis (delis)
# Diners (diners)
# Dinner Theater (dinnertheater)
# Eritrean (eritrean)
# Ethiopian (ethiopian)
# Fast Food (hotdogs)
# Filipino (filipino)
# Fish & Chips (fishnchips)
# Fondue (fondue)
# Food Court (food_court)
# Food Stands (foodstands)
# French (french)
# Mauritius (mauritius)
# Reunion (reunion)
# Game Meat (gamemeat)
# Gastropubs (gastropubs)
# Georgian (georgian)
# German (german)
# Gluten-Free (gluten_free)
# Greek (greek)
# Guamanian (guamanian)
# Halal (halal)
# Hawaiian (hawaiian)
# Himalayan/Nepalese (himalayan)
# Honduran (honduran)
# Hong Kong Style Cafe (hkcafe)
# Hot Dogs (hotdog)
# Hot Pot (hotpot)
# Hungarian (hungarian)
# Iberian (iberian)
# Indian (indpak)
# Indonesian (indonesian)
# Irish (irish)
# Italian (italian)
# Calabrian (calabrian)
# Sardinian (sardinian)
# Sicilian (sicilian)
# Tuscan (tuscan)
# Japanese (japanese)
# Conveyor Belt Sushi (conveyorsushi)
# Izakaya (izakaya)
# Japanese Curry (japacurry)
# Ramen (ramen)
# Teppanyaki (teppanyaki)
# Kebab (kebab)
# Korean (korean)
# Kosher (kosher)
# Laotian (laotian)
# Latin American (latin)
# Colombian (colombian)
# Salvadoran (salvadoran)
# Venezuelan (venezuelan)
# Live/Raw Food (raw_food)
# Malaysian (malaysian)
# Mediterranean (mediterranean)
# Falafel (falafel)
# Mexican (mexican)
# Tacos (tacos)
# Middle Eastern (mideastern)
# Egyptian (egyptian)
# Lebanese (lebanese)
# Modern European (modern_european)
# Mongolian (mongolian)
# Moroccan (moroccan)
# New Mexican Cuisine (newmexican)
# Nicaraguan (nicaraguan)
# Noodles (noodles)
# Pakistani (pakistani)
# Pan Asian (panasian)
# Persian/Iranian (persian)
# Peruvian (peruvian)
# Pizza (pizza)
# Polish (polish)
# Polynesian (polynesian)
# Pop-Up Restaurants (popuprestaurants)
# Portuguese (portuguese)
# Poutineries (poutineries)
# Russian (russian)
# Salad (salad)
# Sandwiches (sandwiches)
# Scandinavian (scandinavian)
# Scottish (scottish)
# Seafood (seafood)
# Singaporean (singaporean)
# Slovakian (slovakian)
# Somali (somali)
# Soul Food (soulfood)
# Soup (soup)
# Southern (southern)
# Spanish (spanish)
# Sri Lankan (srilankan)
# Steakhouses (steak)
# Supper Clubs (supperclubs)
# Sushi Bars (sushi)
# Syrian (syrian)
# Taiwanese (taiwanese)
# Tapas Bars (tapas)
# Tapas/Small Plates (tapasmallplates)
# Tex-Mex (tex-mex)
# Thai (thai)
# Turkish (turkish)
# Ukrainian (ukrainian)
# Uzbek (uzbek)
# Vegan (vegan)
# Vegetarian (vegetarian)
# Vietnamese (vietnamese)
# Waffles (waffles)
# Wraps (wraps)"""
header = [
        'name', 'current_day', 'middle_eastern', 'african', 'american', 'mexican', 'latin_american', 'italian', 'chinese', 
        'japanese', 'southern_central_asian', 'french', 'eastern_europe', 'central_europe', 'caribbean', 'mediterranean', 'indian', 
        'spanish', 'kosher', 'gluten_free', 'wheelchair', 'vegan', 'vegetarian', 'pescatarian', 'keto', 'soy', 'dog', 'covid', 'occasion', 
        'num_people', 'meal', '$', '$$', '$$$', '$$$$', 'rating', 'rest_middle_eastern', 'rest_african', 'rest_american', 
        'rest_mexican', 'rest_latin_american', 'rest_italian', 'rest_chinese', 'rest_japanese', 'rest_southern_central_asian',
        'rest_french', 'rest_eastern_europe', 'rest_central_europe', 'rest_caribbean', 'rest_mediterranean', 'rest_indian', 'rest_spanish',
        'rest_kosher', 'rest_gluten_free', 'rest_$', 'rest_$$', 'rest_$$$', 'rest_$$$$', 'pickup', 'delivery', 'restaurant_reservation',
        'Classy', 'Loud', 'Hipster', 'Groups', 'Kids','Garage', 'Street', 'Valet', 'Validated', 'WiFi','Monday','Tuesday','Wednesday',
        'Thursday','Friday','Saturday','Sunday','TV', 'Waiter', 'Outdoor','Dancing','Working','Smoking','Bike','Casual', 'Intimate',
        'Upscale', 'Moderate', 'Quiet', 'Breakfast','Lunch','Dinner','Dessert','Brunch','Late','Trendy', 'Divey','Bar', 'Catering', 
        'Plastic', 'reusable', 'staffMasks', 'staffVac', 'vaccination', 'Compostable', 'rest_wheelchair', 'rest_vegan', 
        'rest_vegetarian', 'rest_gluten', 'rest_pescatarian', 'rest_keto', 'rest_soy', 'rest_dogs', 'rest_women', 'rest_military', 'Gender', 'ATTEND?'
]
        
data = [['Bob', 'italian,mexican', 'indian,american', 'vegan', 'italian'],
        ['Chuck', 'chinese,american', 'mexican,vietnamese', '', 'mexican']]

restrictions = ['vegan', 'vegetarian', 'gluten-free', 'kosher']
restrictions_dict = {
    'Vegan': 'vegan',
    'Vegetarian': 'vegetarian',
    'Gluten Free': 'gluten-free',
    'Kosher': 'kosher'
}

occasions = ['Myself', 'Friend', 'Date', 'Family', 'Work']

days = ['M', 'T', 'W', 'R', 'F', 'SA', 'SU']

num_people = ['1', '2', '3', '4+']


meals = ['Breakfast', 'Lunch', 'Dinner', 'Dessert']

price_ranges = ['$', '$$', '$$$', '$$$$']

num_rows = 20
num_pot_positives = 8
num_pot_negatives = 8
num_umbrella_terms = 16

restriction_pct = 0.17

scraped_column_ct = 56

num_pot_people = 10

middle_eastern = ['afghani', 'arabian', 'mideastern', 'halal', 'kebab', 'kosher', 'falafel', 'lebanese', 'persian', 'syrian', 'pakistani']
african = ['african', 'senegalese', 'southafrican', 'eritrean', 'ethiopian', 'egyptian', 'moroccan', 'somali']
american = ['newamerican', 'tradamerican', 'hawaiian', 'bbq', 'burgers', 'diners', 'cajun', 'cheesesteaks', 'chickenshop', 'chicken_wings', 'comfortfood', 'delis', 'diners', 'hotdogs', 'food_court', 'hotdog', 'soulfood', 'southern', 'steak', 'tex-mex']
mexican = ['mexican', 'tacos', 'newmexican']
latin_american = ['honduran', 'peruvian', 'venezuelan', 'salvadoran', 'colombian', 'argentine', 'latin', 'brazilian', 'nicaraguan']
italian = ['italian', 'pizza', 'calabrian', 'sardinian', 'sicilian', 'tuscan']
chinese = ['cantonese', 'chinese', 'dimsum', 'asianfusion', 'hainan', 'shanghainese', 'szechuan', 'hkcafe', 'noodles', 'hotpot', 'taiwanese']
japanese = ['japanese', 'conveyorsushi', 'izakaya', 'asianfusion', 'japacurry', 'ramen', 'teppanyaki', 'sushi']
southern_central_asian = ['bangladeshi', 'uzbek', 'mongolian', 'asianfusion', 'cambodian', 'filipino', 'indonesian', 'korean', 'laotian', 'malaysian', 'singaporean', 'thai', 'vietnamese']
french = ['brasseries', 'creperies', 'french', 'reunion']
eastern_europe = ['bulgarian', 'burmese', 'georgian', 'russian', 'slovakian', 'turkish', 'ukrainian']
central_europe = ['austrian', 'scandinavian', 'belgian', 'czech', 'german', 'hungarian', 'polish', 'modern_european']
caribbean = ['dominican', 'haitian', 'puertorican', 'trinidadian', 'caribbean', 'cuban']
mediterranean = ['mediterranean', 'greek', 'armenian']
# oceania = ['guamanian', 'australian', 'polynesian']
indian = ['himalayan', 'indpak', 'srilankan']
# united_kingdom = ['scottish', 'irish', 'british', 'fishnchips']
spanish = ['tapas', 'tapasmallplates', 'portuguese', 'spanish', 'catalan']

restaurant_types = {
        'middle_eastern': middle_eastern, 
        'african': african, 
        'american': american, 
        'mexican': mexican, 
        'latin_american': latin_american, 
        'italian': italian, 
        'chinese': chinese, 
        'japanese': japanese, 
        'southern_central_asian': southern_central_asian, 
        'french': french, 
        'eastern_europe': eastern_europe, 
        'central_europe': central_europe, 
        'caribbean': caribbean, 
        'mediterranean': mediterranean, 
        'indian': indian, 
        'spanish': spanish
}

cuisine_groups = {
    "Middle Eastern": 'middle_eastern', 
    "African": 'african', 
    "American": 'american', 
    "Mexican": 'mexican', 
    "Latin American": 'latin_american', 
    "Italian": 'italian', 
    "Chinese": 'chinese', 
    "Japanese": 'japanese', 
    "Southern / Central Asian": 'southern_central_asian', 
    "French": 'french', 
    "Eastern European": 'eastern_europe', 
    "Central European": 'central_europe', 
    "Caribbean": 'caribbean', 
    "Mediterranean": 'mediterranean', 
    "Indian": 'indian', 
    "Spanish": 'spanish'
}
 

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
# Basque (basque)
# Breakfast & Brunch (breakfast_brunch)
# Pancakes (pancakes)
# Buffets (buffets)
# Cafes (cafes)
# Themed Cafes (themedcafes)
# Cafeteria (cafeteria)
# Dinner Theater (dinnertheater)
# Game Meat (gamemeat)
# Gastropubs (gastropubs)
# Gluten-Free (gluten_free)
# Iberian (iberian)
# Live/Raw Food (raw_food)
# Pop-Up Restaurants (popuprestaurants)
# Salad (salad)
# Sandwiches (sandwiches)
# Seafood (seafood)
# Soup (soup)
# Supper Clubs (supperclubs)
# Vegan (vegan)
# Vegetarian (vegetarian)
# Waffles (waffles)
# Wraps (wraps)"""
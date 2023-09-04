import math
import json

locations = [
    {"name": "Volchiypik", "latitude": 300, "longitude": 2242},
    {"name": "Kamenka", "latitude": 1942, "longitude": 2242},
    {"name": "Kamenka Military Base", "latitude": 2096, "longitude": 3326},
    {"name": "Pavlovo", "latitude": 1702, "longitude": 3825},
    {"name": "Bor", "latitude": 3315, "longitude": 3982},
    {"name": "Komarovo", "latitude": 3663, "longitude": 2482},
    {"name": "Balota", "latitude": 4492, "longitude": 2445},
    {"name": "Balota Airfield", "latitude": 4957, "longitude": 2456},
    {"name": "Vysotovo", "latitude": 5782, "longitude": 2553},
    {"name": "Novoselki", "latitude": 6217, "longitude": 3277},
    {"name": "Dubovo", "latitude": 6723, "longitude": 3630},
    {"name": "Chernogorsk", "latitude": 6472, "longitude": 2568},
    {"name": "Prigorodki", "latitude": 7732, "longitude": 3288},
    {"name": "Pusta", "latitude": 9157, "longitude": 3858},
    {"name": "Kometa", "latitude": 10338, "longitude": 3562},
    {"name": "Elektozavodsk", "latitude": 10196, "longitude": 2130},
    {"name": "Rog", "latitude": 11250, "longitude": 4293},
    {"name": "Tulga", "latitude": 12720, "longitude": 4398},
    {"name": "Kamyshovo", "latitude": 12067, "longitude": 3517},
    {"name": "Voron", "latitude": 13455, "longitude": 3292},
    {"name": "Skalisty", "latitude": 13665, "longitude": 3026},
    {"name": "Zvir", "latitude": 551, "longitude": 5358},
    {"name": "Metalurg", "latitude": 1076, "longitude": 6630},
    {"name": "Sosnovka", "latitude": 2523, "longitude": 6375},
    {"name": "Zelenogorsk", "latitude": 2752, "longitude": 5276},
    {"name": "Zelenogorsk Military Base", "latitude": 2482, "longitude": 5167},
    {"name": "Pogorevka", "latitude": 4451, "longitude": 6427},
    {"name": "Rogovo", "latitude": 4766, "longitude": 6791},
    {"name": "Pulkovo", "latitude": 4942, "longitude": 5696},
    {"name": "Kozlovka", "latitude": 4376, "longitude": 4687},
    {"name": "Nadezhdino", "latitude": 5853, "longitude": 4803},
    {"name": "Vyhnoye", "latitude": 6570, "longitude": 6060},
    {"name": "Zub", "latitude": 6547, "longitude": 5583},
    {"name": "Nadezhda", "latitude": 7248, "longitude": 7008},
    {"name": "Mogilevka", "latitude": 7556, "longitude": 5163},
    {"name": "Kumyrna", "latitude": 8396, "longitude": 5985},
    {"name": "Simurg", "latitude": 228, "longitude": 7512},
    {"name": "Simurg Military Warehouse", "latitude": 975, "longitude": 7638},
    {"name": "Simurg Military Barracks", "latitude": 1166, "longitude": 7233},
    {"name": "Tri Kresta", "latitude": 333, "longitude": 9367},
    {"name": "Galkino", "latitude": 1203, "longitude": 8793},
    {"name": "Kroma", "latitude": 1436, "longitude": 9217},
    {"name": "Bogatyvka", "latitude": 1563, "longitude": 8959},
    {"name": "Myshino", "latitude": 1972, "longitude": 7342},
    {"name": "Vybor", "latitude": 3840, "longitude": 8921},
    {"name": "Pustoska", "latitude": 3071, "longitude": 7912},
    {"name": "Vybor Military Base", "latitude": 4440, "longitude": 8302},
    {"name": "Rogovo", "latitude": 4770, "longitude": 6761},
    {"name": "Kabanlino", "latitude": 5328, "longitude": 8617},
    {"name": "Stary Sobor", "latitude": 6075, "longitude": 7758},
    {"name": "Gnomovzamok", "latitude": 7391, "longitude": 9078},
    {"name": "Novy Sobor", "latitude": 7102, "longitude": 7668},
    {"name": "Nadezhda", "latitude": 7241, "longitude": 6975},
    {"name": "Gaglovo", "latitude": 8433, "longitude": 6652},
    {"name": "Radio Zenit", "latitude": 8107, "longitude": 9330},
    {"name": "Altar", "latitude": 8148, "longitude": 9120},
    {"name": "Guglovo", "latitude": 8433, "longitude": 6630},
    {"name": "Shakovka", "latitude": 9622, "longitude": 6555},
    {"name": "Staroye", "latitude": 10128, "longitude": 5433},
    {"name": "Msta", "latitude": 11321, "longitude": 5486},
    {"name": "Dolina", "latitude": 11305, "longitude": 6600},
    {"name": "Solinechny", "latitude": 13395, "longitude": 6240},
    {"name": "Gorka", "latitude": 9558, "longitude": 8823},
    {"name": "Polyana", "latitude": 10672, "longitude": 8100},
    {"name": "Youth Pioneer", "latitude": 11137, "longitude": 7027},
    {"name": "Orlovets", "latitude": 12176, "longitude": 7297},
    {"name": "Nizhnee", "latitude": 12993, "longitude": 8055},
    {"name": "Skyatoy Roman", "latitude": 225, "longitude": 11880},
    {"name": "Skvsoh Biathlon Arena", "latitude": 502, "longitude": 11081},
    {"name": "Zabolotye", "latitude": 1245, "longitude": 9956},
    {"name": "Sinystok", "latitude": 1511, "longitude": 11970},
    {"name": "Vavilovo", "latitude": 2227, "longitude": 11058},
    {"name": "Lopatino", "latitude": 2760, "longitude": 9963},
    {"name": "North West Airfield", "latitude": 4556, "longitude": 10237},
    {"name": "Baghnya", "latitude": 4020, "longitude": 11730},
    {"name": "Grishino", "latitude": 5966, "longitude": 10323},
    {"name": "Chortovzamok", "latitude": 6907, "longitude": 11456},
    {"name": "Romashka", "latitude": 8163, "longitude": 11036},
    {"name": "Gvozdno", "latitude": 9926, "longitude": 10421},
    {"name": "Verkhnaya Dubrovka", "latitude": 10428, "longitude": 9862},
    {"name": "Dubrovka", "latitude": 11550, "longitude": 10646},
    {"name": "Druzbha", "latitude": 12341, "longitude": 9671},
    {"name": "Berzino", "latitude": 12315, "longitude": 10882},
    {"name": "Whelm", "latitude": 10263, "longitude": 12026},
    {"name": "Chernayasora Zolotar", "latitude": 13837, "longitude": 11216},
    {"name": "Rify", "latitude": 1556, "longitude": 14107},
    {"name": "Vidy Military", "latitude": 2850, "longitude": 12390},
    {"name": "Topolniki", "latitude": 3416, "longitude": 13012},
    {"name": "Novaya Detrovka", "latitude": 3693, "longitude": 14868},
    {"name": "Pobeda", "latitude": 3446, "longitude": 14778},
    {"name": "Tisy", "latitude": 5013, "longitude": 12806},
    {"name": "Zaprudnoye", "latitude": 6288, "longitude": 12701},
    {"name": "Ratnoye", "latitude": 5827, "longitude": 13530},
    {"name": "Polesovo", "latitude": 5696, "longitude": 14422},
    {"name": "Skalka", "latitude": 6641, "longitude": 14467},
    {"name": "Kamensk", "latitude": 4980, "longitude": 15093},
    {"name": "Stary Yar", "latitude": 7860, "longitude": 14662},
    {"name": "Kavhensk Military Base", "latitude": 7582, "longitude": 13537},
    {"name": "Kalinovka", "latitude": 7983, "longitude": 12746},
    {"name": "Severograd", "latitude": 8482, "longitude": 13935},
    {"name": "Arsenovo", "latitude": 9348, "longitude": 14568},
    {"name": "Nagornoye", "latitude": 9510, "longitude": 14568},
    {"name": "Svergino", "latitude": 11148, "longitude": 12277},
    {"name": "Karasnostav", "latitude": 11985, "longitude": 12510},
    {"name": "Krasnostar Airfield", "latitude": 11437, "longitude": 14298},
    {"name": "Kovodmitrovsk", "latitude": 12135, "longitude": 13755},
    {"name": "Chernay Dolyana", "latitude": 12675, "longitude": 14595},
    {"name": "Karmanovka", "latitude": 12971, "longitude": 15037},
    {"name": "Dobroye", "latitude": 14096, "longitude": 15037},
    {"name": "Belaya Dolyana", "latitude": 13571, "longitude": 14006},
    {"name": "Turovo", "latitude": 13308, "longitude": 12956},
    {"name": "Olsha", "latitude": 14051, "longitude": 13226},
    {"name": "Svetloyarsk", "latitude": 15112, "longitude": 13845},
    {"name": "Berezhki", "latitude": 0, "longitude": 0},  # Add your data for Berezhki
]

templates = [
    ""
]

class Build:
   
    def __init__(self, name, x, y, location, location_data, hat, mask, glasses, shirt, vest, gloves, pants, shoes, amount, _hat, _mask, _glasses, _shirt, _vest, _gloves, _pants, _shoes):
        self.name = name
        self.x = x
        self.y = y
        self.location = location
        self.location_data = location_data
        self.template = list(templates)
        self.hat = hat
        self.mask = mask
        self.glasses = glasses
        self.shirt = shirt
        self.vest = vest
        self.gloves = gloves
        self.pants = pants
        self.shoes = shoes
        self.amount = amount
        self._hat = list(_hat)
        self._mask = list(_mask)
        self._glasses = list(_glasses)
        self._shirt = list(_shirt)
        self._vest = list(_vest)
        self._gloves = list(_gloves)
        self._pants = list(_pants)
        self._shoes = list(_shoes)
        
        Build._hat = []
        Build._mask = []
        Build._glasses = []
        Build._shirt = []
        Build._vest = []
        Build._gloves = []
        Build._pants = []
        Build._shoes = []
    
    def data_validation(self, name, x, y, template, hat, mask, glasses, shirt, vest, gloves, pants, shoes, amount):
        if not isinstance(name, str):
            return "Name should be text."
        if not isinstance(x, int):
            return "x coordinate should be number."
        if not isinstance(y, int):
            return "y coordinate should be number."
        if not isinstance(template, str) or (template is not None and template not in templates):
            return "Template should be text."
        if not isinstance(hat, str) or (hat is not None and hat not in Build._hats):
            return "Hat should be text OR hat is not valid."
        if not isinstance(mask, str) or (mask is not None and mask not in Build._masks):
            return "Mask should be text OR mask is not valid."
        if not isinstance(glasses, str) or (glasses is not None and glasses not in Build._glasses):
            return "Glasses should be text OR glasses is not valid."
        if not isinstance(shirt, str) or (shirt is not None and shirt not in Build._shirts):
            return "Shirt should be text OR shirt is not valid."
        if not isinstance(vest, str) or (vest is not None and vest not in Build._vest):
            return "Vest should be text OR vest is not valid."
        if not isinstance(gloves, str) or (gloves is not None and gloves not in Build._gloves):
            return "Gloves should be text OR gloves is not valid."
        if not isinstance(pants, str) or (pants is not None and pants not in Build._pants):
            return "Pants should be text OR pants is not valid."
        if not isinstance(shoes, str) or (shoes is not None and shoes not in Build._shoes):
            return "Shoes should be text OR shoes is not valid."
        if not isinstance(amount, int) or (amount is not None):
            return "Amount has to be zero OR it has to be a whole number."
    
    def dictionary():
        pass
        
    
    def haversine(self, lat1, lon1, lat2, lon2):
        # Convert latitude and longitude from degrees to radians
        lat1 = math.radians(lat1)
        lon1 = math.radians(lon1)
        lat2 = math.radians(lat2)
        lon2 = math.radians(lon2)

        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        radius_of_earth = 6371  # Earth's radius in kilometers
        distance = radius_of_earth * c

        return distance

    def find_closest_location(self, x, y, location_data):
        closest_location = None
        closest_distance = float('inf')

        if x + y == 0:
            # Invalid Input
            print(f"{x},{y} are not valid inputs.")
            return None
        else:
            for location in location_data:
                distance = Build.haversine(Build, x, y, location["latitude"], location["longitude"])
                if distance < closest_distance:
                    closest_distance = distance
                    closest_location = location["name"]

        return closest_location
    
    def template(self, location):
        pass
"""


2026 Winter Games Day 1: Opening Day
Today marks the start of the 2026 Winter Games. The next 17 days will bring you coding challenges inspired by them.

For the first one, you are given a two-letter country code and need to return the flag emoji for that country.

Use this list:

Country	Code	Flag
Albania	"AL"	"🇦🇱"
Andorra	"AD"	"🇦🇩"
Argentina	"AR"	"🇦🇷"
Armenia	"AM"	"🇦🇲"
Australia	"AU"	"🇦🇺"
Austria	"AT"	"🇦🇹"
Azerbaijan	"AZ"	"🇦🇿"
Belgium	"BE"	"🇧🇪"
Benin	"BJ"	"🇧🇯"
Bolivia	"BO"	"🇧🇴"
Bosnia and Herzegovina	"BA"	"🇧🇦"
Brazil	"BR"	"🇧🇷"
Bulgaria	"BG"	"🇧🇬"
Canada	"CA"	"🇨🇦"
Chile	"CL"	"🇨🇱"
China	"CN"	"🇨🇳"
Colombia	"CO"	"🇨🇴"
Croatia	"HR"	"🇭🇷"
Cyprus	"CY"	"🇨🇾"
Czech Republic	"CZ"	"🇨🇿"
Denmark	"DK"	"🇩🇰"
Ecuador	"EC"	"🇪🇨"
Eritrea	"ER"	"🇪🇷"
Estonia	"EE"	"🇪🇪"
Finland	"FI"	"🇫🇮"
France	"FR"	"🇫🇷"
Georgia	"GE"	"🇬🇪"
Germany	"DE"	"🇩🇪"
Great Britain	"GB"	"🇬🇧"
Greece	"GR"	"🇬🇷"
Guinea-Bissau	"GW"	"🇬🇼"
Haiti	"HT"	"🇭🇹"
Hong Kong	"HK"	"🇭🇰"
Hungary	"HU"	"🇭🇺"
Iceland	"IS"	"🇮🇸"
India	"IN"	"🇮🇳"
Iran	"IR"	"🇮🇷"
Ireland	"IE"	"🇮🇪"
Israel	"IL"	"🇮🇱"
Italy	"IT"	"🇮🇹"
Jamaica	"JM"	"🇯🇲"
Japan	"JP"	"🇯🇵"
Kazakhstan	"KZ"	"🇰🇿"
Kenya	"KE"	"🇰🇪"
Kosovo	"XK"	"🇽🇰"
Kyrgyzstan	"KG"	"🇰🇬"
Latvia	"LV"	"🇱🇻"
Lebanon	"LB"	"🇱🇧"
Liechtenstein	"LI"	"🇱🇮"
Lithuania	"LT"	"🇱🇹"
Luxembourg	"LU"	"🇱🇺"
Madagascar	"MG"	"🇲🇬"
Malaysia	"MY"	"🇲🇾"
Malta	"MT"	"🇲🇹"
Mexico	"MX"	"🇲🇽"
Moldova	"MD"	"🇲🇩"
Monaco	"MC"	"🇲🇨"
Mongolia	"MN"	"🇲🇳"
Montenegro	"ME"	"🇲🇪"
Morocco	"MA"	"🇲🇦"
Netherlands	"NL"	"🇳🇱"
New Zealand	"NZ"	"🇳🇿"
Nigeria	"NG"	"🇳🇬"
North Macedonia	"MK"	"🇲🇰"
Norway	"NO"	"🇳🇴"
Pakistan	"PK"	"🇵🇰"
Philippines	"PH"	"🇵🇭"
Poland	"PL"	"🇵🇱"
Portugal	"PT"	"🇵🇹"
Puerto Rico	"PR"	"🇵🇷"
Romania	"RO"	"🇷🇴"
San Marino	"SM"	"🇸🇲"
Saudi Arabia	"SA"	"🇸🇦"
Serbia	"RS"	"🇷🇸"
Singapore	"SG"	"🇸🇬"
Slovakia	"SK"	"🇸🇰"
Slovenia	"SI"	"🇸🇮"
South Africa	"ZA"	"🇿🇦"
South Korea	"KR"	"🇰🇷"
Spain	"ES"	"🇪🇸"
Sweden	"SE"	"🇸🇪"
Switzerland	"CH"	"🇨🇭"
Thailand	"TH"	"🇹🇭"
Trinidad & Tobago	"TT"	"🇹🇹"
Turkey	"TR"	"🇹🇷"
Ukraine	"UA"	"🇺🇦"
United Arab Emirates	"AE"	"🇦🇪"
United States	"US"	"🇺🇸"
Uruguay	"UY"	"🇺🇾"
Uzbekistan	"UZ"	"🇺🇿"
Venezuela	"VE"	"🇻🇪"

"""


import unittest

class CountryCodeTest(unittest.TestCase):
     
    def test1(self):
          self.assertEqual(getFlag("AD"), "🇦🇩")

    def test2(self):
          self.assertEqual(getFlag("AR"), "🇦🇷")

    def test3(self):
          self.assertEqual(getFlag("AM"), "🇦🇲")

    def test4(self):
          self.assertEqual(getFlag("AU"), "🇦🇺")

    def test5(self):
          self.assertEqual(getFlag("AT"), "🇦🇹")

    def test6(self):
          self.assertEqual(getFlag("AZ"), "🇦🇿")

    def test7(self):
          self.assertEqual(getFlag("BE"), "🇧🇪")

    def test8(self):
          self.assertEqual(getFlag("BJ"), "🇧🇯")

    def test9(self):
          self.assertEqual(getFlag("BO"), "🇧🇴")

    def test10(self):
          self.assertEqual(getFlag("BA"), "🇧🇦")

    def test11(self):
          self.assertEqual(getFlag("BR"), "🇧🇷")

    def test12(self):
          self.assertEqual(getFlag("BG"), "🇧🇬")

    def test13(self):
          self.assertEqual(getFlag("CA"), "🇨🇦")

    def test14(self):
          self.assertEqual(getFlag("CL"), "🇨🇱")

    def test15(self):
          self.assertEqual(getFlag("CN"), "🇨🇳")

    def test16(self):
          self.assertEqual(getFlag("CO"), "🇨🇴")

    def test17(self):
          self.assertEqual(getFlag("HR"), "🇭🇷")

    def test18(self):
          self.assertEqual(getFlag("CY"), "🇨🇾")

    def test19(self):
          self.assertEqual(getFlag("CZ"), "🇨🇿")

    def test20(self):
          self.assertEqual(getFlag("DK"), "🇩🇰")

    def test21(self):
          self.assertEqual(getFlag("EC"), "🇪🇨")

    def test22(self):
          self.assertEqual(getFlag("ER"), "🇪🇷")

    def test23(self):
          self.assertEqual(getFlag("EE"), "🇪🇪")

    def test24(self):
          self.assertEqual(getFlag("FI"), "🇫🇮")

    def test25(self):
          self.assertEqual(getFlag("FR"), "🇫🇷")

    def test26(self):
          self.assertEqual(getFlag("GE"), "🇬🇪")

    def test27(self):
          self.assertEqual(getFlag("DE"), "🇩🇪")

    def test28(self):
          self.assertEqual(getFlag("GB"), "🇬🇧")

    def test29(self):
          self.assertEqual(getFlag("GR"), "🇬🇷")

    def test30(self):
          self.assertEqual(getFlag("GW"), "🇬🇼")

    def test31(self):
          self.assertEqual(getFlag("HT"), "🇭🇹")

    def test32(self):
          self.assertEqual(getFlag("HK"), "🇭🇰")

    def test33(self):
          self.assertEqual(getFlag("HU"), "🇭🇺")

    def test34(self):
          self.assertEqual(getFlag("IS"), "🇮🇸")

    def test35(self):
          self.assertEqual(getFlag("IN"), "🇮🇳")

    def test36(self):
          self.assertEqual(getFlag("IR"), "🇮🇷")

    def test37(self):
          self.assertEqual(getFlag("IE"), "🇮🇪")

    def test38(self):
          self.assertEqual(getFlag("IL"), "🇮🇱")

    def test39(self):
          self.assertEqual(getFlag("IT"), "🇮🇹")

    def test40(self):
          self.assertEqual(getFlag("JM"), "🇯🇲")

    def test41(self):
          self.assertEqual(getFlag("JP"), "🇯🇵")

    def test42(self):
          self.assertEqual(getFlag("KZ"), "🇰🇿")

    def test43(self):
          self.assertEqual(getFlag("KE"), "🇰🇪")

    def test44(self):
          self.assertEqual(getFlag("XK"), "🇽🇰")

    def test45(self):
          self.assertEqual(getFlag("KG"), "🇰🇬")

    def test46(self):
          self.assertEqual(getFlag("LV"), "🇱🇻")

    def test47(self):
          self.assertEqual(getFlag("LB"), "🇱🇧")

    def test48(self):
          self.assertEqual(getFlag("LI"), "🇱🇮")

    def test49(self):
          self.assertEqual(getFlag("LT"), "🇱🇹")

    def test50(self):
          self.assertEqual(getFlag("LU"), "🇱🇺")

    def test51(self):
          self.assertEqual(getFlag("MG"), "🇲🇬")

    def test52(self):
          self.assertEqual(getFlag("MY"), "🇲🇾")

    def test53(self):
          self.assertEqual(getFlag("MT"), "🇲🇹")

    def test54(self):
          self.assertEqual(getFlag("MX"), "🇲🇽")

    def test55(self):
          self.assertEqual(getFlag("MD"), "🇲🇩")

    def test56(self):
          self.assertEqual(getFlag("MC"), "🇲🇨")

    def test57(self):
          self.assertEqual(getFlag("MN"), "🇲🇳")

    def test58(self):
          self.assertEqual(getFlag("ME"), "🇲🇪")

    def test59(self):
          self.assertEqual(getFlag("MA"), "🇲🇦")

    def test60(self):
          self.assertEqual(getFlag("NL"), "🇳🇱")

    def test61(self):
          self.assertEqual(getFlag("NZ"), "🇳🇿")

    def test62(self):
          self.assertEqual(getFlag("NG"), "🇳🇬")

    def test63(self):
          self.assertEqual(getFlag("MK"), "🇲🇰")

    def test64(self):
          self.assertEqual(getFlag("NO"), "🇳🇴")

    def test65(self):
          self.assertEqual(getFlag("PK"), "🇵🇰")

    def test66(self):
          self.assertEqual(getFlag("PH"), "🇵🇭")

    def test67(self):
          self.assertEqual(getFlag("PL"), "🇵🇱")

    def test68(self):
          self.assertEqual(getFlag("PT"), "🇵🇹")

    def test69(self):
          self.assertEqual(getFlag("PR"), "🇵🇷")

    def test70(self):
          self.assertEqual(getFlag("RO"), "🇷🇴")

    def test71(self):
          self.assertEqual(getFlag("SM"), "🇸🇲")

    def test72(self):
          self.assertEqual(getFlag("SA"), "🇸🇦")

    def test73(self):
          self.assertEqual(getFlag("RS"), "🇷🇸")

    def test74(self):
          self.assertEqual(getFlag("SG"), "🇸🇬")

    def test75(self):
          self.assertEqual(getFlag("SK"), "🇸🇰")

    def test76(self):
          self.assertEqual(getFlag("SI"), "🇸🇮")

    def test77(self):
          self.assertEqual(getFlag("ZA"), "🇿🇦")

    def test78(self):
          self.assertEqual(getFlag("KR"), "🇰🇷")

    def test79(self):
          self.assertEqual(getFlag("ES"), "🇪🇸")

    def test80(self):
          self.assertEqual(getFlag("SE"), "🇸🇪")

    def test81(self):
          self.assertEqual(getFlag("CH"), "🇨🇭")

    def test82(self):
          self.assertEqual(getFlag("TH"), "🇹🇭")

    def test83(self):
          self.assertEqual(getFlag("TT"), "🇹🇹")

    def test84(self):
          self.assertEqual(getFlag("TR"), "🇹🇷")

    def test85(self):
          self.assertEqual(getFlag("UA"), "🇺🇦")

    def test86(self):
          self.assertEqual(getFlag("AE"), "🇦🇪")

    def test87(self):
          self.assertEqual(getFlag("US"), "🇺🇸")

    def test88(self):
          self.assertEqual(getFlag("UY"), "🇺🇾")

    def test89(self):
          self.assertEqual(getFlag("UZ"), "🇺🇿")

    def test90(self):
          self.assertEqual(getFlag("VE"), "🇻🇪")
    

def getFlag(code):
      

    countries = {
        "Albania": ("AL", "🇦🇱"),
        "Andorra": ("AD", "🇦🇩"),
        "Argentina": ("AR", "🇦🇷"),
        "Armenia": ("AM", "🇦🇲"),
        "Australia": ("AU", "🇦🇺"),
        "Austria": ("AT", "🇦🇹"),
        "Azerbaijan": ("AZ", "🇦🇿"),
        "Belgium": ("BE", "🇧🇪"),
        "Benin": ("BJ", "🇧🇯"),
        "Bolivia": ("BO", "🇧🇴"),
        "Bosnia and Herzegovina": ("BA", "🇧🇦"),
        "Brazil": ("BR", "🇧🇷"),
        "Bulgaria": ("BG", "🇧🇬"),
        "Canada": ("CA", "🇨🇦"),
        "Chile": ("CL", "🇨🇱"),
        "China": ("CN", "🇨🇳"),
        "Colombia": ("CO", "🇨🇴"),
        "Croatia": ("HR", "🇭🇷"),
        "Cyprus": ("CY", "🇨🇾"),
        "Czech Republic": ("CZ", "🇨🇿"),
        "Denmark": ("DK", "🇩🇰"),
        "Ecuador": ("EC", "🇪🇨"),
        "Eritrea": ("ER", "🇪🇷"),
        "Estonia": ("EE", "🇪🇪"),
        "Finland": ("FI", "🇫🇮"),
        "France": ("FR", "🇫🇷"),
        "Georgia": ("GE", "🇬🇪"),
        "Germany": ("DE", "🇩🇪"),
        "Great Britain": ("GB", "🇬🇧"),
        "Greece": ("GR", "🇬🇷"),
        "Guinea-Bissau": ("GW", "🇬🇼"),
        "Haiti": ("HT", "🇭🇹"),
        "Hong Kong": ("HK", "🇭🇰"),
        "Hungary": ("HU", "🇭🇺"),
        "Iceland": ("IS", "🇮🇸"),
        "India": ("IN", "🇮🇳"),
        "Iran": ("IR", "🇮🇷"),
        "Ireland": ("IE", "🇮🇪"),
        "Israel": ("IL", "🇮🇱"),
        "Italy": ("IT", "🇮🇹"),
        "Jamaica": ("JM", "🇯🇲"),
        "Japan": ("JP", "🇯🇵"),
        "Kazakhstan": ("KZ", "🇰🇿"),
        "Kenya": ("KE", "🇰🇪"),
        "Kosovo": ("XK", "🇽🇰"),
        "Kyrgyzstan": ("KG", "🇰🇬"),
        "Latvia": ("LV", "🇱🇻"),
        "Lebanon": ("LB", "🇱🇧"),
        "Liechtenstein": ("LI", "🇱🇮"),
        "Lithuania": ("LT", "🇱🇹"),
        "Luxembourg": ("LU", "🇱🇺"),
        "Madagascar": ("MG", "🇲🇬"),
        "Malaysia": ("MY", "🇲🇾"),
        "Malta": ("MT", "🇲🇹"),
        "Mexico": ("MX", "🇲🇽"),
        "Moldova": ("MD", "🇲🇩"),
        "Monaco": ("MC", "🇲🇨"),
        "Mongolia": ("MN", "🇲🇳"),
        "Montenegro": ("ME", "🇲🇪"),
        "Morocco": ("MA", "🇲🇦"),
        "Netherlands": ("NL", "🇳🇱"),
        "New Zealand": ("NZ", "🇳🇿"),
        "Nigeria": ("NG", "🇳🇬"),
        "North Macedonia": ("MK", "🇲🇰"),
        "Norway": ("NO", "🇳🇴"),
        "Pakistan": ("PK", "🇵🇰"),
        "Philippines": ("PH", "🇵🇭"),
        "Poland": ("PL", "🇵🇱"),
        "Portugal": ("PT", "🇵🇹"),
        "Puerto Rico": ("PR", "🇵🇷"),
        "Romania": ("RO", "🇷🇴"),
        "San Marino": ("SM", "🇸🇲"),
        "Saudi Arabia": ("SA", "🇸🇦"),
        "Serbia": ("RS", "🇷🇸"),
        "Singapore": ("SG", "🇸🇬"),
        "Slovakia": ("SK", "🇸🇰"),
        "Slovenia": ("SI", "🇸🇮"),
        "South Africa": ("ZA", "🇿🇦"),
        "South Korea": ("KR", "🇰🇷"),
        "Spain": ("ES", "🇪🇸"),
        "Sweden": ("SE", "🇸🇪"),
        "Switzerland": ("CH", "🇨🇭"),
        "Thailand": ("TH", "🇹🇭"),
        "Trinidad & Tobago": ("TT", "🇹🇹"),
        "Turkey": ("TR", "🇹🇷"),
        "Ukraine": ("UA", "🇺🇦"),
        "United Arab Emirates": ("AE", "🇦🇪"),
        "United States": ("US", "🇺🇸"),
        "Uruguay": ("UY", "🇺🇾"),
        "Uzbekistan": ("UZ", "🇺🇿"),
        "Venezuela": ("VE", "🇻🇪")
    }

    for d_code, flag in countries.values():
      if code == d_code:
            return flag
    return "Invalid code"


"""
The above solution works but inefficient 

looping through the entire dictionary every time, even though you only need a direct lookup.

1. Unnecessary loop
    -> You already have a dictionary, but you're not using it for direct lookup.
    -> Instead, you're iterating through all values.
2. Structure mismatch
    -> the dictionary keys are country names, but you're searching by code.
    => That forces you to loop instead of using O(n) lookup

Below is the cleaner approach

"""

def get_flag(code: str) -> str:
    flags = {
        "AL": "🇦🇱", "AD": "🇦🇩", "AR": "🇦🇷", "AM": "🇦🇲", "AU": "🇦🇺", "AT": "🇦🇹",
        "AZ": "🇦🇿", "BE": "🇧🇪", "BJ": "🇧🇯", "BO": "🇧🇴", "BA": "🇧🇦", "BR": "🇧🇷",
        "BG": "🇧🇬", "CA": "🇨🇦", "CL": "🇨🇱", "CN": "🇨🇳", "CO": "🇨🇴", "HR": "🇭🇷",
        "CY": "🇨🇾", "CZ": "🇨🇿", "DK": "🇩🇰", "EC": "🇪🇨", "ER": "🇪🇷", "EE": "🇪🇪",
        "FI": "🇫🇮", "FR": "🇫🇷", "GE": "🇬🇪", "DE": "🇩🇪", "GB": "🇬🇧", "GR": "🇬🇷",
        "GW": "🇬🇼", "HT": "🇭🇹", "HK": "🇭🇰", "HU": "🇭🇺", "IS": "🇮🇸", "IN": "🇮🇳",
        "IR": "🇮🇷", "IE": "🇮🇪", "IL": "🇮🇱", "IT": "🇮🇹", "JM": "🇯🇲", "JP": "🇯🇵",
        "KZ": "🇰🇿", "KE": "🇰🇪", "XK": "🇽🇰", "KG": "🇰🇬", "LV": "🇱🇻", "LB": "🇱🇧",
        "LI": "🇱🇮", "LT": "🇱🇹", "LU": "🇱🇺", "MG": "🇲🇬", "MY": "🇲🇾", "MT": "🇲🇹",
        "MX": "🇲🇽", "MD": "🇲🇩", "MC": "🇲🇨", "MN": "🇲🇳", "ME": "🇲🇪", "MA": "🇲🇦",
        "NL": "🇳🇱", "NZ": "🇳🇿", "NG": "🇳🇬", "MK": "🇲🇰", "NO": "🇳🇴", "PK": "🇵🇰",
        "PH": "🇵🇭", "PL": "🇵🇱", "PT": "🇵🇹", "PR": "🇵🇷", "RO": "🇷🇴", "SM": "🇸🇲",
        "SA": "🇸🇦", "RS": "🇷🇸", "SG": "🇸🇬", "SK": "🇸🇰", "SI": "🇸🇮", "ZA": "🇿🇦",
        "KR": "🇰🇷", "ES": "🇪🇸", "SE": "🇸🇪", "CH": "🇨🇭", "TH": "🇹🇭", "TT": "🇹🇹",
        "TR": "🇹🇷", "UA": "🇺🇦", "AE": "🇦🇪", "US": "🇺🇸", "UY": "🇺🇾", "UZ": "🇺🇿",
        "VE": "🇻🇪"
    }
    return flags.get(code.upper(), "🏳️") 


def get_flag(code: str) -> str:
      
      code = code.upper()

      return ''.join(chr(127397 + ord(c)) for c in code)
    

if __name__ == "__main__":
    unittest.main()
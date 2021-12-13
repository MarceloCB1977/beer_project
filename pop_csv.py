import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','beer_project.settings')

import django
# Import settings
django.setup()

from beer.models import BeerData
import csv
import io
import pandas as pd



# def populate():
#     with open('beer_final.csv') as f:
#         reader = csv.reader(f, delimiter=',')
#         for x in reader:
#             BeerData.objects.get_or_create(
#                 style_name = x[0],
#                 style_key = x[1],
#                 style_number = x[2],
#                 ABV_min = x[3],
#                 ABV_max = x[4],
#                 IBU_min = x[5],
#                 IBU_max = x[6],
#                 SRM_min = x[7],
#                 SRM_max = x[8],
#                 style_groups = x[9],
#                 style_key_family = x[10],
#                 recommend = x[11],
#                 image = x[12])

food = ['Aged Ham on Pretzel Bread, Havarti, Cheesecake with Raspberries',
'Seafood such as grilled shrimp, Asian dishes like pad thai, and marinated chicken dishes.',
'Saladas, sea food, chevre and fruit desserts',
'seafood and poultry dishes, salads, mild cheese, and sweet desserts',
'Roasted chicken, gouda, banana cream pie',
'Chicken and dumplings, manchego, banana bread',
'Pineapple ceviche, chevre, Chocolate Creme Caramel',
'Shellfish (Mussels), Mascarpone with Fruit, Rich Chocolate Cake',
'Pineapple ceviche, chevre, Chocolate Creme Caramel',
'Salads, Creamy Cheeses, Vanilla Ice Cream',
'Beef Carbonnade, Mimolette, Pumpkin Pie',
'lobster, shrimp, sautéed monkfish, Dungeness crab, and king salmon.',
'Beer Battered Fried Shrimp, Triple Crème, Baklava',
'Roasted Turkey, Triple Crème, Caramelized Banana Creme Brulee',
'Seafood (Mussels), Brie, Lemon Ginger Sorbet',
'Tempura Fried Fish and Chips, Taleggio, Savory Bread Pudding',
'both desserts and roasted meats, including beef tenderloin, filet.',
'Apple-Smoked Sausage, Washed-Rind Cheeses, Milk Chocolate',
'Leicester Cheddar. Pizza and Mexican Food',
'Roasted or Grilled Meats, Mild or Medium Cheddar, Apple Pie',
'Bone-In Pork Chops, Miso Salmon, Rich Cheeses, Carrot Cake',
'Barbecue, Medium Cheddar, Banana Pound Cake',
'Roasted Chicken, Fish and Chips, Firm English Cheeses, Oatmeal Raisin Walnut Cookies',
'Roasted Chicken, Fish and Chips, Firm English Cheeses, Oatmeal Raisin Walnut Cookies',
'fried batter,British dishes like Bangers & Mash and Shepherds Pie ',
'Variety of Meats and Game, Pungent Cheeses, Creamy Desserts with Fruit',
'Variety of Meats and Game, Pungent Cheeses, Creamy Desserts with Fruit',
'Variety of Meats and Game, Pungent Cheeses, Creamy Desserts with Fruit',
'Grilled Meats and Vegetables, Aged Gouda, Pear Fritters',
'Roasted Pork, Steak, Nuts, Aged Gouda, Pear Fritters',
'Roasted or Grilled Meats, Gruyere, Chocolate Peanut Butter Cookies',
'Roasted or Grilled Meats, Gruyere, Chocolate Peanut Butter Cookies',
'Seafood (Oysters), Ham, Irish Cheddar, Chocolate Desserts',
'Mexican Mole, Spicy BBQ, Buttery Cheddar, Chocolate Cake, Ice Cream',
'Chicken in Mole Sauce, Aged Cheddar, Sweet Potato Cheesecake',
'oysters, seafood and smoked fish.',
'Foie Gras, Aged Cheeses, Flour-less Chocolate Cake',
'Foie Gras, Aged Cheeses, Flour-less Chocolate Cake',
'Shellfish, Chicken, Salads, White Cheddar, Shortbread Cookies',
'Shellfish, Chicken, Salads, White Cheddar, Shortbread Cookies',
'Shellfish, Chicken, Salads, White Cheddar, Shortbread Cookies',
'creamy, light-bodied fresh cheeses like Mozzarella',
'creamy, light-bodied fresh cheeses like Mozzarella',
'creamy, light-bodied fresh cheeses like Mozzarella',
'Chocolate, barbecue, lobster',
'Samosas, Colby, Baklava',
'pork, burgers, seared venison, veal, and plain grilled steak.',
'Sausages, Roasted Vegetables, Washed-Rind Munster, Candied Ginger Beer Cake',
'Mushroom Strudel, Munster-Style Cheese, Fruit Tart',
'Pork or Ham, Strong Cheeses, German Chocolate Cake',
'Grilled Rib-Eye, Aged Swiss, Chocolate',
'Camembert, Game meats, pork',
'Bratwurst, Nutty Cheeses, Light Apricot Cake',
'Grilled Salmon, Emmental, Apple Pie',
'Roasted Lamb with Mint, Soft Ripened Cheeses, Pecan Pie',
'Kielbasa, Jalapeno Jack, Coconut Flan',
'Grilled Meats and Vegetables, Mild Cheeses, Almond Biscotti',
'Salads, Mild Shellfish, Monterey Jack, Lemon Custard Tart',
'The char of grilled meats will pair well with the caramel and toasty flavours of the beer',
'Grilled Sausage, Red Dragon Cheddar, Smores',
'Moroccan Duck, English Stilton, Dark Chocolate',
'roast beef or lamb, and desserts like plum-walnut tart, toffee apple crisp and classic canolli',
'gamey meats like pheasant and quail, as well as more traditional roast pork, smoked salmon, or lamb']

pair = ['Berliner weisse',
'Belgian white',
'American wheat',
'Weizenbier',
'Dunkelweizen',
'Weizenbock',
'Lambic',
'Gueuze',
'Faro',
'Fruit beer',
'Flanders red',
'Oud bruin',
'Belgian gold ale',
'Tripel',
'Saison',
'Belgian pale ale',
'Belgian dark ale',
'Dubbel',
'Pale ale',
'American pale ale',
'India pale ale',
'American amber ale',
'Ordinary bitter',
'Special bitter',
'Extra special bitter',
'Scottish light 60',
'Scottish heavy 70',
'Scottish Export 80',
'American brown',
'English brown',
'Brown porter',
'Robust porter',
'Dry stout',
'Sweet stout',
'Oatmeal stout',
'Foreign extra stout',
'Imperial stout',
'Russian imperial stout',
'German pilsner',
'Bohemian pilsner',
'American pilsner',
'American lite',
'American standard',
'American premium',
'American dark',
'Munich helles',
'Dortmunder',
'Munich dunkel',
'Schwarzbier',
'Doppelbock',
'Traditional bock',
'Eisbock',
'Kolsch',
'Altbier',
'Biere de garde',
'Oktoberfest',
'Vienna',
'Cream ale',
'Steam beer',
'Smoked beer',
'Barleywine',
'English old (strong) ale',
'Strong scotch ale']

# fooddict = {pair[i]: food[i] for i in range(len(pair))}
# #
# #
# # BeerData.objects.get_or_create(food_pair=style_name.map(fooddict))
#
# for x in fooddict:
#     BeerData.objects.filter(style_name=x).update(food_pair=fooddict[x])


description = ['Low in alcohol, refreshingly tart, and often served with a flavored syrup like Woodruff or raspberry, the Berliner-style Weisse presents a harmony between yeast and lactic acid. These beers are very pale in color, and may be cloudy as they are often unfiltered.',
'Crisp and tangy with subtle citrus sweetness, low bitterness',
'Usually clear in contrast to most other wheat beers, slightly tart and very refreshing.',
'Notable clove and banana aroma from German wheat yeast. Fruity, cloudy, low hop profile.',
'The German-style Dunkelweizen can be considered a cross between a German-style dunkel and a hefeweizen. Distinguished by its sweet maltiness and chocolate-like character, it can also have banana and clove (and occasionally vanilla or bubblegum) esters from weizen ale yeast.',
'With flavors of bready malt and dark fruits like plum, raisin, and grape, this style is low on bitterness and high on carbonation. Balanced clove-like phenols and fruity, banana-like esters produce a well-rounded aroma.',
'Often known as cassis, framboise, kriek, or peche, a fruit lambic takes on the color and flavor of the fruit it is brewed with. It can be dry or sweet, clear or cloudy, depending on the ingredients. Sourness is an important part of the flavor profile, though sweetness from fruit may diminish the perceived intensity.',
'Historically, they are dry and completely attenuated, exhibiting no residual sweetness either from malt, sugar or artificial sweeteners.',
'Sweetened version of Lambic',
'Fruit beer is made with fruit, or fruit extracts that are added during any portion of the brewing process, providing obvious yet harmonious fruit qualities. This idea is expanded to “field beers” that utilize vegetables and herbs.',
'Overall, the style is characterized by slight to strong lactic sourness, and Flanders reds sometimes include a balanced degree of acetic acid.',
'Fruity, malty, sherry wine like, slightly sour',
'is fruity, complex and often on the higher end of the ABV spectrum, yet are approachable to many different palates. Look for a characteristic spiciness from Belgian yeast and a highly attenuated dry finish. This style is traditionally drier and lighter in color than a Belgian-style tripel.',
'Tripels are often on the higher end of the ABV spectrum, yet are approachable to many different palates. These beers are commonly bottle-conditioned and finish dry.',
'Beers in this category are gold to light amber in color. Often bottle-conditioned, with some yeast character and high carbonation. Specialty ingredients, including spices, may contribute a unique and signature character. ',
'gold to copper in color and can have caramel or toasted malt flavor. The style is characterized by low but noticeable hop bitterness, flavor and aroma.',
'Complex, with a rich malty sweetness, significant esters and alcohol, and an optional light to moderate spiciness. The malt is rich and strong, and can have a Munich-type quality often with a caramel, toast and/or bready aroma.',
'ranges from brown to very dark in color. They have a malty sweetness and can have cocoa and caramel aromas and flavors. Hop bitterness is medium-low to medium.',
'Low to medium maltiness, high hop bitterness, medium hop profile',
'Characterized by floral, fruity, citrus-like, piney, resinous American hops, the American pale ale is a medium-bodied beer with low to medium caramel, and carries with it a toasted maltiness.',
'high hop bitterness, flavor and aroma. Alcohol content is medium-high to high and notably evident with a medium-high to full body. This style intends to exhibit the fresh, evident character of hops.',
'American ambers are darker in color than their pale ale cousins, the presence of caramel and crystal malts lending a toasted, toffee flavor, along with the perception of a fuller body when compared to beers without such malts.',
'Broad style description commonly associated with cask-conditioned beers. The light- to medium-bodied ordinary bitter is gold to copper in color, with a low residual malt sweetness. Hop bitterness is medium.',
'Most modern bitters are softly malty, usually with a biscuity, nutty, or toasty quality.',
'This style is known for its balance and the interplay between malt and hop bitterness',
'Scottish-style ales vary depending on strength and flavor, but in general retain a malt-forward character with some degree of caramel-like malt flavors and a soft and chewy mouthfeel. Some examples feature a light smoked peat flavor. Hops do not play a huge role in this style. The numbers commonly associated with brands of this style (60/70/80 and others) reflect the Scottish tradition of listing the cost, in shillings, of a hogshead (large cask) of beer. Overly smoked versions would be considered specialty examples.',
'Scottish-style ales vary depending on strength and flavor, but in general retain a malt-forward character with some degree of caramel-like malt flavors and a soft and chewy mouthfeel. Some examples feature a light smoked peat flavor. Hops do not play a huge role in this style. The numbers commonly associated with brands of this style (60/70/80 and others) reflect the Scottish tradition of listing the cost, in shillings, of a hogshead (large cask) of beer. Overly smoked versions would be considered specialty examples.',
'Scottish-style ales vary depending on strength and flavor, but in general retain a malt-forward character with some degree of caramel-like malt flavors and a soft and chewy mouthfeel. Some examples feature a light smoked peat flavor. Hops do not play a huge role in this style. The numbers commonly associated with brands of this style (60/70/80 and others) reflect the Scottish tradition of listing the cost, in shillings, of a hogshead (large cask) of beer. Overly smoked versions would be considered specialty examples.',
'American-style brown ales have evident low to medium hop flavor and aroma and medium to high hop bitterness.',
'English-style brown ales have two variations: a dry, roasted version that is said to have originated from northern England, and a sweeter, less attenuated brown ale variety that is believed to have gained favor in the southern portion of England.',
'has no roasted barley or strong burnt/black malt character. Low to medium malt sweetness, caramel and chocolate is acceptable. Hop bitterness is medium. Softer, sweeter and more caramel-like than a robust porter, with less alcohol and body. ',
'Robust porters have a roast malt flavor, often reminiscent of cocoa, but no roast barley flavor. Their caramel and malty sweetness is in harmony with the sharp bitterness of black malt.',
'The emphasis on coffee-like roasted barley and a moderate degree of roasted malt aromas define much of the character. Hop bitterness is medium to medium high. This beer is often dispensed via nitrogen gas taps that lend a smooth, creamy body to the palate.',
' Malt sweetness, chocolate and caramel should dominate the flavor profile and contribute to the aroma. It also should have a low to medium-low roasted malt/barley-derived bitterness. Milk sugar (lactose) lends the style more body.',
'This beer style is dark brown to black in color. Roasted malt character is caramel-like and chocolate-like, and should be smooth and not bitter. Coffee-like roasted barley and malt aromas are prominent.',
'Aroma: Strong, with pronounced fruity and roast character. Flavour: A full-bodied palate of roast, fruity character.',
'Black in color, these beers typically have an extremely rich malty flavor and aroma with full, sweet malt character. Bitterness can come from roasted malts or hop additions.',
'Black in color, these beers typically have an extremely rich malty flavor and aroma with full, sweet malt character. Bitterness can come from roasted malts or hop additions.',
'straw to pale in color with a malty sweetness that can be perceived in aroma and flavor. Perception of hop bitterness is medium to high. ',
'slightly sweet and evident malt character and a toasted, biscuit-like, bready malt character. ',
'slightly sweet and evident malt character and a toasted, biscuit-like, bready malt character. ',
'Little to no malt aroma, very low in hops, crisp, dry refreshing.',
'similar to american lite, but darker',
'similar to american standard, but darker',
'Malty, some roasted malt flavour and low hops.',
'The malt character is soft and bready, making it a terrific complement to light dishes such as salad or fresh shellfish, like clams',
'Smooth medium sweetness, medium hop aroma and flavour',
'aroma comprised of chocolate roasted malt and bread or biscuit-like features that stem from the use of Munich malt',
'These very dark brown to black beers have a surprisingly pale-colored foam head (not excessively brown) with good cling quality',
'the doppelbock beer style is very food-friendly and rich in melanoidins reminiscent of toasted bread. Color is copper to dark brown. Malty sweetness is dominant but should not be cloying',
'Traditional bock beers are all-malt brews and are high in malt sweetness. Malt character should be a balance of sweetness and toasted or nut-like malt. “Bock” translates as “goat”!',
'Aroma and flavour domintaed by rich malt and concentrated alcohol.',
'The German-style Kolsch is light in color and malt character. This style’s fermentation process yields a light, vinous character which is accompanied by a slightly dry, crisp finish.',
'Altbier strikes a balance between hop and malt flavors and aromas, but can have low fruity esters and some peppery and floral hop aromas.',
'Biere de Garde translates as “beer for keeping.” This style is characterized by a toasted malt aroma and slight malt sweetness. Flavor of alcohol is evident. Often bottle-conditioned, with some yeast character.',
'Toasted bread or biscuit-like malt aroma and flavor is to be expected.  A stronger version was served at early Oktoberfest celebrations and became known as Oktoberfest. Today, the festival’s version of an Oktoberfest is quite a bit lighter than what American craft brewers consider an Oktoberfest.',
'Vienna Lager ranges from copper to reddish brown in color. The beer is characterized by malty aroma and slight malt sweetness.',
'The American cream ale is a mild, pale, light-bodied ale, made using a warm fermentation (top or bottom fermenting yeast) and cold lagering.',
'Malty balanced with hop bitterness and woody hop flavour',
'Traditionally, brewers will cite the specific wood used to smoke the malt, and different woods will lend different flavors to the finished product',
'With a wide color range and characteristically high in alcohol content, this is a style that is often aged, as it evolves well over time.',
'Well aged malty and fruity, high alcohol',
'malty with caramel apparent, hints of roasted malt or smoky falvour.']

discdict = {pair[i]: description[i] for i in range(len(pair))}

for x in discdict:
    BeerData.objects.filter(style_name=x).update(desc=discdict[x])



#
#
# if __name__ == '__main__':
#     print("Populating the databases...Please Wait")
#     populate()
#     print('Populating Complete')

# data = pd.read_csv('beer_final_2.csv')
# print(list(data['sytle_name']))
# print(f'ABV_MIN_min: {data['ABV_min'].min()}')
# print(f'ABV_MIN_max: {data['ABV_min'].max()}')
# print(f'ABV_MAX_min: {data['ABV_max'].min()}')
# print(f'ABV_MAX_max: {data['ABV_max'].max()}')

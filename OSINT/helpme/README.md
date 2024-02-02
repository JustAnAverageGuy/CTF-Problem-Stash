# helpme (300) - OSINT

Total solves - 63

Final score - 60

## Description
I went to this amazing restaurant, but now I've forgotten its name. All I've got is this picture. Can you help me find it.

Flag format: COPS{latitude_longitude} both latitude and longitude exact to 3 decimal places only.

Author - quinnyx

## Attachment
help_me.jpeg

## Writeup
Read everything you can in the picture; the restaurant has won the "Times Food Nightlife Award in 2022." If you guessed that it is a buffet/barbecue kind of restaurant, you can find it in the first Google search result.

Alternatively, start by Googling "Nightlife Awards 2022." You will get various results; consider the first website as the most relevant. If you look carefully, you can see the word "Sethi" below 2022 in the pic. Combine these two into an advanced Google search: "site:hospitality.economictimes.indiatimes.com intext:sethi." In the sixth search result, you will see an article about the owner of the restaurant (Rajan Sethi). It can be further confirmed because we can see "an" to the left of Sethi in the pic. Search all his restaurants to find the one matching the picture.

## FLAG
COPS{28.633_77.222}

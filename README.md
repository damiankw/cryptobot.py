cryptobot.py

A simple IRC bot to pull crypto currencies.

A couple of things are still a little static, so you will have to edit the code (for example, to change the channel it joins to).

Otherwise, edit the start.py and modify the server details.

Usage:
.crypto
- This will pull the top 15 crypto currencies from the internet and give you detail about them, in AUD

.crypto -<"AUD", "BRL", "CAD", "CHF", "CLP", "CNY", "CZK", "DKK", "EUR", "GBP", "HKD", "HUF", "IDR", "ILS", "INR", "JPY", "KRW", "MXN", "MYR", "NOK", "NZD", "PHP", "PKR", "PLN", "RUB", "SEK", "SGD", "THB", "TRY", "TWD", "ZAR">
- This will pull the top 15 crypto currencies from the internet and give you detail about them, in whichever currency you request from the above list

.crypto bitcoin
- This will pull just information about bitcoin, in AUD

The -AUD/USD/etc can be used with other options like so:

.crypto -USD bitcoin
- Will pull bitcoin detail in USD

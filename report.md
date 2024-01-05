# The Making of The Token Bot
-----------------------------
## Planning part
With the advent of GPT4 and its capabilities I used it to prototype the bot with different APIs like OKX (which didn't work since GOOD isn't actually listed on there) and Coin Market cap. The problem is that APIs aren't free... So I went with CoinGecko, the api was went to me by a friend (god bless his soul lmao).

## Scripting and GPT4
So now came the time to start prompting for functional coding. I basically asked GPT4 to help me write out a quick script that satisfies the following:

0. Name format is "GOOD $0.0000 (arrow)
1. Check for price every 2.5 hours
2. Change name to price
3. If price up compared to previous price then put arrow up sign (↗️)
4. If price down compared to previous price then put arrow down sign (↘️)

based on this logic, a script was generated with the integration of CoinGecko's api and the interval checks for price and calls the API whenever it's time to update the price.

## API Understanding
The API understanding drove me nuts because you need to combine the api base url and the other function url thingamagick thing idk lmao. That was just straight up confusing.

## Security
I included an .env file for token reading and not hardcoding it into the main bot script. I installed python_dotenv and that's pretty much it.

## Struggles
Python is actually hard lol. Thanks to the guys at OpenAI for making this even remotely possible. Or else I'm actually screwed. I probably can't find a job like this anyway so lol, morale diminished dot com.

## Conclusion
This project for me was challenging since I'm quite new to programming. But I understood what the code does. I cannot memorise and regurgitate it out but I got the price bot up and running quickly with Google Cloud. Troubleshooting issues like token not being read because of my working directory was the most time consuming. But other than that it's ok. I would like to take on more harder projects as I refresh and learn Python more, Rust and Solidity.

I guess that's all I have to say eeee. Token ain't in this repo yo! 
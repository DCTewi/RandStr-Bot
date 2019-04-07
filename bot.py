#
# The Random String Bot Script
#
# - Code: @dctewi@niu.moe
# - Bot: randstrbot@mastodon.social
# - Modules Required:
#   - Mastodon.py
#

from mastodon import Mastodon
import requests
import time
import json

# Variables
# The instance's homepage url
instance_url = 'https://your.instance'
# The application's token file
app_token_path = 'token.secret'
# Email of bot
bot_username = 'some@email.com'
# Password of bot
bot_password = 'yourpassword'
# The time between two toots
delay_sec = 60 * 30
# The suffex of every toot
sufstr = '\n\n#RandomString'
# The random string api of qrng
qrng_url = 'https://qrng.anu.edu.au/API/jsonI.php?length=1&type=hex16&size=1'
# The motioned user id when failed
owner_id = '@dctewi@niu.moe'

# Set up Mastodon API
api = Mastodon(access_token = app_token_path, api_base_url = instance_url)
api.log_in(bot_username, bot_password, to_file = app_token_path)


# Toot begin
print('Started!')
api.toot('Random String Bot Started!' + sufstr)

# Main Loop
while (True):

	# Get the random string from QRNG
	randhtml = requests.get(qrng_url)
	randstr = json.loads(randhtml.text)

	# Check if success
	if (randstr['success'] == False):
		api.toot('String generate failed!' + owner_id + sufstr)
	else:
		time_text = time.strftime('%H:%M', time.localtime(time.time()))
		toot_text = 'Random String At ' + time_text + '!\n\n' + randstr['data'][0] + sufstr;
		api.toot(toot_text)

	# Sleep for next toot
	time.sleep(60 * 30)


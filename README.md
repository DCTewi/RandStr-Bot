# RandStr-Bot Script

[中文版本点击这里](./README.zh_CN.md)

> This is a sample bot script for Mastodon. 

Bot: [@randstrbot@mastodon.social](https://mastodon.social/@randstrbot)

Owner: [@dctewi@niu.moe](https://niu.moe/@dctewi)

## Basic Usage

You can deploy an random string toot bot easily:

1. Install Mastodon.py on your computer by:

   ```sh
   pip install Mastodon.py
   ```

2. Create a Mastodon account on [a instance](https://joinmastodon.org/#getting-started).

3. `Edit Profile` -> `Development` -> `Your applications` -> `NEW APPLICATION`, and create as default options.

4. Copy the `Your access token` on Application page to `./token.secret`.

5. Set up the variables list in `./bot.py`:

   ```python
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
   ```

6. Run python script by:

   ```sh
   python ./bot.py
   ```

## Customization

- You **should** customize your bot's toots by edit the Main Loop in `./bot.py`.

- You can run it at Linux VPS silently by (One optional choice) :

  ```sh
  nohup sudo python -u ./bot.py > ./bot.log 2>&1 & echo $! > ./botpid.log
  ```

  and kill the progress by:

  ```sh
  kill -9 `cat ./botpid.log`
  ```

  when `./bot.log` for log and `./botpid.log` for PID of bot progress.

## About Mastodon.py

For more details -> [doc](https://mastodonpy.readthedocs.io/en/latest/#)

## License

MIT


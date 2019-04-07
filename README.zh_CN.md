# RandStr-Bot 脚本

[Click here for English Version](./README.md)

> 这是一个长毛象随机字符串Bot的脚本样例。

Bot: [@randstrbot@mastodon.social](https://mastodon.social/@randstrbot)

Owner: [@dctewi@niu.moe](https://niu.moe/@dctewi)

## 基础使用

你可以简单地部署一个随机字符串Bot：

1. 安装依赖项Mastodon.py:

   ```sh
   pip install Mastodon.py
   ```

2. 在[一个长毛象实例](https://joinmastodon.org/#getting-started)中注册一个帐户。

3. `修改个人资料` -> `开发` -> `你的应用` -> `创建新应用`, 然后按默认配置创建应用。

4. 复制 `你的访问令牌` 项 到`./token.secret`.

5. 配置好 `./bot.py` 中的变量列表:

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

6. 运行python脚本:

   ```sh
   python ./bot.py
   ```

## 自定义

- 你**应该**修改 `./bot.py` 中的主循环(Main Loop)中的代码来自定义嘟文内容.

- 你可以通过这种方式在Linux VPS上静默运行脚本（一种选择）:

  ```sh
  nohup sudo python -u ./bot.py > ./bot.log 2>&1 & echo $! > ./botpid.log
  ```

  同时通过这种方式结束运行脚本

  ```sh
  kill -9 `cat ./botpid.log`
  ```

   `./bot.log` 用来记录Log ， `./botpid.log` 用来记录当前脚本的PID。

## 关于Mastodon.py

见[文档](https://mastodonpy.readthedocs.io/en/latest/#)。

## License

MIT
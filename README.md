# **RU**

### Бот для написания комментов под новыми постами на заданых каналах используя рандомные фразы из списка.

**text.txt** - список фраз для ответа в комменты, выбираетя рандомно

**channels.txt** - айди, название или ссылка канала, лучше всего айди так как название и ссылку можно поменять

**config.cfg** - конфиг
| Имя | Значение |
|-------------|-------------|
| api_id | api_id, получить можно в [my.telegram](https://my.telegram.org/auth) |
| api_hash | api_hash, получить можно в [my.telegram](https://my.telegram.org/auth) |
| phone | номер телефона аккаунта |
| password | 2 step вериф пароль, если есть |
| session_name | название сессии |
| bot_token | токен бота для отправки уведомлений, не обязательно |
| admin_user_id | user_id пользователя которому отправлять уведомления, получить можно [тут](https://t.me/username_to_id_bot), если указан bot_token |
| channel_msg_delay | (сек) кд на комментарии для каждого канала, если стоит 120 то бот ответит на пост в канале только раз в 2 минуты |
| text_file | название файла с фразами |
| channels_file | название файла с каналами |

#### Уведомления приходят в виде:
-=- New message in channel (Айди сообщения)  
-=- Time: Время  
-=- Text: Текст поста  
-=- Url: Ссылка на пост  
-=- Bot response: Ответ бота  
-=- Status: Success|Успех или Chat unavailable|Чат недоступен или другая ошибка

# **EN**

### Bot for writing comments under new posts on specified channels using random phrases from a list.

**text.txt** - phrases list for post commenting, selected randomly

**channels.txt** - channel id, name or link, it's best to use an ID, as the name and link can be changed

**config.cfg** - config
| Name | Value |
|-------------|-------------|
| api_id | api_id, you can get it from [my.telegram](https://my.telegram.org/auth) |
| api_hash | api_hash, you can get it from [my.telegram](https://my.telegram.org/auth) |
| phone | account phone number |
| password | 2 step verification password, if any |
| session_name | session name |
| bot_token | bot token to send notifications, not required |
| admin_user_id | user_id of the user to whom to send notifications can be obtained [here](https://t.me/username_to_id_bot)|
| channel_msg_delay | (sec) comment idle time, if it is 120, the bot will be able to reply only once every 2 minutes in each channel |
| text_file | phrases file name |
| channels_file | channels file name |

#### Notifications come in the form of:
-=- New message in channel (Msg id)  
-=- Time: Time  
-=- Text: Post text  
-=- Url: Post link  
-=- Bot response: Bot response  
-=- Status: Success or Chat unavailable or another error

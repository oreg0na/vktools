import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vktools import Keyboard, ButtonColor, Text, OpenLink, Location

vk = vk_api.VkApi(token="token")

def send_message(user_id, message, keyboard=None):
  values = {
    "user_id": user_id,
    "message": message,
    "random_id": 0
  }

  if keyboard is not None:
    values["keyboard"] = keyboard.add_keyboard()

  vk.method("messages.send", values)

for event in VkLongPoll(vk).listen():
  if event.type == VkEventType.MESSAGE_NEW and event.to_me:
    text = event.text.lower()
    user_id = event.user_id
    if text == "text":
      keyboard = Keyboard(
        [
          [
            Text("RED", ButtonColor.NEGATIVE),
            Text("GREEN", ButtonColor.POSITIVE),
            Text("BLUE", ButtonColor.PRIMARY),
            Text("WHITE")
          ],
          [
            OpenLink("VK", "https://vk.com/oreg0na"),
            Location()
          ]
        ]
      )
      send_message(user_id, "VkTools Keyboard by oreg0na ~", keyboard)
class script(object):
    START_TXT = """๐ฏ๐๐๐๐ {},
๐ด๐ ๐๐๐๐ ๐๐ <a href=https://t.me/{}>{}</a> ๐ฐ ๐๐๐ ๐๐๐๐๐๐๐ ๐๐๐๐๐๐ ๐๐ ๐๐๐๐๐, ๐ฑ๐๐๐ ๐๐๐ ๐๐ ๐๐ ๐๐ ๐๐๐๐๐ ๐๐ ๐๐๐๐๐๐"""
    HELP_TXT = """๐ฏ๐๐ {}
๐ฏ๐๐๐ ๐๐ ๐๐ ๐๐๐๐ ๐๐๐๐๐๐๐๐."""
    ABOUT_TXT = """โฏ แดส ษดแดแดแด ยป {}
โฏ แดสแดแดแดแดส ยป <a href=https://t.me/dmx_bots/4>แดแดแดแด แดแดx</a>
โฏ สษชสสแดสส ยป <a href=https://docs.pyrogram.org/>แดสสแดษขสแดแด</a>
โฏ สแดษดษขแดแดษขแด ยป <a href=https://www.python.org/>แดสแดสแดษด</a>
โฏ แด แดสsษชแดษด ยป 3
โฏ แดแดแดแดสแดsแด ยป <a href=https://www.mongodb.com>แดแดษดษขแด แดส</a>
โฏ sแดสแด แดส ยป <a href=https://signup.heroku.com/login>สแดสแดแดแด</a>
โฏ แดส sแดแดแดแดs ยป v8.0.2 [ แดษด สแดแดแด ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- ๐๐๐๐๐๐ ๐๐๐๐๐ ๐๐๐ ๐๐๐ ๐๐๐๐๐ ๐๐ ๐๐๐๐ ๐๐ ๐๐๐๐๐๐
- ๐ฎ๐๐๐๐ - https://dmx_chating_2_0 

<b>แดสแดแดแดแดสs ยป</b>
- <a href=https://t.me/dmx_bots/4>แดแดแดแด แดแดx</a>"""
    MANUELFILTER_TXT = """สแดสแด ยป <b>Fษชสแดแดสs</b>

- ๐ด๐๐๐๐ ๐ญ๐๐๐๐๐ ๐๐ ๐๐๐ ๐๐๐๐๐๐๐ ๐๐๐๐ ๐๐๐๐๐ ๐๐๐ ๐๐๐ ๐๐๐๐ ๐๐๐๐๐๐๐ ๐๐๐ ๐๐๐๐๐๐๐๐๐๐ ๐๐๐๐๐๐๐๐ ๐๐๐ ๐ ๐๐๐๐ ๐๐๐๐๐๐๐ ๐๐๐๐ ๐๐๐๐ ๐๐๐๐ ๐๐๐๐๐๐๐ ๐๐๐๐๐ ๐๐ ๐๐๐๐ ๐๐๐๐..

<b>Nแดแดแด ยป</b>
1. ๐ฐ๐๐ ๐๐๐๐๐๐ ๐๐ ๐ ๐๐๐๐๐ ๐๐ ๐๐๐๐ ๐๐๐๐๐
2. ๐ถ๐๐๐ ๐๐๐๐๐๐ ๐๐๐ ๐๐๐๐๐๐ ๐๐ ๐๐ ๐๐
3. ๐ช๐๐๐๐๐๐ ๐๐๐๐๐ ๐๐ ๐๐ ๐๐ [๐๐๐ ยป `/connect - group id]\n๐๐๐ ๐๐๐๐๐๐๐ `/connect -1234567890`
4. ๐จ๐๐๐๐ ๐๐๐๐๐๐๐ ๐๐๐๐ ๐๐๐๐๐ 64 ๐๐๐๐๐๐๐๐๐๐

<b>Cแดแดแดแดษดแดs แดษดแด Usแดษขแด ยป</b>
โข /filter แดส /add - <code>แดแดแด าษชสแดแดส ษชษด ษขสแดแดแด</code>
โข /filters แดส /viewfilters - <code>สษชsแด แดา แดสส าษชสแดแดสs ษชษด สแดแดส ษขสแดแดแด</code>
โข /del - <code>แดแด แดแดสแดแดแด แด าษชสแดแดส ษชษด ษขสแดแดแด</code>
โข /delall - <code>แดแดสแดแดแด แดกสแดสแด าษชสแดแดสs ษชษด ษขสแดแดแด (แดแดแดษชษด แดษดสส)</code>"""
    BUTTON_TXT = """สแดสแด:ยป <b>Buttons</b>

- ษชแดแด sแดแดแดแดสแดแดแด แดษด สแดแดส สแดแดแดแดษดs (แดสส , แดสแดสแด)

<b>ษดแดแดแด ยป</b>
1. แดแดสแดษขสแดแด แดกษชสส ษดแดแด แดสสแดแดก แดแด sแดษดแด สแดแดแดแดษด แดกษชแดสแดแดแด แดษดส แดแดษดแดแดษดแด, sแด แดแดแด แดษดส แดแดxแด , แดสแดแดแด,แดแดแดแด แดษด สแดแดแดแดษด าษชสแดแดสษชษดษข.
2. ษช sแดแดแดแดสแด แดษด แดษดส แดแดแดษชแด แดสแดแด แดแดสแดษขสแดแด sแดแดแดแดสแดs
3. สแดแดแดแดษด sสแดแดสแด สแด ษชษด แดแดสสแดแดแด แดแดสแดแดแดแดกษด าแดสแดแดแด

<b>Uสส สแดแดแดแดษดs ยป</b>
<code>[Button Text](buttonurl:https://t.me/dmx_chating)</code>

<b>Aสแดสแด สแดแดแดแดษดs ยป</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """สแดสแด ยป <b>แดแดแดแด าษชสแดแดส</b>

<b>ษดแดแดแด แดแด ษชษดแดแดx ยป</b>

สแดแด แดแดษดแด แดสษชษดแด แดสแดแดแด ษชแด สแดแดแดแดแดsแด ษชแดแด แดสสแดแดแดส แดแดแดแดแด แดแดสแด แดสแดษด 2แด าษชสแดs ษชษด แดส แดแดแดแดสแดsแด sแด สแดแด แดแดษดแด ษดแดแดแด แดแด แดแดแด าษชสแดs แดษดสแดแดสแด

1. แดแดแดแด แดแด แดs แดแดแดษชษด ษชา แดสแดแด แดสแดษดษดแดส ษชs แดสษชแด แดแดแด
2. แดแดแดแด sแดสแด แดสแดแด แดสแดษดษดแดส แดแดแดs ษดแดแด แดแดษดแดแดษชษด แดษดส แดสแดษด แดส แดษดส าแดแดแด าษชสแดs ( ษชา ษช าษชษดแด สษชแดแด แดสแดแด ษช แดกษชสส สแดษด สแดแด ษชษด แดส แดส แดษดแด แดแดแด สแดแด ษชษด แดส าแดแด)
3. แดสแดษด าแดสแดกแดสแด แดแด แดสแด สแดsแด แดแดssแดษขแด แดกษชแดษข าแดสแดกแดสแด แดแดษขs (วซแดแดแดแดs)
 ษช'สส แดแดแด แดสส าษชสแดs แดแด แดส แดส"""
    CONNECTION_TXT = """สแดสแด ยป <b>แดแดษดษดแดแดแดษชแดษดs</b>

- แดsแดแด แดแด แดแดษดษดแดแดแด แดแด ษชษด ษขสแดแดแด
- ษชแด สแดสแดs แดแด แดสแดแด แดษดแด แดสแด แดแด แดส sแดแดแดแดษชษดษข แดา ษขสแดแดแด

<b>ษดแดแดแด ยป</b>
1. แดษดสส แดแดแดษชษดs แดแดษด แดแดแด แด แดแดษดษดแดแดแดษชแดษด แดแด สแดแดส ษขสแดแดแด
3. แดแดแดแด sแดสแด แดสแดแด ษชแดแด แดแดแดษชษด แดสแดสแด
2. sแดษดแด <code>/connect (ษขสแดแดแด ษชแด)</code> แดแด แดแดษดษดแดแดแด

<b>แดแดแดแดแดษดแดs แดษดแด แดsแดษขแด ยป</b>
โข /connect  - <code>แดแดษดษดแดแดแด แด แดแดสแดษชแดแดสแดส แดสแดแด แดแด แดส แดแด</code>
โข /disconnect  - <code>แดษชssแดแดษดษดแดแดแด แด แดสแดแด</code>
โข /connections - <code>สษชsแด แดสส สแดแดส แดแดษดษดแดแดแดษชแดษดs</code>"""
    EXTRAMOD_TXT = """สแดสแด ยป<b>แดxแดสแด แดแดแดs</b>

<b>ษดแดแดแด ยป</b>
แดสแดsแด แดสแด sแดแดแด แดxแดสแด แดแดแดs แดสแดแด ษช สแดแด แด

<b>แดแดแดแดแดษดแดs แดษดแด แดsแดษขแด ยป</b>
โข /id - <code>ษขแดแด ษชแด แดา แด sแดแดแดษชาแดแด แดsแดส</code>
โข /info  - <code>ษขแดแด ษชษดาแด แดสแดแดแด แด แดsแดส</code>
โข /imdb  - <code>ษขแดแด าษชสแด ษชษดาแด ษชษด ษชแดแดส sแดแดแดสแด</code>
โข /search  - <code>ษขแดแด แดสแด าษชสแด ษชษดาแด ษชษด แด แดสษชแดแดs sแดแดแดสแด </code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>ษดแดแดแด ยป</b>
Tสษชs แดแดแดแดสแด แดษดสส แดกแดสแดs าแดส แดส แดแดแดษชษดs

<b>แดแดแดแดแดษดแดs แดษดแด แดsแดษขแด ยป</b>
โข /logs - <code>แดแด ษขแดแด แดสแด สแดsแดแดษดแด แดสสแดสs</code>
โข /stats - <code>แดแด ษขแดแด sแดแดแดแดs แดา าษชสแดs ษชษด แดส.</code>
โข /delete - <code>แดแด แดแดสแดแดแด แด sแดแดแดษชาษชแด าษชสแด าสแดแด แดส.</code>
โข /users - <code>แดแด ษขแดแด สษชsแด of แดส แดsแดสs แดษดแด ษชแดs.</code>
โข /chats - <code>แดแด ษขแดแด สษชsแด แดา แดสแด แดส แดสแดแดs แดษดแด ษชแดs </code>
โข /leave  - <code>แดแด สแดแดแด แด าสแดแด แด แดสแดแด.</code>
โข /disable  -  <code>แดแด แดษชsแดสสแด แด แดสแดแด.</code>
โข /ban  - <code>แดแด สแดษด แด แดsแดส.</code>
โข /unban  - <code>แดแด แดษดสแดษด แด แดsแดส.</code>
โข /channel - <code>แดแด ษขแดแด สษชsแด แดา แดแดแดแดส แดแดษดษดแดแดแดแดแด แดสแดษดษดแดสs</code>
โข /broadcast - <code>แดแด สสแดแดแดแดแดsแด แด แดแดssแดษขแด แดแด แดสส แดsแดสs</code>"""
    STATUS_TXT = """โ ๐๐พ๐๐ฐ๐ป ๐ต๐ธ๐ป๐ด๐: <code>{}</code>
โ ๐๐พ๐๐ฐ๐ป ๐๐๐ด๐๐: <code>{}</code>
โ ๐๐พ๐๐ฐ๐ป ๐ฒ๐ท๐ฐ๐๐: <code>{}</code>
โ ๐๐๐ด๐ณ ๐๐๐พ๐๐ฐ๐ถ๐ด: <code>{}</code> ๐ผ๐๐ฑ
โ ๐ต๐๐ด๐ด ๐๐๐พ๐๐ฐ๐ถ๐ด: <code>{}</code> ๐ผ๐๐ฑ"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
สแดแด = #tony
ID - <code>{}</code>
Name - {}
"""

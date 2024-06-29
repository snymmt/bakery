import streamlit as st
import numpy as np
import time
import streamlit as st
import numpy as np
import time

st.title("生駒ベーカリー　クーポンアプリ")
name = st.sidebar.text_input("会員名を入力してください")
date = st.sidebar.date_input("今日の日付を入力してください")

if st.button("本日のクーポン　←ここをクリック"):
  
  options = ["大当たり:シフォンケーキ１ホール無料♪","当たり：岡山県産白桃のふんわりロール90％off","当たり：かりかりメロンパン80％off","当たり：地鶏たまごのとろ～りクリームパン70％off","当たり：外はさっくり中はもちもち山形食パン60％off","当たり：たっぷりチョコレートのコルネ半額","当たり：スイートコーンのぴよぴよちぎりパン50％off","当たり：ひんやり紫イモのモンブラン40％off","当たり：あっかんベーコンサンド30％off","当たり：国産ライ麦100％ハードブレッド20％off"]
  luck = np.random.choice(options, 1, p=[0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1])[0]

  if luck=="大当たり:シフォンケーキ１ホール無料♪":
    image = "ooatari.jpg"
  elif luck=="当たり：岡山県産白桃のふんわりロール90％off":
    image = "90off.jpg"
  elif luck=="当たり：かりかりメロンパン80％off":
    image = "80off.jpg"
  elif luck=="当たり：地鶏たまごのとろ～りクリームパン70％off":
    image = "70off.jpg"
  elif luck=="当たり：外はさっくり中はもちもち山形食パン60％off":
    image = "60off.jpg"
  elif luck=="当たり：たっぷりチョコレートのコルネ半額":
    image = "hangaku.jpg"
  elif luck=="当たり：スイートコーンのぴよぴよちぎりパン50％off":
    image = "50off.jpg"  
  elif luck=="当たり：ひんやり紫イモのモンブラン40％off":
    image = "40off.jpg"
  elif luck=="当たり：あっかんベーコンサンド30％off":
    image = "30off.jpg"
  elif luck=="当たり：国産ライ麦100％ハードブレッド20％off":
    image = "20off.jpg"

  st.image("loading.jpg", caption=f"　↓↓↓{name}さんの{date}のクーポンはこちら★会計時に画面を提示してください★↓↓↓", use_column_width=True)
  time.sleep(2)

  st.write(luck)
  st.image(image, use_column_width=True)

  if st.button("リセット"):
    placeholder = st.empty()
    placeholder.empty()
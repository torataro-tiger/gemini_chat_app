# gemini_chat_app
Geminiによる簡易チャットアプリ用

## 動作方法
```
streamlit run .\run.py --server.port 8080
```
## 使用開始方法
Google AI StudioよりAPIキーを取得し、左のサイドバーのAPI keyに貼り付ける。

## 機能
実験的にGeminiを使えるように以下の機能を備える。
- モデル選択 ("gemini-1.5-flash", "gemini-1.5-pro")
- 温度の変更
- Top_pの調整
- Top_kの調整

## メモ
`ConversationChain`は非推奨とのこと。`RunnableWithMessageHistory`に置き換えの必要あり。
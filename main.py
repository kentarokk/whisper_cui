import whisper

models = ["tiny", "base", "small", "medium", "large"]

print("whisper：処理を開始します。")
print("最初に使用するモデルを選択します。次の５つの数字から選択して入力してください。")
print("1:tiny, 2:base, 3:small, 4:medium, 5:large")


while True:
    model_no = int(input())
    if model_no in [1, 2, 3, 4, 5]:
        selected_model = models[model_no - 1]
        print(selected_model, "が選択されました。")
        break
    else:
        print("適切な数字を選んでください。")

print("モデルをダウンロードします。")
model = whisper.load_model(selected_model)

print("文字起こしをする音声ファイルのパスを入力してください。")

filepath = input()

print("処理を開始します。しばらくお待ちください。")
result = model.transcribe(filepath, fp16=False)

with open('./output.txt', 'w') as f:
    f.write(result["text"])

print("処理が完了しました。プログラムを終了します。")

# 編集ソフトAviUtl専用(exoファイル)　自動字幕プログラム

#ローカルの場合はターミナルで下記のコマンドでwhisper(文字起こしソフト)をダウンロード
# !pip install git+https://github.com/openai/whisper.git
import os
import subprocess
import whisper
from decimal import Decimal, ROUND_HALF_UP
import binascii
import textwrap
import wcwidth


#ローカルで実行する場合はlocalVideo_path=video_path

#字幕をつけたい動画のパス(英語推奨、\に注意)
video_path = "/content/drive/MyDrive/colab/videos/カット済み/outVideo004.mov"
#作りたいexoファイルのパス
outputEXO_path = "/content/drive/MyDrive/colab/videos/字幕素材/ComMovie004.exo"
#一時的な音声ファイル(後に削除)
audio_path = "/content/drive/MyDrive/colab/videos/カット済み/outAudio004.wav"
#ローカルPCの動画パス
localVideo_path = "C:\\Users\\raing\\8_proProgram\\8_autoCut\\cutOK004.mp4"
#字幕の精度を決める。largeは高精度で時間がかかる(ノートPC非推奨)。tinyは低精度で処理速度が最速。smallが中間。  GPU環境下でlarge推奨
decideModel = "large"

#音声変換
command = ["ffmpeg", "-i", video_path, "-ac", "1", "-ar", "44100", "-acodec", "pcm_s16le", audio_path]
result = subprocess.run(command, stderr=subprocess.PIPE, text=True)

#動画のパスが正しいかチェック
def check_video_file(file_path):
    try:
        # 動画ファイルの拡張子リスト（必要に応じて他の拡張子も追加）
        video_extensions = ['.mp4', '.avi', '.mov', '.mkv', '.wmv']

        # ファイルの拡張子を取得
        if any(file_path.lower().endswith(ext) for ext in video_extensions):
            print(f"{file_path} は有効な動画ファイルです。")
        else:
            raise ValueError("指定されたファイルは動画ファイルではありません。")
    except ValueError as e:
        print(e)
#exoファイルのパスが正しいかチェック
def check_exo_file(file_path):
    try:
        # exoファイルかどうかを確認
        if file_path.lower().endswith('.exo'):
            print(f"{file_path} は有効なEXOファイルです。")
        else:
            raise ValueError("指定されたファイルはEXOファイルではありません。")
    except ValueError as e:
        print(e)

#文章の横幅が長いときに２行(以上)にする。切りのいいところで分割(日本語は低精度)
def textSlice(text):
    #幅を算出
    textWidth = sum(wcwidth.wcwidth(c) for c in text)

    #幅が大きいほど１行の文字数を増やす。
    if textWidth >60:
        char_limit = len(text)//2 +1
    else:
        char_limit = len(text)

    #テキストに改行を加える
    wrapped_text = textwrap.fill(text, width=char_limit)
    return wrapped_text

#テキストをAviUtl仕様に変換
# ① text をUTF-16でエンコード
# ②①を16進数文字列に変換
# ③②の文字数が4096になるように0埋め
def textConversion(text):
    # UTF-16にエンコード＆16進数文字列(bytes)に変換
    byte_hex = binascii.hexlify(text.encode('UTF-16'))
    # デコード 最初の無駄を省き、16進数文字列を作る
    str_hex = byte_hex.decode()[4:]
    # 4096文字分の固定長形式にするため0埋め
    result = str_hex + "0" * (4096 - len(str_hex))
    return result


#テキストの幅が広いほど字幕の座標を左にする
def find_closest_result(text):
    #文字数とx軸の比
    # data = {
    #     30: -730,
    #     25: -660,
    #     20: -580,
    #     15: -500,
    #     10: -450,
    #     5: -400
    # }
    #幅を算出
    textWidth = sum(wcwidth.wcwidth(c) for c in text)


    data = {
    10:  -70,
    14:  -154,
    26:  -266,
    27:  -288,
    31:  -612,
    33:  -340,
    34:  -640,
    35:  -648,
    36:  -648,
    37:  -410,
    38:  -432,
    39:  -406,
    41:  -468,
    47:  -530,
    49:  -852,
    50:  -550,
    54:  -700,
    56:  -670,
    58:  -722,
    60:  -688,
    61:  -356,
    64:  -580,
    66:  -500
    }



    keys = list(data.keys())
    closest_num = min(keys, key=lambda x: abs(x - textWidth))
    return data[closest_num]










#ファイルのパスが正しいか確認
check_video_file(video_path)
check_exo_file(outputEXO_path)







#動画を音声に変換
command = ["ffmpeg", "-i", video_path, "-ac", "1", "-ar", "44100", "-acodec", "pcm_s16le", audio_path]
result = subprocess.run(command, stderr=subprocess.PIPE, text=True)






# while not os.path.exists(audio_path):
#     time.sleep(1)


#音声を文字起こし
model = whisper.load_model(decideModel)
result = model.transcribe(audio_path)

#exoファイルの動画と音声部分を記載
dflText = f"[exedit]\n\
width=1920\n\
height=1080\n\
rate=30\n\
scale=1\n\
length=3272\n\
audio_rate=44100\n\
audio_ch=2\n\
[0]\n\
start=1\n\
end=3272\n\
layer=1\n\
group=1\n\
overlay=1\n\
camera=0\n\
[0.0]\n\
_name=動画ファイル\n\
再生位置=1\n\
再生速度=100.0\n\
ループ再生=0\n\
アルファチャンネルを読み込む=0\n\
file={localVideo_path}\n\
[0.1]\n\
_name=標準描画\n\
X=0.0\n\
Y=33.0\n\
Z=0.0\n\
拡大率=211.00\n\
透明度=0.0\n\
回転=0.00\n\
blend=0\n\
[1]\n\
start=1\n\
end=3272\n\
layer=2\n\
group=1\n\
overlay=1\n\
audio=1\n\
[1.0]\n\
_name=音声ファイル\n\
再生位置=0.00\n\
再生速度=100.0\n\
ループ再生=0\n\
動画ファイルと連携=1\n\
file={localVideo_path}\n\
[1.1]\n\
_name=標準再生\n\
音量=100.0\n\
左右=0.0"

with open(outputEXO_path, 'w',encoding="Shift_jis") as file:
        file.write(dflText)






#残りのexoファイルの中身(字幕部分)を追記
for i,data in enumerate(result['segments']):
    convertedText = textConversion(data["text"])
    xPos = find_closest_result(data["text"])

    #下記のstart,endは秒数を30fps換算して四捨五入

    resultStatement = f"[{i+2}]\n\
start={Decimal(data['start']*30).quantize(Decimal('0'), ROUND_HALF_UP)+1}\n\
end={Decimal(data['end']*30).quantize(Decimal('0'), ROUND_HALF_UP)}\n\
layer={i%2+3}\n\
overlay=1\n\
camera=0\n\
[{i+2}.0]\n\
_name=テキスト\n\
サイズ=60\n\
表示速度=0.0\n\
文字毎に個別オブジェクト=0\n\
移動座標上に表示する=0\n\
自動スクロール=0\n\
B=0\n\
I=0\n\
type=0\n\
autoadjust=0\n\
soft=1\n\
monospace=0\n\
align=0\n\
spacing_x=0\n\
spacing_y=0\n\
precision=1\n\
color=ffffff\n\
color2=000000\n\
font=MS UI Gothic\n\
text={convertedText}\n\
[{i+2}.1]\n\
_name=標準描画\n\
X={xPos}\n\
Y=400.0\n\
Z=0.0\n\
拡大率=100.00\n\
透明度=0.0\n\
回転=0.00\n\
blend=0"

    with open(outputEXO_path, 'a',encoding="Shift_jis") as file:
        file.write("\n"+resultStatement)

#音声ファイルを削除
os.unlink(audio_path)

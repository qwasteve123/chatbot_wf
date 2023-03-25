def zen_to_hankaku(text):
    """
    Turn to normal english.
    """
    # 元の文字列
    # text = "！＂＃＄％＆＇（）＊＋，－．／０１２３４５６７８９：；＜＝＞？＠ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ［＼］＾＿｀>？＠ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ｛｜｝～"

    # 変換
    return text.translate(str.maketrans({chr(0xFF01 + i): chr(0x21 + i) for i in range(94)}))

    # 結果
    # '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`>?@abcdefghijklmnopqrstuvwxyz{|}~'


def han_to_zenkaku(text):

    # 元の文字列("と\の記号は「\"」「\\」としてエスケープしています。
    # text = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

    # 変換
    return text.translate(str.maketrans({chr(0x0021 + i): chr(0xFF01 + i) for i in range(94)}))

    # 結果
    # '！＂＃＄％＆＇（）＊＋，－．／０１２３４５６７８９：；＜＝＞？＠ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ［＼］＾＿｀ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ｛｜｝～'

if __name__ == "__main__":
    print(zen_to_hankaku('ｐｙｔｈ'))
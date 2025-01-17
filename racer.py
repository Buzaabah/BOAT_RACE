#!/usr/bin/env python3
import struct

layout = (
#key                            ,byte, descriptions
("登番"                          , 4  , "3415"),
("名前漢字"                      , 16 , "松井　繁"),
("名前カナ"                      , 15 , "マツイ シゲル"),
("支部"                          , 4  , "大阪"),
("級"                            , 2  , "A1"),
("年号"                          , 1  , "S（S:昭和, H:平成）"),
("生年月日"                      , 6  , "441111（昭和44年11月11日）"),
("性別"                          , 1  , "1（1:男, 2:女）"),
("年齢"                          , 2  , "44（才）"),
("身長"                          , 3  , "168（cm）"),
("体重"                          , 2  , "50（kg）"),
("血液型"                        , 2  , "O（型 A, B, AB, O）"),
("勝率"                          , 4  , "0756（7.56 小数点以下2桁）"),
("複勝率"                        , 4  , "0459（45.9 小数点以下1桁）"),
("1着回数"                       , 3  , "037（37回）"),
("2着回数"                       , 3  , "019（19回）"),
("出走回数"                      , 3  , "122（122回）"),
("優出回数"                      , 2  , "05（5回）"),
("優勝回数"                      , 2  , "02（2回）"),
("平均スタートタイミング"        , 3  , "016（0.16 小数点以下2桁）"),

("1コース進入回数"               , 3  , "046（46回）"),
("1コース複勝率"                 , 4  , "0739（73.9 小数点以下1桁）"),
("1コース平均スタートタイミング" , 3  , "015（0.15 小数点以下2桁）"),
("1コース平均スタート順位"       , 3  , "240（2.40 小数点以下2桁）"),
("2コース進入回数"               , 3  , "028（28回）"),
("2コース複勝率"                 , 4  , "0429（42.9 小数点以下1桁）"),
("2コース平均スタートタイミング" , 3  , "015（0.15 小数点以下2桁）"),
("2コース平均スタート順位"       , 3  , "270（2.70 小数点以下2桁）"),
("3コース進入回数"               , 3  , "024（24回）"),
("3コース複勝率"                 , 4  , "0417（41.7 小数点以下1桁）"),
("3コース平均スタートタイミング" , 3  , "016（0.16 小数点以下2桁）"),
("3コース平均スタート順位"       , 3  , "270（2.70 小数点以下2桁）"),
("4コース進入回数"               , 3  , "017（17回）"),
("4コース複勝率"                 , 4  , "0471（47.1 小数点以下1桁）"),
("4コース平均スタートタイミング" , 3  , "015（0.15 小数点以下2桁）"),
("4コース平均スタート順位"       , 3  , "320（3.20 小数点以下2桁）"),
("5コース進入回数"               , 3  , "009（09回）"),
("5コース複勝率"                 , 4  , "0222（22.2 小数点以下1桁）"),
("5コース平均スタートタイミング" , 3  , "020（0.20 小数点以下2桁）"),
("5コース平均スタート順位"       , 3  , "330（3.30 小数点以下2桁）"),
("6コース進入回数"               , 3  , "000（00回）"),
("6コース複勝率"                 , 4  , "0000（00.0 小数点以下1桁）"),
("6コース平均スタートタイミング" , 3  , "000（0.00 小数点以下2桁）"),
("6コース平均スタート順位"       , 3  , "000（0.00 小数点以下2桁）"),

("前期級"                        , 2  , "A1"),
("前々期級"                      , 2  , "A1"),
("前々々期級"                    , 2  , "A1"),
("前期能力指数"                  , 4  , "7400（74.00 小数点以下2桁）"),
("今期能力指数"                  , 4  , "7500（75.00 小数点以下2桁）"),
("年"                            , 4  , "2014（2014年2期の成績）"),
("期"                            , 1  , "2（〃）"),
("算出期間（自）"                , 8  , "20131101（2013年11月01日）"),
("算出期間（至）"                , 8  , "20140430（2014年04月30日）"),
("養成期"                        , 3  , "064（64期）"),

("1コース1着回数"                , 3  , "046（46回）"),
("1コース2着回数"                , 3  , "046（46回）"),
("1コース3着回数"                , 3  , "046（46回）"),
("1コース4着回数"                , 3  , "046（46回）"),
("1コース5着回数"                , 3  , "046（46回）"),
("1コース6着回数"                , 3  , "046（46回）"),
("1コースF回数"                  , 2  , "01（1回）"),
("1コースL0回数"                 , 2  , "01（1回）"),
("1コースL1回数"                 , 2  , "01（1回）"),
("1コースK0回数"                 , 2  , "01（1回）"),
("1コースK1回数"                 , 2  , "01（1回）"),
("1コースS0回数"                 , 2  , "01（1回）"),
("1コースS1回数"                 , 2  , "01（1回）"),
("1コースS2回数"                 , 2  , "01（1回）"),

("2コース1着回数"                , 3  , "046（46回）"),
("2コース2着回数"                , 3  , "046（46回）"),
("2コース3着回数"                , 3  , "046（46回）"),
("2コース4着回数"                , 3  , "046（46回）"),
("2コース5着回数"                , 3  , "046（46回）"),
("2コース6着回数"                , 3  , "046（46回）"),
("2コースF回数"                  , 2  , "01（1回）"),
("2コースL0回数"                 , 2  , "01（1回）"),
("2コースL1回数"                 , 2  , "01（1回）"),
("2コースK0回数"                 , 2  , "01（1回）"),
("2コースK1回数"                 , 2  , "01（1回）"),
("2コースS0回数"                 , 2  , "01（1回）"),
("2コースS1回数"                 , 2  , "01（1回）"),
("2コースS2回数"                 , 2  , "01（1回）"),

("3コース1着回数"                , 3  , "046（46回）"),
("3コース2着回数"                , 3  , "046（46回）"),
("3コース3着回数"                , 3  , "046（46回）"),
("3コース4着回数"                , 3  , "046（46回）"),
("3コース5着回数"                , 3  , "046（46回）"),
("3コース6着回数"                , 3  , "046（46回）"),
("3コースF回数"                  , 2  , "01（1回）"),
("3コースL0回数"                 , 2  , "01（1回）"),
("3コースL1回数"                 , 2  , "01（1回）"),
("3コースK0回数"                 , 2  , "01（1回）"),
("3コースK1回数"                 , 2  , "01（1回）"),
("3コースS0回数"                 , 2  , "01（1回）"),
("3コースS1回数"                 , 2  , "01（1回）"),
("3コースS2回数"                 , 2  , "01（1回）"),

("4コース1着回数"                , 3  , "046（46回）"),
("4コース2着回数"                , 3  , "046（46回）"),
("4コース3着回数"                , 3  , "046（46回）"),
("4コース4着回数"                , 3  , "046（46回）"),
("4コース5着回数"                , 3  , "046（46回）"),
("4コース6着回数"                , 3  , "046（46回）"),
("4コースF回数"                  , 2  , "01（1回）"),
("4コースL0回数"                 , 2  , "01（1回）"),
("4コースL1回数"                 , 2  , "01（1回）"),
("4コースK0回数"                 , 2  , "01（1回）"),
("4コースK1回数"                 , 2  , "01（1回）"),
("4コースS0回数"                 , 2  , "01（1回）"),
("4コースS1回数"                 , 2  , "01（1回）"),
("4コースS2回数"                 , 2  , "01（1回）"),

("5コース1着回数"                , 3  , "046（46回）"),
("5コース2着回数"                , 3  , "046（46回）"),
("5コース3着回数"                , 3  , "046（46回）"),
("5コース4着回数"                , 3  , "046（46回）"),
("5コース5着回数"                , 3  , "046（46回）"),
("5コース6着回数"                , 3  , "046（46回）"),
("5コースF回数"                  , 2  , "01（1回）"),
("5コースL0回数"                 , 2  , "01（1回）"),
("5コースL1回数"                 , 2  , "01（1回）"),
("5コースK0回数"                 , 2  , "01（1回）"),
("5コースK1回数"                 , 2  , "01（1回）"),
("5コースS0回数"                 , 2  , "01（1回）"),
("5コースS1回数"                 , 2  , "01（1回）"),
("5コースS2回数"                 , 2  , "01（1回）"),

("6コース1着回数"                , 3  , "046（46回）"),
("6コース2着回数"                , 3  , "046（46回）"),
("6コース3着回数"                , 3  , "046（46回）"),
("6コース4着回数"                , 3  , "046（46回）"),
("6コース5着回数"                , 3  , "046（46回）"),
("6コース6着回数"                , 3  , "046（46回）"),
("6コースF回数"                  , 2  , "01（1回）"),
("6コースL0回数"                 , 2  , "01（1回）"),
("6コースL1回数"                 , 2  , "01（1回）"),
("6コースK0回数"                 , 2  , "01（1回）"),
("6コースK1回数"                 , 2  , "01（1回）"),
("6コースS0回数"                 , 2  , "01（1回）"),
("6コースS1回数"                 , 2  , "01（1回）"),
("6コースS2回数"                 , 2  , "01（1回）"),

("コースなしL0回数"              , 2  , "01（1回）"),
("コースなしL1回数"              , 2  , "01（1回）"),
("コースなしK0回数"              , 2  , "01（1回）"),
("コースなしK1回数"              , 2  , "01（1回）"),
("出身地"                        , 6  , "大阪"),
)



def load_fanXXXX(filename):
    racers = dict()
    with open(filename, "rb") as f:
        while True:
            try:
                racer_id = int(f.read(layout[0][1]))
            except ValueError:
                break
            X = dict()
            for line in layout[1:]:
                X_key = line[0]
                X_value_buf = f.read(line[1])
                try:
                    X_value = float(X_value_buf)
                except ValueError:
                    X_value = X_value_buf.decode("shift-jis")
                X.update({X_key: X_value})
            racers.update({racer_id: X})
            f.read(2) # "\r\n"
    return racers

if __name__ == "__main__":
    racers = load_fanXXXX("./fan1810.txt")
    import IPython;IPython.embed()


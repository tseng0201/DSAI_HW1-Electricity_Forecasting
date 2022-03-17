# DSAI_HW1-Electricity_Forecasting
1.根據維基百科所述「2019年起備轉納入「冷機」供電機組，已非傳統熱機定義（可立即供電的機組）」，所以不考慮2019年前的資訊
2.觀察歷年淨尖峰供電能力發現六日會較低，但淨尖峰供電能力應該只受當下天氣影響不該是六日比較低，故認為台電會嘗試將備轉容量固定在一個定值，但最終結果會受當天實際狀況影響，所以打算使用備轉容量平均值進行預估

3.將每月的備轉容量平均後發現2021年前4月平均備轉容量相近，並以平均值作為預結果其RMSE < 20 ， 於2019 跟 2020 趨勢差異較大，加上疫情時期特殊性故不故考慮2021 的相關資料，同時也可見台電

4.考量到近期解封的狀況，每月平均備轉容量應該與2020、2019相當，呈現逐月上升的趨勢，最終打算已 2022年2月平均備轉容量作為預估基礎， 2020年4月平均備轉容量與2020年2月平均備轉容量比例為進行預估
(2022年3月停電供電以及恢復不穩所以不考慮)

5.基於相信台電會固定一個定值在預估備轉容量上，且這個預估是準確的，為了盡可能準確地找到這個估計值，我把一個月中備轉容量太大或太小的值視為異常代表估計嚴重失誤應該替除，偵測方法選擇使用IsolationForest 進行異常偵測

最終將每個月剃除異常後計算平均, 且為了降低IsolationForest的性將會重複執行100次後取平均

最終預估值 =  2022年2月平均備轉容量 *  2020年4月平均備轉容量 / 2020年2月平均備轉容量

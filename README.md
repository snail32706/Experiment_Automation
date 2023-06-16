## 使用 PyAutoGUI 達到電腦代替人使用 Labview

### code 架構
- 實驗目的:
此實驗的參數變因有power、pulse number、pulse width，為了可以更好的控制變因，
將原先 power dependence 的實驗，fix pulse energy 變因改為 pulse number。

- 程式邏輯:
將Labview 大部分的按鈕相對位置（螢幕解析度為1080p）放在`Labview_Buttom` 中，
先在 OM 下最左邊打一個能量測試的洞，將能量檢測存擋為 'energy_N'，
檢測檔案是否存在，能量是否正常。
開始做實驗，先以較強的能量在最上排打一排標記點，每組不同的 pulse number 相距 1.5Δx， 
將相同的數據做完 RTO 依照 f"row_{experiment_row_number}_n{Shotter_number}  存擋。
檢查檔案存在後，換下一組。
做完一個 row 後，回到原點移動 Δy 並重新設置原點。

### code 細節
- 程式問題
原先以`pygetwindow`切換畫面，因為此 package 不穩定，
因此將切換畫面改由「工作列第一個」與「工作列第二個」控制。
注意: 若畫面已經為第一個工作視窗，點選會將視窗縮小。


### 準備工作
##### - 測試：
    以不同能量的 pulse，看看最弱的雷射可否打出 LIPSS
    # check_energy(abs_file_path, up_data) # 測試檔案時，註解。
    確認 X, Y 移動方向
    
##### - 先前設置
    1. Labview 放在「最左邊」
    2. MAIN 字體邊緣切齊「左上角」
    3. 準備好 最弱的 energy，檔名為 energy_0
    4. 修改 folder 「日期」。

##### - 正式：
    打標記點確認穩定度。
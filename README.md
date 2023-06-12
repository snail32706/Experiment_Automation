## 使用 PyAutoGUI 控制實驗

count_row = 1
#### 打動程序
先在最上排打上記號每三組一行（間隔為 Δx），打完三組換一個 pulse number（間隔為 1.5*Δx）。
每個檔案都會存擋，檔名會是先放在一個 list，每次打洞會等待預設的 delay time, 
然後對 folder 檢查 檔案是否已經存擋，如果已經存擋，則移動 1.5*Δx，並執行下三個洞。
count_row += 1

#### 一排打洞完成後
每當執行到最後一個 list，將回到 "Home" ，並且移動 count_row*Δy。

#### 更改能量
使用最後一個 pulse number 計算能量使否正確，
首先，將 Δx 更改為 0，
然後，將檔名更改為 Read_RTO_energy_{count_row}，並開始執行
經過 delay time, 閱讀剛剛的 Read_RTO_energy_row{count_row}.txt。
確認能量是否在正常的範圍，
若不正確停止程序，並且發出警報聲。

#### 繼續打洞
移動 1.5*Δx。
執行打洞。

### 準備工作
##### - 測試：
    以不同能量的 pulse，看看最弱的雷射可否打出 LIPSS
    # check_energy(abs_file_path, up_data) # 測試檔案時，註解。
    確認 X, Y 移動方向
##### - 開始：
    1. Labview 放在「最左邊」
    2. MAIN 放在「左上角」
    3. 準備好 最弱的 energy，檔名為 energy_0
    4. 修改 folder 「日期」。
    5. check_energy(abs_file_path, up_data)
    
##### - 正式：
    更改
    「# Code_Stop() # 終止程式」 ----> 「 Code_Stop() # 終止程式」


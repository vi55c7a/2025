<p align="center"><font size="6"><b>資料結構 11224117 蕭冠廷</b></font></p>

<p align="center">資料結構 [Python--Stack] 的應用</p>


一、什麼是棧

棧是一個有序集合，根據其特性可以稱為「先進後出」或「後進先出」，其中添加或刪除都發生在同一端，這一端被稱為「棧頂」，與其對應的叫「棧底」。

棧的底部很重要，因為其底部儲存的資料是時間最長的，最近的添加項總是最先會彈出，這種排序原則有時被稱為「LIFO」。

二、棧

1. 棧的可用操作
      Stack() 創建一個空的棧。它不需要參數，並返回一個空棧。

      push(item) 將一個新項添加到棧的頂端。它需要 item 作為參數並不返回任何內容。

      pop() 從棧中刪除頂部項。它不需要參數並返回 item。棧被修改。

      top() 讓你查看頂部項，但不會刪除它。不需要參數。不能修改。

      isEmpty() 測試棧是否為空。不需要參數，並返回布林值。

      size() 返回棧中 item 數量。不需要參數，並返回一個整數。

      clear 清空棧，沒有返回值。


2. 利用 Python 的內置資料結構 List 實現堆疊全部操作
<img width="545" height="739" alt="二" src="https://github.com/user-attachments/assets/8c61353a-9973-4927-92e9-8498f8405278" />

輸出結果

<img width="330" height="202" alt="二結" src="https://github.com/user-attachments/assets/0f44b504-5286-41a4-a3fc-fe1738f69be1" />


      
3.堆疊的使用示例



3-1 進制轉換


<img width="532" height="756" alt="三-1" src="https://github.com/user-attachments/assets/f90daab8-a4e5-4dc9-9906-a2ef9166ca65" />



輸出結果

<img width="1415" height="83" alt="三-1結" src="https://github.com/user-attachments/assets/0319da34-8887-4b00-8284-ad5794aa78ae" />


說明：這是用 List 結構來實現的「棧」，同樣我們可以自己寫一個棧


3-2 自己寫堆疊

<img width="465" height="611" alt="三-2" src="https://github.com/user-attachments/assets/402637bf-1ef5-4868-93af-bbed80c73164" />
<img width="352" height="402" alt="三-2-" src="https://github.com/user-attachments/assets/812134ff-b477-4115-b188-fd21c6f41cf6" />


輸出結果

<img width="830" height="191" alt="三-2結" src="https://github.com/user-attachments/assets/2b247947-15bd-4982-9257-b19d010f59a7" />

說明：

1.上面所定義的堆疊，是由 top 指針指向一個完整的 Node 實例

2.定義一個堆疊，使用指針控制其最頂端的位置


3-3 程式碼—將數學表達式轉成前序式

<img width="463" height="650" alt="三-3" src="https://github.com/user-attachments/assets/9d820a91-22ce-416c-83a1-7641578e6cea" />

<img width="864" height="749" alt="三-3-" src="https://github.com/user-attachments/assets/17c2b42b-f683-4a15-ae28-c9dd5eb72068" />



輸出結果

<img width="783" height="72" alt="三-3結" src="https://github.com/user-attachments/assets/bc457ada-1b4f-4399-a4bf-a29e6a5e0989" />

說明：

1.程式碼主要是將數學運算中的中序轉換成前序表示法

2.在程式中以堆疊方式來進行操作，有效儲存運算符號、運算元等資料類型與次序位置來進行計算，結果再以人性、直覺方式進行完成。


3-4 程式碼—後序表達式（逆波蘭式）

<img width="997" height="943" alt="三-4" src="https://github.com/user-attachments/assets/18be9101-1208-4c69-8f01-1925ff7a161e" />

<img width="539" height="826" alt="三-4-" src="https://github.com/user-attachments/assets/271d8db4-f449-4c09-b199-16d2ed7183c9" />


輸出結果

<img width="699" height="203" alt="三-4結" src="https://github.com/user-attachments/assets/1919ce58-fe94-4a19-acbf-555e3fc1d98b" />


說明：

1.程式碼是將中序數學運算轉換成了後序數學表示法

2.在程式中以堆疊方式來進行操作，模擬運算順序，遇到符號就依照堆疊的資料與次位置推進並進行計算（如堆疊「放」與「取」操作），結果再以人性、直覺方式完成

3.後序表達式適合用來做計算作業（執行中序轉後序 → 執行後序計算）




總結：使用堆疊實作數學表達式處理（中序 ➜ 前序／後序）




一、堆疊（Stack）基本實作


1.利用**單向鏈結串列（linked list）**實作堆疊結構。


2.提供 push() 與 pop() 操作，遵循 先進後出（LIFO） 的邏輯。


3.適合用來處理運算式的括號對應與運算順序控制。




二、前序表達式（Prefix Expression）處理


功能說明：

1.將一般中序表達式（如：1 + (3 + 4) * 2）轉為前序（如：+ 1 * + 3 4 2）。

2.並且利用堆疊即時進行運算結果的計算。


實作重點：

1.利用反轉字串與交換括號的技巧（prefix reverse）。

2.結合堆疊實作括號範圍的運算處理。

3.搭配 compute_exec() 函式動態執行 + - * / 運算。


適用場景：

表達式需要轉換成前序表示的情境，例如使用某些語言處理器或需要做語法樹建構。




三、後序表達式（Postfix Expression / 逆波蘭式）處理


功能說明：

1.將中序表達式轉換成後序（如：1 3 4 + 2 * +），同樣支援運算處理。

2.適合用來做堆疊式直接計算。


實作重點：

1.經過括號與運算符轉換後，使用堆疊組合後序格式。

2.結合運算處理，逐步將結果推出。


適用場景：

1.程式語言的運算器（expression evaluator）。

2.後序格式更容易讓電腦解譯與直接計算，不需要考慮括號。


### 總結比較

| 類別       | 中序表達式             | 前序轉換               | 後序轉換             |
|------------|------------------------|------------------------|----------------------|
| 表達形式   | `1 + (3 + 4) * 2`      | `+ 1 * + 3 4 2`        | `1 3 4 + 2 * +`      |
| 轉換方式   | 人類可讀，但難處理     | 先處理最外層，再向內遞迴 | 可用堆疊直接計算     |
| 計算難度   | 高                    | 中等                   | 最低                 |
| 適用範圍   | 一般數學              | 語法樹、遞迴計算         | 編譯器、計算器       |











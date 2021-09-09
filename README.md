##環境
ubuntu 18.04 LTS <br>
python = 3.6.9 <br>
scrapy = 2.5.0 <br>
requests = 2.18.4 <br>

##指令(切到最上層目錄) <br>
scrapy crawl hater

##轉存成檔案(csv/json)<br>
scrapy crawl hater -o csv / scrapy crawl hater -o json

## 建議建立虛擬環境
ubuntu建立虛擬環境 <br>
安裝virtualenv(以python3為例) <br>
sudo apt-get install python3-pip <br>
pip3 install virtualenv <br>
which python3 <br>
virtualenv -p <python路徑> <想創建的環境名稱> <br>
啟動虛擬環境 <br>
source <環境名稱>/bin/activate <br>
關閉虛擬環境 <br>
(<環境名稱>)$ deactivate <br>


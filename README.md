<div align='center'>
    <h1><b>🚀 TABCSVLY 🚀</b></h1>
    <img src='./docs/icon.png' width='250' height='250' />
    <p>convert HTML tables into CSV files</p>
</div>

![Python](https://badgen.net/badge/Python/3.10.9/blue?)
![Docker](https://badgen.net/badge/Docker/23.0.1/cyan?)
![Size](https://img.shields.io/github/languages/code-size/ton1czech/tabcsvly.svg)
![License](https://img.shields.io/github/license/ton1czech/tabcsvly.svg)
![GitHub version](https://badge.fury.io/gh/ton1czech%2Ftabcsvly.svg)

</div>

---

## 💾 **ABOUT**

**easy to use** command line convertor (html table -> csv)

With this application, users can simply enter url to the table and the application will convert it to a `CSV` file that can be easily opened and edited in spreadsheet programs such as `Microsoft Excel` or `Google Sheets`. This can be particularly useful for users who need to extract data from web pages or generate reports from `HTML tables`.

<br />

---

## 🗒️ **INSTALLATION**

```bash
# Option 1 (run locally):
# Step 1: Clone the repo
git clone https://github.com/ton1czech/tabcsvly

# Step 2: CD into cloned repo
cd tabcsvly

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Run calcmachine
python src/tabcsvly.py

----------------------------------------------------

# Option 2 (run locally via Docker):
# Step 1: Clone the repo
git clone https://github.com/ton1czech/tabcsvly

# Step 2: CD into cloned repo
cd tabcsvly

# Step 3: Build the app
docker build -t tabcsvly .

# Step 4: Run the app
docker run -ti tabcsvly

----------------------------------------------------

# Option 3 (run remotely via Docker):
# Step 1: Run the app
docker run -ti ton1czech/tabcsvly:0.9.0
```

---

## 🔎 **SHOWCASE**

##### HTML TABLE

<a href='https://en.wikipedia.org/wiki/BMW_3_Series_(F30)#Engines' target="_blank">table link</a>

<img src='https://imgur.com/EB6864Y.png' />

##### .CSV OUTPUT

<img src='https://imgur.com/xFhqGmz.png' />

```csv
Model,Years,Engine- turbo,Power,Torque
316i,2012–2015,N13B16 straight-4,"100 kW (134 hp) at 4,400–6,450 rpm","220 N⋅m (160 lbf⋅ft) at 1,350–4,300 rpm"
318i,2015–2019,B38B15 straight-3,"100 kW (134 hp) at 4,400–6,000 rpm","220 N⋅m (160 lbf⋅ft) at 1,250–4,300 rpm"
320i,2012–2015,N20B20 straight-4,"135 kW (181 hp) at 5,000 rpm","270 N⋅m (200 lbf⋅ft) at 1,250–4,500 rpm"
320i,2015–2019,B48B20 straight-4,"135 kW (181 hp) at 5,000–6,500 rpm","270 N⋅m (200 lbf⋅ft) at 1,350–4,600 rpm"
320i ED,2012–2015,N13B16 straight-4,"125 kW (168 hp) at 4,800–6,450 rpm","250 N⋅m (180 lbf⋅ft) at 1,500–4,500 rpm"
328i,2012–2015,N20B20 straight-4,"180 kW (241 hp) at 5,000–6,500 rpm","350 N⋅m (260 lbf⋅ft) at 1,250–4,800 rpm"
330i,2015–2019,B48B20 straight-4,"185 kW (248 hp) at 5,200–6,500 rpm","350 N⋅m (260 lbf⋅ft) at 1,450–4,800 rpm"
335i,2012–2015,N55B30M0 straight-6,"225 kW (302 hp) at 5,800–6,400 rpm","400 N⋅m (300 lbf⋅ft) at 1,200–5,000 rpm"
340i,2015–2019,B58B30M0 straight-6,"240 kW (322 hp) at 5,500–6,500 rpm","450 N⋅m (330 lbf⋅ft) at 1,380–5,000 rpm"
M3 (F80),2014–2020,S55B30 straight-6,"317 kW (425 hp) at 5,500–7,300 rpm","550 N⋅m (410 lbf⋅ft) at 1,850–5,500 rpm"
M3 Comp (F80),2016–2020,S55B30 straight-6,"331 kW (444 hp) at 7,000 rpm","550 N⋅m (410 lbf⋅ft) at 1,850–5,500 rpm"
M3 CS (F80),2018-2020,S55B30 straight-6,"338 kW (453 hp) at 6,250 rpm","600 N⋅m (440 lbf⋅ft) at 4,000–5,380 rpm"
```

<br />

---

## 💻 **TECHNOLOGIES**

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-130654?style=for-the-badge&logo=pandas&logoColor=white)

---

## 📎 **LICENSE**

MIT License

Copyright © 2022-2023 Daniel Anthony Baudyš (ton1czech)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

<br />

---

## 📌 **CREDITS**

##### Daniel Anthony Baudyš (ton1czech)

programmer, investor and god 🤫

<img alt='ton1czech' src='https://avatars.githubusercontent.com/u/66372827?v=4' />

[<img alt="Github" src="https://img.shields.io/badge/@ton1czech-%23181717.svg?style=for-the-badge&logo=github&logoColor=white" />](https://github.com/ton1czech)
[<img alt="Twitter" src="https://img.shields.io/badge/@ton1czech-%231DA1F2.svg?style=for-the-badge&logo=Twitter&logoColor=white" />](https://twitter.com/ton1czech)
[<img alt="Instagram" src="https://img.shields.io/badge/@ton1czech-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white" />](https://instagram.com/ton1czech)
[<img alt="Youtube" src="https://img.shields.io/badge/@ton1czech-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white" />](https://www.youtube.com/channel/UCblA_CnykG2Dw_6IMwZ9z9A)

[<img alt="Reddit" src="https://img.shields.io/badge/@ton1czech-FF4500?style=for-the-badge&logo=reddit&logoColor=white" />](https://reddit.com/user/)
[<img alt="TikTok" src="https://img.shields.io/badge/@t0n1czech-%23000000.svg?style=for-the-badge&logo=TikTok&logoColor=white" />](https://www.tiktok.com/@ton1czech)
[<img alt="Gitlab" src="https://img.shields.io/badge/@ton1czech-%23181717.svg?style=for-the-badge&logo=gitlab&logoColor=white" />](https://gitlab.com/ton1czech)
[<img alt="Dribbble" src="https://img.shields.io/badge/@ton1czech-EA4C89?style=for-the-badge&logo=dribbble&logoColor=white" />](https://dribbble.com/ton1czech)

[<img alt="Stack Overflow" src="https://img.shields.io/badge/@ton1czech-FE7A16?style=for-the-badge&logo=stack-overflow&logoColor=white" />](https://stackoverflow.com/users/15073347/ton1czech)
[<img alt="Discord" src="https://img.shields.io/badge/@ton1czech%238028-%237289DA.svg?style=for-the-badge&logo=discord&logoColor=white" />]()
[<img alt="Steam" src="https://img.shields.io/badge/@ton1czech-%23000000.svg?style=for-the-badge&logo=steam&logoColor=white" />](https://steamcommunity.com/id/ton1czech)
[<img alt="Spotify" src="https://img.shields.io/badge/@ton1czech-1ED760?style=for-the-badge&logo=spotify&logoColor=white" />](https://open.spotify.com/user/212btc3myry7hwb45aybf4efi)

# Taxi
Searching and creating customer information
פרויקט זיהוי לקוחות
___
להרצת הפרויקט בשרת מקומי יש להתקין גשר שמאזין לבקשות גלובליות ושולח אותם לפורט
*http://localhost:5000/*
___
##### הוראות התקנת ngrok. (גשר)
.
## MacOS
&nbsp;
##### &#160;&#160;&#160;&#160;&#160;  ****Homebrew****
```
brew install ngrok
```
ואח״כ
```

ngrok config add-authtoken 2vmOwEusjxaWAuK2Xcej28zAUB6_6C2v2UXoaXj8YWax5ghnY
```
&nbsp;
##### &#160;&#160;&#160;&#160;&#160;  ****Download****


[הורד עבור Apple Silicon](https://dashboard.ngrok.com/get-started/setup/macos)
.
[הורד עבור אינטל](https://dashboard.ngrok.com/get-started/setup/macos)
ואח״כ בטרמינל
```
ngrok config add-authtoken 2vmOwEusjxaWAuK2Xcej28zAUB6_6C2v2UXoaXj8YWax5ghnY
```
&nbsp;
##### &#160;&#160;&#160;&#160;&#160;  ****הפעלה****
הרץ בטרמינל הקרוב לביתך
לקבלת תחום ארעית הרץ
```
ngrok http http://localhost:5000
```
לקבלת תחום קבוע [כנס לngrok](https://dashboard.ngrok.com/get-started/setup/macos#:~:text=%D7%AA%D7%97%D7%95%D7%9D%20%D7%90%D7%A8%D7%A2%D7%99%D7%AA-,%D7%93%D7%95%D7%9E%D7%99%D7%99%D7%9F,-%D7%A1%D7%98%D7%98%D7%99)
ובחר באפשרות תחום קבוע
___
אחרי ביצוע clone הרצת השרת תתבצע בפורט 5000
http://localhost:5000/

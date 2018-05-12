@echo off
"C:\Users\pub\AppData\Local\VanDyke Software\SecureCRT\SecureCRT.exe" /script "C:\LineCheck\oa_1.vbs"
"C:\Users\pub\AppData\Local\VanDyke Software\SecureCRT\SecureCRT.exe" /script "C:\LineCheck\oa2_1.vbs" 
python C:\LineCheck\linecheck.py
exite
exit
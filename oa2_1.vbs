# $language = "VBScript"
# $interface = "1.0"
Sub Main
        crt.Screen.Synchronous=true
        crt.Session.Connect "/TELNET xxx.xx.xx.xx"
	crt.Screen.WaitForString "Username:"
	crt.Screen.Send "用户名" & chr(13)
	crt.Screen.WaitForString "Password: "
	crt.Screen.Send "密码" & chr(13)
	crt.Screen.WaitForString "CNTZRT01092>"
	crt.Screen.Send "show ip interface brief " & chr(124) & " i :15" & chr(13)
        crt.Screen.WaitForString "CNTZRT01092>"
        crt.Sleep 3000
        crt.Session.Disconnect
        crt.Quit
End Sub
                             

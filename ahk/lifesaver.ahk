#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


	Send, {ScrollLock}
	Send, {ScrollLock}

	#SingleInstance,Force
	SetWinDelay,0
	SetBatchLines,-1
	CoordMode,Mouse,Screen
	SetCapsLockState, AlwaysOff
	SetNumLockState, AlwaysOn
	SetScrollLockState, On
	
	; disable win+F1 help=================================================================================
	#F1::Return
	
	; open folder ====================================================================0
	F13:: Run,R:\Projekte\Level3\E-Projekte\LehrlingsProjekte\_jn_TAF-71
	
	;Move inactive window around =========================================================================
	!LButton::	
	MouseGetPos,oldmx,oldmy,mwin,mctrl
	Loop
	{
	  GetKeyState,lbutton,LButton,P
	  GetKeyState,alt,Alt,P
	  If (lbutton="U" Or alt="U")
		Break
	  MouseGetPos,mx,my
	  WinGetPos,wx,wy,ww,wh,ahk_id %mwin%
	  wx:=wx+mx-oldmx
	  wy:=wy+my-oldmy
	  WinMove,ahk_id %mwin%,,%wx%,%wy%
	  oldmx:=mx
	  oldmy:=my
	}
	Return
	SC16D::DllCall("LockWorkStation")	;LaunchMedia :: Lock win
	; =================================Close Window on Middle Click =====================================
	~MButton::
	  SetBatchLines, -1
	  CoordMode, Mouse, Screen
	  SetMouseDelay, -1 ; no pause after mouse clicks
	  SetKeyDelay, -1 ; no pause after keys sent
	  MouseGetPos, ClickX, ClickY, WindowUnderMouseID
	  WinActivate, ahk_id %WindowUnderMouseID%

	  ; WM_NCHITTEST
	  SendMessage, 0x84,, ( ClickY << 16 )|ClickX,, ahk_id %WindowUnderMouseID%
	  WM_NCHITTEST_Result =%ErrorLevel%
	  

	; Title Bar click closes in below lines
	  If WM_NCHITTEST_Result in 2,3,8,9,20,21 ; in titlebar enclosed area - top of window
		{
		PostMessage, 0x112, 0xF060,,, ahk_id %WindowUnderMouseID% ; 0x112 = WM_SYSCOMMAND, 0xF060 = SC_CLOSE
		}
	return
	
	; counter 9K > variabeln nummerieren =================================================================
	CapsLock & b::
	InputBox,times,Set highest number,,,200,100,,,,3
	i:=1
	Loop, %times%
	{
		Send,{BACKSPACE}
		Send,%i%
		Send,{ESC} ; Avoid popups from distracting down key
		Send,{DOWN}
		if i > 9
		{
			Send,{LEFT}
		}
		if i > 99
		{
			Send,{LEFT}
		}
		i:=i+1
	}
	return	
	
	; copier 9k > Zeile Kopieren==========================================================================
	CapsLock & v::
	InputBox,times,How often?,,,200,100,,,,3
	clipBackup := clipboard
	clipboard := 0
	Sleep 100
	Send ^c
	Sleep 100
	Loop, %times%
	{
		Send ^v
		Sleep 5
		Send {ENTER}
		Sleep 5
	}
	clipboard := clipBackup
	return
	
	
	;=====================================================================================================
	; ==============CAPSLock Modifier actions=============================================================
	;=====================================================================================================
	
	; used: a,b,c,d,e,f,g,h,i,j,,l,m,n,o,p,,r,s,t,u,v,,x,y,z
	;     : 1,2,3,4,,,,,,0
	
	CapsLock & a:: Winset, Alwaysontop, , A	; keep Window always on Top
	CapsLock & u::
	cb := Clipboard
	Clipboard = ; Empty the clipboard so that ClipWait has something to detect
	SendInput, ^c ;copies selected text
	ClipWait
	StringReplace, OutputText, Clipboard, `r`n, `n, All ;Fix for SendInput sending Windows linebreaks 
	StringUpper, OutputText, OutputText
	SendRaw % OutputText
	VarSetCapacity(OutputText, 0) ;free memory
	Clipboard := cb
	return
	CapsLock & i::Send,for(uint8_t i = 0; i < times; i++){{}{ENTER}{ENTER}	
	CapsLock & t::Run,https://www.deepl.com/de/translator	; launch deepL
	CapsLock & s::	; search on google
		cb := clipboard
		SendInput, ^c
		Sleep 50
		search := clipboard
		clipboard := cb
		search = %search%	; trim (leading) spaces
		http := ""	; if starting with http, dont search on google
		StringLeft, http, search, 4
		if(http == "http"){
			Run, %search%
		}
		else{
			Run, http://www.google.com/search?q=%search%
		}
	return
	CapsLock & h::	; **********************toggle hidden Files in expolrer ******************************
		RegRead, HiddenFiles_Status, HKEY_CURRENT_USER, Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced, Hidden
		If HiddenFiles_Status = 2 
		RegWrite, REG_DWORD, HKEY_CURRENT_USER, Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced, Hidden, 1
		Else
		RegWrite, REG_DWORD, HKEY_CURRENT_USER, Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced, Hidden, 2
		send, {F5}
	return
	CapsLock & n:: insertTime("hh:mm")	; insert time
	CapsLock & y:: 
		FormatTime, CurrentDateTime,, dd.MM.yyyy
		SendInput %CurrentDateTime%
	return
	CapsLock & f:: ; serch in CTRL+F
		cb := clipboard
		Send, ^c
		Sleep 50
		Send, ^f
		Sleep 50
		Send, ^v
		Sleep 50
		clipboard := cb
	return
	CapsLock & e::	; translate to english
		TempClipboard:=Clipboard
		Clipboard := ""
		SendInput, ^c
		ClipWait, 1
		if ErrorLevel
		  Return
		Translation:= GoogleTranslate(Clipboard,"auto","en").main
		SENDInput,%Translation%
		Clipboard:=TempClipboard
	Return
	CapsLock & g::  ; translate to german
		TempClipboard:=Clipboard
		Clipboard := ""
		SendInput, ^c
		ClipWait, 1
		if ErrorLevel
		  Return
		Translation:= GoogleTranslate(Clipboard,"auto","de").main
		SENDInput,%Translation%
		Clipboard:=TempClipboard
	Return
	CapsLock & 0::Send,10_Sitzungszimmer ZOL, TON-E, F 221, Securiton, E	; sitzungszimmer F221
	CapsLock & F5::Reload ; reload this script
	CapsLock & SC029::Send •{SPACE} ;CapsLock & °
	
	Shift & SC028::Send, {ASC 0196}	; Ä
	Shift & SC027::Send, {ASC 0214} ; Ö
	Shift & SC01A::Send, {ASC 0220}	; Ü
	
	CapsLock & j::
		Send,_jn_
	return
	CapsLock & l::	; termin für Lernstunde
		AppointmentItem := ComObjActive("Outlook.Application").CreateItem("1")
		AppointmentItem.Subject := "Lernstunde"
		AppointmentItem.Location := "10_Sitzungszimmer ZOL, TON-E, F 221, Securiton, E"
		AppointmentItem.Duration := 60
		AppointmentItem.Display
	return
	CapsLock & 1::Send,8:00
	CapsLock & 2::Send,12:00
	CapsLock & 3::Send,13:00
	CapsLock & 4::Send,17:00
	CapsLock & r::Run,https://www.distrelec.ch/de/passive-bauelemente/widerstaende/chip-smd-widerstaende/c/cat-DNAV_PL_030701
	;CapsLock & c::Run,https://www.distrelec.ch/de/passive-bauelemente/kondensatoren/keramikkondensatoren/keramische-vielschichtkondensatoren-smd/c/cat-DNAV_PL_03020303
	CapsLock & c::Run,https://web2.0rechner.de/
	CapsLock & d:: ; search on distrelec
		TempClipboard:=Clipboard
		Clipboard := ""
		SendInput, ^c
		ClipWait, 1
		stringer := Clipboard
		vText := JEE_StrReplaceChars(stringer, "-", "", vCount)	;remove "-"
		Run,https://www.distrelec.ch/de/p/%vText%?track=true&no-cache=true
		Clipboard:=TempClipboard
	return
	CapsLock & m:: ; search on mouser
		TempClipboard:=Clipboard
		Clipboard := ""
		SendInput, ^c
		ClipWait, 1
		vText := Clipboard
		Run,https://www.mouser.ch/Search/Refine?Keyword=%vText%
		Clipboard:=TempClipboard
	return
	CapsLock & o::
		Send,t
		Sleep,50
		Send,g
		;Sleep,50
		;Send,h
	return
	CapsLock & p::	; save and start python script
		Send, --proxy http://jaegnil1:PASSWORD@iproxy.e.securiton.int:8080
	return
	CapsLock & x::
		MouseClick,Left
		Sleep 50
	return
	;spam down del
	CapsLock & z::
		Send,{DOWN}
		Sleep 20
		Send,{DEL}
		Sleep,20
	return
	; AppsKey Modifier actions============================================================================
	AppsKey::return
	AppsKey & a::Send,α
	AppsKey & b::Send,β
	AppsKey & c::Send,γ
	AppsKey & d::Send,δ
	AppsKey & e::Send,ε
	AppsKey & g::Send,χ
	AppsKey & h::Send,θ
	AppsKey & i::Send,ι
	AppsKey & k::Send,κ
	AppsKey & l::Send,λ
	AppsKey & m::Send,μ
	AppsKey & n::Send,η
	AppsKey & o::Send,Ω
	AppsKey & p::Send,π
	AppsKey & r::Send,ρ
	AppsKey & s::Send,σ
	AppsKey & t::Send,τ
	AppsKey & u::Send,υ
	AppsKey & v::Send,φ
	AppsKey & w::Send,ω
	AppsKey & x::Send,ξ
	AppsKey & y::Send,ψ
	AppsKey & z::Send,ζ

	;remove annoying double tap on ^ / ~ =================================================================
	SC00D::Send,{^}{Space}
	!^SC00D::Send,{~}{Space}
	
	; PrintScrn ==========================================================================================
	SC137::Send +#{s}
	
	; Spotify ============================================================================================
	;play/pause
	;CapsLock & F2::PostMessage, 0x319,, 0xE0000,, ahk_exe Spotify.exe

	;next song
	;CapsLock & F3::PostMessage, 0x319,, 0xB0000,, ahk_exe Spotify.exe

	;previous song
	;CapsLock & F1::PostMessage, 0x319,, 0xC0000,, ahk_exe Spotify.exe
	
	;lower volume
	;CapsLock & F4::PostMessage, 0x319,, 0x90000,, ahk_exe Spotify.exe
	
	;raise volume
	;CapsLock & F7::PostMessage, 0x319,, 0xA0000,, ahk_exe Spotify.exe
	
	:*:htmlTmp::
	(
<html lang="en">
	<head>
		<meta charset="utf-8">
		<title>Foo</title>
		<link rel="stylesheet" href="css/styles.css">
	</head>
	<body>
		<script src="js/scripts.js"></script>
	</body>
</html>
	)
	return
	
	

	
; toggle hotkeys on/off ==================================================================================
ScrollLock::
Suspend
if(A_IsSuspended){
	SetScrollLockState, Off
	SetCapsLockState, Off
}else{
	SetScrollLockState, On
	SetCapsLockState, AlwaysOff
}
return
SC122::
Send {Volume_Mute}
return

;=========================================================================================================
; functions===============================================================================================
;=========================================================================================================



	insertTime(format="|MM.dd.yy|=|h:mm: tt|") ;Function to insert current time
		{ 
		  FormatTime, Time,, %format% 
		  Send %Time%{enter} 
		}
		
	GoogleTranslate(str, from := "auto", to := "en")  {
	   JSON := new JSON
	   JS := JSON.JS, JS.( GetJScript() )
	   
	   sJson := SendRequest(JS, str, to, from)
	   oJSON := JSON.Parse(sJson)

	   if !IsObject(oJSON[2])  {
		  for k, v in oJSON[1]
			 trans .= v[1]
	   }
	   else  {
		  MainTransText := oJSON[1, 1, 1]
		  for k, v in oJSON[2]  {
			 trans .= "`n+"
			 for i, txt in v[2]
				trans .= (MainTransText = txt ? "" : "`n" . txt)
		  }
	   }
	   if !IsObject(oJSON[2])
		  MainTransText := trans := Trim(trans, ",+`n ")
	   else
		  trans := MainTransText . "`n+`n" . Trim(trans, ",+`n ")

	   from := oJSON[3]
	   trans := Trim(trans, ",+`n ")
	   Return {main: MainTransText, full: trans, from: from}
	}

	SendRequest(JS, str, tl, sl)  {
	   ComObjError(false)
	   url := "https://translate.google.com/translate_a/single?client=t&sl="
			. sl . "&tl=" . tl . "&hl=" . tl
			. "&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&otf=1&ssel=3&tsel=3&pc=1&kc=2"
			. "&tk=" . JS.("tk").(str)
	   body := "q=" . URIEncode(str)
	   contentType := "application/x-www-form-urlencoded;charset=utf-8"
	   userAgent := "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
	   Return JSON.GetFromUrl(url, body, contentType, userAgent)
	}

	URIEncode(str, encoding := "UTF-8")  {
	   VarSetCapacity(var, StrPut(str, encoding))
	   StrPut(str, &var, encoding)

	   While code := NumGet(Var, A_Index - 1, "UChar")  {
		  bool := (code > 0x7F || code < 0x30 || code = 0x3D)
		  UrlStr .= bool ? "%" . Format("{:02X}", code) : Chr(code)
	   }
	   Return UrlStr
	}

	GetJScript()
	{
	   script =
	   (
		  var TKK = ((function() {
			var a = 561666268;
			var b = 1526272306;
			return 406398 + '.' + (a + b);
		  })());

		  function b(a, b) {
			for (var d = 0; d < b.length - 2; d += 3) {
				var c = b.charAt(d + 2),
					c = "a" <= c ? c.charCodeAt(0) - 87 : Number(c),
					c = "+" == b.charAt(d + 1) ? a >>> c : a << c;
				a = "+" == b.charAt(d) ? a + c & 4294967295 : a ^ c
			}
			return a
		  }

		  function tk(a) {
			  for (var e = TKK.split("."), h = Number(e[0]) || 0, g = [], d = 0, f = 0; f < a.length; f++) {
				  var c = a.charCodeAt(f);
				  128 > c ? g[d++] = c : (2048 > c ? g[d++] = c >> 6 | 192 : (55296 == (c & 64512) && f + 1 < a.length && 56320 == (a.charCodeAt(f + 1) & 64512) ?
				  (c = 65536 + ((c & 1023) << 10) + (a.charCodeAt(++f) & 1023), g[d++] = c >> 18 | 240,
				  g[d++] = c >> 12 & 63 | 128) : g[d++] = c >> 12 | 224, g[d++] = c >> 6 & 63 | 128), g[d++] = c & 63 | 128)
			  }
			  a = h;
			  for (d = 0; d < g.length; d++) a += g[d], a = b(a, "+-a^+6");
			  a = b(a, "+-3^+b+-f");
			  a ^= Number(e[1]) || 0;
			  0 > a && (a = (a & 2147483647) + 2147483648);
			  a `%= 1E6;
			  return a.toString() + "." + (a ^ h)
		  }
	   )
	   Return script
	}

	class JSON
	{
	   static JS := JSON._GetJScripObject()
	   
	   Parse(JsonString)  {
		  try oJSON := this.JS.("(" JsonString ")")
		  catch  {
			 MsgBox, Wrong JsonString!
			 Return
		  }
		  Return this._CreateObject(oJSON)
	   }
	   
	   GetFromUrl(url, body := "", contentType := "", userAgent := "")  {
		  XmlHttp := ComObjCreate("Microsoft.XmlHttp")
		  XmlHttp.Open("GET", url, false)
		  ( contentType && XmlHttp.SetRequestHeader("Content-Type", contentType) )
		  ( userAgent && XmlHttp.SetRequestHeader("User-Agent", userAgent) )
		  XmlHttp.Send(body)
		  Return XmlHttp.ResponseText
	   }

	   _GetJScripObject()  {
		  VarSetCapacity(tmpFile, (MAX_PATH := 260) << !!A_IsUnicode, 0)
		  DllCall("GetTempFileName", Str, A_Temp, Str, "AHK", UInt, 0, Str, tmpFile)
		  
		  FileAppend,
		  (
		  <component>
		  <public><method name='eval'/></public>
		  <script language='JScript'></script>
		  </component>
		  ), % tmpFile
		  
		  JS := ObjBindMethod( ComObjGet("script:" . tmpFile), "eval" )
		  FileDelete, % tmpFile
		  JSON._AddMethods(JS)
		  Return JS
	   }

	   _AddMethods(ByRef JS)  {
		  JScript =
		  (
			 Object.prototype.GetKeys = function () {
				var keys = []
				for (var k in this)
				   if (this.hasOwnProperty(k))
					  keys.push(k)
				return keys
			 }
			 Object.prototype.IsArray = function () {
				var toStandardString = {}.toString
				return toStandardString.call(this) == '[object Array]'
			 }
		  )
		  JS.("delete ActiveXObject; delete GetObject;")
		  JS.(JScript)
	   }

	   _CreateObject(ObjJS)  {
		  res := ObjJS.IsArray()
		  if (res = "")
			 Return ObjJS
		  
		  else if (res = -1)  {
			 obj := []
			 Loop % ObjJS.length
				obj[A_Index] := this._CreateObject(ObjJS[A_Index - 1])
		  }
		  else if (res = 0)  {
			 obj := {}
			 keys := ObjJS.GetKeys()
			 Loop % keys.length
				k := keys[A_Index - 1], obj[k] := this._CreateObject(ObjJS[k])
		  }
		  Return obj
	   }
	}
	
	JEE_StrReplaceChars(vText, vNeedles, vReplaceText:="", ByRef vCount:="")	; string replace
	{
		vCount := StrLen(vText)
		;Loop, Parse, vNeedles ;change it to this for older versions of AHK v1
		Loop, Parse, % vNeedles
			vText := StrReplace(vText, A_LoopField, vReplaceText)
		vCount := vCount-StrLen(vText)
		return vText
	}
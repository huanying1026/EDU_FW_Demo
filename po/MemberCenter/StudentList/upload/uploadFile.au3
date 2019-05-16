;激活上传窗口（获取焦点）
;ControlFocus("title","text",controlID) Edit1=Edit instance 1
ControlFocus("打开", "","Edit1")
; 设置上传窗口出现的超时时间
WinWait("[CLASS:#32770]","",10)
; 设置文件路径
ControlSetText("打开", "", "Edit1", "E:\ZM20180728\Framework\EDU_FW\po\MemberCenter\StudentList\upload\f_center_03.jpg")
Sleep(2000)
; 单击保存按钮
ControlClick("打开", "","Button1");
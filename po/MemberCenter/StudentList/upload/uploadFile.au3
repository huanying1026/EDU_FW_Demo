;�����ϴ����ڣ���ȡ���㣩
;ControlFocus("title","text",controlID) Edit1=Edit instance 1
ControlFocus("��", "","Edit1")
; �����ϴ����ڳ��ֵĳ�ʱʱ��
WinWait("[CLASS:#32770]","",10)
; �����ļ�·��
ControlSetText("��", "", "Edit1", "E:\ZM20180728\Framework\EDU_FW\po\MemberCenter\StudentList\upload\f_center_03.jpg")
Sleep(2000)
; �������水ť
ControlClick("��", "","Button1");
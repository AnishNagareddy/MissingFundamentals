
#SingleInstance,Force
SetTitleMatchMode,2

^j::
	ControlSetText, Edit1, Anish1, ahk_class #32770
	SetControlDelay -1  ; May improve reliability and reduce side effects.
	ControlClick, &Save, ahk_class #32770
	return 


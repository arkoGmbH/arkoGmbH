Option Explicit
'---------------------------
' 22.03.2022
' arko GmbH, Petros Mitropoulos
'
'
' Run Python file and wait till execution has finished
Sub ShellAndWait()
    Dim Path As String               ' Path to python file including / at the end
    Dim PythonFileName As String ' Python file name including .py at the end
    Dim PythonFilePath As String    ' Finaler Pfad mit kompletten Filepath
    
    
    Dim wsh As Object
    Set wsh = VBA.CreateObject("WScript.Shell")
    Dim waitOnReturn As Boolean: waitOnReturn = True
    Dim windowStyle As Integer: windowStyle = 1
    
    Path = "G:\2500_Technik\V-_Bauphysik_Statik\B_Statik\arko_GmbH\10_PYTHON\"
    'PythonFileName = "PrintHalloWorld.py"
    PythonFileName = "CreateTextFile.py"
    
    PythonFilePath = Path & PythonFileName

    wsh.Run "Python " & PythonFilePath, windowStyle, waitOnReturn

End Sub
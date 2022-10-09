# Write-and-Read-Angles-in-UPBGE
How to work with math 3D angles in the UPBGE With Python


Main Code:
Para obter as informações de orientação:<br>
xyz = own.localOrientation.to_euler() <br>

Para aplicar uma rotação de 45 graus<br>
xyz.z = radians(45)<br>

Para aplicar a rotação local:<br>
own.localOrientation = xyz<br>

Para exibir a rotação em graus:<br>
print(degrees(xyz.z))<br>

Variável de depuração para exibir o ângulo<br>
own['angle'] = degrees(xyz.z)<br>

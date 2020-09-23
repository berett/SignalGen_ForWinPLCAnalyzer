import os
import sys
import re

# USO: crearINI.py 	<Direccion_memoriaPLC> 	<Grupo> 	<Nombre> 	<Descripcion>	<Contador>
#	   argv[0]		argv[1]					argv[2] 	argv[3] 	argv[4]			argv[5]

#Creamos la carpeta del proyecto si no existe y el .SA7
try:
	os.stat("ProyectoGEN");	
except:	
	os.mkdir("ProyectoGEN");
	os.system("copy ProyectoGEN_TEMPLATE.SA7 ProyectoGEN\\ProyectoGEN.SA7");

try:
	os.stat("ProyectoGEN\\" + sys.argv[2]);
except:
	os.mkdir("ProyectoGEN\\" + sys.argv[2]);
	os.system("copy Kurvenfenster_TEMPLATE.CRV ProyectoGEN\\" + sys.argv[2] + "\\Kurvenfenster.CRV");

dato = re.sub(r'DB1\.', 'DB1_', sys.argv[1]);
fichero = open("ProyectoGEN\\" + sys.argv[2] + "\\" + dato + ".INI", "w");
fichero.write("[INIT]\nSmall=0\n");
direccion = re.findall(r"DB1\.DB(.)", sys.argv[1]);
for coincidencia in direccion:
	if coincidencia == "X":
		dato3 = "1";
	if coincidencia == "W":
		dato3 = "6";
	if coincidencia == "D":
		dato3 = "5";
fichero.write("D=" + dato3 + "\n");
fichero.write("Hex=0\nColor=0\nLD=2\nLA=1\n");
fichero.write("Description=\n");
fichero.write("YAuto=1\nYMin=0.0000\nYMax=0.0000\nUnity=" + sys.argv[3] + "\n");
dato2 = re.sub(r'DB1\.', '', sys.argv[1]);
fichero.write("Symbol=\nConnectionID=16752124\nMP=1\nVisible=1\nOperand=" + dato2 + "\n");
fichero.write("DBNr=1\nID=18885815\nBitsIgnore=0\nBitsShift=0\nAddToSignal=0.0000\nUGR=0.0000\nOGR=0.0000\nBipolar=0\n");

if len(sys.argv) == 6:
	fichero2 = open("ProyectoGEN\\ProyectoGEN.SA7","a");
	fichero2.write("Open" + sys.argv[5] + "=" + os.getcwd() + "\\" + sys.argv[2] + "\\Kurvenfenster.CRV\n");

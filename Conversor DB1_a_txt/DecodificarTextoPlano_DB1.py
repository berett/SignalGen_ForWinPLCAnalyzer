import re

linea=[0,0,0,0,0,0];
archivo = open('Output.txt','r');
archgen = open('OutputG.txt','w');

#Buscamos la primera linea 'util' para nosotros del archivo
linea[1] = archivo.readline();
while linea[1].find("Address Name") == -1:
	linea[1] = archivo.readline();
#Cuando la encontramos pasamos a leer la siguiente ya que deberia ser una direccion ya
linea[1] = archivo.readline();

while linea[1] != "":
	#Chequeamos si efectivamente es una direccion
	check_IsAddress=re.compile(r"^(\s{0,15}[0-9]+\.[0-7])");
	IsAddress = check_IsAddress.match(linea[1]);

	#si es una address sabemos que la linea 1 es util asi que comprobamos las siguientes:
	if IsAddress:
		direccion = re.findall(r"\s*(\d+\.\d)", linea[1]);
		for coincidencia in direccion:
			print ("\naqui esta la direccion: %s" % coincidencia);
			direccion = coincidencia;
		grupo = re.findall(r"^\s*\w*\.\d\s*(\w+)", linea[1]);
		for coincidencia in grupo:
			print ("que pertenece al grupo: %s" % coincidencia)
			grupo = coincidencia;
		nombre = re.findall(r"^\s*\w*\.\d\s*\w+\.([\w\d\.\[\]\_]*)", linea[1]);
		for coincidencia in nombre:
			print ("con nombre: %s" % coincidencia);
			nombre = coincidencia;
		tipo = re.findall(r"^\s*\w*\.\d\s*[\w\d]+\.[\w\d\[\]]*\s*([A-Z]{3,5})", linea[1]);
		for coincidencia in tipo:
			print ("del tipo: %s" % coincidencia);
			tipo = coincidencia;
		descripcion = re.findall(r"^\s*\w*\.\d\s*[\w\d]+\.[\w\d\[\]\.\_]*\s*[A-Z]{3,5}\s+[\w\+\.]{1,4}\s{1,2}[\w\+\.]{1,4}\s{1,2}(.*)", linea[1]);
		for coincidencia in descripcion:
			print ("con descripcion: %s" % coincidencia);
			descripcion = coincidencia;

		contAddress = 1;
		i = 2;
		while contAddress:
			linea[i] = archivo.readline();
			#si hay hueco blanco al principio y luego algo tipo "A A " => seguimos leyendo lineas
			check_contAddress = re.compile(r"^\s+([\w\+]{1,4}\s[\w\+]{1,4}\s)");
			contAddress = check_contAddress.match(linea[i]);
			if contAddress:
				descripcion2 = re.findall(r"^\s+[\w\+]{1,4}\s[\w\+]{1,4}\s([^\n]*)", linea[i]);
				for coincidencia in descripcion2:
					descripcion = descripcion + coincidencia;
			else:
				linea_adelantada = linea[i];
				break;
			
		#si hemos llegado aqui significa que tenemos una linea completa de direcciones
		if tipo == "BOOL":
			archgen.write("DB1.DBX" + direccion + "\t" + grupo + "\t" + nombre + "\t" + descripcion + "\n");
		if tipo == "INT" or tipo == "WORD":
			direccion = re.sub(r'\.0', '', direccion);
			archgen.write("DB1.DBW" + direccion + "\t" + grupo + "\t" + nombre + "\t" + descripcion + "\n");
		if tipo == "LREAL" or tipo == "REAL" or tipo == "DWORD":
			direccion = re.sub(r'\.0', '', direccion);
			archgen.write("DB1.DBD" + direccion + "\t" + grupo + "\t" + nombre + "\t" + descripcion + "\n");
	
		linea[1] = linea_adelantada;
	else:
		linea[1] = archivo.readline();

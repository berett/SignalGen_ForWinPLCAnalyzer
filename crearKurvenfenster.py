import os
import sys

# USO: crearKurvenfernster.py <posicion> <direccion> <grupo>
#	   argv[0]					argv[1]    argv[2]   argv[3]


fichero = open("ProyectoGEN\\" + sys.argv[3] + "\\" + "Kurvenfernster.CRV", "a");
fichero.write(sys.argv[1] + "=" + sys.argv[2]) + "\n";


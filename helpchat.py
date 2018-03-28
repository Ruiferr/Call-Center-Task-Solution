# 2017-2018 Programacao II (LTI)
# Grupo 009
# 52172 Rui Ferrão
# 51648 Tiago Sousa

from File import File
import sys

ope = File(sys.argv[1])
req = File(sys.argv[2])


ope.getOperators()
req.getRequests()


ope.assignTasks(req)







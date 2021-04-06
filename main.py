import sys, getopt
from modules import QuestionAnalyzer,DocumentRetriever,AnswerExtractor

def commandline():
 print("Command Line Mode Start")
 QuestionAnalyzer()
 DocumentRetriever()
 AnswerExtractor()
 
def app():
 print("GUI Mode Start")
 QuestionAnalyzer()
 DocumentRetriever()
 AnswerExtractor()
 
 
def main(args):
 try:
  opts, args = getopt.getopt(args,"hm:",["mode="])
 except getopt.GetoptError:
   print("Except Error.\nUsage : IR_QA.py -m <mode> \n\nmode options :  1. cli (for commandline mode)\n\t\t2. app (for gui mode) ")
   sys.exit(2)
 if(len(opts)==0): 
  print("No opts.\nUsage : IR_QA.py -m <mode> \n\nmode options :  1. cli (for commandline mode)\n\t\t2. app (for gui mode) ")
  sys.exit()
 
 for opt,arg in opts:
  if opt == '-h':
   print("Usage : IR_QA.py -m <mode> \n\nmode options :  1. cli (for commandline mode)\n\t\t2. app (for gui mode) ")
   sys.exit()
  elif opt == '-m':
   if arg == 'cli':
     commandline()
   elif arg == 'app':
     app()
   else:
    print("Usage : IR_QA.py -m <mode> \n\nmode options :  1. cli (for commandline mode)\n\t\t2. app (for gui mode) ")
    sys.exit()
  else:
    print("Usage : IR_QA.py -m <mode> \n\nmode options :  1. cli (for commandline mode)\n\t\t2. app (for gui mode) ")
    sys.exit()
	
if __name__ == "__main__":
    main(sys.argv[1:])
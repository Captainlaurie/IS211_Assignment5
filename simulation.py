import argparse
import queue
import csv

#Create Request class and attributes
class Request:
    
    def __init__(self, reqSecond, filePath, secsToProcess):
        self.reqSecond = int(reqSecond)
        self.filePath = filePath
        self.secsToProcess = int(secsToProcess)
        
    #function to get the second of the simulation that the request came in
    def getRequestSecond(self):
        return self.reqSecond
    
    #function to get file path of request
    def getFilePath(self):
        return self.filePath
    
    #function to get the seconds the request takes to process
    def getSecsToProcess(self):
        return self.secsToProcess
    
    
#Create server class and attributes 
class Server:
    
    def __init__(self, reqRate):
        self.requestRate = reqRate
        self.currentTask = None
        self.timeRemaining = 0
        
    #function that establishes tasks and time remaining
    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None
        
    #function to check whether server is busy
    def serverBusy(self):
        if self.currentTask != None:
            return True
        else:
            return False
        
    #function for starting the next request
    def startNext(self, newTask):
        self.currentTask = newTask
        self.timeRemaining = newTask.getSecsToProcess()
        
        
#Function to simulate one server
def simulateOneServer(fileName, reqPerMin):
    server = Server(reqPerMin)
    requests = []
    
    with open(fileName, 'r') as f:
        for row in csv.reader(f, delimiter = ','):
            requests.append(Request(*row))
        
        
        
def main():
    requests = [0]
    with open (args.file, 'r') as f:
        for row in csv.reader(f, delimiter=','):
            requests.append(Request(*row))
            
    print(requests)
    
    
if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser('Server')
    parser.add_argument("--f", "--file", help="Number of servers", type=str, required=True)
    args = parser.parse_args()
    main()        
        
        
        
        
        
        
        
        
        
        
        
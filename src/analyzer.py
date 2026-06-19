class Analyzer:
    def __init__(self, file):
        self.file = file
        return
    
    def analyze(self):
        suspect_ip = {}
        for line in self.file:
            parts = line.split()
            
            if parts[3] == "status=failed":
                if parts[4] not in suspect_ip:
                    suspect_ip[parts[4]] = 1
                else:
                    suspect_ip[parts[4]] += 1
        suspect_list = list(suspect_ip.items())
        risk_factor = self.sort(suspect_list)
        self.displayResult(risk_factor)
        
    def displayResult(self, risk):
        print("====================================================")
        print("REPORT")
        print("====================================================")
        for i in range(len(risk)):
            attempt = risk[i][1]
            ip = risk[i][0]
            if attempt >= 4:
                print("HIGH RISK: ")
            elif attempt >= 3:
                print("MODERATE RISK: ")
            else:
                print("LOW RISK: ")
            print(f"There was {attempt} unsuccessful login attempts from {ip}\n")

        print("====================================================")
            
        
    def sort(self, suspect):
        mid = len(suspect) //2
        if len(suspect) > 1:
            b = self.sort(suspect[:mid])
            c = self.sort(suspect[mid:])
            return self.merge(b, c, suspect)
        else:
            return suspect
    
    def merge(self, b, c, a):
        i = 0
        j = 0
        k = 0
        while i < len(b) and j < len(c):
            if b[i][1] > c[j][1]:
                a[k] = b[i]
                i += 1
            else:
                a[k] = c[j]
                j += 1
            k += 1

        while j < len(c):
            a[k] = c[j]
            j += 1
            k += 1
        while i < len(b):
            a[k] = b[i]
            i += 1
            k += 1 
    
        return a



        
                
